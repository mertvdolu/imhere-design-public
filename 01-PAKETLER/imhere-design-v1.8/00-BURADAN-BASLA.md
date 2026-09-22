# I'M HERE — v1.8 / Paket 4
Güvenlik · Ayarlar · bildirimler · Etkinlikler placeholder. Kabul edilmiş v1.7 üzerine ek tasarım teslimidir.

## İnceleme
- `ONIZLEME.html`: Dosyadan, internetsiz açılır. Ana akış / tüm durumlar / bölüm, TR/EN, iOS/Android ve normal/%200 metin filtreleri.
- `review/GENEL-BAKIS.png` ve `review/GUVENLIK-VE-SILME.png`: Temel ekranlar.
- `specs/`: Akış, davranış, erişilebilirlik ve birleştirme açıklamaları.
- `l10n/v1.8-additions_*.arb` + `migration.json`: Yalnız yeni metinler birleştirilir; canlı ARB'ler üzerine yazılmaz.
- `MANAGER-NOTU.md`: İletmeye hazır özet. `DOGRULAMA.md`: Gerçekleştirilen kontroller ve sınırları.

## Kapsam
73 durum × 2 dil × 2 platform × 2 metin ölçeği = 584 SVG. Her durum için TR iOS normal ve EN Android %200 olmak üzere 146 PNG. Bunların 4 durumu v1.6 kabul edilmiş Çıkış ekranlarının değişmeden yeniden kullanımından oluşur. Artboard uzunluğu tüm içeriği gösterir; native cihaz yüksekliği ayrıca manifesttedir.

52 yeni anahtar, iki dilde 452 referans metni. Kabul edilmiş 400 anahtar ve metadata, token JSON, Geist ve v1.4 kabul eki aynıdır. Önceki paketler değiştirilmedi. Yeni global token veya ürün kuralı yok. Tasarım çizimleri gerçek hesap işlemi başlatmaz; Flutter/backend koduna dokunulmadı.

## Açık teslim bağımlılıkları
**Ayarlar listesi Founder'ın son onayını bekliyor.** Kullanıcının açıkça izin verdiği §12 listesiyle çalışıldı: Dil · Bildirimler · Engellenenler · Gizlilik politikası / Şartlar · Hesabı sil · Çıkış. Ayarlar Profil altındadır.

**Gizlilik ve Şartlar M11 / PL-01'de hazırlanacak.** Satırlar web bağlantısı biçimindedir. URL olmadığı sürece sahte adres/belge açılmaz; kullanılamıyor görünümü kullanılır. Hukuki metin yazılmadı.

Hesap silme açıklaması son Founder/Manager yanıtındaki onaylı davranış çerçevesiyle yazıldı: gerçek, geri alınamaz silme; sayılan içerikler kullanıcının erişiminden kalkar; sınırlı kayıtlar yasal gereklilikle saklanabilir. İstek alındı, tamamlandı ve başarısız durumları ayrı. Süre ve “her şey anında silindi” vaadi yok.

Bu bağımlılıklar yeni ürün kararı olarak kapatılmadı. Tasarım dosyaları incelemeye hazır; uygulamadaki gerçek izin/işlem/erişim bağları M10'da doğrulanır.
