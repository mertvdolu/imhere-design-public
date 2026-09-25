TASARIMCIDAN MANAGERE MESAJ

# Bildirim metinleri v2 — 2026-09-25

| Anahtar | EN | TR |
|---|---|---|
|notificationRequestAccepted|Your request was accepted.|İsteğin kabul edildi.|
|notificationContactShared|Contact details were shared with you.|Seninle iletişim bilgileri paylaşıldı.|
|notificationIntro|Get notified about requests and messages.|İsteklerden ve mesajlardan haberdar ol.|

Başlık, kişi adı, mesaj içeriği yok. CH-133 ön plan kuralı değişmez; bu metin teslimi yeni gösterim, ses veya yönlendirme kararı üretmez.

Yeni katalog durumları: push-request-accepted / push-contact-shared; notifications-intro güncellendi. Her biri TR/EN, iOS/Android, %100/%200. İçerik örnekleri native bildirim kabuğu değildir; uygulama kimliğini OS belirler, payload title yok.

notification-v2-patch_en.arb / _tr.arb: üç anahtar + metadata birleştirilir. notificationIntro için requests-only eki artık geçersizdir. Tam ARB üzerine yazılmaz. Anahtarlar Code mevcut listesiyle eşleşir.

Katalog299 durum, beta292 / ertelenen7. Uygulama kodu değişmedi. Yerel commit; aktarım Code.
