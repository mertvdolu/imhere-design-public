# 02 — Profil oluşturma, düzenleme ve görünürlük
## Form yapısı
Tek kaydırılabilir form: fotoğraf → ad → doğum tarihi → cinsiyet → meslek → bio → ilgi alanları → opsiyonel konuşulan diller → görünürlük → Kaydet. Seçici alt görünümler formun aynı bellek taslağına bağlıdır; ayrı profil, mod veya yeni kayıt adımı değildir. “Tamam” seçimi taslağa geri taşır; tek başına sunucuda profil kaydetmez. Kalıcı taslak veya uygulama kapanınca koruma vaadi yok.

Dolu örnek çizimi bir fixture’dır; ilk kullanıcıya ad/tarih/cinsiyet/meslek/ilgi seçimi önceden doldurulmaz. Görünürlükte ise yeni profilde üç varsayılan TRUE açıkça uygulanır. Düzenlemede sunucuda kayıtlı false değerleri korunur.

## Alanlar
| Alan | Sunum ve sabit kural |
|---|---|
| Fotoğraf | Tam1; tek önizleme + seç/değiştir. Çoklu fotoğraf veya profil galerisi yok. “Fotoğrafı kullan” yalnız seçili fotoğrafı taslağa alır; paylaş/kaydet başarısı değildir. |
| Ad | 2–30 grapheme; gerçek ad/soyad zorunluluğu eklenmez. Kalıcı etiket; sınır hatası mevcut doğrulama. |
| Doğum tarihi | Zorunlu18+; girişte lokalize tarih seçimi veya mevcut native giriş bileşeni. Gösterim örneği sunucu tarih formatı değildir; mevcut tarih-only sözleşmesi korunur, timezone ile gün kaydırılmaz. Tüm ret nedenlerinde aynı profileBirthDateError. |
| Cinsiyet | Dört mevcut seçenek, radyo seçimi; önseçim yok. Kadın/Erkek/Non-binary/Belirtmek istemiyorum. Cinsiyet tercih filtresi yok. |
| Meslek | Zorunlu. Gizleme toggle’ı zorunluluğu kaldırmaz. Mevcut uygulama karakter üst sınırı/normalizasyonu korunur, tasarım yeni max uydurmaz. |
| Bio | Zorunlu≤150 grapheme. Çok satırlı; kalan karakter sayacı mevcut grapheme/normalizasyon fonksiyonuyla. Emoji UTF-16 uzunluğuyla sayılmaz. |
| İlgi alanları | 26 hazır+Diğer, min1/max5. Çoklu seçim; başta boş. Altıncı seçim eklenmez; nötr sınır açıklaması, mevcut seçimler korunur. Diğer yeni serbest alan üretmez. |
| Konuşulan diller | Opsiyonel; boş seçim hata değildir. Arayüz diliyle karıştırılmaz. Çizimdeki iki dil örnek satırdır; gerçek katalog/data yapısı ürünün yetkili veri sözleşmesinden. |

Tarih picker’ında aday tarih, kullanıcı onaylamadan formun seçilmiş doğum tarihi sayılmaz. Native date picker min/max veya yaş reddi detayını UI’dan türetmeyin; mevcut kabul/ret sözleşmesini koruyun. Hata nedeni gösterilmeyen genel ret politikası görsel ipuçlarıyla delinmez.

## Üç görünürlük anahtarı
- Yaşım görünsün, Cinsiyetim görünsün, Mesleğim görünsün: başlangıç açık, ayrı ayrı kapatılabilir. Görünür/Gizli metni + switch durumu; yalnız renk yok. Satır minimum48 hedef; büyük metinde yükseklik büyür.
- Gösterilecek yaş doğum tarihinden hesaplanır; tam tarih kendi veya başka kullanıcının profil görünümünde bulunmaz, yalnız düzenleme formunda.
- Toggle değişikliği taslaktadır. Kaydet gerçek başarıyla sonuçlanana kadar “gizlendi/kaydedildi” başarısı üretilmez. Başarısızlıkta mevcut form taslağı açık kaldığı sürece korunur; kalıcı disk kaydı vaadi yok.
- Gizli alan diğer kişiye gösterilen profil DTO’sundan/alanlarından tamamen dışlanır; yalnız widget opacity’siyle saklanmaz. Kendi profil görünümü de aynı kamusal sunumu örnekler; düzenleme formunda kullanıcı kendi verisini görür.
- Yakındakiler kartında da aynı meslek görünürlüğü kuralı geçerli. Gizlenen alanın boş satırı, maskesi, rozeti veya semantik açıklaması bırakılmaz. Bio serbest metnine otomatik meslek çıkarımı yapılmaz.

## Kendi/başka profil
Tek fotoğraf, görünen ad, izin verilen yaş/cinsiyet/meslek, bio, ilgi alanları ve varsa konuşulan diller. Konum, kişi pini, mesafe, e-posta/telefon/Instagram yok. Bilgi yoksa yeni hayali kişi/alan eklenmez.
Kendi profilinde Profilimi düzenle → kayıtlı değerlerle form. Başka profilde Bir merhaba gönder yalnız sunucunun uygunluğu varsa Paket3 bağımsız niyet seçimine giriş; bu buton doğrudan istek/match oluşturmaz. Uygunluk değişirse tarafsız kullanılamıyor görünümü; engellenme nedeni ifşa edilmez. Block görünmezliği üstündür.

## Kayıt
Gönderme öncesi mevcut doğrulama; ilk hataya odak/kaydırma + alan altı hata. Kayıtta buton disabled, yeni ikinci istek yok. Offline/başarısız kaydetme başarı mesajı göstermez. profile-complete yalnız bağlı işlemin gerçek başarısıyla ve profil tamlığı koşuluyla; sonraki CTA Paket1'e gider. Mevcut onSave/onPublishPhoto bağlı değilse sahte başarı oynatılmaz.
