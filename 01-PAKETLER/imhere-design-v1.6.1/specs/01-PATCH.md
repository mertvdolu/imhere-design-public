# v1.6.1 — Parola ve auth metin düzeltmesi
## Parola
Mevcut kural **en az 8 karakter**; karakter türü şartı, ek minimum/maksimum, parola onayı alanı veya güç ölçeri yok. Mevcut uygulamanın karakter sayımı/doğrulama uygulaması kullanılır; yeni bir regex, normalizasyon, trim veya sayım yöntemi icat edilmez.

`authPasswordRule` kayıt ve giriş parola alanının hemen altında, alan kenarlığından 8 aralıkla 12pt yardımcı metindir. TR “En az 8 karakter.” / EN “At least 8 characters.” Normal ve %200 görünümlerde tek satıra sığar. Bu statik yardımcı satır parola değerinin geçerli olduğunu iddia etmez; uyarı rengiyle gösterilmez. Gerçek ret mesajı ayrı satırda hata rengiyle gelir. Büyük metinde alan, hata ve sonraki CTA aşağı kayar; metin küçültülmez veya kesilmez. Alan etiketi ve göster/gizle erişilebilir adları korunur.

`authPasswordWeak` yalnız kayıt sırasında mevcut doğrulamanın minimum uzunluk reddini sunar: “Parola en az 8 karakter olmalı.” Anahtardaki Weak sözcüğü bir güç sınıflandırması veya gösterge yaratmaz. Mevcut kullanıcının yanlış parolası bu hataya yönlendirilmez; `authSignInFailed` kullanılır. Yardımcı metin eklemek mevcut kullanıcı girişindeki credential kontrolünü yeni bir yerel kurala dönüştürmez.

## Anahtarlar ve uyumluluk
Kanonik auth listesi19 addır; ayrıntı `l10n/ANAHTAR-ESLEMELERI.md`. Eski altı ad migration alias olarak tutulur. Diğer kabul edilmiş auth sunum adları için uydurma eşdeğer üretilmez: örneğin doğrulama gönderiliyor mesajı giriş hatasıyla eşitlenmez. Bu 28 UI adı `authKeyAlignment.compatibilityAliases` içinde saklanır; tam referans ARB'de mevcut ad/metinleriyle kullanılabilir. Bunlar yeni backend hata kodları veya kanonik listeye ek talepler değildir.

Ortak `emailLabel` / `emailInvalid` adları yalnız auth çağrı yerlerinde yeni adlara bağlanır. Gelecekte contact veya başka bağlamda kullanılan etiketler topluca kimlik doğrulama etiketi kabul edilmez. Eski anahtar ancak tüm çağrıları kontrol edildikten sonra kaldırılır; ARB'lerin üzerine yazılmaz.

## Hata ve sonuç metinleri
| Mevcut işlem sonucu | UI anahtarı ve kural |
|---|---|
| Girişte yanlış parola / hesap yok / eşdeğer credential reddi | Tek `authSignInFailed`; hesap varlığı ve hatalı alan ayrımı yok. Alan biçim hatası ayrıca `authEmailInvalid` olabilir; hesap sorgusu değildir. |
| Kayıtta minimum parola uzunluğu reddi | `authPasswordWeak`; yalnız 8 karakter kuralını açıklar. |
| E-posta ile işleme devam edilemiyor | `authEmailUnavailable`; “İşlem tamamlanamadı. Bilgilerini kontrol edip tekrar dene.” “Kayıtlı”, “kullanılıyor” veya “hesap zaten var” denmez. |
| Mevcut sistemin deneme sınırı sonucu | `authTooManyAttempts`; süre, eşik, kalan hak, sayaç yok. Yeniden eylem uygunluğu mevcut backend/auth katmanından. |
| Mevcut oturumun yeniden giriş gerektirmesi | `authReauthRequired`; yeni session süresi veya periyodik yeniden giriş davranışı eklenmez. |
| Reset isteği kabulü; adres kayıtlı veya kayıtsız | Her iki durumda aynı `authResetSent`: “kayıtlıysa gönderildi”. Farklı ikon, başarı ekranı veya yönlendirme ile hesap varlığı açıklanmaz. |
| Gerçek reset ağ/işlem hatası | v1.6 offline/failed görünümü korunur; istek başarısızken gönderildi denmez. Hesabın bulunamaması ağ hatası değildir. |

Yeni örnek görünümler `register-email-unavailable`, `login-too-many-attempts`, `reauth-required` mevcut sonuçların sunumunu tarif eder. Yeni hata koşulları/endpoint'ler yaratmaz. Yeniden giriş ekranındaki eylem mevcut giriş rotasına gider; mevcut oturumu tasarım kendi başına silmez. Deneme sınırı görünümünde yeniden gönderim uygun değilken Giriş yap pasif; tekrar uygun oluş backend durumuna bağlıdır. Zamanlayıcı veya yerel deneme sayacı yok.

## Kabul edilen akışlar
Davet → e-posta + parola → doğrulama e-postası → profil aynı. Tekrar gönderim backend uygunluğu; sayaç yok. Profil, üç görünürlük anahtarı, v1.4 kabul eki ve Profil/Ayarlar altındaki çıkış davranışı aynı. v1.6'daki “parola metni bekleniyor / kuralsız yardımcı alan” açıklamalarının yerine bu patch geçer; diğer kabul maddeleri değişmez.
