# Store 1.5 — ölçü ve kompozisyon

## Görsel sistem

1.4 SVG → sharp üretim yolu. Cream #F4F1E9, Ink #191A17, yardımcı metin #696A62, çerçeve #B7B3A9. Geist Regular/Medium ve aynı marka SVG'si. Yeni renk veya ikon yok.

## iPhone

1320 genişliğinde tasarım koordinatı; çıktı 1320×2868 veya 1206×2622. Oranlarına göre tuval yüksekliği hesaplanır.

- Marka işareti (86,67), 54×34.245; IM HERE (169,96), 28 Medium.
- Başlık iki satır: x82, baseline238/356, 112 Medium, tracking−4.
- Alt satır: x86, baseline426, 34 Regular.
- Native üstü y500; altına158 boşluk. Ekran genişliği kaynağın kendi oranından; yatayda ortalı. İki 1.4 native kaynağın boyutları ayrıca okunur.
- İnce çevre:22 padding, radius62, 1.5 stroke. 1.4 gölgesi: ±10, stdDeviation10, #D6D2C8/#FFFEFA.
- Küçük açıklama ortalı, tuval altından41 baseline, 28 Regular.

1.4'te y444 olan native başlangıcı alt satır için y500 oldu. Tüm ekran orantılı ölçeklenir; hiçbir native pikselin üstüne yeni içerik çizilmez.

## Android

1080×1920 tuval. Marka x82/y36, 44×27.903; IM HERE x149/y61, 24 Medium. Başlık x78 baseline146/235, 82 Medium, tracking−3. Alt satır x82/y287, 28 Regular.

Native y330, yüksekliği1506, genişliği677.7 (1080×2400 oranı), yatayda ortalı. 16 padding, radius44, 1.5 stroke; mevcut ±8/stdDeviation8 gölgesi. Açıklama x540/y1887, 23 Regular. iOS öğesi eklenmez.

## Kaynak bütünlüğü

Her SVG bir marka SVG görüntüsü ve bir tam native PNG görüntüsü içerir; fotoğraf, saat, pil veya UI örtüsü yok. Native dosyası SVG içine aynı baytlarla gömülür. Yeni ekranların kişi/sayı/yazıları, LinkedIn filtresi dahil, kaynaktaki haliyle kalır.

Başlık/alt satır EN metni `source/copy.en-GB.json` içinde. Otomatik yazı küçültme veya kısaltma yok. 03'ün uzun açıklaması aynı puntoyla sığar. Pazarlama metni renkleri krem üzerinde ≥4.5:1. Native uygulama metinlerinin kontrastı bu işin düzenleme kapsamı değildir.

Feature graphic 1024×500 eski dosyanın bayt-aynı kopyasıdır; `source/svg/feature-graphic-v14-unchanged.svg` orijinal düzenlenebilir kaynaktır.
