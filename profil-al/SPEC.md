# PROFIL-AL — ölçü ve akış spesifikasyonu v1.0

7 Ekim 2026 · Cream & Ink v2.3 / 02 — Hafif kabartma.

**PROPOSED — HARBOR + FOUNDER COPY APPROVAL REQUIRED.** Bu teslim görsel tasarım ekidir. Ana ARB, Flutter/backend, üretim veya mağaza paketi değiştirilmez.

## 1. Mevcut tasarıma etkisi

- Ayarlar / Profili düzenle içindeki Networking–Friends kaydırıcısı ve yüzde gösterimleri kaldırılır. Eski yüzde verisinden amaç türetilmez. Yüzde kendi/başkasının profilinde de çizilmez.
- Yerine isteğe bağlı **Your default purpose** bölümü: Networking / Friendship / Not set; tek seçim. Aynı Y2 radyo çipi ailesi.
- Kendi profil görünümünde ek varsayılan amaç baloncuğu **YOK**. Düzenleme alanındaki açıklama yeterli; ayarı oturum rozetiyle karıştıran ikinci bir işaret eklenmez.
- `y1-y2/` teslimindeki boş amaç seçimi artık **ayar yoksa veya okunamıyorsa** geçerlidir. Kayıtlı amaç varsa önseçim gelir; ekran yine açılır, Continue için açık kullanıcı eylemi gerekir. Eski y1-y2 dosyaları tarihsel kaynaktır; bu karar ilgili akışta önceliklidir.
- Y2 10 gün kuralı, farklı amaç uyarısı ve oturum rozetinin mevcut metinleri bu işte yeniden yazılmaz.

## 2. Bileşen ve ölçüler

`../y1-y2/style.css` → mevcut Events kabuğu ve v2.3/v10 kontrolleri. Ortak token dosyasında değişiklik yok.

| Bileşen | Ölçü / yeniden kullanım |
|---|---|
| Sayfa | kenar24; bölüm arası24; ilişkili alan/etiket8 |
| Başlık | Geist Medium28 / 1.15; compactPageTitle |
| Gövde / üç bilgi paragrafı | Geist Regular16 / 1.6; 200%'de32; küçük hukuk metnine çevrilmez |
| Seçim / küçük düğme | Medium14 / 1.4; görünür dolgu8/16; gerçek hedef≥48×48 |
| Alan | Regular16 / 1.6; min48; yatay14/dikey12; radius12; mevcut iç gölge ve kenar |
| İpucu / hata / izleyici notu | Regular14 / 1.5; not bağlantının hemen altında; etkileşim alanı değil |
| Dış bağlantı | düz LinkedIn, Medium16; genel dışa-açılma çizgi ikonu18; tek bağlantı hedefi≥48×48 |
| Yüzey | paper #F4F1E9, ink #191A17, secondary #696A62, kenar #7C7D73; mevcut hafif kabartma |
| Bilgi satırı | mevcut ink çizgili bilgi/işlem bileşeni; gövde16; kırmızı/marka mavisi yok |
| Alt menü | mevcut v10 kabuğu; normal4 sütun, 200%'de2×2; tam ekran amaç/onay/kaldırmada yok |

Seçili radyo: siyah dolu yüzey + açık yazı + dolu radyo noktası + seçili semantik. Yalnız renk farkı yok. Yeni renk/ikon ailesi veya bileşen türü yok. Genel dış bağlantı simgesi mevcut outline çizgisiyle çizilir; native karşılık `open_in_new`. LinkedIn logosu/marka mavisi kullanılmaz.

200% metinde çipler ve eylemler alt alta; metin kesilmez, font küçültülmez. Kaydırma alanı alt menünün gerçek yüksekliğinden önce biter. Düğmeler uzun içeriğin sonunda kaydırılarak erişilebilir; sabit alt panel metnin üstüne binmez. Klavye açıldığında mevcut menü/alan inset kuralı uygulanır. Bu HTML OS klavyesi veya native picker ölçümü değildir.

Yüksek kontrast: gölge kaldırılır, kontrol sınırları ink/kenarla okunur. Şeffaflığı Azalt: opak menü, blur yok. Hareketi Azalt: dekoratif geçiş yok; mevcut işlevsel bekleme göstergesi korunur.

## 3. A — varsayılan amaç

### Düzenleme bölümü

Başlık → üç seçenek → açıklama → aktif oturum varsa bilgi notu → mevcut Save my profile. Kaydırıcının bulunduğu bölümün yerine uygulanır; diğer profil alanları/required kuralları değişmez. Önizleme bölüm odaklıdır; burada gösterilmeyen diğer profil alanlarını kaldırma talimatı değildir.

Not set, boş kayıt değerini anlatır; bir üçüncü oturum amacı değildir. Kaydetmek için Networking/Friendship seçme zorunluluğu yok. Save sunucu yanıtı gelene kadar bekler; başarı/hata mevcut profileSaving/profileSaved/profileSaveFailed anahtarlarıyla. Hata seçimi korur. Aktif oturum notu bölüm açıkken sürekli görünür; seçimden ve kayıttan sonra da kaybolmaz.

LinkedIn düzenleme girişini ayrı küçük satır olarak bu özel ayarlar alanında tut. İletişim kartı bölümünün içine yerleştirme; LinkedIn contact card alanı değildir. Yeni zorunlu onboarding adımı yok.

### I’m here / önseçim

- Varsayılan Networking/Friendship başarıyla okunmuşsa ilgili çip seçili. Hemen seçeneklerin altında **Your default purpose is selected. You can change it for this session.** Gövde16/ink, görünür bilgi satırı; dipnot gibi küçültülmez.
- Oturum seçimi varsayılandan farklı yapılınca önseçim iddiası taşıyan satır kalkar; önerilen `y2PurposeChangedNote` oturuma özel olduğunu açıklar. Ayar yazılmaz. Kullanıcı eski seçime dönerse varsayılan notu yeniden görünür.
- Ayar yok/okunamıyor: iki çip de boş, Continue pasif, varsayılan notu yok. “Not set” check-in seçenekleri arasına eklenmez.
- Continue mevcut konum/izin/check-in kapılarına seçili oturum amacıyla gider. Otomatik check-in yok. Cancel oturum oluşturmaz, ayarı değiştirmez.
- Aktif oturumun amacı ve I’m still here yenilemesi değişmez; yeni varsayılan sonraki yeni oturum için başlangıç seçimidir.
- Başkaları varsayılanı görmez; yalnız gerçek aktif oturum rozeti mevcut izin verilen yüzeyde görünür.

## 4. B — LinkedIn düzenleme

### Ekle / düzenle

Başlık → (görünürlük geçici kapalıysa not) → kayıtlıysa kısa LinkedIn + Remove link satırı → etiket/alan/ipucu → varsa alan hatası → üç bilgi paragrafı → Open and check / Save link → Save pasifliğinin nedeni.

Alan yalnız mevcut sözleşmenin kabul ettiği linkedin.com/in/… adresini alır. Geçersiz alan altında tek biçim hatası; girilen adres hata metninde tekrar edilmez. Link önizleme kartı, başlık/fotoğraf çekme, hesap doğrulama, logo veya marka rengi yok. Kanonikleştirme ve adres doğrulaması mevcut Code sözleşmesine aittir; HTML bu güvenlik doğrulamasını uygulamış sayılmaz.

Boş, geçersiz veya onaysız adresle Save pasif. Pasif neden satırı açıkça görünür ve düğmeye erişilebilir açıklama olarak bağlıdır. Open and check boş/geçersiz/çevrimdışı/busy hâlde pasif. Çevrimdışında durum + Try again bulunur; yeni ağ kuyruğu/otomatik açma eklenmez.

### Açma → uygulamaya dönüş → kullanıcı onayı

1. Open and check, Code'un kanonik adresini mevcut dış açıcıya verir; LinkedIn uygulaması veya tarayıcı. Sayfa uygulama içinde okunmaz/çekilmez.
2. Açma başarısızsa `linkOpenFailed`; onay penceresi açılmaz, Save pasif kalır. Çevrimdışında açma denenmez.
3. Başarılı açılıştan sonra uygulamaya dönüşte **tam ekran, kaydırılabilir mevcut onay şablonu**. %100 ve %200 aynı hiyerarşi:
   - Is this your LinkedIn profile?
   - Kanonik adres, seçilebilir düz metin; burada link düğmesi değil.
   - Geçici görünürlük kapalıysa durum notu.
   - P1 kim görür → P2 LinkedIn'deki ad/işyeri, gizli bilgi ve engelleme sınırı → P3 sayfanın okunmaması, kendi profilini ekleme.
   - Yes, it's mine / No.
4. Yes yalnız o açılan kanonik adrese ilişkin kullanıcı beyanıdır; Save'i etkinleştirir. Doğrudan kaydetmez, doğrulandı/verified iddiası oluşturmaz.
5. No form taslağını korur, Save pasif kalır. Metin değişirse önceki onay düşer; yeniden açma + dönüş + onay gerekir.
6. Kaydet: busy → sunucu onayıyla kayıtlı/success; hata taslağı/onaylı aynı adresi korur ve retry eylemi olarak Save kalır. Success yalnız sunucu kabulünden sonra. Yeni düzenlemede eski başarı/hata temizlenir.

### Kayıtlı / kaldırma

Kısa görünüm **LinkedIn** + Remove link; başkasının profilinde uzun adres yok. Sahibinin düzenleme alanı ve dönüş onayı adresi gösterebilir.

Remove link → nötr onay başlığı/gövdesi + mevcut contactSeenNote + Remove link / Cancel. Kırmızı tehlike yüzeyi yok. Cancel kaydı korur. İşlem sürerken çift gönderim engellenir; hata kaldırılmış gibi çizilmez, tekrar dene eylemi kalır. “Kaldırıldı” yalnız sunucu onayından sonra. Önceden görülmüş/kaydedilmiş bilgilerin geri alınabildiği izlenimi verilmez.

### Sunucu görünürlüğü geçici kapatırsa

Sahibine gelen güncel `linkedinShown`/mevcut izin durumu üzerinden not: **LinkedIn links aren't shown to others at the moment.** Brif wording'i aynen. HARBOR v2'nin yeniden görünürlük anlamını koruyan öneri ikinci cümle: kayıtlı tutulursa durum değişince tekrar görünebilir. Form ve dönüş onayında birlikte gösterilir. Neden/tarih/süre tahmini yok; kalıcı gizleme toggle'ı eklenmez. Ekleme/kaldırma mevcut sözleşmeyle devam eder; görünürlük kapalı diye yeni kaydetme yasağı icat edilmez.

## 5. B — başkasının profilinde

| Yüzey | LinkedIn | Amaç |
|---|---|---|
| Yakındakiler listesi | yok | mevcut oturum rozeti |
| Yakındakiler kişi profili | uygunluk varsa metin linki + izleyici notu | mevcut oturum rozeti; varsayılan ayar asla değil |
| Yanıt bekleyen gelen istek profili | uygunluk varsa metin linki + izleyici notu | **rozet/metin yok** |
| Giden istek / Bağlantılar / sohbet / eşleşme / Engellenenler | yok | mevcut yüzey kuralı; bu iş değiştirmez |
| Nötr/geçersiz/süresi dolmuş istek kartı | yok | mevcut kural |

Link hemen altında `profileLinkedinViewerNote`; her gösterimde, ilk seferle sınırlanmaz. Tıklanınca mevcut dış açıcı. Açılamazsa sakin satır + Try again; link metni aynı. Çevrimdışı hâlde dış açma denenmez. Alan sunucudan gelmiyorsa link, ikon, izleyici notu ve boş bağlantı alanı çizilmez. Eski gelen istekten kabul sonrası taşınan bağlantıyı eşleşme ekranında gösterme. İzin/erişim değişince canlı görünürlük Code'un mevcut kurallarından gelir; gizliliği yalnız istemcide gizleyerek uygulama.

Mevcut kabul/ret/merhaba kontrolleri görsel bağlam için korunur; yeni davranış eklenmez. Profil fotoğrafı/diğer bilgiler bu bölüm önizlemesinde temsil edilmedi; native profil alanları kaldırılmaz.

## 6. Erişilebilirlik

Başlık semantiği; radio group ve checked durumu; seçili alanın ekran okuyucuda anlaşılması. Dış bağlantı gerçek link semantiği, adı LinkedIn profile; hint “Opens in the LinkedIn app or your browser.” İkon dekoratif, ayrı erişim hedefi değil. Düğme/bağlantı≥48. Hata alanla ilişkilendirilir; durum satırı uygun live region. Onay açılınca odak başlığa, kapanınca formdaki ilgili eyleme geri dönmeli; native VoiceOver/TalkBack Code tarafından ölçülür. Browser DOM kontrolleri native uygunluk sertifikası değildir.

## 7. Metin ve kaynak farkı

34 proposed anahtar EN/TR; 27 mevcut anahtar yalnız referans. `COPY-REVIEW.md` her satırın kaynağını ve HARBOR v2 ile farkı gösterir.

Founder brifindeki kısa EN taslaklar aynen. Yereldeki HARBOR v2 onaya hazır dosya; onaylı sayılmadı. Üç uzun paragraf oradan aynen alındı. Özellikle amaç açıklaması, biçim hatası, geçici kapatma notu ve apostrof farkları sessizce birleştirilmedi. Nihai HARBOR + Founder metni gelince ayrı delta gerekir; bu proposed ARB'leri tam ARB üzerine yazma.

## 8. Görüntülerin okunması / açık noktalar

35 durum; EN/TR ×100/200%; 390×844 mantıksal alanın 4× PNG çıktıları. `--full.png` kaydırılabilir içeriğin tamamıdır; yeni telefon oranı veya tek ekrana sığma vaadi değildir. Önizlemede 320/390/412 ve iOS/Android kabuğu seçilebilir.

Örnek A dışında gerçek kişi yok, portre yok. `linkedin.com/in/…` ve `https://www.linkedin.com/in/…` yalnız biçim yer tutucusu; gerçek/geçerli kişi adresi değildir. HTML gerçek LinkedIn sayfası açmaz ve profil/oturum kaydetmez; dış açılış ve sunucu yanıtları telefon dışındaki inceleme kontrolleriyle simüle edilir. Kullanıcının kendi URL'sinin doğrulanması/native dış açılış platform testidir.

Ürün davranışı için yeni açık soru yok. Bekleyen tek onay: HARBOR + Founder nihai metinleri ve COPY-REVIEW'daki kaynak farklarının kapatılması. Yeni bileşen veya renk ailesi gerekmiyor.
