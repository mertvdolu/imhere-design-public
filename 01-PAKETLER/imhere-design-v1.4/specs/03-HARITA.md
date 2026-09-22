# 03 — Harita durumları ve yerleşim
## Sabit sınırlar
Yakındakiler içindeki alt sayfa; check-in olmadan açık. Pan/zoom oturumu veya check-in referansını değiştirmez. Kişisel işaret, GPS puck, mesafe, koordinat, kişi sayısı ve kişisel merkezleme yok. Sabit sunucu H3 poligonları ve bantları; istemci nokta/ısı üretmez. 0–1 hücre hiçbir dolgu/sınır/semantik fark oluşturmaz. Bantlar mavi/sarı/yeşil/kırmızı; kullanıcıya yalnız Sakin/Canlı/Hareketli/Çok hareketli etiketleri.

## Yerleşim
Geri eylemi (minimum48) → mapTitle/mapBody → gezilebilir harita → ayrılmış SDK attribution alanı → varsa snapshot açıklaması → legend. Harita normalde minimum300, büyük metinde minimum360 yükseklik. Sağ üstte 48×48 zoom kontrolleri, arada6; okunabilir etiketler Semantics’tedir. Alt bar ile yasal attribution asla örtüşmez. Native harita dokunması sayfa scroll’u ile çakışmamalı; iki parmak jestleri/platform standardı geliştirici tarafından sınanır.

PARTIAL kartı haritanın üst alanında, zoom kontrollerinin altında, 16 dolgu/köşe, 24 ikon +12 aralık +14sp/1.5 metin. İkon orijinal map-partial.svg; yeni buton değil. EMPTY_NO_REGION kartı gezilebilir harita üzerinde, 40 ikon +14sp/1.5 metin; yeni CTA yok. Harita paneli büyük metinde kart ve jest alanını barındıracak kadar büyür. PARTIAL değerlendirilmemiş alanı sıfır saymaz, otomatik zoom yapmaz. İki orijinal SVG dosyası değişmeden teslimdedir.

## Durum matrisi
| ID | Görünen sunum | Veri/aksiyon sınırı |
|---|---|---|
| map-ready | Sunucu bantları, asOf ve açıklama, legend | Gerçek snapshot; örnek poligonlar üretime alınmaz |
| map-partial | Aynı band snapshot’ı + yaklaştır kartı | Sadece gerçek PARTIAL yanıtı; yeni zoom eşiği yok |
| map-empty-no-region | Temel harita + başlangıç kartı | Aktif check-in VE geçmiş bölge ikisi de yok; hayali bölge yok |
| map-loading | Spinner + Harita yükleniyor | Veri yokken boş/0 kişi iddiası yok |
| map-empty | Gösterilecek hareketlilik yok | Sunucunun tamamlanmış boş sonucu; 0/1 ayrımı yapılmaz |
| map-offline | Bağlantı açıklaması | Son geçerli snapshot çizimi mevcut geçerlilik sözleşmesine bağlı; örnek çizim bant içermez |
| map-failed | Harita yüklenemedi | Servis/render hatası, boş sonuç değildir |
| map-stale | Eski veri uyarısı + asOf | Yalnız mevcut sözleşme çizime izin veriyorsa eski bant; tasarım yeni TTL belirlemez |

Konum izni reddi haritayı kapatmaz; map-permission-denied adında uydurma engel ekranı yok. Bu durum Yakındakiler/check-in örneklerinde gösterilir. Bildirim izni harita durumuna bağlanmaz.

## Erişilebilirlik ve sağlayıcı
Legend renk + metin taşır. Harita hücrelerinin erişilebilir açıklaması yalnız mevcut band etiketi; kişi/sayı/alt grup yok. 0–1 hücrelere erişilebilir düğüm üretilmez. Ekran okuyucu odakları: geri → başlık → zoom → mevcut durum → snapshot → legend → navigasyon. Salt dekoratif SVG ikonları okunmaz. Aynı PARTIAL yenilenmesinde tekrar anons yok.

Mapbox seçimi/final stili M05 adım7 kapsamındadır; bu paket sağlayıcı seçmez. Ham GPS harita kaynağına veya analytics'e geçirilmez. Provider attribution için çizimdeki metin bir ölçü yer tutucusudur; gerçek kredi bileşeni M05 entegrasyonunda kullanılmalı. Çizimdeki şematik taban yolları/nehir, yer/kişi bilgisi değildir; SDK stil dosyası olarak kullanılamaz.
