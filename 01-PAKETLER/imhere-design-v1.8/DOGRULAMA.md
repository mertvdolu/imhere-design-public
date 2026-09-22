# v1.8 doğrulama

## Yapılan kontroller
- 7475 statik dosya/içerik/geometri kontrolü geçti. 73 durum × 8 = 584 benzersiz SVG; 146 PNG açılabilirliği doğrulandı.
- TR/EN 452 anahtar eşit; 52 ek metin delta dosyalarıyla aynı. Baseline 400 metin ve metadata değişmedi; placeholder'lar iki dilde eşleşiyor.
- Token/font/kabul eki ve önceki davranış sözleşmeleri aynı. Kabul edilmiş v1.6, v1.6.1 ve v1.7 paketleri kendi SHA-256 manifestlerine göre değişmedi. Çıkış SVG'leri v1.6 ile byte-identical.
- SVG metinlerinin tuval sınırları ve çözülmemiş alanlar kontrol edildi. Normal TR iOS ve %200 EN Android genel bakışları görsel olarak incelendi; uzun İngilizce başlıklarda harf kopması giderildi.
- Şikâyet başlangıcı boş, 5 kategori ve pasif gönderim; gerçek rapor sonrası ayrı isteğe bağlı engelleme; rapor başarılı/engel hatası ayrımı kontrol edildi.
- Kendi end onayı, unblock sonrası eski sohbetin açılmaması, nötr erişimsizlik ve özel içeriğin kaldırılması kontrol edildi.
- Silme onayındaki onaylı kapsam; istek alındı/tamamlandı ayrımı; belirsiz işlemde kör yeniden gönderim olmaması; reauth'ın kendi başına silmemesi kontrol edildi.
- İzin reddinde uygulamaya devam eylemi ve çevrimdışı cihaz ayarları erişimi var. Etkinlikler yalnız placeholder; çevrimdışı görünümü aynı yerel içerik.
- Dosyadan açılan önizlemede 13 ana akış kartı, 73 durum ve 8 grup kontrol edildi; EN Android %200 görselleri çözüldü. Dış ağ isteği veya sayfa hatası yok. Ayrıntı `evidence/preview-check.json`.

## Sınırlar
Bu kontroller tasarım dosyaları içindir. Flutter, gerçek iOS/Android izin diyaloğu, VoiceOver/TalkBack, Firebase, engelleme veya hesap silme işlemleri çalıştırılmadı. Native akış/erişim/işlem bağları ve 2×2 navigasyon M10 yazılım doğrulamasıdır.

Ayarlar listesi nihai Founder onayı bekler. Gizlilik/Şartlar metin ve web adresleri M11 / PL-01'de hazırlanacak; bu pakette yer tutucu ve açma durumları var, hukuki metin yok. Silme çerçevesi son kullanıcı yanıtıyla onaylandı; süre ve tüm kopyalar anında silindi vaadi yok.
