# ayarlar-topluluk — SPEC

## Bileşenler / ölçü

Mevcut v2.3 başlık, küçük düğme, bilgi kartı, input, radyo ve satır desenleri. Kenar 24 dp. Başlık 28/600, gövde 16/400, yardım 14/400; satır aralığı 1.18/1.5/1.5. Bölüm başlığı 18/500. Ölçek %200: punto 2×, sabit satır sınırı yok. Küçük düğme görünen yüzey en az 36, bağımsız hedef en az 48×48; radius12. Kart radius15.

Mevcut düz Ayarlar satırı (yeni kabartmalı kutu yok), iki topluluk. Aktif: In use + ikon. Tek üyelikte ayrıl düğmesi yok, LastOne açıklaması var. Sınırda join/leave/switch kaldırılır, LimitReached gösterilir. Sabit24 saat kuralı. Onayda remaining sayısı; saat/tarih/geri sayım yok. Aktiften ayrılma metin sırası birebir: ActiveNote → CheckInEndsNote(varsa) → GoingNote(varsa) → LeaveBody → Remaining.

## Durumlar

- **settings-one**: Only own membership. Join/leave/switch count separately in rolling24h; first selection free. No optimistic membership change.
- **settings-both**: Only own membership. Join/leave/switch count separately in rolling24h; first selection free. No optimistic membership change.
- **settings-checked-in**: Only own membership. Join/leave/switch count separately in rolling24h; first selection free. No optimistic membership change.
- **settings-going**: Only own membership. Join/leave/switch count separately in rolling24h; first selection free. No optimistic membership change.
- **settings-limit**: Only own membership. Join/leave/switch count separately in rolling24h; first selection free. No optimistic membership change.
- **settings-last-one**: Only own membership. Join/leave/switch count separately in rolling24h; first selection free. No optimistic membership change.
- **settings-failed**: Only own membership. Join/leave/switch count separately in rolling24h; first selection free. No optimistic membership change.
- **settings-switch-done**: Only own membership. Join/leave/switch count separately in rolling24h; first selection free. Server acknowledgement received.
- **settings-join-done**: Only own membership. Join/leave/switch count separately in rolling24h; first selection free. Server acknowledgement received.
- **settings-leave-done**: Only own membership. Join/leave/switch count separately in rolling24h; first selection free. Server acknowledgement received.
- **settings-switch-confirm**: Confirmation before mutation. Inactive leave/join does not change active community or end check-in. Active leave order: active note, check-in, Going, leave body, remaining. No reset time or countdown.
- **settings-switch-checkin**: Confirmation before mutation. Inactive leave/join does not change active community or end check-in. Active leave order: active note, check-in, Going, leave body, remaining. No reset time or countdown.
- **settings-switch-going**: Confirmation before mutation. Inactive leave/join does not change active community or end check-in. Active leave order: active note, check-in, Going, leave body, remaining. No reset time or countdown.
- **settings-join-confirm**: Confirmation before mutation. Inactive leave/join does not change active community or end check-in. Active leave order: active note, check-in, Going, leave body, remaining. No reset time or countdown.
- **settings-leave-inactive**: Confirmation before mutation. Inactive leave/join does not change active community or end check-in. Active leave order: active note, check-in, Going, leave body, remaining. No reset time or countdown.
- **settings-leave-active**: Confirmation before mutation. Inactive leave/join does not change active community or end check-in. Active leave order: active note, check-in, Going, leave body, remaining. No reset time or countdown.
- **settings-leave-active-going**: Confirmation before mutation. Inactive leave/join does not change active community or end check-in. Active leave order: active note, check-in, Going, leave body, remaining. No reset time or countdown.
- **settings-joining**: Pending server response, no premature success. Controls replaced by status; completion restores action availability.
- **settings-leaving**: Pending server response, no premature success. Controls replaced by status; completion restores action availability.
- **settings-switching**: Pending server response, no premature success. Controls replaced by status; completion restores action availability.

## Erişilebilirlik / native

Her durum tek H1, doğal üstten alta okuma; %200 ve320 genişlikte yatay kaydırma yok. En az48 hedef, renk yanında metin/ikon. Pasif kontrolün koşulu mevcut metin veya işlem durumu ile görünür. Varsa radyo grup etiketi, checkbox çoklu seçim, switch görünür etiketle. Focus visible 2 px Ink +3 offset. `Reduce Motion`: 150 ms doğrusal opaklık, mekânsal hareket yok. Yüksek kontrastta gölge yok, belirgin Ink kenar; şeffaflığı azaltmada menü opak.

## ★ / yeni bileşen

★ Son topluluktan ayrıl düğmesi kaldırıldı; neden satırda. ★ Katıl/ayrıl beklerken aynı işlem durum alanı, yeni başarı rengi yok. YENİ BİLEŞEN — ONAY GEREKİR: yok; mevcut satır, tam sayfa onay ve bekleme desenleri.
