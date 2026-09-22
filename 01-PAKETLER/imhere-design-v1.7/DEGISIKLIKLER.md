# v1.7 — Paket 3 değişiklikleri
Yeni: Mesajlar'ın Bağlantılar/İstekler görünümü; iki niyetle gönderme ve bağımsız alıcı kabulü; bekleyen 19/20 ve süre; ters istek/sonuç ekranları; eşleşme ve iki setin sunumu; metin/emoji/link sohbeti; yumuşak iletişim uyarısı; özel devam kararı; karşılıklı EVET sonrası salt okunur/contact; contact paylaşma, düzenleme, görünürlüğü kaldırma.

93 durumun tümü TR/EN, iOS/Android, normal ve büyük metin varyantlarıyla. Yükleme, boş, kesin hata, offline ve gizlilik nedeniyle kullanılamıyor ayrı. Belirsiz mesaj gönderimi kesin başarısızlıktan ayrılır; körlemesine yeni mesaj gönderme yoluna çevrilmez.

66 yeni metin; 334 kabul edilmiş metin aynı. Yeni token veya iş kuralı yok. v1.6.1 auth/parola düzeltmesi, profil görünürlükleri, tab sırası ve v1.4 kabul eki korunur. Yeni dosyalar tasarım çıktılarıdır; uygulamaya kod eklenmedi.

İlk tasarım incelemesinde “görülmüş bilgi geri alınamaz” açıklaması paylaşım/düzenlemede ayrı `contactSeenNote` olarak ayrıldı. `contactHideNote` yalnız kaldırma bağlamında kullanılır; henüz görünür bilgiyi kaldırılmış gibi sunmaz. Bu sunum açıklığı iş kuralı değişikliği değildir.
