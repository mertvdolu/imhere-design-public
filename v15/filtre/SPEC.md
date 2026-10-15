# filtre — SPEC

## Bileşenler / ölçü

Mevcut v2.3 başlık, küçük düğme, bilgi kartı, input, radyo ve satır desenleri. Kenar 24 dp. Başlık 28/600, gövde 16/400, yardım 14/400; satır aralığı 1.18/1.5/1.5. Bölüm başlığı 18/500. Ölçek %200: punto 2×, sabit satır sınırı yok. Küçük düğme görünen yüzey en az 36, bağımsız hedef en az 48×48; radius12. Kart radius15.

Tam ekran kaydırılan alt sayfa (★), back48. Checkbox meslek satırı + sayım;6 tasarım örneği51/24/12/8/6/3,51→50+. Liste sunucu snapshot sırasıyla açılır; seçimde yer değişmez.5 seçildiğinde seçilmemiş satırlar pasif ve MaxReached görünür. LinkedIn switch yanında hiçbir sayı yok. 0/1/2 TEK not-enough görünümü. Threshold ve privacy notları aynen.

## Durumlar

- **filters-loading**: Networking only. Counts are explicit design fixtures, never live. Each visible option≥3, cap50+. OR among≤5 jobs, AND with LinkedIn Everyone. Panel order frozen while open; 0/1/2 same state; no saved filters.
- **filters-options**: Networking only. Counts are explicit design fixtures, never live. Each visible option≥3, cap50+. OR among≤5 jobs, AND with LinkedIn Everyone. Panel order frozen while open; 0/1/2 same state; no saved filters.
- **filters-selected**: Networking only. Counts are explicit design fixtures, never live. Each visible option≥3, cap50+. OR among≤5 jobs, AND with LinkedIn Everyone. Panel order frozen while open; 0/1/2 same state; no saved filters.
- **filters-max-five**: Networking only. Counts are explicit design fixtures, never live. Each visible option≥3, cap50+. OR among≤5 jobs, AND with LinkedIn Everyone. Panel order frozen while open; 0/1/2 same state; no saved filters.
- **filters-no-options**: Networking only. Counts are explicit design fixtures, never live. Each visible option≥3, cap50+. OR among≤5 jobs, AND with LinkedIn Everyone. Panel order frozen while open; 0/1/2 same state; no saved filters.
- **filters-linkedin-only**: Networking only. Counts are explicit design fixtures, never live. Each visible option≥3, cap50+. OR among≤5 jobs, AND with LinkedIn Everyone. Panel order frozen while open; 0/1/2 same state; no saved filters.
- **filters-failed**: Networking only. Counts are explicit design fixtures, never live. Each visible option≥3, cap50+. OR among≤5 jobs, AND with LinkedIn Everyone. Panel order frozen while open; 0/1/2 same state; no saved filters.
- **filters-offline**: Networking only. Counts are explicit design fixtures, never live. Each visible option≥3, cap50+. OR among≤5 jobs, AND with LinkedIn Everyone. Panel order frozen while open; 0/1/2 same state; no saved filters.
- **filters-not-enough**: Networking only. Counts are explicit design fixtures, never live. Each visible option≥3, cap50+. OR among≤5 jobs, AND with LinkedIn Everyone. Panel order frozen while open; 0/1/2 same state; no saved filters.
- **filters-no-longer-enough**: Networking only. Counts are explicit design fixtures, never live. Each visible option≥3, cap50+. OR among≤5 jobs, AND with LinkedIn Everyone. Panel order frozen while open; 0/1/2 same state; no saved filters.
- **filters-friendship**: Networking only. Counts are explicit design fixtures, never live. Each visible option≥3, cap50+. OR among≤5 jobs, AND with LinkedIn Everyone. Panel order frozen while open; 0/1/2 same state; no saved filters.
- **filters-list**: Networking only. Counts are explicit design fixtures, never live. Each visible option≥3, cap50+. OR among≤5 jobs, AND with LinkedIn Everyone. Panel order frozen while open; 0/1/2 same state; no saved filters.

## Erişilebilirlik / native

Her durum tek H1, doğal üstten alta okuma; %200 ve320 genişlikte yatay kaydırma yok. En az48 hedef, renk yanında metin/ikon. Pasif kontrolün koşulu mevcut metin veya işlem durumu ile görünür. Varsa radyo grup etiketi, checkbox çoklu seçim, switch görünür etiketle. Focus visible 2 px Ink +3 offset. `Reduce Motion`: 150 ms doğrusal opaklık, mekânsal hareket yok. Yüksek kontrastta gölge yok, belirgin Ink kenar; şeffaflığı azaltmada menü opak.

## ★ / yeni bileşen

★ Tam sayfa: %200 ve uzun TR uyarılarda sheet yüksekliğiyle mücadele etmeden tüm satırlar erişilir. ★ Görünen sıra panel açıkken sabit. YENİ BİLEŞEN — ONAY GEREKİR: counted filter row (mevcut checkbox+etiket+tabular sayı birleşimi).
