# 01 — E-posta + parola, doğrulama ve sıfırlama / v1.6
## Akış ve yetki
Yeni kayıt: karşılama → davet kodu → e-posta + parola ile hesap oluşturma → e-posta doğrulama bekleme → doğrulanmış oturum → kabul edilmiş profil → kullanıcının ilk check-in eylemi. Karşılama ekranındaki “Hesabım var · Giriş yap” mevcut kullanıcının giriş formunu açar; bu yolda yeni bir davet kodu isteme davranışı eklenmez.

Mevcut kullanıcı: e-posta + parola ile giriş → auth doğrulanmışlık/profil tamlığı değerlendirmesi → mevcut uygun rota. Doğrulanmamış adres bekleme ekranına gider. Profili tamamlanmış kullanıcı yeniden profil oluşturma adımına zorlanmaz. Kayıt, giriş veya doğrulama otomatik check-in başlatmaz.

Firebase kimlik doğrulaması ve mevcut backend otoritedir. Bağlantıya dokunulmuş olması, kullanıcının “kontrol et” demesi veya istemcinin yerel işareti tek başına doğrulanmışlık sağlamaz. Tasarım yeni endpoint, doğrulama token'ı veya davet tüketme/saklama kuralı tanımlamaz.

## Davet
Kalıcı etiket, tek alan ve Davetimi kullan. Mevcut doğrulama/iş kuralları kullanılır; örnek `IMHERE-7K2P` kodu yeni format şartı değildir. Boş, dolu, hata, doğrulanıyor ve offline durumları korunur. “Davet nasıl alınır” onayı bekleniyor; bekleme listesi, destek adresi, paylaşım linki veya yeni CTA eklenmez.

## Hesap oluşturma
E-posta ve parola ayrı kalıcı etiketli alanlardır. E-posta adresi biçim kontrolü mevcut auth doğrulamasına bağlanır. E-posta için platform e-posta klavyesi; parola için güvenli metin girişi, sistem parola yöneticisi ve uygun yeni-parola autofill bağlamı kullanılır. Parolaya otomatik büyük harf, spellcheck, trim, kısaltma veya tasarımdan türetilen karakter filtresi uygulanmaz.

Parola varsayılan gizlidir. Göz simgesi en az48×48 mantıksal piksel etkileşim alanıyla Parolayı göster/Parolayı gizle anlamını taşır; odağı ve girilmiş değeri kaybetmez. Ekran okuyucuya ham parola anons ettirilmez. Görseldeki sekiz nokta sadece maskeli örnektir, minimum/maksimum uzunluk kuralı değildir. Parola onayı alanı, güç ölçeri, karakter sınıfı veya sayısal sınır eklenmez.

**Parola kural açıklaması:** Mevcut doğrulamanın TR/EN metni Founder tarafından yazılımcıdan alınacak. O gelene kadar alanın altında kural metni yoktur. Mevcut doğrulama devre dışı bırakılmaz. `register-password-rejected` yalnız mevcut doğrulamanın ret sonucunu gösterir; genel `authPasswordInvalid` yeni bir kural belirtmez. Mevcut uygulamada ayrıntılı hata metni varsa kaynak metin alındıktan sonra aynı sözleşmeyle bağlanır; Firebase varsayılanları tahmin edilmez.

Hesap oluştur CTA'sı alanlar boşken ve işlem sürerken pasif; doluluk dışında ret/uygunluk mevcut doğrulamadan. İşlem sırasında tekrar gönderim yok. Hata alan altında veya genel işlem bildirimiyle gösterilir. Ağ hatası ayrı; hesap var/yok veya iç kontrol nedeni ifşa edilmez. İstek sonucu belirsizse mevcut auth/işlem durumu kontrol edilir; tasarım ikinci hesap oluşturmayı otomatik tetiklemez.

## E-posta doğrulama bekleme
Hesap oluşturma başarılı olduktan sonra doğrulama e-postası ayrı işlemdir. `verify-sending` gönderimi, `verify-waiting` gerçek gönderim kabulünü gösterir. Gelen kutusuna teslim garantisi verilmez. Gönderim başarısızsa `verify-send-failed`; kullanıcı hesap oluşturmaya döndürülmez, aynı hesabın doğrulama bağlamında kalır.

Adres ve “E-postadaki bağlantıya dokunarak adresini doğrula” açıklaması görünür. Uygulama arka plandan döndüğünde mevcut auth entegrasyonu doğrulanmış durumu yeniler. “Doğrulamayı kontrol et” aynı mevcut doğrulama kontrolünü kullanıcı eylemiyle tekrarlar; kendi kendine adresi doğrulamaz. Gerçek doğrulanmışlık sonucu sonraki uygun adıma geçilir. Henüz doğrulanmadı sonucunda `verify-not-yet`; geçersiz bağlantı sonucu gerçekten alındıysa `verify-invalid-link`. Link hatası kontrol başarısızlığının her türüne otomatik yapıştırılmaz.

“Bağlantıyı tekrar gönder” yalnız mevcut auth/backend izin veriyorsa etkin. İşlem sürerken pasif ve durum açıklamalı; uygun değilse `verify-resend-disabled` metniyle pasif. Yeni cooldown, saniye sayacı, süre tahmini veya kendiliğinden yeniden gönderim yok. Offline kontrol/gönderim başarı gibi sunulmaz. Yeniden bağlantıda görünüm gerçek duruma göre güncellenir.

Bekleme ekranında parola alanı ve giriş bağlantısı vaadi yok. “E-posta adresini değiştir” eylemi eklenmedi; hesap oluştuktan sonra sıradan alan değişikliğiyle hesabın adresini değiştiren yeni işlem varsayılmaz. E-posta alanının kayıt gönderilmeden önce düzenlenebilmesi korunur. Doğrulama e-postası kullanıcının adresini doğrular; parolasız oturum açma yöntemi değildir.

## Mevcut kullanıcı girişi
E-posta + gizli parola → Giriş yap. “Parolamı unuttum” sıfırlama isteği ekranını açar. Parola yöneticisi mevcut-parola bağlamında kullanılır. Boş, dolu, adres biçim hatası, işlem sürüyor, giriş reddi ve offline durumları vardır. Giriş hatası nötrdür; hangi alanın kullanıcı hesabıyla uyuşmadığını veya hesabın varlığını açıklamaz. Arayüz başarısızlıkta oturum açılmış görünmez.

## Parola sıfırlama
Yalnız e-posta alanı ve Sıfırlama e-postası gönder. Bu uygulama içi adım yeni parola toplamaz; mevcut sağlayıcının reset-link akışına bağlıdır. İstek kabulünde hesap var/yok ayrımı yapmayan açıklama + Girişe dön gösterilir. Bu ekran parolanın değiştiğini veya e-postanın teslim edildiğini iddia etmez. Sağlayıcının gerçek sıfırlama sonucu sonrasında kullanıcı e-posta + yeni parolasıyla mevcut giriş akışını kullanır.

Boş, dolu, geçersiz adres, gönderiliyor, istek alındı, hata ve offline durumları bulunur. Hata/offline ekranında kullanıcı kendi eylemiyle tekrar gönderebilir; otomatik retry veya zamanlayıcı yok. Tasarım yeni sıfırlama web sayfası, süre limiti veya parola politikası tanımlamaz.

## Platform, büyük metin ve erişilebilirlik
Kabul edilmiş 24 yatay dolgu, min56 alan, min52 CTA, Geist ve renk token'ları kullanılır. Alan etiketi dışarıda kalır; hint yokken boş yardımcı satır ayrılmaz. %200 metinde alan/CTA ve açıklama kartları büyür, sayfa kaydırılır. Klavye açıkken odaklanan alan/hata görünür tutulur; klavye veya sistem parola yöneticisi maket olarak çizilmez. iOS/Android sistem autofill, geri davranışı, VoiceOver/TalkBack ve Reduce Motion korunur.

Giriş öncesi tab bar yok. Doğrulama bekleme ekranındaki e-posta hesap sahibine aittir; public profile eklenmez. Parola UI loglarına, analytics'e veya gerçek ekran kanıtlarına taşınmaz. Hata/durum bir kez anlamlı biçimde anons edilir; spinner tek başına açıklama değildir. Gerçek cihaz/klavye/erişilebilirlik ve auth state testleri M10 yazılım doğrulamasıdır.
