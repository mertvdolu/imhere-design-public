# 06 — v1.7 birleştirme ve sözleşme sınırı
- Kabul edilen v1.6.1'in 334 anahtarı ve metadata'sı aynen korunur; 66 yeni UI anahtarı eklenir. İki dil 400 anahtara çıkar. `v1.7-additions_*.arb` deltadır; `app_*.arb` tam referanstır. Canlı ARB'lerin üzerine yazılmaz; app-only anahtarlar silinmez.
- Önceki 19 kanonik auth anahtarı, alias eşlemeleri, 8 karakter parola kuralı ve genel auth sonuç metinleri değişmez. Migration içindeki eski temizleme kuralları/endConfirm/meslek görünürlüğü kabulü geçerlidir.
- Token JSON, fontlar, lisanslar ve v1.4 kabul eki aynı dosyalardır. Token meta sürümü kabul edilmiş temel v1.4; teslim sürümü v1.7. Yeni global renk veya font yok. Profil ve auth çizimleri yeniden üretilmedi.
- `pendingRemaining` metni değiştirilmeden sözlükte korunur; Paket 3 kalan süre etiketinde `requestTimeLeft` kullanır. Mevcut String time parametresi korunur.
- Yeni `chatCharacters.used` gerçek grapheme sayımıyla bağlanır. `pendingSlots.used` giden bekleyen sayısı; `requestTimeLeft.time` kalan istek süresi; `chatRemaining.remaining` yalnız kullanıcının kendi kalan hakkı. Birinin parametresini diğerine taşımayın.
- `requestAccept` seçim ekranı girişi, `requestSelectAccept` gerçek kabul onayıdır. Niyet ekrandaki lokalize label'dan backend enum'a çevrilmez; mevcut sabit option kimlikleri kullanılır. İlk girişte [] başlangıç; kayıtlı profil tercihi olarak otomatik doldurulmaz.
- `checkInRetry` bu pakette yalnız kabul edilmiş “Tekrar dene” metni için tekrar kullanılır. Butonun işlemi ekranın kendi isteğidir; mevcut check-in handler veya test Key'inin kopyası değildir. Lokalizasyon anahtarı, widget Key ve backend hata/işlem adı ayrı kavramlardır.
- Gösterilen işlem aşamaları mevcut controller/auth/backend sonuçlarına bağlanır. Sözleşmelerdeki state adları UI açıklamasıdır; yeni API, endpoint, veritabanı şeması, transaction veya hata kodu icat edilmedi. Idempotency/çatışma çözümü mevcut mühendislik katmanına aittir; sahte yerel başarıyla atlanmaz.
- Mevcut mesaj immutable; contact edit/withdraw farklı kayıttır. Contact taslağı otomatik yayınlanmaz, hesap adresi kopyalanmaz. Paylaşım görünürlüğü kaldırma sunucuda ve Semantics'te bağlanır; salt widget opacity yeterli değildir.
- Engelleme/erişim kaldırma tüm yüzeylerden üstündür. Önceden render/cache edilmiş kişi, mesaj veya contact verisi artık erişim yokken gösterilmez. Kapalı ama erişilebilir sohbetin salt-okunur olması bu kurala istisna değildir.

## Öncelik ve kaynak
Founder'ın güncel iki-niyet ve paket talimatları + Tasarım Gereksinim Özeti v1.0.2 §7–8. Eski envanterin üçüncü niyetli L-40 maddesi geçersiz; L-41..65 davranışları bu düzeltmeyle kullanıldı. End Connection'da “onay istemez” karşı tarafın onayıdır; kullanıcının kendi onay diyaloğu önceki kabul gereği kalır. Kapalı sohbet süresi açık nokta, süre UI'a yazılmaz.

Paket 4 için tam güvenlik/ayar/bildirim/Etkinlikler tasarımı ayrı gelir. Bu paket mevcut güvenlik davranışını ortadan kaldırmaz; erişimsizlik görünümünü verir. Önceki giriş/profil/harita paketleri aynı kalır. Yazılımcıyla doğrudan iletişim kurulmadı; bu belgeler Founder/Manager üzerinden aktarılır.
