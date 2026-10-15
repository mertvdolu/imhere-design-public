# d0 — SPEC

## Bileşenler / ölçü

Mevcut v2.3 başlık, küçük düğme, bilgi kartı, input, radyo ve satır desenleri. Kenar 24 dp. Başlık 28/600, gövde 16/400, yardım 14/400; satır aralığı 1.18/1.5/1.5. Bölüm başlığı 18/500. Ölçek %200: punto 2×, sabit satır sınırı yok. Küçük düğme görünen yüzey en az 36, bağımsız hedef en az 48×48; radius12. Kart radius15.

D0: tek ekran, geri/alt menü yok. Logo mevcut splash-mark SVG; yeni ikon veya renk yok. Başlık/gövde/Update/delete-account link okuma sırası. Gövde normalde dikey ortalı; büyük metinde doğal akış ve kaydırma. Açılış beklerken Update devre dışı ve aria-busy; etiketi korunur, spinner durumun görsel işaretidir. Mağaza açma hata metni Update üstünde, eylem yeniden kullanılabilir. Silme notunun tamamı en az48 hedefli gerçek web bağlantısıdır; uygulama içinde silme vaadi yok.

## Durumlar

- **d0-required**: Cold-launch minimum-version gate. No back, profile, navigation or dismiss. Update opens configured OS store URL.
- **d0-opening**: Store opener pending, spinner plus unchanged Update label; no success claim. Delete-account route remains available. Platform opener completion/failure ends pending state.
- **d0-store-failed**: Store opener failed; Update remains retryable. No invented store URL. Delete link opens approved web deletion route.

## Erişilebilirlik / native

Her durum tek H1, doğal üstten alta okuma; %200 ve320 genişlikte yatay kaydırma yok. En az48 hedef, renk yanında metin/ikon. Pasif kontrolün koşulu mevcut metin veya işlem durumu ile görünür. Varsa radyo grup etiketi, checkbox çoklu seçim, switch görünür etiketle. Focus visible 2 px Ink +3 offset. `Reduce Motion`: 150 ms doğrusal opaklık, mekânsal hareket yok. Yüksek kontrastta gölge yok, belirgin Ink kenar; şeffaflığı azaltmada menü opak.

## ★ / yeni bileşen

★ Tekrar açma eylemi aynı Update düğmesiyle; ikinci bir mağaza düğmesi eklenmedi. YENİ BİLEŞEN — ONAY GEREKİR: yok; mevcut başlangıç engeli ve form/info desenleri.
