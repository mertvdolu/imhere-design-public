# IM HERE — Cream & Ink v2.2 kaynak özeti

Düzeltilmiş tasarımcı özeti v1.0 · 2026-09-26. Skill hazırlığı için kaynak belge; kurulmuş skill değildir. Yeni ürün kuralı koymaz.

## 0. Kapsam ve kaynak kullanımı

Mobil arayüz, mobil varlıklar ve bu pakete dayalı örnek mağaza görselleri için kullan. Tanıtım sitesi ayrı projedir; hukuki metinler, yayın durumu ve kodda uygulanmış davranış bu dosyadan doğrulanamaz.

Depo kökü `imhere-design-public`. Aşağıda P = `02-SON-EKLER/imhere-cream-complete-v2.2`.

- Görsel değerler: `03-GUNCEL-ORTAK/tokens/theme.tokens.json`; fontlar aynı ortak klasörün `fonts/` dizininde.
- Ekran: depo kökündeki `EKRAN-KATALOGU.json`, P/`specs/TASARIM-DEVRI.md` ve ilgili tarihli ek.
- Logo: yalnız P/`brand/README.md` ve gösterdiği varlıklar. BEACON 22 Eylül kılavuzu geri çekildi.
- Hareket: P/`motion/hareket-ve-his-v1/` — token, SPEC, signature-moments, screen-motion-map, S2-DECISION.
- Metin: P/`l10n/` güncel delta + migration; tam ARB üzerine yazılmaz.
- Özel durum: en yeni, ilgili Founder kararı ve tarihli düzeltme eski genel açıklamayı geçersiz kılar. Çelişki çözülemiyorsa belirt; ürün davranışı icat etme.

## 1. Renkler

Tek açık tema; dynamic color kapalı. Arayüz krem ve Ink. Eski yeşil tema, parlak küre ve yeşil gradyan geri gelmez. Hata/seçili durum yalnız renk ile anlatılmaz.

| Token | Değer |
|---|---|
| background | `#F4F1E9` |
| surface | `#FCFAF5` |
| text | `#191A17` |
| onPrimary | `#FCFAF5` |
| textSecondary | `#696A62` |
| inputBorder | `#7C7D73` |
| border | `#D9D5CB` |
| input | `#F0ECE3` |
| friendshipSurface | `#E9E5DA` |
| networkingSurface | `#E9E5DA` |
| densityBlue | `#64A8FF` |
| densityYellow | `#F7D46A` |
| densityGreen | `#7DDEAC` |
| densityRed | `#EE8985` |

`border` dekoratif; form sınırı `inputBorder`. Dört density rengi yalnız harita semantiği; arayüzün ikinci vurgu paleti değil. Friendship/Networking renk ile ayrılmaz. Güncel T2 seçiminde seçili ince çip Ink/açık metin, seçilmemiş çip açık/çerçeveli; yalnız eski yüzey token’ına bakıp büyük iç içe kart çizme.

## 2. Yazı ve ölçüler

Geist, mobil pakette yerel font dosyaları; çalışma anında font indirme eklenmez. Birimler Flutter mantıksal piksel, sistem metin büyütmesinden önce.

| Rol | Boyut | Ağırlık | Satır çarpanı |
|---|---:|---:|---:|
| headline | 36 | 500 | 1.12 |
| body | 16 | 400 | 1.6 |
| label | 14 | 500 | 1.4 |
| metadata | 12 | 400 | 1.5 |
| orbLabel | 18 | 600 | tanımlı değil |
| sectionTitle | 18 | 500 | 1.4 |
| status | 16 | 500 | 1.6 |
| helper | 14 | 400 | 1.4 |

Headline harf aralığı −1.8. `orbLabel` ve diğer eski orb isimleri yeni bir küre bileşeni talimatı değildir.

Boşluk ölçeği: 4/8/12/16/20/24/32/40/48. Sayfa kenarı 24; güvenli alan ve özel ekran çizimini ayrıca uygula. Hedef en az 48×48; görünen ikon daha küçük olabilir. Yarıçap: input/düğme12, kart15, sheet24, hap999. Çizgi1, ikon1.8. Referanslar390×844 ve412×915; sabit cihaz ölçüsü değildir. %200 metin varyantları, kaydırma ve sistem güvenli alanları korunur. Büyük metinde 2×2 navigasyon; native doğrulama ayrıca gerekir.

## 3. Logo

Orijinal iki daireli işaretin SVG geometrisi/oranı korunur. Logo Ink#14161A / Paper#FAFAF8; arayüz Ink’inden farkı bilinçli. Yazısız opak uygulama simgesi, OS köşeleri; Android adaptive katmanları verilen dosyalardır. Eski A-wordmark/B-symbol seçilmez. Telefon adı **IM HERE**.

Native splash krem#F4F1E9 üzerinde orijinal işaret; ek bekleme yok. İlk Flutter karesinin H0 hareketi ayrı katmandır. Android küçük bildirim simgesi doğrudan geometriden beyaz/saydam teknik maske; OS tonlar. Güncel kaynakta 24 px logo minimumu, yarıçap koruma alanı veya 48 px ağırlık eşiği yok; icat etme. Native kırpma/okunabilirlik dosya teslimiyle doğrulanmaz.

## 4. Güncel bileşen ve davranış sınırları

- Sekmeler Profile → Messages → Nearby → Events; başlangıç Nearby. Messages içinde Connections + Requests. Events placeholder.
- Aktif check-in: **I’m still here + Stop** kalır; T1 sadeleştirmesi geri alındı. Kaynak: P/specs/T1-REVERT-NOTIFICATIONS-2026-09-25.md (bildirim paragrafı sonradan v2 ile güncellendi).
- Niyet: Friendship/Networking ince tek satır çipler; varsayılan boş, 1–2 seçim. Kaynak: token policy.intents ve P/specs/FOUNDER-PHONE-T1-T4.md.
- Alt sayfalar: 48×48 geri; iOS sistem geçişi/geri, Android sistem geri. Geri dönüşü kapalı doğrulama/davet-tekrar/ilk profil kurulumunda Çıkış yap korunur.
- Sohbet: Safety/Continue üst sağ ikon hedefleri; Send composer içinde sağ altta, erişilebilir adı Send. Eski “You can be the first…” kartı yok. Klavye üstündeki composer/sayaç/Send yerleşimi korunur. Sayaç eşikleri ve paylaşım daveti için P/specs/DEV-TOUR-H2-H7-H9-H3.md’yi kullan; eşik icat etme.
- Contact düzenleme: sağdaki kalem. Ek alan paylaşımı serbest; yalnız paylaşılmamış alanlar seçilebilir. Support/Contact: adres + kopyala, mailto açma yok.
- Profil: kendi görünümü önce; kalem dişlinin solunda. Onboarding ve form durumları için güncel katalog. Gizlenen alanlar sunucudan karşı tarafa gönderilmez; yalnız yerelde gizleme olarak anlatılmaz.
- Report: 6 kategori; child-safety etiketi onaylı delta’dan. Report-sent ve Safety girişleri P/specs/CODE-ALIGNMENT-CH141-143.md ile okunur. Eski beş kategori/opsiyonel engel akışını geri getirme.
- End connection: kendi onay penceresi; kapalı kart listede kalmaz. P/specs/END-CONNECTION-2026-09-24.md günceldir.
- Saklama satırı yalnız salt-okunur sohbette; yazılabilir chat-active içinde gösterilmez. Kesin silinme saati vaat edilmez; onaylı güncel metinler kullanılır.
- EN etkin, TR teslimlerde hazır; Dil ayarı Türkçe etkinleşene kadar gizli. Yeni ürün davranışı önerisi: DESIGN RECOMMENDATION — FOUNDER APPROVAL REQUIRED.

## 5. Tam ekran harita

Harita açılınca sekmeleri örter; geri Nearby. MapLibre + OpenFreeMap. Görünür atıf: **© OpenStreetMap contributors · OpenFreeMap**; OpenMapTiles kredisi korunur, örtülmez. Kişisel konum noktası, pin, kişi sayısı, mesafe etiketi yok. Dört semantik bant zoom ile anlam değiştirmez. Dalga harita sınırlarından başlar, kişi/merkez noktasından değil. Örnek harita “Illustrative map · Not live data”; kurmaca profil “Fictional profiles · Illustrative content” etiketi taşır. Örnek veri canlı durum izlenimi vermez.

## 6. Hareket

Flutter yerleşik animasyon + CustomPainter; yeni bağımlılık, Lottie/Rive veya Liquid Glass taklidi yok.

| Token | Değer |
|---|---|
| motion.quick |150ms; easeOutCubic [0.215,0.61,0.355,1]|
| motion.standard |mass1; dampingRatio0.9; response0.35s; stiffness322.27279677026473; damping32.313524436923586; velocity0|
| motion.expressive |mass1; dampingRatio0.75; response0.45s; stiffness194.9551486634935; damping20.943951023931955; velocity0|
| motion.stagger |40ms; en fazla6 öğe/200ms gecikme|
| motion.reduced |150ms linear opacity; mekânsal hareket/döngü/stagger yok; soğuk logo hemen görünür|

Standard yaklaşık483ms, expressive650ms yerleşme referansıdır; tepki süresiyle karıştırma. Kare/kesin özellik tabloları H0 SPEC/JSON/CSV’de; bu kısa özet onları değiştirmez.

| An | Görünüm / koşul |
|---|---|
|01|İlk Flutter karesinde800ms logo; native splash ayrı. Hazır yönlendirmeyi bekletmez; sıcak dönüşte oynatılmaz.|
|02|1200ms kenardan dalga, yalnız harita ve onaylı aktif check-in.|
|03|Yeni gerçek liste ID’leri için8→0 kâğıt yerleşmesi; tekrar çizimde tekrar yok.|
|04|İki uçta aynı yetkili fotoğraf varsa profil fotoğrafı geçişi.|
|05|500ms Hello sent, sunucu isteği onayladıktan sonra bekleyen ekranın üstünde bir kez.|
|06|1000ms tek karşı taraf portresi + tek halka; kendi fotoğrafı gerekmez; karşı fotoğraf yoksa nötr yer tutucu. Eski two-points ID’si iki portre talimatı değil.|
|07|Onaylı mesaj ID’si ile balon yerleşmesi; giden başarı sunucu onayından önce gösterilmez.|

S2: iOS rota geçişleri sistemin; iki ayrı geçiş üst üste eklenmez. H3 profil kaydından dönüş ilgili spesifikasyona göre. Reduce Motion imza an tablolarını uygula; yükleme göstergesini süs hareketiyle karıştırma. Haptik yalnız olayın tanımlı anında, bir kez; scroll titreşimi ve ön plana dönüşte telafi yok, OS tercihi geçerli. Animasyon bitişi backend onayı değildir.

## 7. Metin ve bildirim

Kısa, sakin, suçlamayan; “anonim” kullanılmaz. Gizlilik/güvenlik veya sonuç garantisi uydurulmaz. Her yerde sayı kullanma kuralı yok: ilgili ekranın sözleşmesi ve kısıtları geçerli. Yerel hukuk/acil numara/yayın tarihi bu tasarım dosyasından türetilmez. Hukuki belgede bir özelliğin anılmaması desteklenmediğinin kanıtı değildir; tasarım ve Code teyidi ayrı okunur.

Bildirim başlığı, kişi adı ve mesaj içeriği yok; onaylı genel gövdeler kullanılır. İzin metni güncel v2 ile requests and messages kapsamındadır. Kabul/yeni mesaj/contact paylaşımı: “Messages and connections” kanalı, varsayılan ses+titreşim, OS ayarı geçerli. Düşük öncelik sessiz; Updates ve mevcut Check-in reminders adı değişmez. CH-133 ön plan kuralı değiştirilmez. Kaynak: P/specs/NOTIFICATION-V2-COPY.md ve NOTIFICATION-CHANNEL-2026-09-26.md. Genel “her bildirim sessiz” eski karardır.

## 8. Teslim ve sınırlar

ARB delta + migration ile birleştir; tüm ARB üzerine yazma. Katalog, çizim, metin ve manifest değişiyorsa birlikte doğrula. Kaynak kod/cihaz testini tasarım çizimiyle tamamlanmış sayma. Mağaza metni revizyon kararları bu klasörde INCELEME.md’de; mevcut PNG’ler henüz o metinlerle dışa aktarılmadı. Canlı web gözlemleri mobil tasarım sistemi kuralı değildir. Hukuki/mağaza politika uygunluğu bu özetle onaylanmaz.
