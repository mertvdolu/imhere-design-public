# Cream & Ink — Founder seçimi / v1.0

Founder, Cream study v1.0 yönünü ana uygulama teması olarak seçti. Forest & Mint artık aktif tasarım hedefi değildir; eski kaynaklar arşiv olarak korunur.

## Aktif kaynaklar
- Güncel tema: `03-GUNCEL-ORTAK/tokens/theme.tokens.json` (token sürümü 2.1).
- Bu teslim: `02-SON-EKLER/imhere-cream-theme-v1.0/`.
- Onaylanan altı ekranın görsel referansı: `02-SON-EKLER/imhere-cream-study-v1.0/ONIZLEME.html` ve `REVIEW.png`.
- Harita: bu teslimdeki `map-cream-en.json`; TR dosyası hazır ama dil kapalı.

## Tema eşlemesi
Krem zemin #F4F1E9, açık kart #FCFAF5, siyah mürekkep #191A17. Siyah ana düğme / açık yazı; giden mesaj siyah, gelen mesaj krem. İnce ikonlar ve ayırıcılar; Geist medium başlık. Siyah-beyaz fotoğraf görünümü yalnız arayüz filtresidir; orijinal kullanıcı fotoğrafı saklama/yükleme davranışı değiştirilmez.

Başlık 36, weight 500, sıkı harf aralığı; native gövde 16, etiket 14 ve metadata 12 başlangıç ölçüleri korunur. HTML telefon kartlarındaki sıkıştırılmış inceleme yazıları native boyutlara kör kopyalanmaz. Native sistem metin ölçeği ve en az 48 birim dokunma hedefleri korunur. HTML ×1,55 denemesi native %200 doğrulaması değildir.

İnce ayırıcı rengi dekoratiftir. Giriş/outline eylem sınırında inputBorder kullanılır. Hata, kapalı, seçili ve disabled hâller yalnız renkle ayırt edilmez; mevcut metin/ikon ve kontrol durumu korunur. Niyet isimleri kalır, boş seçim başlangıcı değişmez.

## Harita
Krem alt harita seçildi; önceki koyu stil tarihsel alternatif olarak kalır. Dört band rengi aynen korunur. Eski/geçersiz/bilinmeyen band, hücre geometrisi, yoğunluk eşiği veya veri güncelliği değişmez. JSON yalnız basemap içerir; örnek poligonları veya kamerayı uygulamaya taşımayın. Attribution: © OpenStreetMap contributors · OpenFreeMap; kaynağın OpenMapTiles kredisi de korunur. Mevcut adapter rengini/katmanını bağlar.

## Kapsam ve eski çizimler
Tema yönü onaylıdır. Bu teslim native uygulamaya uygulanmış veya tüm 287 ekranın yeniden çizilmiş olduğu anlamına gelmez. Eski PNG/SVG ekranlar davranış/yerleşim arşividir; eski yeşil/mint renkleri uygulanmaz. Login/onboarding, hata, güvenlik, contact ve diğer ekranlar bu ortak tema üzerinden uyarlanacaktır. Logo dosyalarının uygulanma koordinasyonu önceki talebe göre Manager'dadır; bu tema kararı yeni logo tasarlamaz veya eski B-symbol'ü yeniden dayatmaz.

Açılış ekranı ve simge çevresi yeni açık temayla native entegrasyonda eşleştirilmeli; önceki koyu splash kaynağı aktif görsel hedef değildir. Ayrı resmî logo paketinin Ink/Paper renkleri gelişigüzel recolor edilmez. Marka uygulaması Manager koordinasyonundadır.

Ürün davranışı, metin anahtarları, TR'nin kapalı oluşu, sekme sırası ve iletişim/gizlilik kuralları değişmedi. Uygulama kodu değiştirilmedi. Code entegrasyonu ve gerçek cihaz turu sonraki doğrulama adımıdır.
