# Doğrulama — v1.4 / Paket 1
15 Eylül 2026

## Tamamlanan dosya kontrolleri
- Tüm JSON/ARB dosyaları ayrıştırıldı; TR/EN 254’er kanonik metin anahtarı, placeholder adları ve metadata eşliği kontrol edildi.
- Mevcut uygulamada v1.3’e göre eksik 83 anahtarın tamamı ekleme/alias envanterinde. Canlı ARB veya çağrılar değiştirilmedi.
- v1.3 check-in durum/uyarı/test-key/harita sunum sözleşmeleri ve iki harita SVG’si byte düzeyinde aynı.
- Yalnız izin verilen renk değişikliği inputBorder; kaldırılan üçüncü niyet renkleri dışında mevcut renkler aynı. Tipografi, boşluk, radius, nativeLayout ve motion bölümleri aynı.
- Kontrast yerel sRGB hesabıyla doğrulandı: yeni sınır dolguda 3.02:1, zeminde 3.50:1. Hesap ham değerleri evidence/contrast.json içinde.
- 34 görünümün her biri 8 varyantla mevcut: toplam272 SVG. XML ayrıştırma, tuval boyutu, metin taban çizgilerinin tuval içinde kalması, açık placeholder kalmaması ve eylem test-key tekilliği kontrol edildi.
- 68 PNG üretildi ve dosyalar yeniden açılarak doğrulandı. Pasif/aktif/izin/PARTIAL genel görünümü, büyük metin PARTIAL ve yenileme hatası görsel olarak incelendi; ilk kontrolde portre raster uyumu, uzun navigasyon etiketleri ve kart yerleşimi düzeltilip yeniden üretildi.
- ONIZLEME.html yerel dosya olarak Chrome’da açıldı: başlangıçta34 görünüm, EN/Android/%200/Harita filtresinde8 görünüm; SVG yüklemesi doğrulandı. Sunucu veya internet gerektirmiyor.
- Ayrıntılı statik kontrol sonuçları evidence/validation.json içinde. Otomatik dosya kontrolü, uygulama davranışı/erişilebilirlik doğrulaması değildir.

## Henüz yapılmayanlar / entegrasyon sınırı
Flutter kodu uygulanmadı; analyze/build/widget/backend testleri çalıştırılmadı. VoiceOver, TalkBack, gerçek iOS/Android, 320px ve maksimum sistem metin ölçeği, harita SDK’sı/jestleri/attribution, gerçek izin akışları ve cihaz performansı sınanmadı. %200 çizimler görsel tasarım varyantıdır, cihaz testi kanıtı değildir.

Şematik harita gerçek H3/SDK stil doğrulaması sağlamaz. Sağlayıcı seçimi/final stil M05 adım7'de. Kişi görselleri/bio/adlar tasarım fixture’ıdır. Örnek kalan süre 14:06 → 14:30 =24 dakika; harita snapshot örneği14:05, saatler gerçek oturum değildir.

## İnceleme sırasında sonraki paketlere taşınanlar
- Meslek varsayılan görünür; profil düzenlemede gizlenebilir (iletilen Founder kararı). Paket2’de uygulanır.
- Ayarlar listesi onayı paket4 öncesinde; saklama süresi M11’de, UI süre göstermez.
- End Connection: özette “onay istemez”, eski sözlükte endConfirm var. Bunun kendi onayı mı karşı tarafın onayı mı olduğu paket4’te Manager üzerinden netleşmeli. Bu pakette bu akış çizilmedi ve yeni karar alınmadı.

## Kabul sonrası düzeltme
End Connection açık noktası kapanmıştır: karşı tarafın onayı aranmaz; kullanıcının kendi onay diyaloğu ve endConfirm korunur. Önceki açık nokta kaydı tarihsel olarak okunmalıdır.
