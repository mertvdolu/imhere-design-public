# v1.6.1 — Yazılımcının anahtar listesi
## Kanonik 19 anahtar
| Anahtar | TR | EN |
|---|---|---|
| authEmail | E-posta adresi | Email address |
| authPassword | Parola | Password |
| authPasswordRule | En az 8 karakter. | At least 8 characters. |
| authPasswordShow | Parolayı göster | Show password |
| authPasswordHide | Parolayı gizle | Hide password |
| authSignIn | Giriş yap | Sign in |
| authCreateAccount | Hesap oluştur | Create account |
| authForgotPassword | Parolamı unuttum | Forgot password |
| authSignInFailed | Giriş yapılamadı. Bilgilerini kontrol edip tekrar dene. | Couldn’t sign in. Check your details and try again. |
| authEmailInvalid | E-posta adresini kontrol et. | Check your email address. |
| authPasswordWeak | Parola en az 8 karakter olmalı. | Password must be at least 8 characters. |
| authEmailUnavailable | İşlem tamamlanamadı. Bilgilerini kontrol edip tekrar dene. | The action couldn’t be completed. Check your details and try again. |
| authTooManyAttempts | Şu anda işlemi tamamlayamıyoruz. Daha sonra tekrar dene. | We can’t complete this action right now. Please try again later. |
| authReauthRequired | Devam etmek için yeniden giriş yap. | Sign in again to continue. |
| authResetTitle | Parolanı sıfırla | Reset your password |
| authResetBody | Hesabınla kullandığın e-posta adresini gir. | Enter the email address you use for your account. |
| authResetSend | Sıfırlama e-postası gönder | Send reset email |
| authResetSent | Bu e-posta adresi kayıtlıysa parola sıfırlama bağlantısı gönderildi. | If this email address is registered, a password reset link has been sent. |
| authResetBackToSignIn | Girişe dön | Back to sign in |

## Eski ad → yeni ad
| v1.6 adı / alias | Kanonik ad |
|---|---|
| emailLabel | authEmail |
| emailInvalid | authEmailInvalid |
| authShowPassword | authPasswordShow |
| authHidePassword | authPasswordHide |
| authPasswordInvalid | authPasswordWeak |
| authBackToSignIn | authResetBackToSignIn |

`authPasswordInvalid` eşlemesi yalnız kayıt minimum-uzunluk reddi için. Girişte yanlış parola veya hesap yok sonucu daima `authSignInFailed`. Ortak e-posta anahtarları yalnız auth çağrı yerlerinde taşınır. Localization anahtarı backend hata kodu veya widget test anahtarı değildir.

## Listede karşılığı olmayan kabul edilmiş UI adları
`emailSend`, `emailSent`, `emailPrivate`, `emailResend`, `emailTitle`, `emailHelp`, `emailSending`, `emailWaitingTitle`, `emailWaitingHelp`, `emailChange`, `emailVerifying`, `emailVerifyFailed`, `authCreating`, `authCreateFailed`, `authSignInTitle`, `authSignInBody`, `authExistingAccount`, `authSigningIn`, `authResetSending`, `authResetFailed`, `authVerifyCheck`, `authVerifyRequired`, `authVerifyNotYet`, `authVerifySendFailed`, `authVerifyResendUnavailable`, `authSignOut`, `authSigningOut`, `authSignOutFailed`

Bu 28 ad migration'da `compatibilityAliases` altında kaldı. `canonicalTarget: null`, yazılımcının listesinde birebir anlam karşılığı bulunmadığını belirtir; bir anahtarı kendisine yönlendiren döngü değildir. `retainKey` ve `retainCopy` mevcut sunum metnini korur. Değerleri 334 anahtarlı tam referans ARB'lerde mevcut adlarıyla bulunur. Yeni bir kanonik isim icat edilmez veya mesaj yanlış hata türüne zorla eşlenmez. Yeni doğrulama davranışı eklenmez.

## Dosya kullanımı
`auth_tr.arb` / `auth_en.arb` yalnız 19 kanonik metin içerir. `app_tr.arb` / `app_en.arb` tam referanstır; canlı dosyanın üzerine yazılmaz. Altı alias çağrı yerleriyle birlikte taşınır; iki dil birlikte birleştirilir. Mevcut app-only anahtarlar, profil metinleri ve parametrik API'ler korunur.
