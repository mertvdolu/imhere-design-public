TASARIMCIDAN MANAGERE MESAJ

# H0 — Hareket ve His v1 · Final teslim

**25 Eylül2026 · Cream & Ink v2.2 · Tasarım; native uygulama kodu değil.**

## Teslim özeti

Founder planı korundu. Önceden mevcut taslaklar güncel kararlara göre tamamlandı; yedi GIF yeniden üretildi, her biri3–6 saniye, normal/azaltılmış yan yana. Veri yerine açıkça işaretli soyut şekiller kullanılır; kişi, fotoğraf, mesaj veya yoğunluk sayısı uydurulmaz. Önizlemedeki olay saati yalnız tasarım canlandırmasıdır; gerçek gönderim başarısı zamanlayıcıdan türetilmez.

- [Normatif hareket belirteçleri](motion.tokens.json)
- [Tetikleyici / zaman çizgileri / iptal koşulları](signature-moments.json)
- [Ayrıntılı spesifikasyon](SPEC.md)
- [§6 ekran his haritası](SCREEN-FEEL-MAP.md)
- [297 durumun hareket eşleştirmesi](screen-motion-map.json)
- [İsteğe bağlı oynatılan önizleme galerisi](ONIZLEME.html)

## Belirteçler — plandaki değerler değişmedi

| Ad | Değer |
|---|---|
| motion.quick |150ms ease-out (easeOutCubic)|
| motion.standard |ζ0.90, tepki0.35s|
| motion.expressive |ζ0.75, tepki0.45s|
| motion.stagger |40ms, en çok6 öğe|
| motion.reduced |150ms yalnız opaklık; döngü/ölçek/konum hareketi yok|

Yay tanımı: tepki doğal periyot; mass1, başlangıç hızı0, k=m(2π/T)², c=2ζm(2π/T). Standard k322.272797/c32.313524; expressive k194.955149/c20.943951. Tepki değeri kesin bitiş süresi değildir. Dokunma alanları48×48 sabit kalır; yalnız görsel içerik hareket eder. Metin kontrastı sabit tam görünür durumda korunur; geçiş opaklığı ayrı dekoratif sunumdur, okunması gereken tek bilgi animasyona bırakılmaz.

## Yedi imza an — zamanlama ve önizleme

Tabloda belirtilmeyen eksen/ölçek sabit, opaklık1'dir. Opaklık0..1'e sınırlanır. Kısaltma: standard/expressive yukarıdaki yay; quick150ms easeOutCubic. Her GIF sonunda inceleme beklemesi vardır; uygulamada ek gecikme yoktur. CSV'ler60fps örnek tablolardır; gerçek uygulama kare sayısıyla değil geçen zamanla ilerler.

### 01-ink-signature — Mürekkep imzası

[GIF (3.04s)](previews/01-ink-signature.gif) · [Kare kare60fps CSV](frames/01-ink-signature.csv)

Tetikleyici: first Flutter frame of cold process start; never warm resume

| Başlangıç ms | Süre ms | Özellik / konum | Değer | Eğri / opaklık |
|---:|---:|---|---|---|
|0|620|canonical logo contour reveal|0 → 1|linear cumulative path length|
|620|140|canonical intersection fill opacity|0 → 0.92|quick|
|760|40|hold canonical mark|1 → 1|none|

Hareketi azalt: canonical logo fully visible at 0; no stroke reveal

Titreşim: Yok

İptal: if routing ready before 800ms, stop reveal and crossfade to destination in 150ms; never delay authentication or network error

### 02-presence-boundary — Varlık dalgası — kenardan

[GIF (5.72s)](previews/02-presence-boundary.gif) · [Kare kare60fps CSV](frames/02-presence-boundary.csv)

Tetikleyici: authoritative check-in active state confirmed; no wave during acquiring/verifying/unknown

| Başlangıç ms | Süre ms | Özellik / konum | Değer | Eğri / opaklık |
|---:|---:|---|---|---|
|0|960|first viewport contour inset|0 → 10% of shortest viewport side|expressive position; opacity .12*(1-progress)|
|240|960|second viewport contour inset|0 → 10% of shortest viewport side|expressive position; opacity .12*(1-progress)|
|1200|4000|active boundary opacity|0.04 → 0.08|one 4000ms cosine breathing cycle, repeats only while active/foreground|
|5200|150|confirmed stop: boundary opacity|current → 0|linear150; contracting inset toward viewport edge|

Hareketi azalt: active status appears at 0..150ms; boundary remains static .06 while confirmed active, no rings/breathing; stop disappears within150ms

Titreşim: {'event': 'active confirmation', 'atMs': 0, 'type': 'lightImpact'}

İptal: stop input cancels decoration immediately; only authoritative stopped state gets completion presentation. Failed/unknown stop uses existing state; no deletion claim. Lose access/expiry/offline => stop loops immediately.

### 03-paper-list — Kâğıt yerleşmesi

[GIF (3.04s)](previews/03-paper-list.gif) · [Kare kare60fps CSV](frames/03-paper-list.csv)

Tetikleyici: committed visible list diff; new real IDs only

| Başlangıç ms | Süre ms | Özellik / konum | Değer | Eğri / opaklık |
|---:|---:|---|---|---|
|0|684|item i translateY|8 → 0|standard spring; start min(i,5)*40ms for first six; remaining appear directly|
|0|350|item opacity|0 → 1|150ms linear per same start offset|

Hareketi azalt: all new items opacity0→1 simultaneously150ms; no translation or stagger

Titreşim: Yok

İptal: same ID content update, sort, scroll/rebuild or cached restoration must not replay. Removed users disappear from accessible data immediately; never retain for exit animation.

### 04-photo-hero — Fotoğraf kahramanı

[GIF (3.04s)](previews/04-photo-hero.gif) · [Kare kare60fps CSV](frames/04-photo-hero.csv)

Tetikleyici: tap on accessible profile with the same authorized cached photo at source and destination

| Başlangıç ms | Süre ms | Özellik / konum | Değer | Eğri / opaklık |
|---:|---:|---|---|---|
|0|484|photo rect|measured source rect → measured destination rect|standard normalized SpringSimulation; clamp rect extent to avoid exposing outside clip|
|0|150|destination content opacity|0 → 1|linear|
|1000|484|return photo rect in preview|destination → source|standard; actual gesture follows OS progress, not this clock|

Hareketi azalt: disable Hero flight; destination opacity150ms, no resizing/motion; preserve back gesture and navigation

Titreşim: Yok

İptal: missing source, recycled card, denied photo, changed photo ID => simple150ms fade, never fly another user photo. Predictive back cancel returns to unchanged profile without route commit.

### 05-hello-ink — Merhaba — el yazısı

[GIF (3.04s)](previews/05-hello-ink.gif) · [Kare kare60fps CSV](frames/05-hello-ink.csv)

Tetikleyici: request success acknowledgement, unique operation ID. Network waiting is unbounded.

| Başlangıç ms | Süre ms | Özellik / konum | Değer | Eğri / opaklık |
|---:|---:|---|---|---|
|-150|150|tap compression (separate input clock)|1 → 0.98|quick; release back to1 in150ms, never tied to server duration|
|0|500|success text reveal mask|0 → 1|linear left-to-right clipping of fully laid out text; do not type individual glyphs|

Hareketi azalt: full success label fades150ms after same acknowledgement; pending status static; no mask/compression

Titreşim: {'event': 'successful request acknowledgement', 'atMs': 0, 'type': 'lightImpact'}

İptal: failed/offline/unknown => no sent reveal and no success haptic. Timeout is not success. Very fast response may skip pending flicker. Rebuild/reentry does not replay.

### 06-two-points — Bağlantı — iki portre

[GIF (3.04s)](previews/06-two-points.gif) · [Kare kare60fps CSV](frames/06-two-points.csv)

Tetikleyici: server confirms connection created, not just current user accepting. Play once for new connection ID; not on ordinary existing-chat open.

| Başlangıç ms | Süre ms | Özellik / konum | Değer | Eğri / opaklık |
|---:|---:|---|---|---|
|0|650|portrait horizontal offset each|±28dp → 0|expressive; final72dp circles touch at centers distance72dp; clip/clamp to avoid overlap|
|300|700|single ink ring radius|42 → 104|easeOutCubic; opacity .12→0|
|850|150|existing open-chat CTA opacity|0 → 1|linear; visual reveal only, no automatic navigation or state mutation|

Hareketi azalt: portraits static, no ring; full content and CTA fade150ms from confirmed event; one light haptic at0ms

Titreşim: {'event': 'confirmed new connection', 'atMs': 300, 'type': 'lightImpact', 'note': 'cancel delayed haptic if leaving/backgrounded; never wait for haptic to enable action'}

İptal: Open-chat presentation fades850..1000ms after confirmation, as in approved plan. Existing navigation/back is never blocked; no automatic navigation or backend wait is introduced. Reduced motion exposes the CTA within150ms. If route is already being opened, skip the scene. Missing authorized portraits use existing placeholders.

### 07-paper-message — Mesaj — yerine oturan kâğıt

[GIF (3.04s)](previews/07-paper-message.gif) · [Kare kare60fps CSV](frames/07-paper-message.csv)

Tetikleyici: outgoing: acknowledged message ID inserted; incoming: actual newly received authorized message ID

| Başlangıç ms | Süre ms | Özellik / konum | Değer | Eğri / opaklık |
|---:|---:|---|---|---|
|0|484|outgoing bubble offset|min(24dp, distance from composer top to final slot) → 0|standard; pending stays pending until confirmed|
|0|150|outgoing opacity|0 → 1|linear|
|800|484|incoming bubble offset in preview|-12 → 0|standard; actual receipt has its own t=0|
|800|150|incoming opacity in preview|0 → 1|linear|

Hareketi azalt: confirmed bubble opacity150ms only; no travel; composer uses current actual keyboard inset without additional tween

Titreşim: Yok

İptal: failed/unknown messages never get success flight. Existing optimistic bubble reconciles by stable ID, no duplicate. History load/rebuild/scroll not a new message. Do not move history or auto-scroll away from someone reading.

## Son kararlarla uyum / sınırlar

- Haritada kendi konum noktası yok: önceki Founder yanıtı gereği dalga viewport kenarından başlar. Coğrafi sınır veya uzaklık göstermez.
- Aktif check-in: I’m still here + Stop korunur; animasyon yenileme düğmesinin yerine geçmez (FD-47/FD-40).
- Sohbet Send simgesi composer içinde48×48; chat-empty kartı yok. Sayaç görünürlüğü için H7(c) onaysız öneri uygulanmaz.
- Gönderildi/bağlantı oluştu yalnız sunucu onayından sonra. Başarısız/belirsiz/çevrimdışı hiçbir sonuç başarı animasyonu oynatmaz.
- Bağlantı bitince satır listeden kalkar; salt okunur olmak tek başına bitmiş olmak değildir. Profil kaydı sonrası güncel150ms dönüş notu korunur.
- Yeni runtime bağımlılığı, uygulama kodu, Lottie/Rive, Liquid Glass taklidi yok. Eski reference/ klasörü tarihsel; bu H0 tesliminde kod yazılmadı/değiştirilmedi.
- GIF'ler tasarım önizlemesidir. Gerçek cihaz60fps, platform geri hareketi, haptics, ekran okuyucu ve klavye testi Code tarafından yapılacak; ölçülmüş performans iddiası yoktur.
- Kaynak plan arşivi değiştirilmedi. Motion token değerleri ve mevcut ürün davranışı değiştirilmedi.

Yerel commit; aktarımı Code yapar. Bu dosya tek giriş noktasıdır.
