# IM HERE — mağaza görselleri 1.5

16 Ekim 2026 · Cream & Ink v2.3 · 1.4 mağaza setinin görsel dili.

## Yüklenecek dosyalar

- `ios-15-1206x2622/`: 6 PNG, 1206×2622.
- `ios-15-1320x2868/`: 6 PNG, 1320×2868.
- `play-15-phone/`: 6 PNG, 1080×1920.
- `play-feature/feature-graphic.png`: 1024×500; 1.4 dosyası bayt-aynı.

Hepsi opak RGB. Sıra: community, nearby, filters, request-profile, chat, events.

[HTML önizleme](ONIZLEME.html) · [Teslim notu](HANDOFF.md) · [Ölçüler](SPEC.md) · [Kontroller](VALIDATION.md) · [MANIFEST](MANIFEST.json) · [PNG SHA256 listesi](SHA256SUMS.txt)

## Kaynaklar

Beş yeni sahne/platform Founder'ın `IMHERE-1.5-tasarimci` klasöründen. 04 istek profili her platformun kendi 1.4 native kaynağından; bitmiş mağaza karesini ikinci kez çerçevelemiyoruz. Kaynak görselleri, saat, pil, kişi, sayı ve uygulama metinleri değiştirilmedi. Yeni portre eklenmedi. Native ekran içindeki LinkedIn satırı korunur; dış başlıklarda/alt satırlarda LinkedIn yok, logosu veya marka mavisi eklenmedi.

Metinler Founder'ın 16 Ekim mesajıyla aynıdır; bağımsız HARBOR incelemesi yapılmış olduğu iddia edilmez. Bu teslim dosya üretimidir; mağaza konsollarına yükleme veya yayın yapılmadı.

## Tekrar üretim

Python 3 + Pillow; Node.js + sharp. Yerel Geist dosyaları ve lisansı pakettedir.

1. `python3 source/build.py`
2. `node source/render.cjs`
3. `python3 source/validate.py --write`
4. `python3 source/manifest.py`
5. `python3 source/validate.py`

Öne çıkan görsel yeniden render edilmez; 1.4'ün aynı PNG'si korunur. Contact sheet'ler `review/` altında, mağaza yüklemesi için değildir.
