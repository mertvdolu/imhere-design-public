# Events V1 — screen/state matrix

36 deterministic preview states. Every state: EN/TR, iOS/Android, 320/390/412 logical pixels, 100%/200% text; high contrast, reduced transparency and reduced motion toggles. These are design simulations, not native screenshots.

| ID | Screen/state | Last confirmed own RSVP | Special condition | Preview |
|---|---|---|---|---|
| `list-loading` | Liste · yükleniyor | NONE | loading | [Open](ONIZLEME.html?scene=list-loading) |
| `list-populated` | Liste · dolu / üç kategori | NONE | populated | [Open](ONIZLEME.html?scene=list-populated) |
| `list-empty` | Liste · boş | NONE | empty | [Open](ONIZLEME.html?scene=list-empty) |
| `list-error` | Liste · hata | NONE | error | [Open](ONIZLEME.html?scene=list-error) |
| `list-offline` | Liste · çevrimdışı | NONE | offline | [Open](ONIZLEME.html?scene=list-offline) |
| `list-cancelled` | Liste · iptal görünür | NONE | cancelled | [Open](ONIZLEME.html?scene=list-cancelled) |
| `list-started` | Liste · başlamış / kilitli | NONE | started | [Open](ONIZLEME.html?scene=list-started) |
| `list-image-failed` | Liste · görsel alınamıyor | NONE | image-failed | [Open](ONIZLEME.html?scene=list-image-failed) |
| `detail-none` | Detay · Henüz seçim yok | NONE | ready | [Open](ONIZLEME.html?scene=detail-none) |
| `detail-interested` | Detay · Interested | INTERESTED | ready | [Open](ONIZLEME.html?scene=detail-interested) |
| `detail-going` | Detay · Going | GOING | ready | [Open](ONIZLEME.html?scene=detail-going) |
| `detail-updating-interested` | Detay · Interested kaydediliyor | NONE | updating | [Open](ONIZLEME.html?scene=detail-updating-interested) |
| `detail-updating-going` | Detay · Interested → Going | INTERESTED | updating | [Open](ONIZLEME.html?scene=detail-updating-going) |
| `detail-withdrawing` | Detay · geri çekiliyor | GOING | updating | [Open](ONIZLEME.html?scene=detail-withdrawing) |
| `detail-save-failed` | Detay · seçim güncellenemedi | INTERESTED | save-failed | [Open](ONIZLEME.html?scene=detail-save-failed) |
| `detail-locked-none` | Detay · Başlamış / kilitli / NONE | NONE | locked | [Open](ONIZLEME.html?scene=detail-locked-none) |
| `detail-locked-interested` | Detay · Başlamış / kilitli / INTERESTED | INTERESTED | locked | [Open](ONIZLEME.html?scene=detail-locked-interested) |
| `detail-locked-going` | Detay · Başlamış / kilitli / GOING | GOING | locked | [Open](ONIZLEME.html?scene=detail-locked-going) |
| `detail-cancelled-none` | Detay · İptal / NONE | NONE | cancelled | [Open](ONIZLEME.html?scene=detail-cancelled-none) |
| `detail-cancelled-interested` | Detay · İptal / INTERESTED | INTERESTED | cancelled | [Open](ONIZLEME.html?scene=detail-cancelled-interested) |
| `detail-cancelled-going` | Detay · İptal / GOING | GOING | cancelled | [Open](ONIZLEME.html?scene=detail-cancelled-going) |
| `detail-changed-none` | Detay · Bilgiler güncellendi / NONE | NONE | changed | [Open](ONIZLEME.html?scene=detail-changed-none) |
| `detail-changed-interested` | Detay · Bilgiler güncellendi / INTERESTED | INTERESTED | changed | [Open](ONIZLEME.html?scene=detail-changed-interested) |
| `detail-changed-going` | Detay · Bilgiler güncellendi / GOING | GOING | changed | [Open](ONIZLEME.html?scene=detail-changed-going) |
| `detail-loading` | Detay · Yükleniyor | NONE | loading | [Open](ONIZLEME.html?scene=detail-loading) |
| `detail-error` | Detay · Hata | NONE | error | [Open](ONIZLEME.html?scene=detail-error) |
| `detail-offline` | Detay · Çevrimdışı | NONE | offline | [Open](ONIZLEME.html?scene=detail-offline) |
| `detail-not-found` | Detay · Ulaşılamıyor | NONE | not-found | [Open](ONIZLEME.html?scene=detail-not-found) |
| `detail-image-failed` | Detay · Görsel alınamıyor | NONE | image-failed | [Open](ONIZLEME.html?scene=detail-image-failed) |
| `detail-long-content` | Detay · Uzun içerik | NONE | long-content | [Open](ONIZLEME.html?scene=detail-long-content) |
| `detail-category-social` | Detay · kategori SOCIAL | NONE | ready | [Open](ONIZLEME.html?scene=detail-category-social) |
| `detail-category-activity` | Detay · kategori ACTIVITY | NONE | ready | [Open](ONIZLEME.html?scene=detail-category-activity) |
| `detail-calendar-opening` | Detay · calendar / opening | GOING | calendar-opening | [Open](ONIZLEME.html?scene=detail-calendar-opening) |
| `detail-calendar-failed` | Detay · calendar / failed | GOING | calendar-failed | [Open](ONIZLEME.html?scene=detail-calendar-failed) |
| `detail-map-opening` | Detay · map / opening | GOING | map-opening | [Open](ONIZLEME.html?scene=detail-map-opening) |
| `detail-map-failed` | Detay · map / failed | GOING | map-failed | [Open](ONIZLEME.html?scene=detail-map-failed) |

All three categories appear in list-populated; NETWORKING uses detail-none, SOCIAL/ACTIVITY have dedicated cases. Locked/cancelled/changed cover all three RSVP values. The 299-screen baseline remains intact: this is an additive development delivery, not a silent replacement of the production placeholder.
