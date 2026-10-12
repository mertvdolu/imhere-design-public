# STORE-IOS-14 — Kompozisyon ve üretim spesifikasyonu

13 Ekim 2026 · Cream & Ink v2.3 · iPhone only

## Kaynaklar ve tema

- Görsel sistem: `02-SON-EKLER/imhere-cream-complete-v2.2/theme-v2.3/SPEC.md`.
- Logo kaynağı: aynı paketin `brand/README.md`; Founder'ın orijinal iki daireli işareti, oranı korunmuş.
- Geist Regular / Medium, OFL lisansı pakette. Bitmap metin yerine dış başlıklar SVG metnidir; WOFF2 gömülü, render için TTF de bulunur.
- Zemin `#F4F1E9`, başlık `#191A17`, yardımcı metin `#696A62`, dekoratif kenar `#B7B3A9`. Yeni renk ailesi yok; harita renkleri kaynak PNG'dendir.
- Dış çerçeve hafif kabartmalıdır. Arayüzün kendi gölgeleri/renkleri kaynakta olduğu gibi bırakılır.

## Ana kompozisyon

1320 birim genişliğinde çalışma alanı; çıktı yüksekliğine göre alt çerçeve alanı hesaplanır. Tüm metinler ve dış ölçüler çıktı genişliğiyle eşit oranda ölçeklenir.

| Öğe | Ölçü / yerleşim |
|---|---|
| Logo | x86 / y67, 54×34.245, orijinal oran |
| Marka yazısı | x169, baseline96, 28 / 500, harf aralığı2 |
| Başlık | x82, baseline238 ve356, 112 / 500, satır farkı118, harf aralığı−4 |
| Native ekran | üst444, yükseklik = kompozisyon yüksekliği−602; genişlik = yükseklik×1206/2622; yatay merkez |
| Kabartmalı çevreleme | Native sınırın dışında22 boşluk, köşe62, 1.5 dekoratif kenar |
| Çerçeve gölgesi | ±10 x/y, sigma10; koyu `#D6D2C8`, açık `#FFFEFA`; dış yüzey, metne gölge yok |
| Açıklama | Alt kenardan41 baseline, 28 / 400, ortalı |
| Ek harita kredisi | Alt kenardan84 baseline, 25 / 400, ortalı |

Altı sahne aynı görsel hiyerarşiyi kullanır. Ekranlar perspektifle eğilmez; uygulamanın tamamı gösterilir. Native görüntü üzerinde Dynamic Island, yeni saat, yeni pil, ek eylem, yeni metin veya cihaz markası çizilmez. Dış çerçevenin yuvarlak köşeleri native alanı kırpmaz.

## Yetkili portre katmanı

Önceki mağaza paketindeki kurmaca yetişkin Maya portresi kullanılır. Orijinal 1206×2622 koordinatları:

| Sahne | x | y | w | h | r |
|---|---|---|---|---|---|
| 02-nearby | 108 | 1857 | 192 | 240 | 36 |
| 04-chat | 108 | 606 | 192 | 240 | 36 |

Portre SVG'de bu dikdörtgenlere kırpılarak yerleştirilir; yalnız fotoğraf yeri kaplanır. Native PNG dosyası değiştirilmez. 03-request-profile'da yuva yok; overlay yok. Diğer dört sahnede de overlay yok. Maya'nın aynı portresi kullanılır, Alex ekranına yeni fotoğraf alanı eklenmez. Altı karede kurmaca içerik açıklaması vardır.

## Çıktı boyutları

Apple [Screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/) 13 Ekim 2026 kontrolüne göre 1320×2868 ve 1242×2688 kabul edilen ölçülerdir; sayfanın zorunlu iPhone / Dynamic Island medium grubu için 1206×2622 set de sağlanır. iPad kapsam dışıdır. Tüm çıktılar 24-bit RGB PNG, sRGB, opak, alfa kanalı olmadan üretilir.

## Yeniden üretim

Paket kökünde:

```sh
python3 source/build.py
node source/render.cjs
python3 source/validate.py
python3 source/manifest.py
```

- `build.py`: Python standart kütüphanesi; native SHA256 doğrular ve 18 SVG + DELIVERY.json üretir.
- `render.cjs`: Node.js / sharp; paketteki Geist fontlarını kullanır, 18 PNG ve üç contact sheet üretir. `NODE_PATH` çalışma ortamındaki sharp kurulumunu gösterebilir. Uygulamaya yeni bağımlılık eklenmez.
- `validate.py`: Python / Pillow; PNG ölçüleri, renk modu, native gömme, portre kapsamı, metin sığması ve kontrastı kontrol eder.
- `manifest.py`: Python / Pillow; kendisi hariç paketin tüm dosyalarını SHA256 ve varsa görsel boyutuyla listeler. İçerik değişirse son adımda yeniden çalıştırılır.

Orijinal kaynaklar ve çekim kanıtı `source/native/ios/` ile `source/evidence/` içindedir. `source/evidence/BENIOKU.md` eski NOT RUN başlığını içerir; orijinali korundu. Daha sonraki çekim kaydı ve eşleşen altı PNG, çekimin yapıldığını doğrular. Yerel çekim scriptleri bu tasarım işinde çalıştırılmadı.
