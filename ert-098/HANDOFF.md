# ERT-098 — Code / Manager teslimi

2026-10-06 · v1.0 · Cream & Ink v2.3 · Yalnız tasarım

Önce [SPEC.md](SPEC.md), ardından [ONIZLEME.html](ONIZLEME.html) ve [ekran listesi](SCREEN-STATE-MATRIX.md) okunmalı.

## Teslim

- Tek şablon, `DELETION_PENDING` / `ACCESS_DISABLED` içerik varyantı.
- 8 ana PNG: EN/TR ve %100/%200. Ayrıca 8 büyük metin kaydırma/tam metin kanıtı + 2 kopyalandı görüntüsü.
- `copy.locked.json`: brifin aynen kullanılan metinleri; `copy-source.json`: TR kaynak ve anahtar önceliği. Yeni metin önerisi yok, ana ARB birleştirmesi yok.
- `validation.json`: tarayıcı ölçümleri ve sınırları. `MANIFEST.json`: dosya listesi, boyut ve SHA-256.
- `ONIZLEME.html`, `style.css`, `preview.js`, `copy.js`: yerel HTML önizlemesi. Geist dosyaları mevcut v2.2 yolundan kullanılır; önizlemeyi repo içinden açın.

## Code'a uygulama notu

1. Mevcut ortak bileşenler: kompakt birincil/ikincil, SafeArea ve Contact us kopyalama/başarı satırı. Tema tokenları değişmez.
2. İki durumda da geri/alt menü yok. DELETION_PENDING tek çıkış; ACCESS_DISABLED çıkış + kopyala. İptal, geri alma veya e-posta uygulaması açma yok.
3. Büyük metinde gövde kaydırılır; alt eylemler ayrı yerleşim bölgesinde kalır. Metin kesme/küçültme yok.
4. Kopyalama başarısından önce `Copied` gösterilmez. EN kısa ifade bu briften; TR mevcut `Adres kopyalandı.`. Genel Contact us metin anahtarlarını değiştirmeyin.
5. Mevcut onaylı gövdeler aynen. DELETION_PENDING TR kaynağı HARBOR §2 / §5.3; teslimde tam metin mevcut.

## Doğrulama / sorular

32 tarayıcı yerleşimi geçti; kaydırma sonu ve kopyalama kontrolleri tamamlandı. Native uygulama, derleme, hesap silme/kapama veya mağaza yayını yapılmadı.

Açık soru yok. `ert-098/` dışındaki Events ekranları, proposed metinler ve önceki 144 Events doğrulaması değişmedi.
