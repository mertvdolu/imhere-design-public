# ikonlar — SPEC

## Bileşenler / ölçü

Mevcut v2.3 başlık, küçük düğme, bilgi kartı, input, radyo ve satır desenleri. Kenar 24 dp. Başlık 28/600, gövde 16/400, yardım 14/400; satır aralığı 1.18/1.5/1.5. Bölüm başlığı 18/500. Ölçek %200: punto 2×, sabit satır sınırı yok. Küçük düğme görünen yüzey en az 36, bağımsız hedef en az 48×48; radius12. Kart radius15.

5 çizgi işareti: Professional çanta, Social konuşma, Activity yükselen hareket çizgisi, Networking bağlı kareler, Friendship iki kişi. Professional ve Networking farklı geometridir. 16/20/24 SVG, görünür çizgi 1.8 dp; 24 birim grid. Kategori Ink, topluluk ikon/etiketli control içinde kendi tonu.

## Durumlar

- **icons-categories**: Design-system specimen:16/20/24 visible sizes,48 interaction target. Category Ink; community coloured only with text. Professional bag differs from Networking connected squares.
- **icons-communities**: Design-system specimen:16/20/24 visible sizes,48 interaction target. Category Ink; community coloured only with text. Professional bag differs from Networking connected squares.

## Erişilebilirlik / native

Her durum tek H1, doğal üstten alta okuma; %200 ve320 genişlikte yatay kaydırma yok. En az48 hedef, renk yanında metin/ikon. Pasif kontrolün koşulu mevcut metin veya işlem durumu ile görünür. Varsa radyo grup etiketi, checkbox çoklu seçim, switch görünür etiketle. Focus visible 2 px Ink +3 offset. `Reduce Motion`: 150 ms doğrusal opaklık, mekânsal hareket yok. Yüksek kontrastta gölge yok, belirgin Ink kenar; şeffaflığı azaltmada menü opak.

## ★ / yeni bileşen

★ 5 ikon yeterli; yeni bir ikon ailesi yok, v2.3 round cap/join 1.8 devamı. ★ Kategoriler renksiz, topluluk ikonu yalnız community yüzeylerinde renkli. YENİ BİLEŞEN — ONAY GEREKİR: yok; talep edilen mevcut çizgi ailesi uzantısı.
