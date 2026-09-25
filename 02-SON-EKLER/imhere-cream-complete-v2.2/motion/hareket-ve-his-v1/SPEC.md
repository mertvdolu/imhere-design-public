# Hareket ve His — Uygulama spesifikasyonu v1.0

**Cream & Ink v2.2 · 25 Eylül 2026 · H0 final · Tasarım teslimi; native uygulama değildir.**

## Kaynak ve kararlar

Founder onaylı kaynak `source/hareket-ve-his-plani-v1.md` arşivlendi. Plandaki 295 durum sayısı eski; güncel katalog **297 durum / 2376 SVG**. Bu iş yeni ekran durumu eklemez.

- Founder ek yanıtı: “sınırların kenarından … 0 noktasından başlamasın”. Varlık dalgası **harita viewport kenarından içeri** başlar; coğrafi sınır/yarıçap, kendi noktan veya başka kişi işareti değildir. Dört semantik harita rengi, sayısız/mesafesiz gösterim ve attribution korunur. Nokta yerine yalnız dekoratif kenar vurgusu nefes alır.
- **Güncel Founder kararı (2026-09-24):** Bağlantı bitince kart listeden kalkar. Önceki kartı tutma kararı geçersizdir. Yalnız doğrulanmış bitişte satır150ms opaklıkla çıkar; normal harekette yeri150ms daralır, azaltılmış harekette yer değiştirme animasyonu yoktur. Liste boşalırsa mevcut boş durum açılır. Bu, geçmişin anında silinmesi değildir.
- Profilden şikâyet girişi onaylandı ve hareketten önce `e1f4bbe` ile teslim edildi; 6. kategori `079ee74`.
- Yeni runtime bağımlılığı yok. Flutter animasyonları, CustomPainter ve HapticFeedback yeterli. Cam/blur/backdrop taklidi, Lottie/Rive yok.

## Dosya sözleşmesi

- `motion.tokens.json`: normatif hareket değerleri; tema jetonlarının `motion` alanında da bulunur.
- `signature-moments.json`: olay tetikleyicileri, zaman çizgileri, iptal ve azaltılmış karşılıklar.
- `frames/*.csv`: **her 16.6667ms** için 60fps örnek değerleri. Bunlar süre garantisi değildir; Flutter gerçek geçen zamanla örnekler.
- `previews/*.gif`: her an için normal/azaltılmış yan yana, **25fps tasarım önizlemesi**. Tek oynatma; HTML'de kendiliğinden başlamaz.
- `screen-motion-map.json`: katalogdaki her durumun referansı; bunlar her girişte koşulsuz oynatma talimatı değildir.
- `reference/` önceki teslimin tarihsel referansıdır; H0 finalinde kod yazılmadı/değiştirilmedi. Bu teslimin uygulama sözleşmesi JSON, CSV ve bu belgedir.

## Yayların kesin anlamı

Plandaki “sönüm” oranı **ζ**, fiziksel sönüm katsayısı **c** değildir. Bu spesifikasyon “tepki”yi sönümsüz doğal periyot olarak tanımlar: `ω=2π/T`, `k=mω²`, `c=2ζmω`; kütle1, ilk hız0. Normalleştirilmiş0→1 yay kullanılır.

| Jeton | ζ | T | k | c | Referans yerleşme |
|---|---:|---:|---:|---:|---:|
| standard |0.90|0.35s|322.272797|32.313524|483.33ms|
| expressive |0.75|0.45s|194.955149|20.943951|650ms|

Önizleme sahne saatleri: Merhaba ACK örneği800ms; mesaj girişi örneği800ms; Hero dönüşü1000ms; Stop örneği5200ms. Bunların hiçbiri uygulama bekleme süresi değildir. CSV bu sahne saatini, JSON ise gerçek olaydan itibaren zamanı kullanır.

Yerleşme toleransı: konum0.001, hız0.01/s. Tepki350ms, “yay tam350ms sürer” anlamına gelmez. Yeniden hedefte mevcut konum/hız korunur; erişim kesilirse dekorasyon durur. Opaklık0..1 aralığına kısılır, metin/görsel çizimi clip içinde kalır. Quick150ms easeOutCubic; reduced150ms lineer opaklık.

## Ortak çalışma kuralları

1. Başarılar **gerçek domain sonucu** ile başlar. Örnekteki ACK işareti yalnız gösterim saatidir. Bekleme süresi sınırsızdır;500/800ms sonunda otomatik başarı yok.
2. `reduceMotion OR disableAnimations` okunur; MediaQuery de kontrol edilir. Ayar çalışma sırasında değişince devam eden uzamsal hareket/döngü iptal edilir, son doğru durum en çok150ms opaklıkla görünür. Soğuk açılış logosu doğrudan görünür. Azaltılmış durumda işlem göstergesi de dönmez; durum metni kalır. Gerçek ilerleme halkası yalnız ölçülen değere atlar.
3. Haptic istek zamanı belirtilen olay saatidir; donanımın kesinms titreşimi garanti edilmez. Seçim `selectionClick`; başarı tek `lightImpact`; yeni hata tek `mediumImpact`. Scroll, her rebuild, her snapshot, arka plan dönüşü titreşim üretmez. Olay ID'siyle tekilleştir; destek yoksa sessizce geç.
4. Aynı ekranda en fazla bir dekoratif döngü. Görünmez sekme/arka plan/route disposal sırasında Ticker kapalı. Pending işlemin callback'i kaybolmasın; yalnız sunumu durdur.
5. Focus sırası, erişilebilir adlar, ≥48dp hedefler ve %200 metin korunur. Görsel maske tam metnin Semantics değerini değiştirmez. Ekran okuyucuya harf harf okuma yaptırma. Haptic tek bilgi kanalı değildir.
6. Statik referans çizimleri bozulmaz; animasyon katmanı kapalıyken aynı işlev/durumlar kalır. Mevcut read-receipt desteği doğrulanmadan okundu işareti yaratma. Görünen kart sayısı animasyonun max6 sınırından türetilmez.

## 01-ink-signature — Mürekkep imzası

**Tetikleyici:** first Flutter frame of cold process start; never warm resume

**Yay:** Yok; aşağıdaki sabit eğriler

| Başlangıç–bitiş (ms) | Özellik | Değer | Eğri / uygulama |
|---|---|---|---|
|0–620|canonical logo contour reveal|0 → 1|linear cumulative path length|
|620–760|canonical intersection fill opacity|0 → 0.92|quick|
|760–800|hold canonical mark|1 → 1|none|

**Titreşim:** Yok.

**Hareketi azalt:** canonical logo fully visible at 0; no stroke reveal

**İptal/istisna:** if routing ready before 800ms, stop reveal and crossfade to destination in 150ms; never delay authentication or network error

**Flutter:** CustomPainter Path.computeMetrics / extractPath and clipPath; static native launch screen, animate only first Flutter frame

[Önizleme](previews/01-ink-signature.gif) · [60fps kare tablosu](frames/01-ink-signature.csv)

## 02-presence-boundary — Varlık dalgası — kenardan

**Tetikleyici:** authoritative check-in active state confirmed; no wave during acquiring/verifying/unknown

**Yay:** expressive

| Başlangıç–bitiş (ms) | Özellik | Değer | Eğri / uygulama |
|---|---|---|---|
|0–960|first viewport contour inset|0 → 10% of shortest viewport side|expressive position; opacity .12*(1-progress)|
|240–1200|second viewport contour inset|0 → 10% of shortest viewport side|expressive position; opacity .12*(1-progress)|
|1200–5200|active boundary opacity|0.04 → 0.08|one 4000ms cosine breathing cycle, repeats only while active/foreground|
|5200–5350|confirmed stop: boundary opacity|current → 0|linear150; contracting inset toward viewport edge|

**Titreşim:** active confirmation +0ms: lightImpact.

**Hareketi azalt:** active status appears at 0..150ms; boundary remains static .06 while confirmed active, no rings/breathing; stop disappears within150ms

**İptal/istisna:** stop input cancels decoration immediately; only authoritative stopped state gets completion presentation. Failed/unknown stop uses existing state; no deletion claim. Lose access/expiry/offline => stop loops immediately.

**Flutter:** CustomPainter two clipped rounded-rectangle contours inside map viewport, IgnorePointer, no location coordinates; fixed border is decorative, not a geographic boundary

[Önizleme](previews/02-presence-boundary.gif) · [60fps kare tablosu](frames/02-presence-boundary.csv)

## 03-paper-list — Kâğıt yerleşmesi

**Tetikleyici:** committed visible list diff; new real IDs only

**Yay:** standard

| Başlangıç–bitiş (ms) | Özellik | Değer | Eğri / uygulama |
|---|---|---|---|
|0–684|item i translateY|8 → 0|standard spring; start min(i,5)*40ms for first six; remaining appear directly|
|0–350|item opacity|0 → 1|150ms linear per same start offset|

**Titreşim:** Yok.

**Hareketi azalt:** all new items opacity0→1 simultaneously150ms; no translation or stagger

**İptal/istisna:** same ID content update, sort, scroll/rebuild or cached restoration must not replay. Removed users disappear from accessible data immediately; never retain for exit animation.

**Flutter:** stable ValueKey IDs, AnimationController + Transform.translate + FadeTransition; no global list rebuild per frame

[Önizleme](previews/03-paper-list.gif) · [60fps kare tablosu](frames/03-paper-list.csv)

## 04-photo-hero — Fotoğraf kahramanı

**Tetikleyici:** tap on accessible profile with the same authorized cached photo at source and destination

**Yay:** standard (programmatic only)

| Başlangıç–bitiş (ms) | Özellik | Değer | Eğri / uygulama |
|---|---|---|---|
|0–484|photo rect|measured source rect → measured destination rect|standard normalized SpringSimulation; clamp rect extent to avoid exposing outside clip|
|0–150|destination content opacity|0 → 1|linear|
|1000–1484|return photo rect in preview|destination → source|standard; actual gesture follows OS progress, not this clock|

**Titreşim:** Yok.

**Hareketi azalt:** disable Hero flight; destination opacity150ms, no resizing/motion; preserve back gesture and navigation

**İptal/istisna:** missing source, recycled card, denied photo, changed photo ID => simple150ms fade, never fly another user photo. Predictive back cancel returns to unchanged profile without route commit.

**Flutter:** Hero with stable tag + clipped same child; built-in platform route/predictive back. Never run a second scale animation over OS interactive back.

[Önizleme](previews/04-photo-hero.gif) · [60fps kare tablosu](frames/04-photo-hero.csv)

## 05-hello-ink — Merhaba — el yazısı

**Tetikleyici:** request success acknowledgement, unique operation ID. Network waiting is unbounded.

**Yay:** Yok; aşağıdaki sabit eğriler

| Başlangıç–bitiş (ms) | Özellik | Değer | Eğri / uygulama |
|---|---|---|---|
|-150–0|tap compression (separate input clock)|1 → 0.98|quick; release back to1 in150ms, never tied to server duration|
|0–500|success text reveal mask|0 → 1|linear left-to-right clipping of fully laid out text; do not type individual glyphs|

**Titreşim:** successful request acknowledgement +0ms: lightImpact.

**Hareketi azalt:** full success label fades150ms after same acknowledgement; pending status static; no mask/compression

**İptal/istisna:** failed/offline/unknown => no sent reveal and no success haptic. Timeout is not success. Very fast response may skip pending flicker. Rebuild/reentry does not replay.

**Flutter:** ClipRect/CustomPainter mask over complete Text, one Semantics liveRegion announcement of complete text at acknowledgement; new delta motionHelloSent; existing requestSending while pending

[Önizleme](previews/05-hello-ink.gif) · [60fps kare tablosu](frames/05-hello-ink.csv)

## 06-two-points — Bağlantı — iki portre

**Tetikleyici:** server confirms connection created, not just current user accepting. Play once for new connection ID; not on ordinary existing-chat open.

**Yay:** expressive

| Başlangıç–bitiş (ms) | Özellik | Değer | Eğri / uygulama |
|---|---|---|---|
|0–650|portrait horizontal offset each|±28dp → 0|expressive; final72dp circles touch at centers distance72dp; clip/clamp to avoid overlap|
|300–1000|single ink ring radius|42 → 104|easeOutCubic; opacity .12→0|
|850–1000|existing open-chat CTA opacity|0 → 1|linear; visual reveal only, no automatic navigation or state mutation|

**Titreşim:** confirmed new connection +300ms: lightImpact.

**Hareketi azalt:** portraits static, no ring; full content and CTA fade150ms from confirmed event; one light haptic at0ms

**İptal/istisna:** Open-chat presentation fades850..1000ms after confirmation, as in approved plan. Existing navigation/back is never blocked; no automatic navigation or backend wait is introduced. Reduced motion exposes the CTA within150ms. If route is already being opened, skip the scene. Missing authorized portraits use existing placeholders.

**Flutter:** Transform.translate+ClipOval, CustomPainter ring; no new people photos or mutual intent inference

[Önizleme](previews/06-two-points.gif) · [60fps kare tablosu](frames/06-two-points.csv)

## 07-paper-message — Mesaj — yerine oturan kâğıt

**Tetikleyici:** outgoing: acknowledged message ID inserted; incoming: actual newly received authorized message ID

**Yay:** standard

| Başlangıç–bitiş (ms) | Özellik | Değer | Eğri / uygulama |
|---|---|---|---|
|0–484|outgoing bubble offset|min(24dp, distance from composer top to final slot) → 0|standard; pending stays pending until confirmed|
|0–150|outgoing opacity|0 → 1|linear|
|800–1284|incoming bubble offset in preview|-12 → 0|standard; actual receipt has its own t=0|
|800–950|incoming opacity in preview|0 → 1|linear|

**Titreşim:** Yok.

**Hareketi azalt:** confirmed bubble opacity150ms only; no travel; composer uses current actual keyboard inset without additional tween

**İptal/istisna:** failed/unknown messages never get success flight. Existing optimistic bubble reconciles by stable ID, no duplicate. History load/rebuild/scroll not a new message. Do not move history or auto-scroll away from someone reading.

**Flutter:** AnimatedBuilder/Transform/FadeTransition; composer follows actual viewInsets.bottom per frame, no independent spring. Counter and Send stay attached; read receipt opacity only if a real supported read event exists, never from delivery.

[Önizleme](previews/07-paper-message.gif) · [60fps kare tablosu](frames/07-paper-message.csv)

## Ekran haritası, öncelik ve uygulama dilimleri

`screen-motion-map.json` §6'nın bütün ekran ailelerini kapsar. Öncelik sırası: erişim/başarı gerçeği → azaltılmış hareket → native klavye/geri hareketi → hata/güvenlik → imza an → sıradan geçiş. Aynı property'ye iki controller bağlanmaz.

- H1: token, reduced-motion observer, haptic tekilleştirme, standart route/sekme, yerleşik predictive back.
- H2: sınır dalgası, merhaba, bağlantı, fotoğraf Hero, mesaj.
- H3: liste yerleşmesi, yükleme halkası, boş durum, hata şeridi ve açılış.
- Hareket ana anahtarı kapalı çalışabilmeli; dağıtım/kapalı test takvimi bu dosyadan türetilmez.

## Code doğrulama kapıları

- Gerçek veri: geciken ACK, hızlı ACK, hata, offline ve belirsiz sonuç; hiçbirinde sahte başarı yok. Aynı olay tekrarı titreşimi/animasyonu çoğaltmaz.
- Reduce Motion ve Remove animations ayrı ayrı; uygulama açıkken aç/kapat. Döngü/translate/scale/mask yok; native OS yüzeylerine ikinci hareket eklenmez.
- Gerçek profile git/geri, Android predictive-back iptal/tamamla; eksik Hero kaynağı150ms fade.
- Klavye ve büyük metin: Send, sayaç, Done erişilebilir; compose alanı klavyeden bağımsız sıçramaz.
- Veri silinmesi/erişim kaybında fotoğraf ve mesaj overlay'i anında kaldırılır; geçiş sonunda hassas içerik tutulmaz.
- Düşük seviye Android profil modunda FrameTiming:60Hz için16.67ms bütçe, UI/raster ayrı, kaçırılan kare oranı ve cihaz/model kaydedilsin. Hedef60fps; **bu teslim cihaz performansı ölçtü iddiası taşımaz**.
- Canvas sadece ilgili küçük repaint alanında; bitmap önbelleğini büyütme, backdrop blur/saveLayer döngüsü yok. İşlem durumunun zamanı UI animasyonundan bağımsız.

## Teknik kaynaklar

Yerel Flutter3.47.3 kaynakları kontrol edildi. Sıfır yeni bağımlılık sınırı korunur. API dayanakları:

- [SpringDescription](https://api.flutter.dev/flutter/physics/SpringDescription-class.html): sönüm oranı/katsayı ayrımı.
- [AccessibilityFeatures.reduceMotion](https://api.flutter.dev/flutter/dart-ui/AccessibilityFeatures/reduceMotion.html) ve [disableAnimations](https://api.flutter.dev/flutter/widgets/MediaQueryData/disableAnimations.html): iki erişilebilirlik işareti birlikte değerlendirilir.
- [Hero](https://api.flutter.dev/flutter/widgets/Hero-class.html): aynı tag ve ilk destination frame gereği.
- [PredictiveBackPageTransitionsBuilder](https://api.flutter.dev/flutter/material/PredictiveBackPageTransitionsBuilder-class.html): yerleşik Android geri geçişi; desteklenmeyen sürümde platform fallback.
- [HapticFeedback](https://api.flutter.dev/flutter/services/HapticFeedback-class.html): platform geri bildirimi, kesin fiziksel zamanlama garantisi yok.

## H0 final — son kararlarla uyum

Aktif oturumda I’m still here + Stop korunur (FD-47/FD-40); kenar dalgası düğmenin yerine geçmez. Sohbet Send simgesi composer içinde48×48; klavye ile aynı katmanda. İlk merhaba boş kartı ve ona bağlı nefes kaldırılmıştır. Paylaşım daveti yalnız doğrulanmış contact durumunda standart geçiştir. Profil kayıt dönüşü150ms opacity (profile-save-return). Başarılı rapor engellemeyi içerir; kapalı bağlantı satırı listeden kalkar.

H0 önizlemeleri3.04–5.72 saniyedir; animasyon bittikten sonraki bekleme yalnız inceleme içindir. Canlı arayüz bekleme süresi değildir. H0-DELIVERY.md tek dosyalık özet ve önizleme dizinidir.
