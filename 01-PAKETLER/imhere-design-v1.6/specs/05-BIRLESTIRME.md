# 05 — Birleştirme / v1.6
1. `migration.json` kurallarıyla anlam bazında birleştir; canlı ARB dosyalarının üzerine yazma. Uygulamaya özel, tasarım sözlüğünde olmayan anahtarları silme. Mevcut generated localization API ve parametreleri koru.
2. v1.5 temelinde yalnız `emailTitle`, `emailHelp`, `emailWaitingTitle` TR/EN değerlerini düzelt; `v1.6-auth-diff.json` içindeki29 yeni auth anahtarını ekle. Tasarım sözlüğü her dilde330 anahtar. İlk defa v1.4'ten geçiliyorsa kabul edilmiş v1.5 profil ekleri de tam sözlükten anlam bazında alınır.
3. Hesap oluştur CTA'sı `authCreateAccount`; giriş `authSignIn`; parola sıfırlama isteği `authResetSend`. Eski `emailSend` yalnız doğrulama e-postası gönderimidir. `emailTitle` yalnız kayıt başlığıdır. Eski e-posta-only ekranlarını ve passwordless giriş bağlantısı çağrılarını bu revizyonun rotalarıyla değiştir.
4. `emailChange` anahtarının sözlükte korunması yeni hesap-adresi değiştirme eylemi değildir. Bekleme ekranında bu eylem çizilmedi. `emailSent` yalnız gerçek doğrulama e-postası gönderimi kabul edildiğinde kullanılır.
5. Profil metinlerini/görsellerini/sözleşmesini, görünürlük varsayılanlarını ve kayıtlı false tercihlerini değiştirme. `accepted-profile-manifest.json` SHA-256 listesi bu korumayı denetler. Token ve fontlar aynı; token meta1.4 teslim sürümüyle karıştırılmaz.
6. Eski navMap/alias/çift anahtar temizliği, endConfirm yorumu ve meslek görünürlüğü kabul eki aynen taşınır. `v1.4-kabul-eki` birleştirme kuralı geçerlidir. Yeni harita sekmesi veya Flört eklenmez.
7. Parola kural açıklaması Founder'dan bekleniyor. Şimdilik yeni limit/regex/karakter şartı/güç ölçeri ekleme; mevcut doğrulama kodunu koru. Genel hata anahtarı bir validator tanımı değildir. Kaynak metin geldiğinde TR/EN aynı kapsamda bağlanır.
8. Auth UI'ını mevcut Firebase/auth state katmanına bağla; tasarım dosyaları çalışan auth kodu içermez. Profil iş kurallarını veya davet yaşam döngüsünü UI'dan yeniden üretme. Çıkışta mevcut session sonucu ve korunan rota yönetimi kullanılır.

## Öncelik ve korunmuş belgeler
Auth için bu v1.6 `01-AKIS.md` ve `contracts/onboarding.json` geçerlidir. Kabul edilen `02-PROFIL.md`, `04-PLATFORM.md` dosyaları byte düzeyinde v1.5 ile aynıdır; 04'teki e-posta bağlantısıyla uygulamaya dönüş cümlesi adres doğrulama dönüşünü ifade eder. Parolasız giriş olarak yorumlanmaz.

R3 davet edinme yönlendirmesi Founder'dadır. Tam Ayarlar listesi Paket4; yalnız çıkış bölümü bu pakette. Profildeki konuşulan diller örnek satırları mevcut ürün kataloğunu sınırlandırmaz. Native uygulama/cihaz kontrolleri yazılım aşamasındadır; yazılımcıya doğrudan mesaj gönderilmedi.
