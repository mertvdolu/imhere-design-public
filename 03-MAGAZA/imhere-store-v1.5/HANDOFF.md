# TASARIMCIDAN MANAGERE MESAJ

## IM HERE 1.5 — App Store + Google Play

Depo: `mertvdolu/imhere-design-public`  
Dal: `design/store-15-cream-ink-v23`  
Konum: `03-MAGAZA/imhere-store-v1.5/`

6 sahne × 3 boyut = 18 PNG hazır. Ek olarak 1 adet 1024×500 Play öne çıkan görseli var. Tüm mağaza görselleri opak RGB. Dosya isimleri ve sırası Founder brief'iyle aynıdır.

| Klasör | Boyut | Adet |
|---|---|---|
| ios-15-1206x2622 | 1206×2622 | 6 |
| ios-15-1320x2868 | 1320×2868 | 6 |
| play-15-phone | 1080×1920 | 6 |
| play-feature | 1024×500 | 1 |

## Uygulananlar

- 1.4 rengi, Geist, marka işareti, iki satırlı başlık ve ince kabartmalı çerçeve korundu. İstenen alt satır için çerçeve aşağı alındı; native görüntünün tamamı orantılı küçültüldü, kırpılmadı.
- 01/02/03/05/06 verilen 1.5 native kaynaklardır. 03: **KARE-3b-filtre-paneli.png**. 06: **KARE-5-etkinlik.png**; ayrıntı alternatifi kullanılmadı.
- 04: önceki iOS ve Android setlerinin özgün istek profili ekranları aynen. Platformlar karıştırılmadı.
- Alt açıklama tüm karelerde “Fictional profiles · Illustrative content”; yalnız 03'te “Fictional profiles and numbers · Illustrative content”.
- Play öne çıkan görselinde “purpose” bulunmadığından Founder talimatına göre dosya aynı kaldı: “Start with a conversation.” Eski native küçük önizlemeler de aynı dosyanın parçası olarak korunur.
- Kaynak saatleri/pilleri aynı: yeni iPhone kareleri 09:41; 1.4 istek profili iPhone 07:37, Android 08:06. Kaynaklara saat/pil makyajı veya portre eklemesi yapılmadı.

## Doğrulama ve kaynak

[VALIDATION](VALIDATION.md): 18 PNG ölçü/RGB, 12 native SHA256, SVG içindeki native dosya eşitliği, tam kadraj/oran, tüm pazarlama metinleri ve yerleşimi; feature SHA256 eski dosyayla aynı. [MANIFEST](MANIFEST.json) tüm dosyaları kapsar. [SHA256SUMS](SHA256SUMS.txt) 19 mağaza PNG'sini listeler.

Kaynak build/commit yeni çekimlerle verilmedi; 1.5 sürüm bilgisi Founder beyanıdır. Eski iki native ve feature'ın Git kaynağı `source/capture-provenance.json` içindedir. Uygulama kodu, ARB, tema tokenları veya ürün davranışı değişmedi. Mağazaya yükleme/yayın yapılmadı.

Commit ve uzak SHA doğrulaması teslim mesajında verilir. 1.4 dosyaları tarihçe olarak korunur.
