# STORE-IOS-14 EK1 — Google Play hazırlık ve çekim notu

Tarih: 13 Ekim 2026 · Hedef: Android 1.4.0 · Cream & Ink v2.3

**Durum: NATIVE ÇEKİMLER BEKLENİYOR — MAĞAZAYA YÜKLENECEK TESLİM DEĞİL.**

13 Ekim güncellemesi: iPhone seti üretildi; [iPhone teslimi](../imhere-store-v1.4-ios/HANDOFF.md). Android API 36 kaynakları henüz gelmedi; bu klasörde Play görseli yok.

Sıra: önce [iPhone seti](../imhere-store-v1.4-ios/NATIVE-CAPTURE-REQUEST.md), ardından Google Play seti. Bu dosya yalnız EK1 kapsamını ve kaynak ihtiyacını kaydeder. Henüz Play PNG'leri, contact sheet veya son çıktı MANIFEST'i üretilmedi. Native çekimler Code'dan Founder üzerinden gelecek.

## Android native kaynakları

- API 36 Android emülatörü; 1.4.0'ın güncel Cream & Ink v2.3 görünümü.
- iPhone çekimlerinden hemen sonra, aynı kurmaca kişi ve sohbet verisi, aynı etkinlik ve aynı ekran durumlarıyla çekim.
- İngilizce, normal yazı boyutu, açık tema; portresiz fakat mevcut fotoğraf yuvaları görünür. Sentetik Maya/Alex portreleri yalnız bu yuvalara yerleştirilecek.
- Kaynaklar ham dikey PNG olsun. Tercihen 1080×1920 native; mevcut emülatör daha uzun bir ekran kullanıyorsa gerçek tam çözünürlüğü korunarak gönderilsin. Çekimi 9:16'ya zorlamak için kırpma/germe yapılmasın; final dış kompozisyonunu tasarımcı düzenleyecek.
- Android'in kendi durum çubuğu ve sistem gezinme öğeleri korunsun. Saat 09:41, dolu pil ve sade durum çubuğu; bildirim, operatör adı, klavye, toast, debug rozeti ve yükleme katmanı görünmesin.
- Gerçek kişisel veri veya kullanıcı konumu kullanılmasın. Kullanıcıların yerini gösteren işaret, kişi sayısı veya mesafe eklenmesin. Gerçek yayındaki etkinlik için Founder'ın STORE-IOS-14 izni geçerli.
- Uygulama içi metinler gerçek 1.4.0 çıktısı olarak kalsın. İstenen durum uygulamada farklıysa fark not edilsin; ekran üzerine düğme veya metin çizilmesin.

| Kaynak dosya | Durum |
|---|---|
| `01-purpose.png` | “Why are you here?”; Networking / Friendship, ilk açılışta seçim yok. |
| `02-nearby.png` | Networking ile aktif oturum; “Good, you're here.”, kurmaca Maya kartı ve “Here for Networking”. |
| `03-request-profile.png` | Gelen istek göndereninin profili; henüz yanıt yok; “I'd like to connect” / “Not this time” görünür. |
| `04-chat.png` | Aynı kurmaca Alex/Maya sohbeti; kısa nötr mesajlar, kalkan ve composer; klavye kapalı. |
| `05-event-detail.png` | “I'M HERE Coffee & Connect”, 7 Nov 2026, Royal Festival Hall; Interested / Going görünür, RSVP verilmemiş durum tercih edilir. |
| `06-area-activity.png` | Tam ekran Area activity; güncel kontroller ve dört renkli yoğunluk sistemi; mevcut harita atıfları eksiksiz. |

Etkinlik ayrıntısının başlığı ve eylemleri birlikte sığmıyorsa normal Events listesi alternatif çekim olabilir; uygulama yerleşimi çekim için değiştirilmez. Harita atıfları (OpenStreetMap / OpenMapTiles ve mevcut OpenFreeMap kredisi) kırpılmaz veya örtülmez. Kaynakta bulunmayan yoğunluk boyanmaz.

Altı PNG'nin yanındaki `CAPTURE-NOTES.md`: sürüm/build numarası, kaynak commit, API/emülatör modeli, çözünürlük, tarih, kurmaca veri teyidi ve varsa üretim görünümünden farkları içersin. Giriş bilgisi veya gerçek kullanıcı verisi eklenmesin.

## Çıktılar ve güncel Google kontrolü

Kaynak: [Google Play — Add preview assets to showcase your app](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en), 13 Ekim 2026 kontrolü.

Google telefon görüntülerinde cihaz türü başına en fazla sekiz görsel kabul ediyor; yayın için en az iki ekran görüntüsü gerekiyor. 320–3840 px kenar sınırları ve en uzun kenarın kısa kenarı en fazla iki kat aşması şartıyla, opak JPEG veya 24-bit PNG kullanılıyor. Bazı öneri alanları için en az dört, 1080×1920 dikey ekran öneriliyor. Altı 1080×1920 çıktımız bunlara uyuyor. Feature graphic ölçüsü 1024×500, alfa kanalı olmadan. Bunlar teknik uygunluk kontrolüdür; mağaza kabulü veya önerilme garantisi değildir.

Planlanan dosyalar:

| Yol | İçerik / ölçü |
|---|---|
| `google-play/phone/01-purpose.png` … `06-area-activity.png` | 6 adet 1080×1920, 9:16, opak RGB PNG |
| `google-play/feature-graphic.png` | 1024×500, opak RGB PNG |
| `review/contact-sheet.png` | Altı telefon karesi + öne çıkan görselin genel önizlemesi |
| `source/` | Düzenlenebilir üretim dosyaları ve kaynak eşlemesi |
| `COPY-REVIEW.md` | Başlık, alt not, kısa tanıtım ifadesi ve erişilebilir alternatif metinler |
| `MANIFEST.json` | Teslim dosyası, ölçü ve SHA256 bilgisi |

## Görsel ve copy yönü

- Cream & Ink v2.3, hafif kabartma, mevcut logo. Android native arayüz önde; kısa başlıklar dış kompozisyonda en fazla %20 alan hedefiyle yerleşir. Google'ın cihaz görsellerinden kaçınma önerisiyle uyumlu olarak markalı donanım kasası yerine sade çevreleme ve gerçek Android sistem öğeleri kullanılır.
- iOS durum çubuğu / Dynamic Island eklenmez. Native görüntü oranı korunur; içerik gerilmez veya kesilmez.
- Her telefon karesinde “Fictional profiles · Illustrative content” alt notu bulunur. Öne çıkan görselde native parça/örnek kişi kullanıldığında aynı not da görünür tutulur.
- Feature graphic: mevcut logo, kısa ölçülü ifade ve uygulamayı gösteren gerçek Android native parça. Odak ortada; logo ve ifade kenar kesimlerine bırakılmaz. Nihai kompozisyon iPhone setinden sonra hazırlanır.
- Mağaza düğmesi/logosu, sahte ödül, sıralama veya kullanıcı sonucu iddiası kullanılmaz. “verified”, “secure”, “anonymous” yok. Telefon içindeki copy gerçek ARB ile aynı kalır.
- Başlıklar, alt notlar, feature graphic ifadesi ve alternatif metinler **DRAFT — HARBOR + FOUNDER COPY APPROVAL REQUIRED**. Copy dosyası hazırlanırken iPhone setiyle aynı sahne başlıkları temel alınır; yeni bir onay varsayılmaz.
- Google'ın alternatif metin önerisine uygun olarak her ekran/feature graphic için kısa EN açıklama da copy dosyasına eklenir (en fazla 140 karakter hedefi).

## Süre ve teslim sınırı

**Play tahmini: 30–45 dakika**, iPhone seti tamamlandıktan ve altı kullanılabilir Android kaynak çekimi geldikten sonra. iPhone tahmini 45–60 dakika ile birlikte toplam aktif tasarım/üretim tahmini **75–105 dakika**. Kaynak çekimi, HARBOR/Founder onayı veya yeniden çekim beklemeleri hariç.

Şu an yalnız hazırlık dosyası mevcut. Final görselleri üretilmeden MANIFEST veya kontrol sonucu tamamlanmış gösterilmeyecek. Yeni set onaylanınca eski v1.2 Play görsellerinin yerine kullanılacak; mağazada değişiklik bu tasarım çalışması kapsamında yapılmıyor.
