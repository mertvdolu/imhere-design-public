TASARIMCIDAN MANAGERE MESAJ

# T1 geri alma ve bildirim izin metni — 2026-09-25

## Aktif oturum — FD-47 / FD-40

Founder kararıyla450f842 T1 geri alındı. Aktif oturumda mevcut durum/süre bilgisi, `checkInRenew` (I’m still here / mevcut TR karşılığı) ve Stop birlikte korunur. Yenilemenin tek yolu kullanıcının bu düğmeye dokunmasıdır; otomatik uzatma yok. T1'in etkilediği8 durumun64 SVG /16 PNG'si T1 öncesi18d189c çizimine döndürüldü. Diğer T2–T4 ve H teslimleri korunur.

Durumlar: checkin-04-active; nearby-empty/failed/loading/offline; notice-renewalFailed/stopPending/stopSuperseded.

## Bildirim izin ekranı

Mevcut anahtar: notificationIntro

EN: Get notified about requests.
TR: İsteklerden haberdar ol.

İlk sürüm yalnız istek bildirimi gönderir; bu metin mesaj bildirimi vaat etmez. Mesaj bildirimleri gerçekten yayınlandığında önceki istek+mesaj metni geri getirilebilir. Bildirim gönderim davranışı veya kanal ayarları bu teslimde değiştirilmez.

Metin delta: l10n/notification-requests-only-patch_en.arb ve _tr.arb. Yalnız notificationIntro + metadata birleştirilir; tam ARB üzerine yazılmaz.

Yerel commit; aktarım Code. Native uygulama değiştirilmedi.
