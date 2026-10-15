# meslek — SPEC

## Bileşenler / ölçü

Mevcut v2.3 başlık, küçük düğme, bilgi kartı, input, radyo ve satır desenleri. Kenar 24 dp. Başlık 28/600, gövde 16/400, yardım 14/400; satır aralığı 1.18/1.5/1.5. Bölüm başlığı 18/500. Ölçek %200: punto 2×, sabit satır sınırı yok. Küçük düğme görünen yüzey en az 36, bağımsız hedef en az 48×48; radius12. Kart radius15.

Manager meslek-katalogu-uygulama.json 1.0.1 gerçek etiketleriyle yerel gruplu liste. Arama tüm etiket/sinonimleri tarar; grup başlıkları 48 hedefli açılır satırlar. Bir grup açılınca diğerleri kapanmak zorunda değildir. Her grubun sonunda tek Other (katalogdaki diğer satırını ikinci kez üretme). Seçim ve Mesleğim görünsün aynı kaydırılan ekranda; varsayılan açık yalnız yeni seçimde, mevcut false korunur. Other unvan isteğe bağlı ve filtreye girmez.

## Durumlar

- **occupation-empty**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-search**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-no-match**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-selected**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-other**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-hidden**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-legacy**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-replace**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-saving**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-saved**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-removed**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-failed**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-catalog-failed**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-loading**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-removing**: Pending remove; no removed status until server confirms. Failure returns selected old title.
- **occupation-profile-networking**: Other profile: community never displayed. Occupation only in Networking, omitted entirely in Friendship; no blank line. Fixture uses catalogue title.
- **occupation-profile-friendship**: Other profile: community never displayed. Occupation only in Networking, omitted entirely in Friendship; no blank line. Fixture uses catalogue title.

## Erişilebilirlik / native

Her durum tek H1, doğal üstten alta okuma; %200 ve320 genişlikte yatay kaydırma yok. En az48 hedef, renk yanında metin/ikon. Pasif kontrolün koşulu mevcut metin veya işlem durumu ile görünür. Varsa radyo grup etiketi, checkbox çoklu seçim, switch görünür etiketle. Focus visible 2 px Ink +3 offset. `Reduce Motion`: 150 ms doğrusal opaklık, mekânsal hareket yok. Yüksek kontrastta gölge yok, belirgin Ink kenar; şeffaflığı azaltmada menü opak.

## ★ / yeni bileşen

★ Yaklaşık 150 mesleği dev bir liste yapmamak için mevcut açılır satır düzeni, aramada eşleşen gruplar açık. ★ Gizleme aynı ekranın seçimden sonraki bölümünde. YENİ BİLEŞEN — ONAY GEREKİR: grouped occupation selector (mevcut arama+disclosure+radio birleşimi).
