# EMAIL-01 — English (UK) copy v1.0

12 Ekim 2026 · **PROPOSED — HARBOR + FOUNDER COPY APPROVAL REQUIRED**.

## 1. Founder brifindeki metinler — aynen

Aşağıdaki metinler kısaltılmadı; straight apostrophe dahil özgün yazım korundu. Null/eksik alanlar aşağıda açıkça ayrılır. E-posta dili yalnız EN-GB; TR üretilmedi.

### 01-confirm-email

Alıcı / tetik: Registration email; resend uses the same template

| Alan | Metin |
|---|---|
| subject | Confirm your email for I'M HERE |
| preheader | One tap to finish setting up your account. |
| heading | Confirm your email |
| body | Tap the button to confirm this is your email address. Then go back to I'M HERE and tap Check verification. |
| button | Confirm email |
| expiry | This link expires in {{EXPIRY}}. |
| safety | Didn't create an I'M HERE account? You can ignore this email. |
| action | {{ACTION_URL}} |

### 02-reset-password

Alıcı / tetik: Account email

| Alan | Metin |
|---|---|
| subject | Reset your I'M HERE password |
| preheader | Choose a new password. |
| heading | Reset your password |
| body | We received a request to reset the password for {{EMAIL}}. Tap the button to choose a new one. |
| button | Choose a new password |
| expiry | This link expires in {{EXPIRY}}. |
| safety | Didn't ask for this? You can ignore this email. Your password won't change. |
| action | {{ACTION_URL}} |

### 03-confirm-new-email

Alıcı / tetik: New email, before confirmation

| Alan | Metin |
|---|---|
| subject | Confirm your new email for I'M HERE |
| preheader | Brifte belirtilmedi; öneri/ortak yerleşim aşağıda. |
| heading | Confirm your new email |
| body | Tap the button to make {{NEW_EMAIL}} the sign-in email for your I'M HERE account. Your profile, photo and connections stay the same. |
| button | Confirm new email |
| expiry | Brifte belirtilmedi; öneri/ortak yerleşim aşağıda. |
| safety | Didn't ask for this? You can ignore this email. Nothing will change. |
| action | {{ACTION_URL}} |

### 04-email-changed

Alıcı / tetik: Old email, after the change

| Alan | Metin |
|---|---|
| subject | Your I'M HERE sign-in email was changed |
| preheader | Brifte belirtilmedi; öneri/ortak yerleşim aşağıda. |
| heading | Your sign-in email was changed |
| body | The sign-in email for your I'M HERE account was changed to {{NEW_EMAIL}}. If this was you, you don't need to do anything. |
| button | This wasn't me |
| expiry | Brifte belirtilmedi; öneri/ortak yerleşim aşağıda. |
| safety | Brifte belirtilmedi; öneri/ortak yerleşim aşağıda. |
| action | {{REVERT_URL}} |

### Ortak footer

You're receiving this email because of activity on your I'M HERE account.

Help · Privacy

I'M HERE · London

Üstteki marka yazısı ve logo alt metni: `I'M HERE`. Bu e-posta brifine özeldir; telefon uygulama adı `IM HERE` değişmez.

## 2. ÖNERİ — brifte eksik olan yerleşim metinleri

Aşağıdaki dört satır, çizimlerde kullanılmış **öneridir**, onaylı metin değildir.

| Alan | Öneri |
|---|---|
| fallbackHelp | If the button doesn't work, copy and paste this link into your browser. |
| 03-confirm-new-email.preheader | Confirm the email you use to sign in. |
| 04-email-changed.preheader | Review this change to your account. |
| 04-email-changed.safety | Didn't make this change? Use the button above to undo it. |

## 3. Ortak expiry satırının kullanımı

E03/E04 brifinde ayrı expiry metni yok. Her e-postada son kullanma notu istenmesi nedeniyle E01/E02’deki `This link expires in {{EXPIRY}}.` aynen kullanıldı. E04 için süre geri-alma bağlantısına aittir; başka e-postanın süresi kopyalanmaz. Son süre ve uygun ifade HARBOR + Code tarafından netleştirilecek. Hiçbir saat/gün varsayılmadı.

## 4. Yer tutucular

| Yer tutucu | Kural |
|---|---|
| `{{ACTION_URL}}` | E01/E02/E03 ana düğmesi ve aynı düz bağlantı satırı |
| `{{REVERT_URL}}` | E04 düğmesi ve aynı düz bağlantı satırı; normal giriş/ayar URL’si değil |
| `{{EMAIL}}` | E02 hesap e-postası; çizimde yalnız alex@example.com |
| `{{NEW_EMAIL}}` | E03 yeni adres; E04 tam/maskeli kararı HARBOR’da |
| `{{EXPIRY}}` | Gerçek eylemin sözleşmesine ait yerelleştirilmiş süre, yer tutucu olarak bırakıldı |
| `{{HELP_URL}}` / `{{PRIVACY_URL}}` | Yalnız entegrasyon slotları; onaylı URL’ler Code/Founder’dan. Yeni görünür metin yok. |

Uzun içerik kontrolünde yalnız example.com altında kurmaca uzun adres ve işlem bağlantısı kullanılır. Gerçek e-posta/işlem tokenı yok. Maskeli görünüm `a***@example.com` yalnız yerleşim örneği; maskeleme kuralı tanımlamaz.

## 5. Açık kararlar

- HARBOR + Founder final copy approval, including the proposed fallback, preheaders and E04 safety line.
- HARBOR chooses full or masked NEW_EMAIL in E04; the preview supports both without deciding the production policy.
- Code supplies the actual EXPIRY per action; no duration or revert window is invented.
- Code/Founder supplies approved HELP_URL and PRIVACY_URL; these integration slots are not new product copy.
- Latest brief uses I'M HERE in email copy; phone app name IM HERE is unchanged.
