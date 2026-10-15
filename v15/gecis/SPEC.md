# gecis — SPEC

## Bileşenler / ölçü

Mevcut v2.3 başlık, küçük düğme, bilgi kartı, input, radyo ve satır desenleri. Kenar 24 dp. Başlık 28/600, gövde 16/400, yardım 14/400; satır aralığı 1.18/1.5/1.5. Bölüm başlığı 18/500. Ölçek %200: punto 2×, sabit satır sınırı yok. Küçük düğme görünen yüzey en az 36, bağımsız hedef en az 48×48; radius12. Kart radius15.

İlk geçiş: Intro → topluluk → linkedinTransitionNeeded varsa görünürlük → isteğe bağlı meslek daveti. LINK_CHANGED ise yalnız görünürlük ekranı açılır; intro/topluluk tekrarlanmaz. FIRST gövdesi v15LinkedinBody, LINK_CHANGED gövdesi v15LinkedinChangedBody. Kayıtlı ayar seçili gelir; değişmiş link örneğinde Nobody. Radyo legend erişilebilir kalır, H1 ile aynı başlık görsel olarak gizlidir. Kapatılırsa kayıtlı ayar kalır; hata aynı ekranda kayıtlı ayara döner.

## Durumlar

- **migration-intro**: No inferred choice. Not visible in discovery until community selection.
- **migration-community**: Reuses registration selection component. Initial selection ends previous check-in; no rate-limit cost. LinkedIn step only if stored.
- **migration-linkedin-everyone**: Shown only when linkedinTransitionNeeded=true. FIRST uses v15LinkedinBody. Dismiss keeps the stored setting; first-transition fixture is Everyone. Failure restores the stored setting and stays here. Group legend is visually hidden but accessible.
- **migration-linkedin-connections**: Shown only when linkedinTransitionNeeded=true. FIRST uses v15LinkedinBody. Dismiss keeps the stored setting; first-transition fixture is Everyone. Failure restores the stored setting and stays here. Group legend is visually hidden but accessible.
- **migration-linkedin-nobody**: Shown only when linkedinTransitionNeeded=true. FIRST uses v15LinkedinBody. Dismiss keeps the stored setting; first-transition fixture is Everyone. Failure restores the stored setting and stays here. Group legend is visually hidden but accessible.
- **migration-linkedin-saving**: Shown only when linkedinTransitionNeeded=true. FIRST uses v15LinkedinBody. Dismiss keeps the stored setting; first-transition fixture is Everyone. Failure restores the stored setting and stays here. Group legend is visually hidden but accessible.
- **migration-linkedin-failed**: Shown only when linkedinTransitionNeeded=true. FIRST uses v15LinkedinBody. Dismiss keeps the stored setting; first-transition fixture is Everyone. Failure restores the stored setting and stays here. Group legend is visually hidden but accessible.
- **migration-linkedin-offline**: Shown only when linkedinTransitionNeeded=true. FIRST uses v15LinkedinBody. Dismiss keeps the stored setting; first-transition fixture is Everyone. Failure restores the stored setting and stays here. Group legend is visually hidden but accessible.
- **migration-occupation**: Optional one-time invitation. Equal button treatment. Existing free text is not mapped automatically.
- **migration-offline**: Network failure keeps route and avoids inferred membership.
- **migration-linkedin-changed-default**: Standalone LINK_CHANGED review, no intro/community steps. Stored setting Nobody; other-selection example Connections. Dismiss and failure retain stored Nobody; success only after server ack returns to the existing app. No transition if linkedinTransitionNeeded=false.
- **migration-linkedin-changed-other**: Standalone LINK_CHANGED review, no intro/community steps. Stored setting Nobody; other-selection example Connections. Dismiss and failure retain stored Nobody; success only after server ack returns to the existing app. No transition if linkedinTransitionNeeded=false.
- **migration-linkedin-changed-saving**: Standalone LINK_CHANGED review, no intro/community steps. Stored setting Nobody; other-selection example Connections. Dismiss and failure retain stored Nobody; success only after server ack returns to the existing app. No transition if linkedinTransitionNeeded=false.
- **migration-linkedin-changed-failed**: Standalone LINK_CHANGED review, no intro/community steps. Stored setting Nobody; other-selection example Connections. Dismiss and failure retain stored Nobody; success only after server ack returns to the existing app. No transition if linkedinTransitionNeeded=false.
- **migration-linkedin-changed-offline**: Standalone LINK_CHANGED review, no intro/community steps. Stored setting Nobody; other-selection example Connections. Dismiss and failure retain stored Nobody; success only after server ack returns to the existing app. No transition if linkedinTransitionNeeded=false.

## Erişilebilirlik / native

Her durum tek H1, doğal üstten alta okuma; %200 ve320 genişlikte yatay kaydırma yok. En az48 hedef, renk yanında metin/ikon. Pasif kontrolün koşulu mevcut metin veya işlem durumu ile görünür. Varsa radyo grup etiketi, checkbox çoklu seçim, switch görünür etiketle. Focus visible 2 px Ink +3 offset. `Reduce Motion`: 150 ms doğrusal opaklık, mekânsal hareket yok. Yüksek kontrastta gölge yok, belirgin Ink kenar; şeffaflığı azaltmada menü opak.

## ★ / yeni bileşen

Mevcut radyo/confirm görünüşleri korundu. Yeni v15LinkedinChangedBody HB-37 r6 / HB-41 §15, karar58 ile onaylıdır; önceki değerler değişmedi. Yeni görsel karar yok.
