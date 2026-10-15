# kart-adimi — SPEC

## Bileşenler / ölçü

Mevcut v2.3 başlık, küçük düğme, bilgi kartı, input, radyo ve satır desenleri. Kenar 24 dp. Başlık 28/600, gövde 16/400, yardım 14/400; satır aralığı 1.18/1.5/1.5. Bölüm başlığı 18/500. Ölçek %200: punto 2×, sabit satır sınırı yok. Küçük düğme görünen yüzey en az 36, bağımsız hedef en az 48×48; radius12. Kart radius15.

İsteğe bağlı kayıt adımı: telefon/e-posta/Instagram. E-posta boş; giriş e-postasından türetilmez. StepBody aynen, EmailNote e-posta altında. StepLater düğmelerin üstünde. Save/Not now aynı ikincil krem yüzey, aynı14/500, en az48 hedef; wrap/flex ile büyük yazıda alt alta. Boş Save etkin; Send bu ekranda yok.

## Durumlar

- **card-empty**: Optional for both communities. Sign-in email not prefilled. Example.invalid is reserved fictional layout data. Fields only shared when sent in a chat, never on profile. Blank Save behaves as Not now. Equal action treatment; invalid input reason inline. Saved only after server acknowledgement.
- **card-filled**: Optional for both communities. Sign-in email not prefilled. Example.invalid is reserved fictional layout data. Fields only shared when sent in a chat, never on profile. Blank Save behaves as Not now. Equal action treatment; invalid input reason inline. Saved only after server acknowledgement.
- **card-invalid**: Optional for both communities. Sign-in email not prefilled. Example.invalid is reserved fictional layout data. Fields only shared when sent in a chat, never on profile. Blank Save behaves as Not now. Equal action treatment; invalid input reason inline. Saved only after server acknowledgement.
- **card-saving**: Optional for both communities. Sign-in email not prefilled. Example.invalid is reserved fictional layout data. Fields only shared when sent in a chat, never on profile. Blank Save behaves as Not now. Equal action treatment; invalid input reason inline. Saved only after server acknowledgement.
- **card-saved**: Optional for both communities. Sign-in email not prefilled. Example.invalid is reserved fictional layout data. Fields only shared when sent in a chat, never on profile. Blank Save behaves as Not now. Equal action treatment; invalid input reason inline. Saved only after server acknowledgement.
- **card-failed**: Optional for both communities. Sign-in email not prefilled. Example.invalid is reserved fictional layout data. Fields only shared when sent in a chat, never on profile. Blank Save behaves as Not now. Equal action treatment; invalid input reason inline. Saved only after server acknowledgement.
- **card-skipped**: No skipped confirmation screen in production. Shown destination after optional onboarding completes; Friendship-only also gets card step. No card is created by skipping. Other pending onboarding steps take precedence.

## Erişilebilirlik / native

Her durum tek H1, doğal üstten alta okuma; %200 ve320 genişlikte yatay kaydırma yok. En az48 hedef, renk yanında metin/ikon. Pasif kontrolün koşulu mevcut metin veya işlem durumu ile görünür. Varsa radyo grup etiketi, checkbox çoklu seçim, switch görünür etiketle. Focus visible 2 px Ink +3 offset. `Reduce Motion`: 150 ms doğrusal opaklık, mekânsal hareket yok. Yüksek kontrastta gölge yok, belirgin Ink kenar; şeffaflığı azaltmada menü opak.

## ★ / yeni bileşen

★ Boş Save, Not now ile aynı ilerlemeyi yapar; boş kart kaydı/başarı mesajı üretmez. ★ Eşit ağırlık için iki düğme de aynı kabartmalı krem. YENİ BİLEŞEN — ONAY GEREKİR: yok. Kurmaca e-posta example.invalid; iletişim kurulmaz.
