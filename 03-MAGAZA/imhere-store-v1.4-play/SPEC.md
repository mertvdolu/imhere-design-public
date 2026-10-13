# STORE-IOS-14 EK1 — Ölçüler ve üretim

## Sistem

Cream & Ink v2.3, mevcut iki daireli işaret (orijinal oran) ve Geist Regular/Medium. Renkler: zemin #F4F1E9, metin #191A17, yardımcı #696A62, dekoratif kenar #B7B3A9. Hafif yüzey gölgesi ±8, sigma8, #D6D2C8 / #FFFEFA; metin gölgesi yok. Yeni arayüz bileşeni, ürün eylemi veya renk ailesi eklenmedi.

## Telefon — 1080×1920

| Öğe | Ölçü |
|---|---|
| Marka işareti | x82 y36, 44×27.903 |
| IM HERE | x149 baseline61, 24/500, tracking1.7 |
| Başlık | x78, baseline146/235, 82/500, tracking−3 |
| Native tam ekran | x189 y276, 702×1560; orijinal 1080×2400, 0.65 ölçek |
| Kabartmalı çevreleme | Native dışında16; radius44; kenar1.5 |
| Alt not | merkez540 baseline1887, 23/400 |
| Harita altı | OpenMapTiles baseline1870,19/400; açıklama baseline1900,23/400 |

Native içerik görüntü alanının %52.81'ini kaplar; başlık bölgesi üst %12.24 içindedir. Oran korunur, native görüntü kırpılmaz veya gerilmez. Çevreleme bir donanım kasası değildir; iOS öğesi, Dynamic Island veya üretici işareti eklenmez.

## Portre yerleşimi — kaynak koordinatları

Yalnız mevcut Maya fotoğraf yuvası. 1080×2400 koordinatlarında 02: x94.5/y1598; 04: x94.5/y503.5; ikisi de168×210, radius31.5. Piksel sınırları native kaynakla ölçüldü, finalde görsel kontrol edildi. Aynı sentetik portre SVG katmanında yuva içine kırpılır; native PNG değişmez. 03 dahil diğer dört ekrana fotoğraf alanı eklenmez.

## Öne çıkan görsel — 1024×500

Logo x64/y97,68×43.125; IM HERE x158/baseline133,27/500. Başlık x64/baseline236 ve300,54/500,tracking−1.7. 02 ve04 native ekranları x566 ve777/y62,171×380; tüm kadraj, oran korunur. Dış yüzey boşluğu10/radius28. Açıklama merkez512/baseline480,16/400. Kritik başlık ve marka kenarlardan içeridedir; native ekranlar birbirini örtmez. Yeni reklam sözü eklenmeden 04 başlığı yeniden kullanılır.

## Üretim

Paket kökünde: `python3 source/build.py` → `node source/render.cjs` → `python3 source/validate.py` → `python3 source/manifest.py`.

Python/Pillow, Node/sharp; Geist fontları pakettedir. `NODE_PATH` mevcut sharp kurulumunu gösterebilir. Uygulamaya bağımlılık eklenmez. SVG kaynakları native PNG baytlarını gömer; validate gömülü SHA256 ile orijinali karşılaştırır. PNG'ler sRGB/RGB, alfa yoktur. MANIFEST son dosya düzenlemesinden sonra çalıştırılır.

## Mağaza ölçü kontrolü

[Google Play resmî önizleme gereksinimleri](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en-en), 13 Ekim 2026 kontrolü: telefonlar için opak 24-bit PNG/JPEG, kenar320–3840, uzun kenar kısa kenarın en çok iki katı. Bu teslimde altı adet 1080×1920 (9:16) vardır. Feature graphic 1024×500 opak PNG'dir. Bu teknik kontrol mağaza kabulü anlamına gelmez.
