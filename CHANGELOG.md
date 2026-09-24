# Değişiklik kaydı

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
