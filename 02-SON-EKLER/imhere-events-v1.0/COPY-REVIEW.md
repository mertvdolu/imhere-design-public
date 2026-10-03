# Events V1 — proposed copy / EN + TR

**Status: PROPOSED; Founder approval required.** New copy is not canonical. Files in `l10n/` are review-only deltas. They are deliberately not registered in the shared migration.json and must not overwrite the full ARBs. Existing navigation / retry text is reused in preview only.

| Key | EN proposal | TR proposal |
|---|---|---|
| `eventsV1Intro` | Find a moment that fits. | Sana uyan bir an bul. |
| `eventsV1Loading` | Loading events… | Etkinlikler yükleniyor… |
| `eventV1Loading` | Loading event… | Etkinlik yükleniyor… |
| `eventsV1EmptyTitle` | Nothing planned just yet. | Henüz bir etkinlik yok. |
| `eventsV1EmptyBody` | Events will appear here when they’re available. | Etkinlikler hazır olduğunda burada görünecek. |
| `eventsV1ErrorTitle` | Events aren’t available right now. | Şu an etkinliklere ulaşılamıyor. |
| `eventsV1ErrorBody` | Please try again. | Tekrar deneyebilirsin. |
| `eventsV1OfflineTitle` | You’re offline. | Çevrimdışısın. |
| `eventsV1OfflineBody` | Reconnect to see the latest event details. | Güncel etkinlik bilgilerini görmek için yeniden bağlan. |
| `eventV1UnavailableTitle` | This event isn’t available. | Bu etkinliğe ulaşılamıyor. |
| `eventV1UnavailableBody` | You can return to the events list. | Etkinlik listesine dönebilirsin. |
| `eventV1Back` | Back to events | Etkinliklere dön |
| `eventV1CategoryNetworking` | Networking | Networking |
| `eventV1CategorySocial` | Social | Sosyal |
| `eventV1CategoryActivity` | Activity | Aktivite |
| `eventV1CategoryLabel` | Category: {category} | Kategori: {category} |
| `eventV1Start` | Starts | Başlangıç |
| `eventV1End` | Ends | Bitiş |
| `eventV1Venue` | Venue | Mekân |
| `eventV1About` | About this event | Etkinlik hakkında |
| `eventV1YourChoice` | Your choice | Tercihin |
| `eventV1Interested` | Interested | İlgileniyorum |
| `eventV1Going` | Going | Gideceğim |
| `eventV1None` | No choice yet | Henüz bir tercih yok |
| `eventV1Withdraw` | Withdraw | Tercihimi geri çek |
| `eventV1ChoiceHelp` | Only your own choice is shown here. Going does not check you in. | Burada yalnız kendi tercihin görünür. Gideceğim seçeneği check-in yapmaz. |
| `eventV1Saving` | Updating your choice… | Tercihin güncelleniyor… |
| `eventV1SaveFailed` | Your choice couldn’t be updated. Please try again. | Tercihin güncellenemedi. Tekrar deneyebilirsin. |
| `eventV1SavedAnnouncement` | Your choice is now {choice}. | Tercihin artık {choice}. |
| `eventV1WithdrawnAnnouncement` | Your choice has been withdrawn. | Tercihin geri çekildi. |
| `eventV1Started` | Event started | Etkinlik başladı |
| `eventV1LockedBody` | Choices can no longer be changed after the event starts. | Etkinlik başladıktan sonra tercihler değiştirilemez. |
| `eventV1Cancelled` | Cancelled | İptal edildi |
| `eventV1CancelledBody` | This event has been cancelled. Event actions are unavailable. | Bu etkinlik iptal edildi. Etkinlik işlemleri kullanılamıyor. |
| `eventV1CancelledChoice` | Your previous choice: {choice}. It is no longer active. | Önceki tercihin: {choice}. Artık geçerli değil. |
| `eventV1ChangedTitle` | Event details updated | Etkinlik bilgileri güncellendi |
| `eventV1ChangedBody` | Review the latest information below. | Güncel bilgileri aşağıda inceleyebilirsin. |
| `eventV1ChoiceKept` | Your choice is unchanged. | Tercihin değişmedi. |
| `eventV1Plan` | Make a plan | Planına ekle |
| `eventV1Calendar` | Add to Calendar | Takvime ekle |
| `eventV1Map` | Open venue on map | Mekânı haritada aç |
| `eventV1CalendarHelp` | Calendar entries won’t update automatically if event details change. | Etkinlik bilgileri değişirse takvim kaydı otomatik güncellenmez. |
| `eventV1CalendarOpening` | Opening your calendar… | Takvimin açılıyor… |
| `eventV1CalendarFailed` | Your calendar couldn’t be opened. Please try again. | Takvimin açılamadı. Tekrar deneyebilirsin. |
| `eventV1MapOpening` | Opening the venue on your map… | Mekân haritada açılıyor… |
| `eventV1MapFailed` | The map couldn’t be opened. Please try again. | Harita açılamadı. Tekrar deneyebilirsin. |
| `eventV1ReminderPush` | An event you’re going to starts soon. | Gideceğin bir etkinlik yakında başlıyor. |
| `eventV1ChangedPush` | An event you chose has been updated. | Tercih belirttiğin bir etkinlik güncellendi. |
| `eventV1CancelledPush` | An event you chose has been cancelled. | Tercih belirttiğin bir etkinlik iptal edildi. |
| `eventV1TimeZone` | Times shown in {zone}. | Saatler {zone} saat diliminde gösterilir. |
| `eventV1ImageUnavailable` | Event image unavailable | Etkinlik görseli kullanılamıyor |
| `eventV1ListChoice` | Your choice: {choice} | Tercihin: {choice} |

Push proposals have no event title, venue, user name, sender title or attendee data. Reminder: GOING only, scheduled one hour before start; delivery text says “soon” so it does not promise precise delivery. No channel, sound or foreground rule is invented. Use the existing approved notification plumbing.

Founder decision needed: approve or amend this copy set. Technical content limits (80/1000) and the production timezone are proposals in Code documents; this design does not make them policy. Timezone is explicit in the preview as a fixture; use the approved display timezone in native.
