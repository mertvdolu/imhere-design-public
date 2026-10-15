# ayarlar-topluluk — durum matrisi

Her durum: EN/TR × %100/%200 × 390×844 / 412×915; 4× opak PNG. `--full` yalnız kaydırılan içerikte. Dar ekran: 320/%200 iOS + Android ölçümü.

| State | Davranış |
|---|---|
| settings-one | Only own membership. Join/leave/switch count separately in rolling24h; first selection free. No optimistic membership change. |
| settings-both | Only own membership. Join/leave/switch count separately in rolling24h; first selection free. No optimistic membership change. |
| settings-checked-in | Only own membership. Join/leave/switch count separately in rolling24h; first selection free. No optimistic membership change. |
| settings-going | Only own membership. Join/leave/switch count separately in rolling24h; first selection free. No optimistic membership change. |
| settings-limit | Only own membership. Join/leave/switch count separately in rolling24h; first selection free. No optimistic membership change. |
| settings-last-one | Only own membership. Join/leave/switch count separately in rolling24h; first selection free. No optimistic membership change. |
| settings-failed | Only own membership. Join/leave/switch count separately in rolling24h; first selection free. No optimistic membership change. |
| settings-switch-done | Only own membership. Join/leave/switch count separately in rolling24h; first selection free. Server acknowledgement received. |
| settings-join-done | Only own membership. Join/leave/switch count separately in rolling24h; first selection free. Server acknowledgement received. |
| settings-leave-done | Only own membership. Join/leave/switch count separately in rolling24h; first selection free. Server acknowledgement received. |
| settings-switch-confirm | Confirmation before mutation. Inactive leave/join does not change active community or end check-in. Active leave order: active note, check-in, Going, leave body, remaining. No reset time or countdown. |
| settings-switch-checkin | Confirmation before mutation. Inactive leave/join does not change active community or end check-in. Active leave order: active note, check-in, Going, leave body, remaining. No reset time or countdown. |
| settings-switch-going | Confirmation before mutation. Inactive leave/join does not change active community or end check-in. Active leave order: active note, check-in, Going, leave body, remaining. No reset time or countdown. |
| settings-join-confirm | Confirmation before mutation. Inactive leave/join does not change active community or end check-in. Active leave order: active note, check-in, Going, leave body, remaining. No reset time or countdown. |
| settings-leave-inactive | Confirmation before mutation. Inactive leave/join does not change active community or end check-in. Active leave order: active note, check-in, Going, leave body, remaining. No reset time or countdown. |
| settings-leave-active | Confirmation before mutation. Inactive leave/join does not change active community or end check-in. Active leave order: active note, check-in, Going, leave body, remaining. No reset time or countdown. |
| settings-leave-active-going | Confirmation before mutation. Inactive leave/join does not change active community or end check-in. Active leave order: active note, check-in, Going, leave body, remaining. No reset time or countdown. |
| settings-joining | Pending join/leave response, no visible progress text. Reuse 24×24 loading arc, stroke1.8; progressbar labelled by screen title for accessibility. Failure uses communitySettingsChangeFailed; no premature success. |
| settings-leaving | Pending join/leave response, no visible progress text. Reuse 24×24 loading arc, stroke1.8; progressbar labelled by screen title for accessibility. Failure uses communitySettingsChangeFailed; no premature success. |
| settings-switching | Pending server response, no premature success. Controls replaced by status; completion restores action availability. |
| settings-switch-failed | Switch failed: old membership and active community remain. Uses communitySwitchFailed; join/leave failure remains settings-failed / communitySettingsChangeFailed. |
| settings-loading | Settings read gate. No guessed membership, link, default visibility, or stale controls until current server data is read. Existing generic error + Retry; no mutation is attempted. |
| settings-read-failed | Settings read gate. No guessed membership, link, default visibility, or stale controls until current server data is read. Existing generic error + Retry; no mutation is attempted. |
