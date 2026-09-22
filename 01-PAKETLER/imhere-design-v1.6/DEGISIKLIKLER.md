# v1.6 — Değişiklikler
## Kimlik doğrulama düzeltmesi
- v1.5'in parolasız giriş yorumu kaldırıldı. Firebase e-posta + parola ile hesap oluşturma/giriş, ardından e-posta adresi doğrulama esas alındı.
- Yeni kayıt formuna kalıcı etiketli, varsayılan gizli parola alanı ve göster/gizle eylemi eklendi. Parola kuralı veya güç göstergesi eklenmedi.
- Mevcut kullanıcı girişi ve e-posta üzerinden parola sıfırlama tasarlandı.
- Doğrulama bekleme ekranında gelen kutusundaki bağlantıya dokunma açıklaması, doğrulamayı kontrol et ve mevcut sunucu durumuna bağlı tekrar gönderim bulunur. Sayaç veya yeni bekleme süresi yoktur.
- Hesap oluşmadan alınan hata ile hesap oluştuktan sonra doğrulama e-postasının gönderilememesi ayrılır. İkinci durumda yeniden hesap oluşturulmaz; doğrulama bağlamında kalınır.
- Profil/Ayarlar altında çıkış, işlem sürüyor, hata ve offline sunumları eklendi. Çıkış için yeni internet zorunluluğu veya check-in sonlandırma vaadi eklenmedi.

## Değişmeden korunanlar
Kabul edilmiş profil görselleri, profil sözleşmesi, profil/platform spesifikasyonları, yaş/cinsiyet/meslek görünürlükleri ve v1.4 kabul eki byte düzeyinde aynı. Profil görseline çıkış satırı eklenerek kabul edilen yerleşim değiştirilmedi; çıkış için ayrı Ayarlar bölümü verildi. Tam Ayarlar tasarımı hâlâ Paket 4 kapsamındadır.

## Metin birleştirme
`emailTitle`, `emailHelp`, `emailWaitingTitle` iki dilde düzeltildi; 29 yeni auth anahtarı eklendi. 301 anahtarlı v1.5 sözlüğü 330'a çıktı. Diğer 298 mevcut anahtar değişmedi. `emailSend` hesap oluşturma butonu değildir; yalnız doğrulama e-postası göndermeye ayrılır. Yeni kayıt `authCreateAccount`, giriş `authSignIn` kullanır.

## Teslim durumu
v1.6 tasarım incelemesine hazır. Parola kuralının mevcut TR/EN açıklaması yazılımcıdan bekleniyor; Founder'ın isteğiyle alan şimdilik açıklamasız. “Davet nasıl alınır” için yeni karar eklenmedi. Uygulama ve backend koduna müdahale edilmedi.
