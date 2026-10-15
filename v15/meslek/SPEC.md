# meslek — SPEC

## Bileşenler / ölçü

Mevcut v2.3 başlık, küçük düğme, bilgi kartı, input, radyo ve satır desenleri. Kenar 24 dp. Başlık 28/600, gövde 16/400, yardım 14/400; satır aralığı 1.18/1.5/1.5. Bölüm başlığı 18/500. Ölçek %200: punto 2×, sabit satır sınırı yok. Küçük düğme görünen yüzey en az 36, bağımsız hedef en az 48×48; radius12. Kart radius15.

Manager meslek-katalogu-uygulama.json 1.0.1 gerçek etiketleriyle yerel gruplu liste. Arama tüm etiket/sinonimleri tarar; grup başlıkları 48 hedefli açılır satırlar. Bir grup açılınca diğerleri kapanmak zorunda değildir. Her grubun sonunda tek Other (katalogdaki diğer satırını ikinci kez üretme). Seçim ve Mesleğim görünsün aynı kaydırılan ekranda; varsayılan açık yalnız yeni seçimde, mevcut false korunur. Other unvan isteğe bağlı ve filtreye girmez. Düzeltme1: profil düzenleme title=occupation, geri + Save; Atla yok. Kayıt örnekleri occupation-empty/search/no-match ve occupation-signup-*; profil örnekleri occupation-edit-empty ve mevcut selected/other/hidden/legacy/replace/save/remove durumları. Other unvan alanı seçili Other satırının hemen altında, aynı grup içinde; aşağıdaki grup başlıklarının ardına itilmez.

## Durumlar

- **occupation-empty**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-search**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-no-match**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-selected**: Profile editing: Job title label/H1, Back and Save; no Skip. Return to the existing Profile editor. Other title immediately follows the selected Other row. Save/remove success only after server response; existing visibility preserved.
- **occupation-other**: Profile editing: Job title label/H1, Back and Save; no Skip. Return to the existing Profile editor. Other title immediately follows the selected Other row. Save/remove success only after server response; existing visibility preserved.
- **occupation-hidden**: Profile editing: Job title label/H1, Back and Save; no Skip. Return to the existing Profile editor. Other title immediately follows the selected Other row. Save/remove success only after server response; existing visibility preserved.
- **occupation-legacy**: Profile editing: Job title label/H1, Back and Save; no Skip. Return to the existing Profile editor. Other title immediately follows the selected Other row. Save/remove success only after server response; existing visibility preserved.
- **occupation-replace**: Profile editing: Job title label/H1, Back and Save; no Skip. Return to the existing Profile editor. Other title immediately follows the selected Other row. Save/remove success only after server response; existing visibility preserved.
- **occupation-saving**: Profile editing: Job title label/H1, Back and Save; no Skip. Return to the existing Profile editor. Other title immediately follows the selected Other row. Save/remove success only after server response; existing visibility preserved.
- **occupation-saved**: Profile editing: Job title label/H1, Back and Save; no Skip. Return to the existing Profile editor. Other title immediately follows the selected Other row. Save/remove success only after server response; existing visibility preserved.
- **occupation-removed**: Profile editing: Job title label/H1, Back and Save; no Skip. Return to the existing Profile editor. Other title immediately follows the selected Other row. Save/remove success only after server response; existing visibility preserved.
- **occupation-failed**: Profile editing: Job title label/H1, Back and Save; no Skip. Return to the existing Profile editor. Other title immediately follows the selected Other row. Save/remove success only after server response; existing visibility preserved.
- **occupation-catalog-failed**: Profile editing: Job title label/H1, Back and Save; no Skip. Return to the existing Profile editor. Other title immediately follows the selected Other row. Save/remove success only after server response; existing visibility preserved.
- **occupation-loading**: Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.
- **occupation-removing**: Profile editing: Job title label/H1, Back and Save; no Skip. Return to the existing Profile editor. Other title immediately follows the selected Other row. Save/remove success only after server response; existing visibility preserved.
- **occupation-profile-networking**: Other profile: community never displayed. Occupation only in Networking, omitted entirely in Friendship; no blank line. Fixture uses catalogue title.
- **occupation-profile-friendship**: Other profile: community never displayed. Occupation only in Networking, omitted entirely in Friendship; no blank line. Fixture uses catalogue title.
- **occupation-signup-selected**: Optional signup job step; Skip stays available. Separate from Profile editing. Save waits for server acknowledgement; no forced occupation. Other title is directly under the selected Other row.
- **occupation-signup-other**: Optional signup job step; Skip stays available. Separate from Profile editing. Save waits for server acknowledgement; no forced occupation. Other title is directly under the selected Other row.
- **occupation-signup-saving**: Optional signup job step; Skip stays available. Separate from Profile editing. Save waits for server acknowledgement; no forced occupation. Other title is directly under the selected Other row.
- **occupation-signup-saved**: Optional signup job step; Skip stays available. Separate from Profile editing. Save waits for server acknowledgement; no forced occupation. Other title is directly under the selected Other row.
- **occupation-signup-failed**: Optional signup job step; Skip stays available. Separate from Profile editing. Save waits for server acknowledgement; no forced occupation. Other title is directly under the selected Other row.
- **occupation-edit-empty**: Profile editing: Job title label/H1, Back and Save; no Skip. Return to the existing Profile editor. Other title immediately follows the selected Other row. Save/remove success only after server response; existing visibility preserved.

## Erişilebilirlik / native

Her durum tek H1, doğal üstten alta okuma; %200 ve320 genişlikte yatay kaydırma yok. En az48 hedef, renk yanında metin/ikon. Pasif kontrolün koşulu mevcut metin veya işlem durumu ile görünür. Varsa radyo grup etiketi, checkbox çoklu seçim, switch görünür etiketle. Focus visible 2 px Ink +3 offset. `Reduce Motion`: 150 ms doğrusal opaklık, mekânsal hareket yok. Yüksek kontrastta gölge yok, belirgin Ink kenar; şeffaflığı azaltmada menü opak.

## ★ / yeni bileşen

★ Yaklaşık 150 mesleği dev bir liste yapmamak için mevcut açılır satır düzeni, aramada eşleşen gruplar açık. ★ Gizleme aynı ekranın seçimden sonraki bölümünde. YENİ BİLEŞEN — ONAY GEREKİR: grouped occupation selector (mevcut arama+disclosure+radio birleşimi).
