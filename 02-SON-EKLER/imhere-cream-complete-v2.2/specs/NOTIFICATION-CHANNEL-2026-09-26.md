TASARIMCIDAN MANAGERE MESAJ

# Sesli bildirim kanalı — 2026-09-26

| Anahtar | EN | TR |
|---|---|---|
| notificationChannelMessagesConnections | Messages and connections | Mesajlar ve bağlantılar |
| notificationChannelMessagesConnectionsDescription | When someone accepts your request, messages you, or shares their contact details. | Birisi isteğini kabul ettiğinde, sana mesaj gönderdiğinde veya iletişim bilgilerini seninle paylaştığında. |

Kapsam yalnız: istek kabul edildi / yeni mesaj / iletişim paylaşıldı. Telefonun varsayılan sesi ve titreşimi; kullanıcının sistem/kanal tercihleri geçerlidir. Her teslimde mutlaka ses/titreşim olacağı vaat edilmez. Özel ses veya titreşim deseni tasarlanmadı.

**Mevcut sessiz kanal adı değişmiyor:** notificationChannelUpdates — Updates / Güncellemeler. Düşük öncelikli türler sessiz kalır. Diğer türlere yeni ses kararı genişletilmez. Check-in reminders kanal adı da değiştirilmedi.

Android kanal kimliğini Code belirler; bu metinler ayrı kanalın kullanıcıya görünen adı/açıklamasıdır. Adsız/başlıksız bildirim gövdeleri ve CH-133 ön plan gösterim kuralı korunur.

Delta: l10n/notification-channel-patch_en.arb ve _tr.arb. Yalnız iki yeni anahtar + metadata birleştirilir; tam ARB üzerine yazılmaz.

Katalog: push-request-accepted / push-message / push-contact-shared (24 dil/platform/ölçek kaydı). Sistem Ayarları görünümü platforma aittir; yeni uygulama ekranı veya çizim eklenmedi. Toplam299 durum değişmedi.

Yerel commit; aktarım Code. Uygulama koduna dokunulmadı.
