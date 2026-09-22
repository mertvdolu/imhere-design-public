# 02 — Metin ve birleştirme
`contactAddDetails` / Ek bilgi paylaş / Share more details bu ekin tek yeni NOT LOCKED UI anahtarıdır. Yeni placeholder veya mevcut metin değişikliği yok. Giriş anahtarı gerçek submit değildir: `contactShare` seçilen ek alanları gönderir.

`l10n/v1.7.2-patch_tr.arb` ve `...en.arb` delta; yalnız bu anahtar/metadata birleştirilir. Mevcut auth alias'ları, v1.7.1 pendingSlots used/max imzası, profileAgeYears/requestCooldown ve v1.8 metinleri korunur. Tam referans ARB 457 anahtar içerir; canlı dosyaya komple kopyalanmaz. Önceki ek uygulanmamışsa kendi migration'ı ayrıca ele alınır; bu yeni label onu otomatik uygulamış sayılmaz.

`checkInRetry` yalnız ortak Tekrar dene label'ıdır; check-in işlemini çağırmaz. Salt okunur geçiş retry hedef chat verisini yükler. Yükleme yeni vote veya contact paylaşımı oluşturmaz.

Kaynak: bu konuşmadaki Founder/Manager talimatı (Master20.3 özeti) ve kabul edilmiş v1.7 continue/contact kuralları. Master'ın kendisi okunmadı. Uygulama, backend ve canlı tanıtım sitesi değiştirilmedi.
