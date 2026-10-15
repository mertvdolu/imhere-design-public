# secici — SPEC

## Bileşenler / ölçü

Mevcut v2.3 başlık, küçük düğme, bilgi kartı, input, radyo ve satır desenleri. Kenar 24 dp. Başlık 28/600, gövde 16/400, yardım 14/400; satır aralığı 1.18/1.5/1.5. Bölüm başlığı 18/500. Ölçek %200: punto 2×, sabit satır sınırı yok. Küçük düğme görünen yüzey en az 36, bağımsız hedef en az 48×48; radius12. Kart radius15.

B varyantı: 48 hedefli hap, own active community. Dokunma→Ayarlar. Segment/switch rolü yok. Harita üstünde sol, konum hedefi sağ 48; %200 hap metni sarar. Alt menü v10 edge16/radius26/inner4, büyük yazıda 2×2. Atıf ayrı opak akış satırı: © OpenStreetMap contributors · OpenFreeMap. Eski harita temizlenir; K=2 altında mevcut mapNoActivity. STATE_CHANGED boş harita diye gösterilmez: failed ve retry.

## Durumlar

- **nearby-networking**: Indicator only: opens Settings → Communities. Single community is also actionable. Other person community label absent. Switching removes old content before new load.
- **nearby-friendship**: Indicator only: opens Settings → Communities. Single community is also actionable. Other person community label absent. Switching removes old content before new load.
- **nearby-single**: Indicator only: opens Settings → Communities. Single community is also actionable. Other person community label absent. Switching removes old content before new load.
- **nearby-loading**: Indicator only: opens Settings → Communities. Single community is also actionable. Other person community label absent. Switching removes old content before new load.
- **nearby-empty**: Indicator only: opens Settings → Communities. Single community is also actionable. Other person community label absent. Switching removes old content before new load.
- **nearby-failed**: Indicator only: opens Settings → Communities. Single community is also actionable. Other person community label absent. Switching removes old content before new load.
- **nearby-offline**: Indicator only: opens Settings → Communities. Single community is also actionable. Other person community label absent. Switching removes old content before new load.
- **map-networking**: Full-area map. Own community pill top-left and Show my area top-right, attribution separate above bottom nav. K=2 suppression empty result; no inference about people. Geometry is a fictional design fixture; no precise locations.
- **map-friendship**: Full-area map. Own community pill top-left and Show my area top-right, attribution separate above bottom nav. K=2 suppression empty result; no inference about people. Geometry is a fictional design fixture; no precise locations.
- **map-single**: Full-area map. Own community pill top-left and Show my area top-right, attribution separate above bottom nav. K=2 suppression empty result; no inference about people. Geometry is a fictional design fixture; no precise locations.
- **map-empty**: Full-area map. Own community pill top-left and Show my area top-right, attribution separate above bottom nav. K=2 suppression empty result; no inference about people. Geometry is a fictional design fixture; no precise locations.
- **map-loading**: Full-area map. Own community pill top-left and Show my area top-right, attribution separate above bottom nav. K=2 suppression empty result; no inference about people. Geometry is a fictional design fixture; no precise locations.
- **map-failed**: Full-area map. Own community pill top-left and Show my area top-right, attribution separate above bottom nav. K=2 suppression empty result; no inference about people. Geometry is a fictional design fixture; no precise locations.
- **map-offline**: Full-area map. Own community pill top-left and Show my area top-right, attribution separate above bottom nav. K=2 suppression empty result; no inference about people. Geometry is a fictional design fixture; no precise locations.
- **events-community**: Own active community indicator opens Settings; Events-specific approved empty state.
- **connection-networking**: Historical connection community from the connection record only. Not the other person’s current membership.
- **connection-friendship**: Historical connection community from the connection record only. Not the other person’s current membership.

## Erişilebilirlik / native

Her durum tek H1, doğal üstten alta okuma; %200 ve320 genişlikte yatay kaydırma yok. En az48 hedef, renk yanında metin/ikon. Pasif kontrolün koşulu mevcut metin veya işlem durumu ile görünür. Varsa radyo grup etiketi, checkbox çoklu seçim, switch görünür etiketle. Focus visible 2 px Ink +3 offset. `Reduce Motion`: 150 ms doğrusal opaklık, mekânsal hareket yok. Yüksek kontrastta gölge yok, belirgin Ink kenar; şeffaflığı azaltmada menü opak.

## ★ / yeni bileşen

★ Hap seçildi: iki seçenekli kontrol gibi davranma beklentisi yaratmaz. ★ Tek toplulukta dokunulur, ikinci topluluğa katılma yolu aynı yerde bulunur. ★ Atıf büyük yazıda da ayrı 12 px harita lisans satırı olarak korunur; uygulama metinleri 2× büyür. YENİ BİLEŞEN — ONAY GEREKİR: Community indicator (mevcut hap+ikon+etiketin yeni birleşimi), 2 topluluk renk token ailesi.
