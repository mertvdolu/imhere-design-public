TASARIMCIDAN MANAGERE MESAJ

# Sürüm8 — üç önceliğin birleşik metin teslimi v1.0

28 Eyl2026. Code app/lib/l10n/app_en.arb ve app_tr.arb, email_change_screen.dart, networking_orani.dart ve test/l10n_parity_test.dart içindeki9 kPendingDesigner anahtarı incelendi. Uygulama deposu değiştirilmedi.

## Birleştirme

**Tek birleşik çift:** l10n/release8-approved-patch_en.arb ve _tr.arb. Önceki compact-signals-v1 deltasının yerine bu çift kullanılabilir.18 anahtar + metadata:9 bekleyen anahtar,6 aynen kullanılan ortak anahtar,2 kaydırıcı yardım/erişilebilirlik anahtarı,1 işlem metni. Tam ARB üzerine yazılmaz. Eski delta uygulandıysa değerler ve metadata bu teslimle birleştirilir; eski anahtarlar zorla silinmez.

İsim hizalaması: profileIntentBalance → profileNetworkingMix; profileIntentBalanceTitle → profileNetworkingMixTitle. networking/friends int yer tutucuları korunur. emailChangeSent email:String yer tutucusu korunur. alias kaydı migration’da; aynı metnin iki yeni kullanımını üretmeyin. Uygulamadaki dokuz bekleyen metin bu teslimle onaylıdır; bekleme listesini Code günceller.

## 1. Okunmamış nokta — ONAY

messagesUnread: Unread messages / Okunmamış mesaj.
colors.notificationUnread: #B63A32; harita densityRed kullanılmaz.8 dp satırın sağında; Messages ikonunun sağ üstünde8 dp +2 dp zemin halkası. Ayrı eylem veya sayı değil; animasyon yok. Ekran okuyucu satır/sekme adına etiketi bir kez ekler, nokta ayrı düğüm değildir. Önceki d73c299 kompakt görünüş aynen geçerli. Renk deltası theme.delta.json; ARB renk taşımaz.

## 2. Networking / Friends — ONAY

profileNetworkingMix ve profileNetworkingMixTitle Code adlarıyla kullanılır. Kendi ve başkasının profili: çerçevesiz14/400 oran satırı; ayarlanmamışsa yok. Form: başlık18/500, altında oran14/400, sonra tek kaydırıcı. Ray2 dp/tutamak16 dp; etkileşim alanı en az48 dp.0–100,10’ar adım; Friends=100−Networking. Ayrı büyük kart/düğme yok.

Code’daki mevcut oran satırı kaydırıcının altında; onaylı tasarımda üstüne alınır. Not set / Ayarlanmadı için profileIntentBalanceNotSet; erişilebilir ad için profileIntentBalanceAdjust. Ekran okuyucu değeri iki oranı da söyler. Dokunulmamış null değer kaydedilmiş50/50 gibi gösterilmez/gönderilmez. Son kaydetme davranışı değişmez. Tam spec: compact-signals-v1.0/SPEC.md.

## 3. E-posta değiştirme — ONAYLI metinler

### EN

- `settingsChangeEmail`: Change email address
- `emailChangeNewLabel`: New email address
- `emailChangeSubmit`: Send verification link
- `emailChangeReauth`: To change your email address, first sign in again with your current password.
- `emailChangeSent`: If this address can be used, you’ll receive a verification link at {email}. Open it to change your email address, then sign in again with your new address.
- `emailChangeFailed`: This couldn’t be completed. Please try again.
- `emailChangeSending`: Sending verification link…
- `authEmailInvalid`: Check your email address.
- `authTooManyAttempts`: We can’t complete this action right now. Please try again later.
- `offline`: You’re offline.
- `authPassword`: Password
- `authReauthRequired`: Sign in again to continue.
- `cancel`: Cancel

### TR

- `settingsChangeEmail`: E-posta adresini değiştir
- `emailChangeNewLabel`: Yeni e-posta adresi
- `emailChangeSubmit`: Doğrulama bağlantısı gönder
- `emailChangeReauth`: E-posta adresini değiştirmek için önce mevcut parolanla yeniden giriş yap.
- `emailChangeSent`: Bu adres kullanılabiliyorsa {email} adresine bir doğrulama bağlantısı gelecek. E-posta adresini değiştirmek için bağlantıyı aç, ardından yeni adresinle yeniden giriş yap.
- `emailChangeFailed`: İşlem tamamlanamadı. Tekrar dene.
- `emailChangeSending`: Doğrulama bağlantısı gönderiliyor…
- `authEmailInvalid`: E-posta adresini kontrol et.
- `authTooManyAttempts`: Şu anda işlemi tamamlayamıyoruz. Daha sonra tekrar dene.
- `offline`: İnternet bağlantısı yok.
- `authPassword`: Parola
- `authReauthRequired`: Devam etmek için yeniden giriş yap.
- `cancel`: Vazgeç

## Durum eşlemesi

- Form: settingsChangeEmail başlık, emailChangeNewLabel alan, emailChangeSubmit eylem.
- Boş/mevcut adres: mevcut pasif eylem davranışı; yeni ürün doğrulaması yok.
- Geçersiz biçim: authEmailInvalid.
- İşlem sürüyor: mevcut pasif eylem/işlem durumu; ayrı görünür durum metni gerekiyorsa emailChangeSending. Bu metin eklenmesi başarı göstermez, ikinci istek açmaz.
- Yakın giriş gerekli: emailChangeReauth + authPassword. Mevcut ekranın parola ile yeniden doğrulaması korunur; kullanıcıyı zorla çıkışa veya başka akışa yönlendirmeyin. authReauthRequired genel sistem mesajı olarak aynen teslim edildi.
- Nötr sonuç: emailChangeSent. Code AuthOutcome.ok ve emailUnavailable için aynı ekranı kullandığı için “We sent” kesinliği kaldırıldı. Adresin başka hesapta olduğunu açıklamaz, e-postanın ulaştığını veya adresin şimdiden değiştiğini iddia etmez.
- Genel hata/yeniden doğrulama hatası: emailChangeFailed; yanlış parola/hesap yok ayrımı yok. Offline: offline. Sınırlama: authTooManyAttempts; süre/eşik verilmez.
- cancel mevcut ortak metin; bu delta yeni Cancel düğmesi zorunluluğu getirmez.

Yerleşim mevcut form bileşenleri; uzun e-posta/metin sarılır, büyük yazıda kaydırılır, ellipsis yok. Tek ana eylem; büyük yeni kart yok. Firebase e-posta şablonları/konsol bu teslimde değişmez.

Bu tasarım/metin onayıdır; Play yayın veya native test onayı değildir. Code:9 bekleyen anahtarı eşleştir, l10n üretimi/placeholder parity, geçersiz/offline/limit/reauth/nötr sonuç testlerini doğrula; görünüş bekleme listesini renk ve kompakt spec uygulanınca kapat.
