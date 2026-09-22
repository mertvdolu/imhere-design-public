# I'M HERE — v1.6 / Paket 2
**Kimlik doğrulama revizyonu; kabul edilmiş profil bölümü aynen korunur.**

Yeni kayıt: **Davet kodu → e-posta + parola ile hesap oluşturma → doğrulama e-postası → doğrulanmış oturum → profil.** Mevcut kullanıcı girişi, e-posta ile parola sıfırlama ve Profil/Ayarlar altında çıkış eylemi eklendi. Parolasız bağlantıyla giriş akışı geçersizdir; v1.5'in kimlik doğrulama ekranları yerine bu paket kullanılır.

Founder'ın sürümleme tercihi gereği bu teslim **v1.6**; v1.5.1 kullanılmaz. Bu dosya tasarım teslimidir, uygulama kodu değildir. Kimlik doğrulama revizyonu incelemeye sunulur; profil daha önce kabul edilmiştir.

## Önce bakılacaklar
- `ONIZLEME.html`: İnternet olmadan açılır. Dil, platform, metin ölçeği ve akış grubu seçilebilir.
- `review/GENEL-BAKIS.png`: Beş temel kimlik doğrulama görünümü.
- `specs/01-AKIS.md`: Kayıt, giriş, doğrulama ve sıfırlama davranışları.
- `specs/06-CIKIS.md`: Ayarlar içindeki çıkış bölümü ve durumları.
- `l10n/migration.json` + `v1.6-auth-diff.json`: Mevcut ARB'lere birleştirilecek değişiklikler. Canlı ARB dosyalarının üzerine yazılmaz.
- `DEGISIKLIKLER.md`, `DOGRULAMA.md`: Kapsam, korunanlar ve kontrol sınırları.

## Dosya kapsamı
66 durum × TR/EN × iOS/Android × %100/%200 = **528 bağımsız SVG**. Her durum için TR iOS normal ve EN Android büyük metin olmak üzere **132 PNG**. 39 kimlik doğrulama/davet/çıkış durumu bu revizyondadır. Kabul edilen 27 profil durumu, 216 SVG ve 54 PNG dosyası v1.5'ten byte düzeyinde aynı taşınmıştır. Tam ekran listesi `contracts/screen-manifest.json` içindedir.

Her dilde 330 metin anahtarı: 29 yeni auth anahtarı, 3 mevcut auth metni düzeltmesi. Diğer 298 mevcut metin aynıdır. Kabul edilen profil sözleşmesi, görünürlük anahtarları, token'lar, Geist fontları ve `v1.4-kabul-eki` değiştirilmedi. Token dosyasının meta sürümü kabul edilen temel v1.4 olarak kalır; teslim sürümü v1.6'dır.

## Parola metni bekleniyor
Founder, mevcut parola doğrulama metnini yazılımcıdan alıp iletecek; bu gelene kadar alanın kural açıklaması olmadan bırakılmasını istedi. Bu teslimde uzunluk/karakter şartı, güç ölçeri, güçlü-zayıf sınıflandırması veya yeni parola kuralı yoktur. Mevcut uygulama doğrulaması çalışmaya devam eder. `authPasswordInvalid` genel hata sunumudur; ayrıntılı kural metni yerine geçmez ve doğrulama mantığı oluşturmaz.

## Kaynak ve kapsam
Bu revizyonun dayanağı Founder üzerinden iletilen güncel Manager düzeltmesidir. Sözü edilen v1.0.2 özeti erişilen eklerde bulunmadı; okunmuş olarak gösterilmez. Önceki erişilebilir özet v1.0.1'dir. Yerel mühendislik örneğinde e-posta + parola ve ayrı VERIFY_EMAIL akışı salt okunur doğrulandı; `evidence/auth-source-check.json` ayrıntıyı içerir. Kaynak Master belge okunmadı.

“Davet nasıl alınır” Founder'da; yeni yönlendirme eklenmedi. Ayarlar'ın tam listesi Paket 4'tedir; burada yalnız talep edilen çıkış bölümü teslim edilir. Örnek e-posta, davet kodu, portre ve maskeli parola gerçek kullanıcı verisi veya ürün varsayılanı değildir.
