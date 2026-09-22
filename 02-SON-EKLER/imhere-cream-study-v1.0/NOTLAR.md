# IM HERE — Cream study v1.0

Durum: Founder tarafından ana tema yönü olarak seçildi. Forest & Mint görsel yönünün yerini alır; bu HTML bir görsel demo olarak kalır. Ürün veya uygulama kodu değiştirilmedi.

## İnceleme
ONIZLEME.html dosyasını tarayıcıda aç. Üstten Krem/Beyaz seçilebilir; altı ekran filtrelenebilir. Yakındakiler kartından örnek kişi ve boş niyet seçici açılır; Bağlantılar listesinden sohbet görünümüne geçilir. Tüm işlemler yerel görsel demodur. E-posta, mesaj, istek veya profil değişikliği gönderilmez. Harita dışındaki ekranlar internet olmadan çalışır; harita için OpenFreeMap tile/glyph erişimi gerekir. Ekran içleri kaydırılabilir.

## Görsel yaklaşım
- Krem #F4F1E9, kart #FCFAF5, mürekkep #191A17.
- Geist: düzenli metin, medium başlık; sıkı başlık aralığı, geniş beyaz boşluk.
- İnce çizgili ikonlar; siyah ana eylemler; sade ayırıcılar.
- Portrelerde yalnız CSS siyah-beyaz önizleme filtresi. Kaynak fotoğraflar değişmedi; bu bir görsel teklif, kullanıcının fotoğrafına kalıcı müdahale değil.
- v1.1: Kullanıcının gönderdiği iki daireli logo HTML inceleme başlığında ve örnek uygulama üst alanlarında kullanılır. Normal ve küçük boyut ağırlığı orijinal SVG dosyalarıyla, Ink rengi ve koruma alanı korunarak yerleştirildi. İç kullanım kılavuzu PDF’si yayımlanmadı. Telefon uygulama adı IM HERE kararı değişmez. Bu güncelleme native simge/splash entegrasyonu değildir.

## Altı görünüm
1. Yakındakiler: aktif check-in örneği, kişi kartları ve nearbyLimited.
2. Tam ekran harita: krem alt harita; mavi/sarı/yeşil/kırmızı anlam katmanı korunur. Örnek poligonlar yalnız tasarım fixture'ıdır; gerçek kişiler/yoğunluk değildir. Konum izni yok; kişisel marker, sayı, mesafe yok. OpenStreetMap/OpenFreeMap/OpenMapTiles attribution görünür.
3. Bağlantılar: nötr kapalı kart durumu; istekler boş durum önizlemesi.
4. Sohbet: iki örnek giden mesaj nedeniyle 18/20, 500 grapheme taslak sınırı, saklama açıklaması. Gönder'e basmak mesaj göndermez ve başarı göstermez.
5. Profil: tek fotoğraf, yaş/meslek örneği, kısa bio ve ilgi alanları. Fotoğraf yüklendi metni var; düzenleme yalnız açıklamalı demo.
6. Ayarlar: mevcut İngilizce modda yedi satır; Dil gizli. Bildirimler, Engellenenler, Gizlilik, Şartlar, Bize yaz, Hesabımı sil, Çıkış yap.

Etkinlikler sekmesi mevcut placeholder'ı açar; sahte etkinlik yok. Dört sekmenin sırası korunur. Niyet seçenekleri Friendship/Networking, seçici boş başlar. İngilizce arayüz ve Türkçe inceleme çerçevesi kullanıldı. Yeni fallback başlık/sloganlar yalnız görsel çalışma metnidir; ARB'lere aktarılmadı.

## Sınırlar
Bu, altı ana ekranın HTML görsel alternatifi; tüm boş/hata/offline/izin hâllerinin yeniden tasarımı değildir. Büyük metin düğmesi ×1,55 tasarım denemesidir; native %200 erişilebilirlik kabulü değildir. Masaüstü ve dar ekran kontrolü yapıldı; iOS/Android gerçek cihaz entegrasyonu yapılmadı. Krem harita yönü seçildi; native aktarım JSON dosyaları imhere-cream-theme-v1.0 içindedir. Konuşma kuralları ve son Manager kararları değişmedi.

## Dosyalar
- ONIZLEME.html, style.css, app.js: yerel HTML demo.
- assets/: fontlar, örnek portreler, MapLibre runtime/lisansı ve bu demoya özel harita stili.
- REVIEW.png: altı ekranın masaüstü inceleme görüntüsü.
- validation.json: kontrol kapsamı.
