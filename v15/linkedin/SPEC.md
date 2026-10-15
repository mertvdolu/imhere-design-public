# linkedin — SPEC

## Bileşenler / ölçü

Mevcut v2.3 başlık, küçük düğme, bilgi kartı, input, radyo ve satır desenleri. Kenar 24 dp. Başlık 28/600, gövde 16/400, yardım 14/400; satır aralığı 1.18/1.5/1.5. Bölüm başlığı 18/500. Ölçek %200: punto 2×, sabit satır sınırı yok. Küçük düğme görünen yüzey en az 36, bağımsız hedef en az 48×48; radius12. Kart radius15.

Sıra: link alanı → Open and check → dış açılış başarılıysa dönüş onayı → aynı formdaki üç görünürlük radiosu → Save. Everyone varsayılan, yalnız dot işaretli; stil ağırlığı eşit. Signup Skip/Save aynı yüzey/etiket ölçüsü; koşul nedeniyle Save pasifken neden CheckRequired ile görünür. DefaultNote yalnız ilk ekleme. Kayıtlı ayarda NetworkingNote. Görüntüleyen sayfada düz LinkedIn + genel external icon; altında ViewerNote.

## Durumlar

- **linkedin-empty**: Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.
- **linkedin-invalid**: Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.
- **linkedin-unconfirmed**: Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.
- **linkedin-opening**: Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.
- **linkedin-confirmed**: Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.
- **linkedin-nobody**: Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.
- **linkedin-connections**: Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.
- **linkedin-saving**: Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.
- **linkedin-saved**: Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.
- **linkedin-save-failed**: Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.
- **linkedin-stored**: Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.
- **linkedin-offline**: Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.
- **linkedin-open-failed**: Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.
- **linkedin-paused**: Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.
- **linkedin-removed**: Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.
- **linkedin-confirm-return**: Shown only after successful external opening and app return. Yes confirms ownership declaration only; next Save still required. Editing URL invalidates confirmation.
- **linkedin-remove-confirm**: Removal keeps seen-information warning. Failed removal keeps stored link. Acknowledge before Removed.
- **linkedin-remove-busy**: Removal keeps seen-information warning. Failed removal keeps stored link. Acknowledge before Removed.
- **linkedin-remove-failed**: Removal keeps seen-information warning. Failed removal keeps stored link. Acknowledge before Removed.
- **linkedin-connection**: Link plain text + generic external icon. Connections/chat profile can see according to visibility across communities. Before connection Networking only. Hidden/no link identical omission; no placeholder or community field. Viewer notice immediately below link.
- **linkedin-chat**: Link plain text + generic external icon. Connections/chat profile can see according to visibility across communities. Before connection Networking only. Hidden/no link identical omission; no placeholder or community field. Viewer notice immediately below link.
- **linkedin-networking-before**: Link plain text + generic external icon. Connections/chat profile can see according to visibility across communities. Before connection Networking only. Hidden/no link identical omission; no placeholder or community field. Viewer notice immediately below link.
- **linkedin-friendship-before**: Link plain text + generic external icon. Connections/chat profile can see according to visibility across communities. Before connection Networking only. Hidden/no link identical omission; no placeholder or community field. Viewer notice immediately below link.
- **linkedin-hidden**: Link plain text + generic external icon. Connections/chat profile can see according to visibility across communities. Before connection Networking only. Hidden/no link identical omission; no placeholder or community field. Viewer notice immediately below link.
- **linkedin-viewer-offline**: Link plain text + generic external icon. Connections/chat profile can see according to visibility across communities. Before connection Networking only. Hidden/no link identical omission; no placeholder or community field. Viewer notice immediately below link.
- **linkedin-viewer-failed**: Link plain text + generic external icon. Connections/chat profile can see according to visibility across communities. Before connection Networking only. Hidden/no link identical omission; no placeholder or community field. Viewer notice immediately below link.

## Erişilebilirlik / native

Her durum tek H1, doğal üstten alta okuma; %200 ve320 genişlikte yatay kaydırma yok. En az48 hedef, renk yanında metin/ikon. Pasif kontrolün koşulu mevcut metin veya işlem durumu ile görünür. Varsa radyo grup etiketi, checkbox çoklu seçim, switch görünür etiketle. Focus visible 2 px Ink +3 offset. `Reduce Motion`: 150 ms doğrusal opaklık, mekânsal hareket yok. Yüksek kontrastta gölge yok, belirgin Ink kenar; şeffaflığı azaltmada menü opak.

## ★ / yeni bileşen

★ Uzun gövdeler tam sayfa kaydırılır; bir onay metni bile kısaltılmadı. ★ Üç seçenek plain radio row; community blue bu alanda kullanılmaz. YENİ BİLEŞEN — ONAY GEREKİR: yok (mevcut form/radio/confirm). HB-37 r5 §14.1 üç son değer bulundu; METİN-EKİ BEKLİYOR yok.
