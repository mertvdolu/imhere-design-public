# STORE-IOS-14 — Native çekim listesi

Tarih: 13 Ekim 2026 · Hedef: iOS 1.4.0 · Cream & Ink v2.3

**Güncel durum (13 Ekim): Altı iPhone çekimi alındı; 18 PNG üretildi. Copy onayı bekliyor. [Son teslim](HANDOFF.md).**

Bu dosya tasarıma başlamadan önce Founder / Manager üzerinden Code'a iletilen özgün çekim tarifini korur. Teslim edilen kaynakların gerçek farkları ve son çıktılar HANDOFF.md'dedir. Aşağıdaki çekim talepleri uygulamada farklı görünen öğelerin sonradan çizilmesi için talimat değildir. Uygulama kodu değişmedi.

## Neden yeni çekim?

`03-MAGAZA/V2.3-DURUM.md` ve önceki v1.2 paketinin README'si, eski native görüntülerin v2.3 öncesi görünümü belgelediğini söylüyor. Eski paketin kaynak çekimleri 27 Eylül, sürüm 7 sahnesinden geliyor. Bu nedenle 1/2/3/5'e ek olarak sohbet ve haritayı da güncel 1.4.0'dan istiyoruz. Eski telefon içi görüntülerinin üzerine gölge veya yeni kontrol çizilerek güncel uygulama izlenimi verilmeyecek.

## Ortak çekim koşulları

- iPhone / iOS, 1.4.0'ın mağazaya gönderilecek görünümü; Cream & Ink v2.3. Gerçek build numarası ve kaynak commit teslim notuna yazılmalı.
- Tercihen **1206×2622 PNG**, dikey; 1320×2868 native de uygundur. Ham ekran görüntüsü: cihaz kasası, pazarlama başlığı, kırpma veya yeniden boyutlandırma eklenmesin.
- İngilizce; normal yazı boyutu; açık tema. 09:41, tam pil; durum çubuğu Code'un çekim ortamında ayarlansın.
- Klavye, yükleme katmanı, hata, debug rozeti, bildirim ve geçici toast görünmesin. OS öğeleri iOS'a ait olsun.
- Kişiler ve sohbet yalnız kurmaca test sahnesinden. Alex/Maya gibi örnek adlar; gerçek kişi, kişisel e-posta, mesaj veya kullanıcının gerçek konumu görünmesin. Üretimde kişilere istek/mesaj gönderilerek sahne kurulmasın.
- Sentetik portreyi ben yalnız mevcut native fotoğraf yuvasına yerleştireceğim. Yuva görünür olmalı; fotoğrafın bulunmadığı ekrana yeni alan eklenmeyecek. Code mevcut sentetik portreyi native olarak kullanabiliyorsa ayrıca overlay gerekmez.
- Telefon içindeki başlık, düğme, rozet, sayaç ve navigasyon gerçek 1.4.0 çıktısı olarak kalmalı. Brief ile uygulama farklıysa fark not edilsin; çekim sonradan metin boyanarak düzeltilmesin.

## İstenen altı kare

| Dosya | Ekran / durum | Kadrajda bulunması gerekenler |
|---|---|---|
| `01-purpose.png` | I'm here → amaç seçimi, ilk açılış | “Why are you here?”, Networking / Friendship. İlk açılışta seçili seçenek yok; devam eylemi uygulamadaki gerçek pasif hâlinde. İki seçenek ve mevcut eylemler görünür. |
| `02-nearby.png` | Networking amacıyla aktif check-in | “Good, you're here.”, People nearby ve tek kurmaca Maya kartı. Yeni “Here for Networking” etiketi, mevcut fotoğraf yuvası ve kart eylemi görünür. Başka gerçek kişiler bulunmasın. |
| `03-request-profile.png` | Gelen istekte Maya'nın profili; henüz cevap verilmemiş | Gönderenin profili/fotoğraf yuvası ve “I'd like to connect” / “Not this time” eylemleri aynı native görüntüde. Hiçbir istek kabul edilmiş gibi gösterilmez. |
| `04-chat.png` | Alex / Maya arasında açık, yazılabilir sohbet | Birkaç kısa, nötr kurmaca mesaj; kişi adı, sağ üst kalkan, güncel composer ve uygulamanın gerçekten gösterdiği sayaç. Klavye kapalı. Yeni okundu/gönderildi işareti veya bildirim eklenmez. |
| `05-event-detail.png` | Gelecekteki etkinliğin ayrıntısı | Founder'ın izin verdiği “I'M HERE Coffee & Connect”, 7 Nov 2026, Royal Festival Hall; gerçek içerik ve Interested / Going kontrolleri. Çekimde RSVP verilmemiş durum tercih edilir. Yapay katılımcı sayısı veya katılım sonucu oluşturulmaz. |
| `06-area-activity.png` | Area activity, tam ekran harita | Güncel v2.3 harita kontrolleri ve doğal native yerleşim; kişisel konum işareti, kişi sayısı veya mesafe yok. Yoğunluk katmanının mevcut mavi/sarı/yeşil/kırmızı sistemi korunur; haritada yapay yoğunluk çizilmez. Test alanı kişisel konumu temsil etmesin. Atıf eksiksiz ve okunur kalsın. |

**Etkinlik kadrajı:** Başlık ve eylemler doğal yerleşimde birlikte sığmıyorsa, normal Events listesi de alternatif kaynak olarak gönderilebilir. Başlığı veya yerleşimi çekim için değiştirmeyin. Gerçek yayındaki etkinlik erişilemiyorsa durumu bildirin; yayınlanmış gibi yeni kayıt uydurmayın.

**Harita kadrajı:** Native OpenStreetMap / OpenFreeMap / OpenMapTiles atıflarından mevcut olanlar kesilmez veya örtülmez. Briefin istediği OpenStreetMap / OpenMapTiles kredisi finalde de korunacak; ihtiyaç olan ek dış kredi kaynak tesliminde netleştirilir. Alt menü o build'in gerçek görünümü olarak kalır.

## Kaynağın teslimi

Altı PNG ile birlikte kısa bir `CAPTURE-NOTES.md` yeterli:

- Uygulama sürümü + build numarası; kaynak commit.
- iPhone / simülatör modeli, iOS sürümü, çözünürlük, çekim tarihi.
- Alex/Maya ve mesajların kurmaca olduğunun teyidi.
- Çekilen ekranların üretim arayüzünü değiştirmeyen test verisiyle oluşturulduğu; varsa debug/fixture farkları.
- Briefteki ekran/metinlerle gözlenen farklar ve eksik kareler.

Dosyalar hazır olduğunda Founder teslim klasörünün tam yolunu iletebilir. Gizli bilgi, gerçek kullanıcı verisi veya test hesabı giriş bilgisi teslim notuna eklenmez.

## Mağaza çıktılarının ölçüleri

Apple'ın [güncel screenshot specifications sayfası](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/) 13 Ekim 2026'da kontrol edildi. Sayfa zorunlu iPhone grubunu Dynamic Island / medium olarak adlandırıyor; 1206×2622 bu gruptaki kabul edilen dikey ölçülerden biri. İstenen diğer iki ölçü de kabul edilen listede.

| Çıktı klasörü | PNG ölçüsü | Plan |
|---|---|---|
| `app-store/iphone-6.9/` | 1320×2868 | Briefte istenen set |
| `app-store/iphone-6.5/` | 1242×2688 | Briefte istenen set |
| `app-store/iphone-dynamic-island-medium/` | 1206×2622 | Güncel zorunlu grup için ek set |

Her sette aynı altı kare: toplam 18 opak RGB PNG; alfa kanalı yok. Harita kaynağı sağlanamazsa isteğe bağlı altıncı kare tamamlanmış sayılmaz ve teslim listesinde açıkça belirtilir. iPad görseli kapsamda değil. Kaynak çekimin en-boy oranı korunur; farklı çıktı ölçüsüne geçerken dış kompozisyon düzenlenir, telefon arayüzü gerilmez veya kırpılmaz.

## Copy ve süre

Briefteki altı başlık, her karedeki “Fictional profiles · Illustrative content” satırı ve eklenecek tüm pazarlama metinleri **DRAFT — HARBOR + FOUNDER COPY APPROVAL REQUIRED** olarak kalır. Telefon içindeki gerçek uygulama metinleri bu onay sürecinden ayrı olarak değiştirilmeden kullanılır.

**Tahmin:** Altı kullanılabilir native çekim geldikten sonra ilk tam üretim ve ölçü/görsel kontrol için yaklaşık 45–60 dakika. Kaynakların gelmesi, HARBOR / Founder incelemesi veya yeniden çekim bekleme süresi bu tahmine dahil değil.

Son teslim PNG setleri, düzenlenebilir üretim kaynakları, contact sheet, copy dosyası ve dosya/ölçü/SHA256 MANIFEST'ini içerir. Bu dosya önceki hazırlık kaydıdır; güncel durum için HANDOFF.md esas alınır.

## EK1 — Android çekimleri ve ikinci teslim

Founder'ın STORE-IOS-14 EK1 isteğiyle, aynı altı sahne için ayrı Google Play seti eklendi. Sıra değişmedi: önce bu iPhone seti, ardından Play. Code, iPhone çekimlerinden hemen sonra aynı kurmaca sahne verisiyle API 36 Android çekimlerini alacak; teslim Founder üzerinden yapılacak.

Play'in çekim ve çıktı ayrıntıları: [Google Play hazırlık notu](../imhere-store-v1.4-play/NATIVE-CAPTURE-REQUEST.md). Android kaynakları iOS görüntülerinden türetilmeyecek. Play için ek aktif çalışma tahmini 30–45 dakika; iki set toplamı 75–105 dakika (kaynak/onay beklemeleri hariç).
