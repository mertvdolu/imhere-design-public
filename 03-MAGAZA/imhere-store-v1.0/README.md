# IM HERE — Mağaza görselleri v1.0

Cream & Ink **v2.2** için İngilizce mağaza tasarım teslimi. **19 tanıtım PNG + 19 düzenlenebilir SVG + güncel 512×512 Play simgesi.** Dosyalar ayrı ayrı sürümlenir.

## Başlangıç

- [HTML önizleme](ONIZLEME.html) — indirip tarayıcıda aç; internet gerekmez.
- [App Store toplu bakış](review/app-store-contact-sheet.png)
- [Google Play toplu bakış](review/google-play-contact-sheet.png)
- [Google Play öne çıkan görsel](google-play/feature-graphic.png)
- [Manager notu](MANAGER-NOTU.md) · [Dosya listesi](DELIVERY.json) · [Doğrulama](evidence/validation.json)

## Teslim klasörleri

| Kullanım | Klasör | Ölçü | PNG adedi |
|---|---|---|---|
| iPhone 6,9 inç | `app-store/iphone-6.9/` | 1320×2868 | 6 |
| iPhone 6,5 inç | `app-store/iphone-6.5/` | 1242×2688 | 6 |
| Google Play telefon | `google-play/phone/` | 1080×1920 | 6 |
| Google Play öne çıkan görsel | `google-play/feature-graphic.png` | 1024×500 | 1 |

Ekran görüntüsü ve öne çıkan görsel PNG'leri opak, 8 bit/kanal RGB (24 bit), sRGB. Uygulama simgesi ayrı olarak 512×512 RGBA'dır. Mağaza panellerine yalnız PNG'ler yüklenir; yanlarındaki SVG'ler düzenlenebilir kaynaklardır. Telefon karelerinin sırası: **01 açılış/niyet · 02 Yakındakiler · 03 tam ekran harita · 04 Bağlantılar · 05 Sohbet · 06 Profil**.

Açılış karesi, uygulamanın niyet seçimini gösteren tanıtım girişidir; yerel splash ekranını veya onboarding davranışını değiştirmez. App Store'da yalnız logo/splash yerine uygulamanın kullanımını gösterir.

## Kaynak ve yayın öncesi son adım

**Bunlar onaylı tasarımın ekran çizimleridir; native iOS/Android derlemesinden alınmış cihaz görüntüleri değildir.** Tasarım teslimi tamamdır. Mağazaya göndermeden önce Manager/Code güncel native ekranlarla karşılaştırmalıdır. Yerleşim farklıysa aynı kompozisyon içindeki ekran alanı, aynı kurmaca örnek içerikle alınmış native görüntüyle değiştirilir. Mağazalara yükleme/yayınlama bu işte yapılmadı.

- Görsel kaynak: `02-SON-EKLER/imhere-cream-complete-v2.2`, commit `f3dbd40bdedad4ec0b3ed06f38b72d1c1cfcebf2`.
- Renkler, Geist, orijinal iki daireli logo ve ortak bileşen dili v2.2'den gelir. Kullanılan logo dosyası değiştirilmemiştir.
- Harita onaylı `map-ready` katalog çizimidir. Şematik zemin ve örnek renk alanlarıdır; gerçek/coğrafi konum veya güncel yoğunluk iddiası yoktur. `Illustrative map · Not live data` notu görünürdür. Harita karesinde profil işareti, kişi sayısı ve mesafe yok; mavi/sarı/yeşil/kırmızı ve **© OpenStreetMap contributors · OpenFreeMap** korunur. Kaynakta bulunan OpenMapTiles attribution'ı da korunur.
- Maya ve Alex tamamen kurmaca örnek profillerdir; fotoğraflar sıfırdan yapay olarak üretilmiştir. Gerçek kişi fotoğrafı, hesap veya iletişim bilgisi kullanılmadı. Görsellerde `Fictional profiles · Illustrative content` notu vardır. Kareler bağımsız durum örnekleridir; tek hesabın ardışık oturum kaydı değildir.
- İki niyet, boş başlangıç ve seçim yapılmadan pasif istek eylemi gösterilir. Bağlantılar ve İstekler aynı Mesajlar alanındadır; kapalı kartın açıklaması nötrdür.
- Yazılabilir sohbet karesinde saklama satırı **yoktur** (ENG-M10-08(5)). Medya/düzenleme/silme eylemi yoktur; klavye kapalıdır. Mesaj hakkı/karakter sayacı ürün arayüzüne aittir; haritada kişi sayısı gösterilmez.
- Profilde yaş/cinsiyet gizli, meslek görünür örnek veri kullanılır. Bu seçimler varsayılan davranış değişikliği değildir.

## Yeniden üretim

`source/build.py` SVG'leri üretir; Pillow gerekir. `source/render.cjs` PNG'leri ve toplu bakışları üretir; Node + sharp gerekir. Fontlar ve örnek fotoğraflar pakettedir. `source/marketing-copy.en.json` başlıkların referans listesidir; başlık değişikliği `build.py` içindeki SHOTS bölümüne de uygulanır. `source/ui-copy.en.json` yalnız tasarım referansıdır, uygulamanın ARB dosyasının üzerine yazılmaz.

`source/IMAGEGEN-PROMPTS.json` üretim aracını ve portre komutlarını; `source/PROVENANCE.md` kaynakları açıklar. `MANIFEST.json` bu teslimin tüm dosya boyutlarını ve SHA-256 özetlerini içerir.

## Kontrol edilen mağaza kaynakları — 23 Eylül 2026

- [Apple screenshot ölçüleri](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications): seçilen iki ölçü kabul edilen boyutlardandır; alpha yoktur.
- [Apple App Review §2.3.3 ve §2.3.9](https://developer.apple.com/app-store/review/guidelines/#accurate-metadata): uygulama kullanımını gösterme ve kurmaca hesap bilgileri.
- [Google Play görsel gereksinimleri](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en-GB): öne çıkan görsel 1024×500; telefon seti 9:16, 1080×1920; opak RGB PNG.

Teknik ölçü ve tasarım kontrolleri mağaza kabulü veya fiziksel cihaz doğrulaması anlamına gelmez.

## Güncel Google Play simgesi

Mağaza yüklemesinde [google-play/app-icon-512.png](google-play/app-icon-512.png) kullanılır: **512×512, RGBA**, güncel Cream & Ink v2.2 simgesinin yeniden boyutlandırılmamış, yeniden kodlanmamış birebir kopyası. Paket 19 tanıtım karesi + 1 uygulama simgesi içerir. Eski A-wordmark ve B-symbol kullanılmaz.
