# gecis — SPEC

## Bileşenler / ölçü

Mevcut v2.3 başlık, küçük düğme, bilgi kartı, input, radyo ve satır desenleri. Kenar 24 dp. Başlık 28/600, gövde 16/400, yardım 14/400; satır aralığı 1.18/1.5/1.5. Bölüm başlığı 18/500. Ölçek %200: punto 2×, sabit satır sınırı yok. Küçük düğme görünen yüzey en az 36, bağımsız hedef en az 48×48; radius12. Kart radius15.

Intro → boş topluluk seçimi → yalnız eski LinkedIn varsa görünürlük → isteğe bağlı meslek daveti. LinkedIn açıklaması §14.1r5. Üç radyoda aynı kenar, renk, ağırlık ve açıklama stili; Everyone yalnız standart radyo noktasıyla seçili. Kaydet/Devam bekleme-hata ayrımı. Kapatınca mevcut Everyone korunur; sonraki açılış tekrar. Meslek seç / Şimdi değil düğmeleri aynı yüzey, punto ve hedef.

## Durumlar

- **migration-intro**: No inferred choice. Not visible in discovery until community selection.
- **migration-community**: Reuses registration selection component. Initial selection ends previous check-in; no rate-limit cost. LinkedIn step only if stored.
- **migration-linkedin-everyone**: Only for stored LinkedIn. Everyone is existing value; no extra visual emphasis. Dismiss keeps Everyone and repeats next launch. Save failure restores Everyone and stays on screen. Body uses HB-37 r5.
- **migration-linkedin-connections**: Only for stored LinkedIn. Everyone is existing value; no extra visual emphasis. Dismiss keeps Everyone and repeats next launch. Save failure restores Everyone and stays on screen. Body uses HB-37 r5.
- **migration-linkedin-nobody**: Only for stored LinkedIn. Everyone is existing value; no extra visual emphasis. Dismiss keeps Everyone and repeats next launch. Save failure restores Everyone and stays on screen. Body uses HB-37 r5.
- **migration-linkedin-saving**: Only for stored LinkedIn. Everyone is existing value; no extra visual emphasis. Dismiss keeps Everyone and repeats next launch. Save failure restores Everyone and stays on screen. Body uses HB-37 r5.
- **migration-linkedin-failed**: Only for stored LinkedIn. Everyone is existing value; no extra visual emphasis. Dismiss keeps Everyone and repeats next launch. Save failure restores Everyone and stays on screen. Body uses HB-37 r5.
- **migration-linkedin-offline**: Only for stored LinkedIn. Everyone is existing value; no extra visual emphasis. Dismiss keeps Everyone and repeats next launch. Save failure restores Everyone and stays on screen. Body uses HB-37 r5.
- **migration-occupation**: Optional one-time invitation. Equal button treatment. Existing free text is not mapped automatically.
- **migration-offline**: Network failure keeps route and avoids inferred membership.

## Erişilebilirlik / native

Her durum tek H1, doğal üstten alta okuma; %200 ve320 genişlikte yatay kaydırma yok. En az48 hedef, renk yanında metin/ikon. Pasif kontrolün koşulu mevcut metin veya işlem durumu ile görünür. Varsa radyo grup etiketi, checkbox çoklu seçim, switch görünür etiketle. Focus visible 2 px Ink +3 offset. `Reduce Motion`: 150 ms doğrusal opaklık, mekânsal hareket yok. Yüksek kontrastta gölge yok, belirgin Ink kenar; şeffaflığı azaltmada menü opak.

## ★ / yeni bileşen

★ Uzun metne göre kaydırılan tam sayfa; bottom sheet değil. ★ Kapat/Vazgeç mevcut cancel değeriyle, üründeki geçiş tekrar davranışı korunarak. YENİ BİLEŞEN — ONAY GEREKİR: yok. METİN-EKİ BEKLİYOR kapanmış: HB-37r5§14.1 son değerleri mevcut.
