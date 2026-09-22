# Forest Night — koyu alt harita v1.0

MapLibre Style Specification v8, OpenFreeMap vector tiles. Bu stil özgün, sade bir katman tanımıdır; eski Mapbox URL/font/source-layer referanslarının yerine OpenMapTiles şemasındaki water, waterway, park, landcover, building, transportation, transportation_name ve place kullanılır. OpenFreeMap dark stilinin tasarım katmanları kopyalanmadı. Gölge rasterı, sprite, POI ikonları, adres numaraları veya kullanıcı işaretleri yok.

Zemin #17251D, su #0D1C1A, yeşil alan #1E3428. Yollar düşük doygunlukta; açık etiketlerde koyu halo var. Map fontu OpenFreeMap'ten Noto Sans Regular; uygulama arayüzünün Geist fontu değişmez. EN aktif; TR yalnız uyuyan kaynak. Etiket, dile ait isim varsa onu, yoksa yerel adı gösterir.

## Renk katmanı
Dosyalar yalnız alt haritadır; mevcut adapter kaynak ve renk katmanını eklemeye devam eder. İkinci bir activity source veya sahte hücre yok. Hücre geometrisi, eşikler, band hesabı, veri tazeliği, kamera/zoom limitleri ve gizlilik kuralları değişmez. Kaynakta kullanıcı konumu, pin, kişi sayısı veya mesafe yok.

Mavi #64A8FF, sarı #F7D46A, yeşil #7DDEAC, kırmızı #EE8985 korunur. Mevcut adapter'ın 0.45 dolgu opaklığı ve rgba(255,255,255,0.35) kenarı korunur. Okunurluk için renk katmanını road-labels öncesine eklemek uygundur; böylece etiketler üstte kalır. Uygulama styleLoaded sonrasında mevcut band verisini kendi akışıyla tekrar bağlar. Uygulamaya ait source/layer adları yeniden adlandırılmaz. Eski Mapbox dosyaları yalnız tarihsel referanstır; bunlarla birlikte yüklenmez.

## Attribution
Her harita görünümünde görünür ve güvenli alan içinde kalacak zorunlu satır:
© OpenStreetMap contributors · OpenFreeMap

Kaynağın ayrıca verdiği © OpenMapTiles kredisi de korunur. Önizlemede birlikte gösterilir. Adlar ilgili copyright/provider sayfalarına bağlantılıdır. Bottom sheet/sekme/sistem alt alanı satırı örtmemeli; büyük yazıda satır kırılmalı, kırpılmamalıdır. Haritaya yazı yerleşimi native uygulamada yapılır; style metadata tek başına attribution görünürlüğünü sağlamaz.

## Doğrulama
EN/TR JSON dosyaları MapLibre GL tarayıcı renderer'ında OpenFreeMap döşemeleri ve glyph'leriyle yüklendi; hata olmadan harita çizildi. Kanıt evidence/map-validation.json. Önizleme İstanbul'da sabit bir tasarım kamerasıdır; kullanıcı konumu değildir. Native Flutter/MapLibre, gerçek renk katmanı, zoom uçları, offline ve cihaz performansı entegrasyon turunda doğrulanacak. Tarayıcı testi native onayı yerine geçmez.

Kaynaklar:
- https://openfreemap.org/quick_start/
- https://tiles.openfreemap.org/planet
- https://maplibre.org/maplibre-style-spec/

MapLibre önizleme runtime lisansı MAPLIBRE-LICENSE.txt içindedir. OpenStreetMap/OpenMapTiles veri atıfları korunur.
