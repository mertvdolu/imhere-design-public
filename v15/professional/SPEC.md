# professional — SPEC

## Bileşenler / ölçü

Mevcut v2.3 başlık, küçük düğme, bilgi kartı, input, radyo ve satır desenleri. Kenar 24 dp. Başlık 28/600, gövde 16/400, yardım 14/400; satır aralığı 1.18/1.5/1.5. Bölüm başlığı 18/500. Ölçek %200: punto 2×, sabit satır sınırı yok. Küçük düğme görünen yüzey en az 36, bağımsız hedef en az 48×48; radius12. Kart radius15.

eventV1CategoryNetworking ve y1CategoryNetworking değerleri Professional / Profesyonel; anahtar adı ve teldeNETWORKINGenum değişmez. Listede topluluk pillNetworking yukarıda, kartta çanta+Professional; kategori ve topluluk ayrımı açık. Detay ve geçmişte Category: {category} anahtarı; öneri formunda3radyo aynıağırlık.

## Durumlar

- **professional-list**: Category label renamed to Professional/Profesyonel; enum and keys preserved. Category is not community. Fictional event/venue for layout; other Events controls remain governed by existing Events spec, no new RSVP behavior.
- **professional-detail**: Category label renamed to Professional/Profesyonel; enum and keys preserved. Category is not community. Fictional event/venue for layout; other Events controls remain governed by existing Events spec, no new RSVP behavior.
- **professional-suggest**: Category label renamed to Professional/Profesyonel; enum and keys preserved. Category is not community. Fictional event/venue for layout; other Events controls remain governed by existing Events spec, no new RSVP behavior.
- **professional-past**: Category label renamed to Professional/Profesyonel; enum and keys preserved. Category is not community. Fictional event/venue for layout; other Events controls remain governed by existing Events spec, no new RSVP behavior.
- **professional-loading**: Category label renamed to Professional/Profesyonel; enum and keys preserved. Category is not community. Fictional event/venue for layout; other Events controls remain governed by existing Events spec, no new RSVP behavior.
- **professional-failed**: Category label renamed to Professional/Profesyonel; enum and keys preserved. Category is not community. Fictional event/venue for layout; other Events controls remain governed by existing Events spec, no new RSVP behavior.
- **professional-empty**: Category label renamed to Professional/Profesyonel; enum and keys preserved. Category is not community. Fictional event/venue for layout; other Events controls remain governed by existing Events spec, no new RSVP behavior.

## Erişilebilirlik / native

Her durum tek H1, doğal üstten alta okuma; %200 ve320 genişlikte yatay kaydırma yok. En az48 hedef, renk yanında metin/ikon. Pasif kontrolün koşulu mevcut metin veya işlem durumu ile görünür. Varsa radyo grup etiketi, checkbox çoklu seçim, switch görünür etiketle. Focus visible 2 px Ink +3 offset. `Reduce Motion`: 150 ms doğrusal opaklık, mekânsal hareket yok. Yüksek kontrastta gölge yok, belirgin Ink kenar; şeffaflığı azaltmada menü opak.

## ★ / yeni bileşen

★Networking yalnız topluluk, Professional yalnız kategori etiketi olarak birlikte gösterildi; ikonu farklı. YENİ BİLEŞEN — ONAY GEREKİR: yok.
