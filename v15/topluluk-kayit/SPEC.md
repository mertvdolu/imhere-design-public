# topluluk-kayit — SPEC

## Bileşenler / ölçü

Mevcut v2.3 başlık, küçük düğme, bilgi kartı, input, radyo ve satır desenleri. Kenar 24 dp. Başlık 28/600, gövde 16/400, yardım 14/400; satır aralığı 1.18/1.5/1.5. Bölüm başlığı 18/500. Ölçek %200: punto 2×, sabit satır sınırı yok. Küçük düğme görünen yüzey en az 36, bağımsız hedef en az 48×48; radius12. Kart radius15.

3 mevcut radyo kartı; önseçim yok. Networking/Friendship ikon+renk+etiket. Both tarafsız Ink, ardından 2 radyo ile başlangıç sorusu. Devam için seçim şartı mevcut errorGenderRequired metniyle açık (anahtar adı eski; değeri genel seçim çağrısıdır). Hata seçimi korur. İlk seçim 3 değişiklik sınırını tüketmez; mevcut check-in biter. Friendship-only akışı meslek ve LinkedIn’i atlayıp kart adımına geçer.

## Durumlar

- **community-none**: No preselection. Both requires explicit starting community. Initial selection does not consume a change. Friendship-only skips job/LinkedIn; card step still appears. Error retains chosen community.
- **community-networking**: No preselection. Both requires explicit starting community. Initial selection does not consume a change. Friendship-only skips job/LinkedIn; card step still appears. Error retains chosen community.
- **community-friendship**: No preselection. Both requires explicit starting community. Initial selection does not consume a change. Friendship-only skips job/LinkedIn; card step still appears. Error retains chosen community.
- **community-both**: No preselection. Both requires explicit starting community. Initial selection does not consume a change. Friendship-only skips job/LinkedIn; card step still appears. Error retains chosen community.
- **community-both-start**: No preselection. Both requires explicit starting community. Initial selection does not consume a change. Friendship-only skips job/LinkedIn; card step still appears. Error retains chosen community.
- **community-both-networking**: No preselection. Both requires explicit starting community. Initial selection does not consume a change. Friendship-only skips job/LinkedIn; card step still appears. Error retains chosen community.
- **community-both-friendship**: No preselection. Both requires explicit starting community. Initial selection does not consume a change. Friendship-only skips job/LinkedIn; card step still appears. Error retains chosen community.
- **community-saving**: No preselection. Both requires explicit starting community. Initial selection does not consume a change. Friendship-only skips job/LinkedIn; card step still appears. Error retains chosen community.
- **community-failed**: No preselection. Both requires explicit starting community. Initial selection does not consume a change. Friendship-only skips job/LinkedIn; card step still appears. Error retains chosen community.

## Erişilebilirlik / native

Her durum tek H1, doğal üstten alta okuma; %200 ve320 genişlikte yatay kaydırma yok. En az48 hedef, renk yanında metin/ikon. Pasif kontrolün koşulu mevcut metin veya işlem durumu ile görünür. Varsa radyo grup etiketi, checkbox çoklu seçim, switch görünür etiketle. Focus visible 2 px Ink +3 offset. `Reduce Motion`: 150 ms doğrusal opaklık, mekânsal hareket yok. Yüksek kontrastta gölge yok, belirgin Ink kenar; şeffaflığı azaltmada menü opak.

## ★ / yeni bileşen

★ Both kartı nötr; mavi-yeşil karışım üçüncü bir topluluk izlenimi vermesin. ★ Mevcut errorGenderRequired değeri genel seçim gereğini anlatmak için yeniden kullanıldı; Code isterse alias kullanabilir, değer değişmez. YENİ BİLEŞEN — ONAY GEREKİR: yok; mevcut radyo kartı, yeni topluluk renk tokenları öneri.
