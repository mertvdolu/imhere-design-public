KİME: MANAGER
KONU: IM HERE — bütün uygulama tasarımının Cream & Ink temasına geçişi / v2.2

Founder tüm ekranlar için krem/siyah temayı onayladı. Eski yeşil görsel yönün yerini alan tam tasarım kataloğu teslim edildi.

DEPO: https://github.com/mertvdolu/imhere-design-public
PAKET: 02-SON-EKLER/imhere-cream-complete-v2.2/
GİRİŞ: ONIZLEME.html (depo kökü güncel kataloğa yönlendirir)
SPESİFİKASYON: 02-SON-EKLER/imhere-cream-complete-v2.2/specs/TASARIM-DEVRI.md
TOKEN: 03-GUNCEL-ORTAK/tokens/theme.tokens.json (v2.2)

KAPSAM: Eski güncel katalogdaki 287 durumun tamamı + son ekler = 295 durum / 2360 SVG; TR/EN, iOS/Android, %100/%200. PNG referansları ayrıca var. Boş/yükleme/hata/offline akışları korunur. Harita tam ekran; dört semantik band korunur. Gönderilen iki daireli logo, açık simge/splash ve tek renk bildirim maskesi teslim edildi.

SON EKLER: Mesaj saklama bilgileri, nearbyLimited, sunucu gizliliği açıklaması, photoUploaded, onboarding çıkışı, yedi aktif Ayarlar satırı ve destek kopyalama hali çizimlere işlendi. Cooldown/pending/connected, ek contact paylaşımı, güncelleme başarısı/boş durum, nötr kapalı kart ve salt okunur geçiş de yeni temada.

YENİ METİN: Yalnız supportCopyEmail / supportEmailCopied (TR/EN). l10n/cream-v2.2-patch_*.arb + migration.json ile birleştirin; tam ARB'yi canlı dosyanın üstüne yazmayın. Önceki M09/M10 metinleri tam referansta korunur.

ÜRÜN DAVRANIŞI DEĞİŞMEDİ. EN aktif, TR uyuyor, Dil satırı askıda. Flutter/backend/mağaza derlemesi değiştirilmedi. Paket tasarım teslimidir; native entegrasyon ve fiziksel cihaz turu ayrı doğrulama adımıdır. Eski yeşil paketler yalnız arşivdir.

DOĞRULAMA: evidence/validation.json, review/ ve MANIFEST.json. Dosyalar ZIP yerine tek tek depoya işlendi; CHANGELOG'da sürüm kaydı var.
