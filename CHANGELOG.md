# Değişiklik kaydı

## 2026-10-03 — Events V1 / mobil tasarım eki v1.0

- Founder onaylı sınırlı Events kapsamı için 36 liste/detay/RSVP/iptal/kilit/değişiklik/takvim/harita durumu; EN/TR, iOS/Android, 320/390/412, %100/%200 önizleme.
- Cream & Ink v2.3 + v10 kompakt bileşenler, 48 hedef, yüksek kontrast/azaltılmış şeffaflık/hareket; katılımcı sayısı/listesi/avatarı ve check-in bağı yok.
- 52 yeni EN/TR metin **PROPOSED**: Founder onayı olmadan canonical ARB'ye birleştirilmez; migration kaydı eklenmedi.
- `02-SON-EKLER/imhere-events-v1.0/HANDOFF.md`, `SPEC.md`, `catalog.json`, `SCREEN-STATE-MATRIX.md`, `tokens.components.json`, önizleme ve doğrulama kaydı. 299 eski durum, uygulama/backend ve mağaza varlıkları değiştirilmedi. Üretim yayını ayrı kapı.

## 2026-10-01 — Cream & Ink v2.3 / Hafif kabartma (02)

Founder'ın onayladığı hafif kabartma bütün güncel tasarım yüzeylerine uygulandı. 299 temel durum / 2.392 SVG / 598 PNG; v10 sıkı yerleşim ve v9 iletişim kartı HTML ekleri. Siyah ana eylem, kabartmalı krem ikincil yüzey, içe oturan alan; en az 48 hedef. Token 2.3; dosya yolları korunur. Logo, harita renkleri, ürün kuralları ve HARBOR uyarıları değişmez.

Ek tutarlılık: boş Save serbest kararı (88567c9) kart HTML/cataloguna işlendi; boş Send pasif. `contactCardProfileHelp` EN/TR tek anahtarlı delta + migration. Tam ARB'ler korunur. Yüksek kontrast / azaltılmış hareket / opak menü kuralları. 60 tarayıcı kontrolü; SVG metin ve geometri koruma doğrulaması. Yerel teslim; native uygulama ve mağaza görüntüleri Code aktarımı/cihaz turundan sonra.

[Önizleme](02-SON-EKLER/imhere-cream-complete-v2.2/theme-v2.3/ONIZLEME.html) · [Rapor](02-SON-EKLER/imhere-cream-complete-v2.2/theme-v2.3/RAPOR.md) · [Spesifikasyon](02-SON-EKLER/imhere-cream-complete-v2.2/theme-v2.3/SPEC.md)


## Neumorphism görsel denemesi v1.0 · 2026-10-01

- `05-INCELEMELER/imhere-neumorphism-study-v1.0/ONIZLEME.html`:4 buton yoğunluğu örneği, her biri düz/hafif/belirgin kabartma karşılaştırması. Eşzamanlı örnek seçimler, büyük yazı ve klavye görünümü.
- İnceleme çalışmasıdır; onaylı tema veya native uygulama değişikliği değildir.

## İletişim kartı — boş kaydetme kararı · 2026-09-28

- Manager kararı SPEC §2’ye işlendi: boş Save serbest (kartı silme hakkı); boş Send pasif. Önceki pasif Save yorumu geçersiz. Ek çizim/ARB değişmedi.

## Sürüm9 iletişim kartı tamamlayıcı v1.1 · 2026-09-28

- Dört eksik parça,16 önizleme durumu;12 EN/TR anahtar delta. `contact-card-v1.1/HANDOFF.md`.
- HARBOR §H önceliği ve eski uyarılar korundu; yalnız kendi profil bölümü. Save boşluk kuralındaki kod/talep farkı SPECte açık.
-32 tarayıcı boyut/hedef kontrolü; native uygulama Code'da. v10 kabuğu erkenden uygulanmadı.

## Sıkılaştırma v10 · tasarım eki v1.0 · 2026-09-28

- 12 önce/sonra HTML örneği, kompakt kontrol ölçüleri ve yüzen menü; kurulum/klavye/tam ekran rapor istisnaları.
- HARBOR konum metni aynen; 5 EN/TR yerleşim anahtarı delta. Referans JPG/HTML dosyaları depoya alınmadı.
- `02-SON-EKLER/imhere-cream-complete-v2.2/compact-v10-v1.0/HANDOFF.md`; native uygulama/test Code tarafından. Eski SVGler tarihsel.

## Networking kaydırıcı uç metinleri v1.0 · 2026-09-28

- Sol Friends / Arkadaşlık, sağ Networking / Networking; iki anahtar EN/TR delta + migration.
- `compact-signals-v1.0/SLIDER-ENDPOINTS.md`; sonraki paket, sürüm8 engeli değil.

## Sürüm8 birleşik ARB onayı v1.0 · 2026-09-28

- Code’un9 bekleyen anahtarı mevcut isimleriyle onaylandı; oran alias eşlemesi ve e-posta değiştirme tüm durumları. Birleşik18 anahtar EN/TR delta + migration.
- E-posta nötr sonuç metni gerçek gönderim garantisi vermez; mevcut emailUnavailable/ok ortak ekranıyla uyumlu.
- `release8-copy-v1.0/HANDOFF.md` + integration.json + renk deltası. Native birleştirme/test Code’da.

## Sürüm8 kompakt oran + okunmamış nokta v1.0 · 2026-09-28

- Çerçevesiz profil oranı ve tek0–100/10 adımlı kaydırıcı; ayarlanmamışta profil satırı yok.
- Satır/sekmede8 dp okunmamış nokta: notificationUnread#B63A32; harita densityRed değişmez. Beş EN/TR anahtar delta + migration.
- `compact-signals-v1.0/`: SPEC, token eki, katalog ve interaktif HTML. Genel sıkılaştırma kapsam dışında, native test Code’da.

## İletişim kartı üç durum v1.0 · 2026-09-28

- HARBOR metinleriyle ilk gönderim onayı, boş kart/pasif Send ve sonraki gönderim uyarısı;6 anahtar EN/TR delta + migration.
- `contact-card-v1.0/`: spesifikasyon, ek katalog ve büyük yazı/telefon genişliği seçenekli HTML önizleme. Diğer ürün önerileri kapsam dışında; native test yapılmadı.

## Native mağaza v1.2 kısmi teslim · 2026-09-27

- Gelen native çekimlerle13 mağaza karesi; Maya portresi mevcut yuvalarda, kurmaca etiketleri korunur. iOS01–05 iki boyut; A13 01/04/05. Android02/03 ve fotoğraf yuvalı06 bekler.
- Sohbet sayacı Your message üstünde8 dp ile sabit blokta onaylandı. Başkasının profilinde mevcut profileLanguagesLabel: Languages spoken / Konuşulan diller; delta + kullanım notu.
- Giriş: `03-MAGAZA/imhere-store-v1.2/README.md`. Set henüz tam yayın paketi değil; yerel commit.

## Mağaza sahne uyumu + konum marka boşluğu · 2026-09-27

- Walking kaldırıldı; Design + Coffee korundu. Bağlantı listesinin son mesaj önizlemesi kaldırıldı; SVG/PNG ve üretim kaynağı güncellendi.
- locationPermissionRationale EN/TR yalnız marka boşluğu U+00A0; ayrı delta + migration. Native portresiz görüntüler bekleniyor; sentetik portre/etiket talimatı kaydedildi.
- Devir: `specs/STORE-SCENE-LOCATION-NOWRAP-2026-09-27.md`.

## Marka başlığı bölünmez boşluk · 2026-09-27

- appTitle EN/TR: mevcut I’M HERE yazımı korunarak boşluk U+00A0 yapıldı; ARB delta + migration.
- Büyük metinde kırpma/küçültme yerine yeterli genişlik; native doğrulama Code’da. Devir: `specs/BRAND-NOWRAP-2026-09-27.md`.

## Sürüm 6 son üç metin onayı v1.1 · 2026-09-26

- authConsentLine TR sen dili, HARBOR I-7 uzun locationPermissionRationale ve mapShowMyArea EN/TR onaylandı; üç anahtarlı ARB delta + migration.
- Uzun konum metni için kaydırılabilir yerleşim onayı; A13 kayıt bağlantıları kabul,48 dp korunarak yalnız düğme öncesi boşlukta isteğe bağlı16→8 önerisi.
- Devir: `specs/V6-FINAL-COPY-APPROVAL.md`; Code uygulama listesini kapatır, cihaz ölçümü ayrıca. Yerel commit.

## Mağaza metin revizyonu v1.1 · 2026-09-26

- Onaylı02/05/06 ve öne çıkan metinleri10 SVG/PNG’ye aktarıldı; kaynaklar, önizlemeler ve manifest güncellendi.
- `03-MAGAZA/imhere-store-v1.0/COPY-v1.1-HANDOFF.md`: eski telefon içi çizim farkları açıkça kaydedildi; native karşılaştırma tamamlanmadan yayın hazır değil.

## Sürüm 6 kayıt ve konum tasarım onayı · 2026-09-26

- Beş TR/EN anahtar delta + migration: metinler onaylandı; kayıt bağlantıları için48×48 hedef düzeltmesi ve serbest satır kaydırma tanımlandı. Konum açıklaması yerleşimi onaylandı.
- `specs/V6-REGISTER-LOCATION-APPROVAL.md`: uygulama listesini Code günceller; cihaz/Play uygunluk onayı değildir. Mağaza yeniden üretimi ayrı teslim.

## BEACON GECE02 kaynak incelemesi v1.0 · 2026-09-26

- G02-1 yanlış/eksik kurallar bölüm bazında işaretlendi; güncel kaynaklara bağlı düzeltilmiş sistem özeti eklendi. Logo için yalnız brand/README; geri çekilmiş kılavuz ölçüleri aktarılmaz.
- G02-4 §4 mağaza metni kararları kaydedildi. Mağaza JSON/SVG/PNG değişmedi; yeniden dışa aktarım ayrı. Skill kurulmadı, uygulama/ürün davranışı değişmedi.
- Teslim: `05-INCELEMELER/beacon-gece02-v1.0/INCELEME.md`. Yerel commit; aktarım Code.

## Firebase e-posta metinleri EN v1.0 · 2026-09-26

- IM HERE gönderen adı, doğrulama ve şifre sıfırlama konuları, %LINK% içeren üç cümlelik sıfırlama gövdesi.
- Doğrulama gövdesi değişmez. Konsola aktarım Code/Founder; yalnız yerel metin teslimi. Devir: `specs/FIREBASE-EMAIL-COPY-EN-v1.0.md`.

## Sesli bildirim kanalı · 2026-09-26

- Messages and connections / Mesajlar ve bağlantılar kanal adı + açıklaması TR/EN eklendi. Üç tür: kabul, mesaj, iletişim paylaşımı; varsayılan ses+titreşim.
- Updates / Güncellemeler adı değişmez; düşük öncelikli türler sessiz, CH-133 ve adsız gövdeler korunur.24 katalog kaydı; ARB delta + kanal sözleşmesi.

## H0 S2 — tek portre · 2026-09-25

- Statik tek karşı taraf fotoğrafı korundu;06 hareketi ve GIF/CSV tek portreye uyarlandı. Kendi fotoğrafı gerekmez; fotoğraf yok örneği nötr placeholder.
- Haritada dalga, bekleyen ekranda Hello sent, iOS sistem rota geçişleri kaydedildi. Devir: `motion/hareket-ve-his-v1/S2-DECISION.md`.

## Bildirim metinleri v2 · 2026-09-25

- Kabul / iletişim paylaşımı bildirim gövdeleri TR/EN eklendi; notificationIntro yeniden istek ve mesajları kapsar. Adsız, başlıksız; CH-133 değişmez.
- İki yeni içerik durumu,24 SVG /6 PNG; üç anahtarlı ARB delta. Devir: `specs/NOTIFICATION-V2-COPY.md`.

## Cream & Ink v2.2 — H0 hareket finali · 2026-09-25

- Plan belirteçleri korundu;7 imza an zamanlaması ve60fps kare tabloları tamamlandı. GIF süreleri3.04–5.72s; gerçek tema renkleri ve composer içi Send ile yeniden üretildi.
- §6 his haritası,297 durum eşleştirmesi ve tek dosyalık `motion/hareket-ve-his-v1/H0-DELIVERY.md` teslim girişi. Uygulama kodu/dependency değişikliği yok. Yerel commit; aktarım Code.

## Cream & Ink v2.2 — T1 geri alma / bildirim kapsamı · 2026-09-25

- FD-47/FD-40: aktif oturumda I’m still here ve Stop korundu; T1 öncesi8 durum geri getirildi. T2–T4 ve H teslimleri değişmez.
- notificationIntro TR/EN yalnız bağlantı isteklerini anlatır; delta ile birleştirme. Katalog, çizimler ve MANIFEST güncellendi. Yerel teslim; aktarım Code.

## Cream & Ink v2.2 — Dev turu H2/H7/H9/H3 · 2026-09-24

- Alt sayfalarda48×48 geri; kurulumda Çıkış yap istisnası. Sohbet başlangıç kartı kaldırıldı, gönder simgesi composer içine taşındı.
- Yeni chat-contact-invite ve iki TR/EN delta anahtarı; profil kaydı sonrası150ms dönüş notu. H7(c) sayaç eşiği önerisi Founder onayı bekler, uygulanmadı.
- Devir: `02-SON-EKLER/imhere-cream-complete-v2.2/specs/DEV-TOUR-H2-H7-H9-H3.md`. Yerel commit, aktarım Code.

## Cream & Ink v2.2 — Founder T1–T4 · 2026-09-24

- Aktif check-in: tek durum + Stop; niyet: ince çipler; sohbet: sağ üst Safety/Continue simgeleri; paylaşılan iletişim: sağ kalem.
- 35 durum /280 SVG /70 PNG; TR/EN, iOS/Android ve büyük metin. Yeni metin yok; ARB ve beta kapsamı korunur.
- Devir: `02-SON-EKLER/imhere-cream-complete-v2.2/specs/FOUNDER-PHONE-T1-T4.md`. Yerel teslim, aktarım Code.

## Cream & Ink v2.2 — Code uyumu CH-141–143 · 2026-09-24

- Report sonucu: reportSent + blockDone + Go back; ayrı engelleme akışı ve üç eski durum kaldırıldı.
- Profil altına Safety ikincil düğmesi; üst bayrak yerine Şikâyet/Engelle menüsü, End yok. Kapalı bağlantı tek başına merhaba eylemini engellemez.
- Kapalı kartın kaldırılması ve End onayı e1c7aed ile zaten hazır; 6.kategori079ee74 ile hazır. Tek code-alignment ARB deltası aynı teslimde birleştirildi.
-80 SVG /20 PNG güncellendi/eklendi;24 SVG /6 PNG eski rapor durumu çıkarıldı. Güncel296 durum. Yerel teslim.

## Cream & Ink v2.2 — End connection onayı · 2026-09-24

- Onay penceresi:30 günlük güvenlik saklama/silme, listeden kalkma ve iki taraf isterse yeniden bağlanma; EN/TR delta. Ana End connection, Report instead ve Cancel.
- Report instead yalnız şikâyet akışını açar; bağlantıyı bitirmez.
- Founder kararı değişti: `connections-open-closed` yerine `connections-after-end`; kapalı kart listede tutulmaz. Motion `closed-card-preserved` kaldırılıp `ended-card-removal` eklendi.
- 16 SVG /4 PNG; toplam298 durum ve mevcut beta kapsamı korunur. Tam ARB üzerine yazılmadı. Yerel teslim.

## Cream & Ink v2.2 — Hareket ve His v1.0 · 2026-09-24

- 5 motion token grubu, kesin Flutter yay katsayıları; 7 imza an için zamanlama, titreşim, veri tetikleyicisi, iptal ve azaltılmış karşılık.
- 7 karşılaştırmalı GIF, 7 poster,60fps CSV kare tabloları ve yerel önizleme. Bütün298 katalog durumuna hareket referansı.
- Founder açıklaması: varlık dalgası harita kenarından; kişisel konum noktası yok. Kapalı bağlantı kartı korunur.
- `motionHelloSent` TR/EN ayrı delta; canlı ARB üzerine yazılmaz. Yeni runtime bağımlılığı ve native uygulama değişikliği yok. Yerel commit, aktarım Code.

## Cream & Ink v2.2 — Profilden şikâyet · 2026-09-24

- 8 kişi/profil durumu, 64 SVG / 16 PNG: sağ üst bayrak → mevcut altı kategorili şikâyet formu. Hedef 48×48, mevcut `reportTitle` erişilebilir adı. Kendi profilinde gösterilmez.
- Şikâyet sonrası ayrı engelleme sorusu korunur; bağlantı bitirme eylemi bu girişe eklenmedi. Yeni ARB anahtarı yok. Yerel teslim.

## Cream & Ink v2.2 — Altıncı şikâyet kategorisi · 2026-09-24

- `reportChildSafety`: EN “Underage user or child safety”; TR “Reşit olmayan kullanıcı veya çocuk güvenliği”. Safety concern sonrasında, Other öncesinde.
- Beş seçim durumu × sekiz varyant güncellendi; 40 SVG / 10 PNG. Yeni durum veya beta değişikliği yok.
- Yalnız yeni ARB deltaları + migration; tam ARB dosyalarına dokunulmadı. Yardım satırı ve yeni operasyonel vaat eklenmedi. Yerel teslim, aktarım Code.

## Cream & Ink v2.2 — Founder telefon turu · 2026-09-24

- Own-profile: sağ üstte kalem ve dişli; alt düzenleme düğmesi kaldırıldı. 16 çizim güncellendi. `profileHiddenToOthers`: EN “Not visible to others” / TR “Başkalarına görünmez”; yalnız kendi gizli alanlarının altında.

- Fotoğraf yükleme ve işleme ayrı durumlar olarak eklendi: 16 SVG / 4 PNG, TR/EN, iOS/Android, normal/büyük metin. İki yeni anahtar: `photoUploading`, `photoProcessing`; başarı için mevcut `photoUploaded` korunur.
- Klavye kapatma ve Done çubuğu, iOS çark / Android takvim kararları `contracts/profile-inputs.json` ve [telefon turu devrine](02-SON-EKLER/imhere-cream-complete-v2.2/specs/TELEFON-TURU-2026-09-24.md) işlendi. 56 tarih alanı tanımı okunur, yazı girdisi almayan platform seçicisi olarak belirtildi.
- Yeni durumlar beta: true. Toplam 298 durum / 2384 SVG / 596 PNG; own-profile dışındaki mevcut ekran görselleri ve önceki beta kararları değişmedi.
- Yerel teslim; GitHub aktarımını Code yapar. Native uygulama değiştirilmedi.

## Cream & Ink v2.2 — CH-138, ERT-050 ve Code soruları · 2026-09-23

- CH-138: e-posta kartı canlı TR/EN metinlerine hizalandı; mevcut ikincil giriş düğmesi eklendi. ERT-050: kayıt deneme sınırı için 8 varyant ve beta işareti eklendi.
- Tekrar doğrulama gönderimi `authVerifyResending` metniyle ilk gönderimden ayrıldı. Toplam 24 SVG ve 6 PNG üretildi/güncellendi; katalog 296 durum / 2368 SVG / 592 PNG.
- `sectionTitle` 18/500, `status` 16/500, `helper` 14/400 tokenları eklendi; beş Material ikon eşlemesi onaylandı.
- ERT-046'nın dört durumu da `8078bfb` içinde mevcut; 32 varyant kontrol edildi, çizimleri değişmedi. [Yedi madde için devir notu](02-SON-EKLER/imhere-cream-complete-v2.2/specs/CODE-SORULARI-CH138-ERT050.md).
- Güncel 512×512 RGBA Play simgesi mağaza paketine birebir kopyalandı; eski A-wordmark ve B-symbol klasörleri “ESKİ — kullanma” olarak işaretlendi.
- Referans metinler, delta/migration, kataloglar ve doğrulama güncel. Yerel commit teslimi; GitHub aktarımını Code yapar.

## Cream & Ink v2.2 — hata ekranlarında yeniden deneme · 2026-09-23

- `nearby-failed`, `nearby-offline`, `map-failed`, `map-offline` çizimlerine mevcut `checkInRetry` anahtarıyla ikincil **Try again / Tekrar dene** düğmesi eklendi.
- TR/EN, iOS/Android ve %100/%200 metin boyutlarında 32 SVG ile 8 PNG güncellendi. Haritada düğme alt panelde, hata açıklamasından sonra ve attribution’dan önce yer alır.
- Ekran manifesti, tasarım devri ve doğrulama kayıtları güncellendi. Ürün davranışı, diğer durumlar ve beta işaretleri korunur.

## Mağaza görselleri v1.0 — 2026-09-23

- [03-MAGAZA/imhere-store-v1.0](03-MAGAZA/imhere-store-v1.0/): App Store 1320×2868 ve 1242×2688 için altışar kare; Google Play 1080×1920 için altı kare ve 1024×500 öne çıkan görsel. Toplam 19 PNG + 19 düzenlenebilir SVG.
- Cream & Ink v2.2; İngilizce başlıklar; kurmaca profil/fotoğraf açıklamaları; tam ekran harita, dört renk ve zorunlu attribution. Yazılabilir sohbette saklama satırı yok.
- Yerel HTML önizleme, toplu bakışlar, kaynak/üretim dosyaları, manifest ve doğrulama eklendi. Native çekim karşılaştırması yayın öncesi adımdır; uygulama ve mağaza kaydı değiştirilmedi.

## Cream & Ink v2.2 — bütün mobil tasarım tamamlandı

- [Tam paket](02-SON-EKLER/imhere-cream-complete-v2.2/): eski 287 durumun tamamı yeniden çizildi; 8 güncel ekle 295 durum, 2360 SVG, 590 PNG. TR/EN, iOS/Android, %100/%200.
- Kök ONIZLEME.html ve EKRAN-KATALOGU.json artık yalnız yeni krem/siyah ekrana yönlenir; eski yeşil paketler arşivde korunur.
- Tüm giriş/profil, Nearby/check-in, istek/eşleşme, sohbet/devam/contact, güvenlik, Ayarlar, bildirim ve Events durumları ortak yeni görsel dilde.
- Harita cihaz ekranını kaplar; açıklama sheet’i ayrı. MapLibre/OpenFreeMap attribution ve dört semantik band korunur.
- Orijinal iki daireli logo; açık uygulama simgesi, splash ve doğrudan işaretten türetilmiş saydam beyaz Android küçük simgesi.
- Son metin/yerleşim ekleri çizimlerde: saklama bilgileri, nearbyLimited, visibilityHelp, photoUploaded, onboarding authSignOut, destek satırı, kapalı kart ve ek contact paylaşımı.
- Yeni iki yardımcı metin: supportCopyEmail / supportEmailCopied; delta + migration.json, tam ARB üzerine yazılmaz. Ortak token sürümü 2.2; büyük başlık satır yüksekliği 1.12, büyük metin alt barı 184.
- [Manager notu](02-SON-EKLER/imhere-cream-complete-v2.2/MANAGER-NOTU.md), [tasarım devri](02-SON-EKLER/imhere-cream-complete-v2.2/specs/TASARIM-DEVRI.md), manifest, SVG sınır/kapsam kontrolleri ve masaüstü/mobil HTML kanıtları eklendi. Live map önizlemesi yüklendi.
- Flutter/backend değiştirilmedi; fiziksel cihaz/native entegrasyon testi bu tasarım kontrolüyle tamamlandı sayılmaz. Dosyalar tek tek yüklenir.

## Cream HTML v1.1 — Founder logosu

- Kullanıcının gönderdiği orijinal iki daireli logo krem HTML başlığına ve uygulama üst alanlarına eklendi.
- assets/imhere-mark.svg ve imhere-mark-icon-weight.svg değişmeden kullanıldı; PDF kılavuz yayımlanmadı.
- [Önizleme ve notlar](02-SON-EKLER/imhere-cream-study-v1.0/LOGO-GUNCELLEMESI-v1.1.md); REVIEW ve manifest güncel. Klasör adresi korunuyor.
- Tam ekran harita yerleşimi Founder onayı güncel karar notuna işlendi.
- Native uygulama ve simge varlıkları değişmedi.


## Cream & Ink ana tema seçildi — token v2.1

- Founder Cream study v1.0 yönünü onayladı; Forest & Mint aktif tema olmaktan çıktı, arşivde korunuyor.
- Ortak theme.tokens.json krem/siyah eşlemesine ve light moda güncellendi.
- [Geçiş teslimi](02-SON-EKLER/imhere-cream-theme-v1.0/): tokenlar, EN/TR krem alt harita, eski tema referansı, doğrulama ve Manager notu.
- HTML incelemesinin onay durumu güncellendi. Dört band rengi ve ürün kuralları aynı.
- Native uygulama değişmedi; eski ekran çizimleri topluca yenilenmedi.


## Cream study v1.0 — Görsel alternatif

- Founder talebiyle krem/siyah tema için [altı ekranın HTML denemesi](02-SON-EKLER/imhere-cream-study-v1.0/) eklendi.
- Yakındakiler, tam ekran harita, Bağlantılar, Sohbet, Profil, Ayarlar; Krem/Beyaz ve ×1,55 metin seçenekleri.
- Ana tema, logo dosyaları, ürün kuralları ve uygulama kodu değişmedi. Onay bekleyen görsel alternatif; native final paket değil.
- [Manager notu](02-SON-EKLER/imhere-cream-study-v1.0/MANAGER-NOTU.md) ve REVIEW.png içerir.


## A4 devam v1.0 — B seçimi sonrası

- Founder B-symbol seçti; A uygulanmayacak. Simge klasörünün seçim kaydı, README, spec ve manifesti güncellendi; simge geometrisi aynı.
- [Yeni teslim](02-SON-EKLER/imhere-a4-suite-v1.0/): resmî bildirim küçük simgesi, B ile yerel açılış varlıkları ve EN/TR koyu OpenFreeMap MapLibre stilleri.
- Code türetmesi görülmedi; yerine resmî küçük simge sağlandı.
- Dil, panel ve bildirim soru yanıtları KARAR-KAPANISLARI.md içinde.
- Map EN/TR tarayıcı çizimi geçti; native entegrasyon/görüntü karşılaştırması bekliyor.


## Uygulama simgesi v1.0 — 2026-09-22

- Founder kararı: telefondaki ad **IM HERE**, büyük harf ve kesme işaretsiz.
- [Simge adayları](02-SON-EKLER/imhere-app-icon-v1.0/): A yazılı, B yazısız; Founder seçimi bekleniyor.
- [Karşılaştırma](02-SON-EKLER/imhere-app-icon-v1.0/KARSILASTIRMA.png), SVG/PNG kaynaklar ve Android adaptif katmanları dosya bazlı eklendi. Tema renkleri korunuyor.
- Eski geçici simgenin yerine geçecek aday henüz seçilmedi; uygulama değiştirilmedi.
- Splash, bildirim küçük simgesi ve koyu harita kapsam dışında; sonraki teslimler.


## v2.0 — Dosya bazlı depo yayını · 2026-09-22

- Önceden tek ZIP olarak verilen 3.426 dosya depo köküne klasörleri korunarak aktarıldı.
- Tasarım içeriği değiştirilmedi; tüm dosyalar yerel v2.0 toplamasıyla aynı.
- Güncel metinler: `03-GUNCEL-ORTAK/l10n/`.
- Son kararlar: `04-GUNCEL-KARARLAR.md`.
- Son ekler: `02-SON-EKLER/`; ekranlar ve önceki paketler: `01-PAKETLER/`.
- Eski v2.0 ZIP eki kaldırıldı; sürüm açıklaması dosya yollarına yönlendirildi.
- Birleştirme kuralları değişmedi: canlı ARB dosyalarının tamamının üzerine yazılmaz.
