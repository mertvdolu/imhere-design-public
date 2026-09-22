# Cream & Ink — tam tasarım devri / v2.2

## 1. Kaynak sırası

Founder’ın son onayı: krem/siyah tüm uygulamanın tek aktif temasıdır. Bu paket eski yeşil çizimlerin görsel yerini alır. Ürün kuralları ve önceki sözleşmeler yürürlüktedir; UI rengi değişirken iş kuralları değişmez. Önceki paketler davranış geçmişi için arşivde tutulur. Güncel ekran matrisi `contracts/screen-manifest.json` içindedir.

## 2. Ortak görünüm

- Zemin #F4F1E9, açık yüzey #FCFAF5, metin/ana eylem #191A17, ikincil metin #696A62.
- Geist: başlık 36/1.12, medium 500, harf aralığı −1.8; gövde 16/1.6; etiket 14/1.4; yardımcı metin 12/1.5. Başlık satır yüksekliği uzun TR/EN ve %200 yerleşiminde 1.12 olarak tamamlandı.
- Form kenarlığı #7C7D73; #D9D5CB yalnız dekoratif ayırıcı/kart sınırı. İnce çizgi 1; ikon çizgisi 1.8. Hata/kapalı/seçili ayrımı yalnız renge dayanmaz: anlamlı metin, simge ve durum da gerekir.
- Düğme 12, kart 15, sheet 24 köşe yarıçapı. Birincil siyah/açık metin; ikincil açık yüzey/siyah sınır; disabled ikincil ton + gerçek pasif semantiği.
- Eski parlak küre ve yeşil gradyanlar kaldırıldı. Check-in eylemleri düz, açık durum metinleriyle sunulur; animasyon başarı veya sürekli konum izleme izlenimi vermez.
- Fotoğraf griliği yalnız sunum filtresi/örnek türevidir. Kullanıcının yüklenen orijinalini değiştirmez. Fotoğraf seçim/editör işlevleri korunur.
- Orijinal iki daireli logo, kendi Ink #14161A / Paper #FAFAF8 renkleri ve oranıyla kullanılır. Telefon uygulama etiketi IM HERE. Eski B-symbol güncel varlıklara kaynak değildir.

## 3. Yerleşim ve erişilebilirlik

Sayfa kenarı 24 mantıksal birim. Eylem hedefi en az 48×48; küçük ikonun etkileşim alanı geniş tutulur. iOS/Android güvenli alanları platformdan alınır; çizimlerde 390×844 ve 412×915 referansları kullanılır. Durum çubuğu koyu içeriktir.

%200 metin için bütün ekranlar ayrı yeniden dizildi. Formlar, uyarılar, seçimler ve butonlar içerikle büyür. Dört sekme, normalde tek sıra; büyük metinde kabul edilmiş 2×2 yerleşim. Normal alt bar 80; büyük metin barı 184 + sistem alt güvenli alanı. Sıra Profile → Messages → Nearby → Events; ilk açılan Nearby. Uzun SVG tam kaydırılabilir içeriği gösterir; uygulamada alt navigasyon sabit kalır, gövde bağımsız kaydırılır. Uzun SVG’nin piksel yüksekliği cihaz ekran yüksekliği değildir.

Klavye açılınca form/sohbet içerikleri klavye yüksekliğine göre kaydırılır. Gönder düğmesi ve odaklanan alan erişilebilir kalır. Cihazda klavye yerleşimi yazılım/M10 doğrulamasıdır; bu tasarım teslimi klavye sorununun kodda çözüldüğünü iddia etmez. Ekran okuyucu sırası görsel sıra; yükleme/hata/başarı mesajları uygun canlı bildirimle duyurulur. Reduce Motion açıkken geçiş ve dekoratif hareket kaldırılır. Erişim, sonuç, seçim, sunucu verisi veya süre tasarımdan türetilmez.

## 4. Giriş ve profil

Davet → e-posta + parola → e-posta doğrulama bağlantısını bekleme → profil. Mevcut kullanıcı girişi ve e-posta ile parola sıfırlama korunur. Parola en az 8 karakter; tür şartı ve güç göstergesi yok. Giriş hatası tek genel mesaj, sıfırlama sonucu koşullu; resend mevcut backend durumundan gelir, sayaç yok.

Doğrulama ekranlarının tümünde, hesap oluşturulduktan sonraki davet-tekrar ekranında ve profil oluşturma ekranlarında `authSignOut`: ana eylem grubundan 24 birim sonra ikincil buton; güvenli alandan önce, ekranı kaydırınca ulaşılabilir. Doğrulamada geri tuşu çıkış yerine konmaz. İlk davet ekranı ile hesabı açılmış davet-tekrar durumu ayrı çizimlerdir. Profil düzenleme ekranına onboarding çıkışı eklenmez.

Fotoğraf form durum satırı: yüklenmişse `photoUploaded`, boşsa `photoNone`; seçim/değiştirme düğmeleri ayrı kalır. Hazırlanıyor durumu yükleme başarısı sayılmaz. Profil görünürlük metni son sunucu açıklamasını kullanır. Yaş/cinsiyet/meslek varsayılan görünür; public veri gizliyse alan/boş yer/dolaylı çıkarım gösterilmez.

## 5. Yakındakiler ve tam ekran harita

Harita açılınca sayfanın tamamını kaplar; alt sekmeler görünmez. Geri Nearby’a döner. Üstte geri + kısa harita başlığı; sağda zoom hedefleri. Alt yüzeyde gerçek duruma uygun bilgi, varsa snapshot zamanı ve açıklaması, açılabilir hareketlilik açıklaması, attribution. Kişisel konum, pin, kişi sayısı veya mesafe yok.

Normal çizimler cihaz boyundadır; büyük metinde alt sheet içeriği taşarsa sheet kendi içinde kaydırılır, harita sabit viewport’ta kalır. Tam içerik SVG’de ayrıca okunabilir. `map-legend` açıklama sheet’ini gösterir. Harita üstündeki demo alanları temsili sabit hücre örnekleridir, kişilere ait alanlar veya canlı veri değildir. Stil JSON’larında bu örnekler yoktur.

MapLibre + OpenFreeMap. Zorunlu görünür attribution: **© OpenStreetMap contributors · OpenFreeMap**. Kaynak OpenMapTiles kredisi de korunur. İlgili atıflar gerçek bağlantılar olur; içerik bunları örtmez. Krem basemap yalnız görünümü değiştirir; dört mavi/sarı/yeşil/kırmızı band ve sabit veri geometrisi korunur. Haritadaki yeşil semantik bandın varlığı eski yeşil tema değildir. Native tile/glyph ağ erişimi ve cache davranışı mevcut adapter’a aittir.

`nearbyLimited` yalnız sunucudan liste kırpıldığı biliniyorsa gösterilir. Kişi görünümünde cooldown, bekleyen istek ve mevcut bağlantı ayrı; pasif Bir merhaba gönder + kendi nötr açıklaması. Süre, neden ve karşı kişinin özel kararı çıkarsanmaz.

## 6. İstek, sohbet, devam ve contact

Messages = Connections + Requests. İki niyet: Friendship / Networking; başlangıç boş, kabul seçimi gerekli. Bekleyen sayaç `pendingSlots(used,max)`; max sözleşmeden, örnek 20. 19/20 ve 20/20 ile kalan süre çizimleri korunur.

Sohbet metin + emoji + link, en çok 500 grapheme, 20 kendi gönderim hakkı. Medya/düzenleme/silme yok. Yumuşak iletişim uyarısı ve Yine de gönder korunur. Kapalı/salt okunurda composer yok; kapalı kart kilit ve nötr `connectionEndedNeutral` ile ayırt edilir. Salt okunur olmak tek başına sona ermiş bağlantı değildir.

Saklama (ENG-M10-08(5)): `chatRetentionInfo` yalnız salt-okunur sohbette gösterilir; yazılabilir sohbette gösterilmez. Gönderim, geçici çevrimdışı olma veya belirsiz sonuç tek başına salt-okunur durum sayılmaz; uyarı yalnız mevcut gerçek backend eşiğiyle, silinmiş durum yalnız doğrulanmış sonuçla. Sayaç veya tam saat vaadi yok; profiller kalır. Yazılabilirlik bitiş tetikleyicileri son Manager kuralından gelir, tasarım yeniden tanımlamaz. Erişim/engel sonucu saklama mesajlarından önceliklidir; eski veri gösterilmez.

Devam tercihi özel; karşı karar gösterilmez. HAYIR final, kendi onayı korunur. EVET+EVET → mevcut salt okunur/contact geçişi. Geçişin loading/failed çizimleri korunur; yapay gecikme eklenmez.

Contact yalnız Telefon/Instagram/E-posta/Diğer. Alan seçimi boş başlar, açık paylaşım gerekir. Paylaşılmış alanlar düzenlenir/kaldırılır; yalnız paylaşılmamış uygun alanlar Ek bilgi paylaş seçimine gelir. Hepsi paylaşılmışsa ek paylaşım girişi yok. `contactUpdated` doğrulanmış güncellemede; son alan kaldırıldığında kendi paylaşımları altında `contactNothingShared`. Görülmüş bilgiyi geri sildiğini vaat etmez.

## 7. Güvenlik, Ayarlar, bildirimler

Report beş kategori → ayrı ayrıca engelle sorusu. Block/unblock ve End Connection kendi onayları korunur. Hesap sil gerçek ve geri alınamaz; istek alındı / tamamlandı / başarısız ayrı. Sınırlı kayıtların hukuki saklanabileceği açıklaması korunur. Yeniden giriş gerekebilir. Hukuki metin/URL uydurulmaz.

Aktif Ayarlar sırası: Notifications · Blocked users · Privacy policy · Terms · Contact us · Delete my account · Sign out. İngilizce aktif. Dil satırı ve dil ekranları askıda; katalog varsayılanında gizli, ayrı filtreyle hazırlık referansı olarak açılır. Türkçe açıldığında Language ilk sıraya geri gelir. Profilde konuşulan diller alanı, uygulama dil ayarından ayrıdır.

Contact us → info@useimhere.com adresine e-posta uygulaması. Açılamazsa `supportEmailUnavailable`, seçilebilir adres ve açık kopyalama düğmesi. Bu teslim iki yardımcı anahtar ekler: `supportCopyEmail` ve `supportEmailCopied`; ikincisi yalnız gerçekten kopyalanınca. Yeni ağ davranışı veya mail gönderme eylemi eklenmez.

Bildirim: yakınlık bildirimi başlıksız, uygulama açıkken gösterilmez; başka bildirim türlerine genellenmez. Varsayılan sessiz; kullanıcının OS tercihi korunur. Android kanalları Updates / Check-in reminders. İstek bildirimi güncel yetki kontrolünden sonra ilgili isteğe gider. Küçük simge yeni gönderilen işaret geometrisinden beyaz/saydam maske olarak teslim edildi. Gerçek durum çubuğu kontrolü ayrıca gerekir.

Events yalnız placeholder. Hesap durumu açılışta okunamıyorsa sakin ulaşılamıyor/offline + yalnız Tekrar dene; logout veya veri kaybı varsayımı yok. İç yönetim paneli bu mobil tasarım paketinin kapsamında değildir.

## 8. Uygulama sınırı ve devir

Dosyalar ayrı ayrı GitHub’a yüklenir. Canlı ARB’ler tam referansla ezilmez; `migration.json` ve delta ile birleştirilir. Önceki alias ve parametre sözleşmeleri korunur. Bu paketteki PNG/SVG/HTML kontrolleri native ekran okuyucu, fiziksel cihaz, klavye, OEM launcher, push teslimi veya sunucu testleri değildir. Bunlar M10 uygulama turunda doğrulanır. Founder’a gönderilecek özet `MANAGER-NOTU.md` içindedir.
