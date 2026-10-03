# Events V1 — mobile design specification v1.0

2026-10-03 · Cream & Ink v2.3 · Design branch delivery

## 1. Authority and release boundary

The current Founder brief is preserved in `source/FOUNDER-BRIEF.txt`. It supersedes the earlier Events-placeholder restriction **for this limited development scope**. Founder/Admin-created events only; no user creation, tickets, payments, attendee lists/counts/avatars, social proof, chat, matching, intent selection, attendance verification or location tracking.

Supporting reads: Code `docs/events-v1/07-tasarim-brifi.md`, `00-founder-karari-2026-10-03.md`, `01-veri-modeli.md`, `03-sunucu-sozlesme.md`, `05-bildirim.md`, `06-acik-kararlar.md`. These contain earlier proposals/open questions. The current brief settles reminder recipients/time, changed-notification fields and cancellation visibility; those questions are not reopened here. Draft backend names are mapping hints, not new APIs defined by design.

Theme authority: design SHA `58bf8c4380c9e2b8487b32d5d94f6f1e683ad649`, `../imhere-cream-complete-v2.2/theme-v2.3/SPEC.md` and v10 compact layout. This package does not modify the app, backend, contracts, production feature flags or existing 299 base illustrations. It adds 36 deterministic development views. The old placeholder is replaced in native only when the approved Events implementation is released.

**Copy is PROPOSED.** `COPY-REVIEW.md` and `l10n/events-v1-proposed_{en,tr}.arb` need Founder approval. They are not in the shared migration registry. Do not auto-merge or overwrite full ARBs. EN active / TR prepared remains the existing language policy.

## 2. Navigation and hierarchy

- Events remains the fourth tab: Profile → Messages → Nearby → Events. No new tab.
- List is the Events root. A card opens its detail; back returns to the existing list, preserving its scroll position. Native iOS/Android back behavior remains unchanged.
- Both list and detail retain the post-onboarding bottom menu. List root has the existing brand mark; detail has a left 48×48 back target. No top-right menu, share action, filter or search is introduced.
- Event actions do not switch to Nearby, change check-in, write a location, or paint an activity map. Venue opens the device's map experience; it is not the in-app privacy heatmap.
- No local countdown for start, reminder or cancellation expiry. Visibility/lock comes from the current server-authoritative state, not a device-clock-only decision.

## 3. Exact visual layout

Logical pixels (dp on Android, points in Flutter on iOS). Safe areas added by native, never scaled twice.

| Element | Specification |
|---|---|
| Page edge | 24; app-bar controls keep 48 target |
| App bar | minimum 64 in preview; native safe-area/app-bar behavior retained |
| Page/detail title | compactPageTitle 28 / 500 / 1.15 / −0.7; wraps, no ellipsis |
| Section heading | sectionTitle 18 / 500 / 1.4 |
| Body description | body 16 / 400 / 1.6; plain text; wraps long words/URLs without adding click behavior |
| Metadata | helper 14 / 400 / 1.5 or metadata 12 / 400 / 1.5; never reduced to fit |
| List card | cream, border surfaceEdge 1, radius 16 (Events component token), padding 14, gap 14; raised role |
| List thumbnail | 72×90, radius 9; decoration, no separate hit target |
| List card title | 18 / 500 / 1.3; unlimited wrapping |
| Category | static text 11 / 500 / 1.4 + simple 14 icon; uppercase presentation; meaningful text retained |
| Detail hero | 16:9, full content width, radius 16; object-fit cover; no text burned into image |
| Facts | icon 20, gap 12; explicit Starts, Ends, Venue labels |
| Sections | 24 above/below, divider border 1; no nested card around every section |
| Choice control | label 14 / 500 / 1.4, face padding 8 vertical / 16 horizontal, pill; minimum hit 48×48 |
| Two choices | 8 gap between hit boxes; wrap/stack when labels do not fit; no overlap |
| Selected choice | flat ink face + checkmark + selected semantic state; no own shadow |
| Unselected choice | raised cream face; shadow cannot paint over selected neighbor |
| Withdraw | quiet underlined text, minimum 48×48; no destructive red treatment |
| Calendar/map | compact secondary actions, wrapping independently; icon 20, target ≥48 |
| Notice | inline icon 20 + text, gap 12, padding 14 vertical; neutral rule, no red alarm card |
| Bottom menu | v10: edge16 (8 at large text), radius26, inner4, label12; 2×2 at large text; actual measured height reserved |

The component-specific 16/9/11 values above are **Events-only additions**, declared in `tokens.components.json`; they do not replace the common card/input radius or typography. No global token edits.

Color references: paper/navigation `#F4F1E9`, ink `#191A17`, on-ink `#FCFAF5`, secondary `#696A62`, control border `#7C7D73`, decorative edge `#B7B3A9`, divider `#D9D5CB`. Raised shadow: dark `#D6D2C8` +5/+5 sigma5; light `#FFFEFA` −5/−5 sigma5; spread0. Primary black actions, if reused in a host flow, use the existing primary shadow. **RSVPs are choices, not a new black default selection:** NONE shows both unselected; selected state is black only after confirmed response. No added Save/Confirm RSVP step.

Categories NETWORKING / SOCIAL / ACTIVITY share one neutral style. They are not interactive chips, intent choices, map colors or attendee identities. Icons are decorative; text carries the category. Missing/failed imagery uses a fixed neutral image placeholder with no person avatar and no retry that would block the whole event.

## 4. List states

| State | Rendering / recovery |
|---|---|
| loading | One 24×24, 1.8 stroke functional spinner with accessible status; two inert non-shimmer placeholder rows. No fake event text. |
| populated | Image, title, static category, start/end date-time, venue and **own** confirmed RSVP. Card has one accessible activation target. |
| empty | Calm title/body, calendar illustration. No fake events, create button or notification opt-in. |
| error | Calm title/body + secondary Try again. Do not call an unknown server problem offline. |
| offline | Use only a confirmed connectivity state; retry stays available. No invented cached list or offline RSVP queue. |
| cancelled visible | Neutral cancellation icon + CANCELLED label. Card still opens the read-only cancelled detail; no RSVP shortcuts. |
| started | Neutral lock + Event started; own last confirmed choice can remain visible. No attendance claim. |
| image failure | Same real metadata/card action; image-only placeholder. |

The server supplies visible events and ordering. Supporting brief proposes upcoming/ongoing sorted by start time; do not introduce client-side discovery rules or past archive. Cancelled events may remain visible for 24 hours, then leave the normal list, per Founder. **No client countdown, archival section or retention promise.** Detail from an old notification resolves against current access and availability. List removal does not itself mean data deletion.

## 5. RSVP matrix and response handling

State is mutually exclusive: NONE / INTERESTED / GOING. Two compact choice buttons form one semantic group. Buttons have clear selected state/checkmark; only the user's own choice is exposed.

| Last confirmed state | Before start | While request pending | After start | Cancelled |
|---|---|---|---|---|
| NONE | choose Interested or Going | both temporarily unavailable; state stays NONE | both disabled + explanation | all event actions disabled |
| INTERESTED | switch to Going or Withdraw | keep Interested selected; controls unavailable | Interested remains marked, all RSVP controls disabled | no active selected choice; optional previous-choice sentence |
| GOING | switch to Interested or Withdraw | keep Going selected; controls unavailable | Going remains marked, all RSVP controls disabled | no active selected choice; optional previous-choice sentence |

- Tapping the already selected choice does not silently withdraw it. Withdraw is explicit and uses the existing NONE transition. No confirmation dialog added.
- No optimistic checkmark or success statement. Display the final state only after server confirmation. On failure, restore/retain the last confirmed state, show inline error and retry for the attempted transition. Do not fabricate a successful withdrawal.
- On a server lock/cancellation response while editing, refresh the event and render the authoritative locked/cancelled state; no retry loop that promises the change remains possible.
- Start lock applies to RSVP changes only. Calendar and map remain available for an available, non-cancelled started event. They do not unlock RSVP or verify attendance.
- Cancelled overrides start-lock/changed styling. All event actions (Interested, Going, Withdraw, Calendar, Map) are disabled. Back and normal navigation stay available. The list card remains an entry to read the cancellation.
- NONE has no active choice. Cancellation does not visually reset retained backend data to NONE; prior choice is historical and explicitly inactive.
- Choice helper clarifies Going does not check in. Never use I'm here, presence rings, heatmap colors, location precision, badges implying arrival, or other people's avatars.

## 6. Changed event

Render current event content. A subtle neutral “Event details updated” notice sits above the hero on an authoritative changed-event entry (e.g. changed notification route after refresh). INTERESTED/GOING remains selected and the “Your choice is unchanged” line may be shown. NONE remains NONE. No reconfirmation requirement, auto-withdrawal, old/new personal history or red warning.

Push-triggering fields: **title, start, end, venue**. Description/image/category changes **do not trigger push**. Design does not derive a new push/notice rule from client-side string comparisons. An in-app notice depends on a trustworthy existing change context; if no such context is available, show current content only. No new persistent read/acknowledged backend field is required by this design.

## 7. Calendar and map

- Add to Calendar opens the platform's existing one-time calendar handoff/editor, populated with the current event's title, description, start/end and venue. This is not a subscription or synchronization promise. Use the approved native integration; this design adds no dependency or permissions policy.
- Display the proposed helper explaining calendar entries do not auto-update. No attendee counts/RSVP identity list is transferred. Calendar does not alter RSVP.
- During handoff only the initiating action is busy; the result is never “saved” merely because the editor opened. Returning/cancelling leaves RSVP unchanged. If a platform gives no reliable save callback, show no save-success claim.
- Opening failure: inline error under action row; the original action is enabled for retry. Do not redirect to app settings or invent a clipboard fallback.
- Open venue on map opens the device map experience for the **event venue**, using the approved coordinates/address contract. It neither recenters the I’M HERE heatmap nor obtains/updates user location. No embedded attendee map or live position.
- If event payload lacks the data required to launch, keep the action unavailable with the approved error treatment and report the contract issue; do not fabricate an address/coordinate. Missing venue is not added as a product state because venue is a required event field in the brief.
- Calendar/map return and calendar editor cancellation are normal returns, not error states. The prototype simulates opening/failure; it never launches system apps.

## 8. Responsive, text, accessibility, platforms

- Deliver EN/TR on 320/390/412 widths, 100/200% text. Both platform shells are selectable. These are HTML design views, not native device evidence.
- At 200%, list thumbnails use a shallow full-row image and text moves below. Categories, titles, dates, venue, warnings and buttons wrap fully. RSVP and external actions stack when needed. Do not shrink text or truncate titles to preserve a row.
- Bottom navigation is 2×2, reading order Profile, Messages, Nearby, Events. Its real height + safe area is reserved outside the content scroll area. The body and detail sections scroll; no tall pinned RSVP panel. All actions remain reachable.
- Always label full start **and end** dates, including cross-day events. Use localized native date/time formatting and an explicit approved display timezone; never silently equate event timezone with device timezone. Fixture Europe/London is not a new global product setting.
- Images are decorative when title/category provide identity; alt empty. Missing-image fallback has an accessible name. No image-baked text or assumed photo identity.
- Card semantics: one button, then category/title/time/venue/own status in reading order; no nested interactive element. Details: back → state notice → title → facts → choice group → actions → description → bottom menu.
- Native choice semantics: selected/checked + enabled state + label. Disabled controls remain discoverable to assistive technology; the lock/cancel explanation precedes them. Empty choice is not read as either selected.
- Success changes announce once with a polite live region after server confirmation. Error announces once; preserve focus on the action/choice when possible, not at page top. Full route changes use the existing heading focus behavior. No focus is hidden behind the menu.
- Focus: native fields may use the accepted 2dp ink boundary; Events has no text-entry field. Buttons retain clear focus indication (2 ink stroke +3 gap in HTML). Touch ≥48×48, adjacent hitboxes never overlap.
- High contrast removes all shadows and keeps control borders, icons, checkmarks and text. Reduce Transparency uses 100% paper menu without backdrop blur. Reduce Motion removes decorative transition/scale; the essential 24dp progress spinner may rotate per the accepted loading rule. Motion uses existing H0/quick timing (150ms); no new haptic or confetti.
- iOS uses system route transitions and safe areas; Android uses existing approved transitions/back. No custom OS calendar or permission-sheet drawing is supplied as native truth.

## 9. Notifications — proposed bodies only

`eventV1ReminderPush`: GOING only, scheduled one hour before start. INTERESTED receives no reminder. INTERESTED and GOING can receive changed/cancelled notifications. No event title, venue, user name or body content is put into the lock-screen proposal. No extra notification title is supplied.

Tap resolves current event detail. Cancellation → cancelled if still accessible; unavailable event → neutral unavailable view. Opening a notification never submits RSVP. Reuse the approved notification infrastructure: this package does not create channel names, sound defaults, foreground rules, delivery guarantees, quotas or coalescing intervals.

## 10. State precedence / non-covered product contracts

1. Cannot read event: loading/error/offline/unavailable, no stale enabled RSVP.
2. CANCELLED overrides changed or started.
3. Started + available: locked own RSVP, external actions usable.
4. Pre-start authoritative changed context: updated notice, same own choice.
5. Pending request: retain confirmed choice until success/error/lock.

The 24-hour cancellation visibility is a list rule, not retention. Event/RSVP retention, exact content limits, finalized DTO field names, notification channel policy and release authorization remain Manager/Code/Founder responsibilities. No new requirement is created by fixture values. 80/1000 character values in the draft engineering brief are not promoted to locked limits; the long-content view stress-tests wrapping without truncation.

## 11. Code handoff checks

- Bind to finalized authoritative contracts; verify empty → selected → switch → withdraw, late response at start, cancellation during update and offline retry. No backend code supplied here.
- Verify 320-wide native +200% EN/TR, actual menu height/insets, scrolling to all actions, screen reader order/selected/disabled announcements, device high contrast and Reduce Transparency.
- Verify both choice orders for shadow overlap, divider `#D9D5CB`, menu `#F4F1E9`; Founder-accepted global native deviations are not reopened.
- Calendar cancel must not announce saved; map launch must not trigger location permission/check-in; started must not re-enable RSVP; cancelled must not leave Calendar/Map active.
- Fresh native iOS/Android screenshots are required before store preparation. This package includes no store assets and no production deployment.
