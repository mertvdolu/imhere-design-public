## 7. M06 uygulama notları (2026-09-16) — Designer'a

Kod: `app/lib/screens/{messages_screen, other_profile_screen, intent_select_screen, request_screens, match_screen, events_placeholder_screen}.dart`, `app/lib/main.dart` (kabuk). Kayıt: `docs/engineering-decisions.md` ENG-M06-07.

| Konu | Uygulama | Designer'dan beklenen |
|---|---|---|
| Metinler | v1.7 istek / eşleşme / mesajlar ve v1.8 sekme / Etkinlikler anahtarları **birebir** (`app/test/m06_l10n_test.dart`) | — |
| `pendingSlots` | Tasarım `"{used}/20 bekleyen istek"`; uygulama `"{used}/{max} bekleyen istek"` (üst sınır sözleşmeden parametre) | Paket anahtarını `{max}` ile hizala |
| `profileAgeYears` **NOT LOCKED** | `"{age} yaşında"` / `"{age} years old"` — v1.6 `view-other-visible` "28 yaşında" satırı için; pakette anahtar yok | Kanonik anahtar adı + metin |
| `requestCooldown` **NOT LOCKED** (S4) | `"Şu an bu kişiye istek gönderilemiyor."` / `"You can’t send a request to this person right now."`; kişi görünümünde pasif düğme altında; süre / neden yok | Metin ve görsel durum (paket v1.7'de cooldown durumu yok) |
| `requestClosed` (FD-79) | "Bu istek sona erdi." — REJECTED ve engel / hesap sonlanması için tek nötr kart | — (anlam LOCKED, metin paketteki) |
| Sohbete geç (S2) | M06'da gizli | — (M07 açar) |
| Görsel (M10) | Büyük metinde 2×2 sekme çubuğu; istek / eşleşme ekranları sekme çubuğu altında (M06'da tam ekran rota); üst başlık bandı; seçim kartı renk token'ları | M10 UX checkpoint'inde doğrulama |

