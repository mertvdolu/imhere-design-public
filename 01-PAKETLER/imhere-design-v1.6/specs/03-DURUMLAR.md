# 03 — Durum kapsamı / v1.6
Her satırın ilgili ekranları TR/EN, iOS/Android ve %100/%200 olarak vardır. SVG'ler tüm varyantları, PNG'ler TR iOS normal + EN Android büyük metin örneklerini içerir.

| Akış | Boş/dolu | İşlem sürüyor | Hata/ret | Offline |
|---|---|---|---|---|
| Davet | invite-empty / filled | invite-checking | invite-invalid | invite-offline |
| Hesap oluşturma | register-empty / filled | register-creating | register-email-invalid / password-rejected / failed | register-offline |
| E-posta doğrulama | verify-waiting; burada boş form uygulanmaz | verify-sending / checking / resend-busy | verify-not-yet / invalid-link / send-failed / resend-disabled | verify-offline |
| Mevcut giriş | login-empty / filled | login-submitting | login-invalid / failed | login-offline |
| Parola sıfırlama | reset-empty / filled | reset-sending | reset-invalid / failed | reset-offline |
| Çıkış | logout-ready; boş form uygulanmaz | logout-busy | logout-failed | logout-offline |

`reset-sent` isteğin kabul edildiğini bildirir. Çıkış başarısı ayrı yeni başarı ekranı değildir; oturum gerçekten kapandığında var olan karşılama/giriş rotasına geçilir. Çıkışta offline sunumu eylemi zorunlu olarak engellemez; mevcut yerel/sağlayıcı işleminin sonucu esas alınır. Resend pasiflik koşulları mevcut sistemden okunur, görselin durum adı backend kod adı değildir.

## Kabul edilen profil kapsamı
27 profil durumu aynen taşındı: form empty/filled/invalid/saving/save-failed/offline/edit; photo selected/preparing/denied/failed; interests empty/selected/max; gender; languages-empty; visibility default/hidden; view own-visible/own-hidden/other-visible/other-hidden/loading/failed/offline/unavailable; profile-complete.

Fotoğraf için gerçek native picker/izin sonucu esas; çizimler yeni geniş galeri izni zorunluluğu oluşturmaz. Yerel seçim listeleri için uydurma ağ yüklemesi eklenmez. Fotoğraf hatası ile profil kaydetme hatası ayrımı korunur. Gizli veya erişilemeyen public alanlar cache üzerinden görünür hâle getirilmez. Ayrıntılı profil kuralları değiştirilmeden `02-PROFIL.md` içinde korunur.

## M10 kontrol senaryoları
Yeni kayıt başarısı; mevcut doğrulamadan parola reddi; hesap oluştuktan sonra doğrulama e-postası hatası; uygulamaya dönüşte doğrulanmış/henüz doğrulanmamış sonuç; tekrar gönderim uygun/pasif; unverified mevcut kullanıcı; tamamlanmış profille giriş; nötr parola sıfırlama cevabı; çıkış başarısı/hatası/offline gerçek sonucu. Uzun e-posta, TR karakterleri, parola yöneticisi, klavye, %200 metin ve okuyucu odak sırası cihazda doğrulanır.

Bu senaryolar uygulama testi yapıldığına dair kanıt değildir; tasarımın entegrasyon kabul kapsamını tarif eder. Ekran manifestindeki fixture değerleri backend sınırı veya seed veri olarak alınmaz.
