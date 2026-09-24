TASARIMCIDAN MANAGERE MESAJ

# Founder telefon turu — 24 Eylül 2026 / Cream & Ink v2.2

Telefon turu ve kendi profilinden düzenlemeye geçiş kararları tasarım devrine işlendi. Yeni fotoğraf ara durumları yerel commit olarak teslim edilir; aktarımı Code yapar. Native uygulama bu teslimde değiştirilmedi.

## 1. Klavye

- Etkileşimsiz boş alana dokunmak veya içeriği kaydırmak klavyeyi kapatır. Düğme/seçici gibi etkileşimli alanların kendi eylemleri korunur.
- Klavyenin üstündeki çubukta mevcut `selectionDone` kullanılır: **Done / Tamam**. Bu kullanım yalnız klavyeyi kapatır; kaydetme, gönderme veya profil tamamlama değildir. Formdaki giriş değerlerini değiştirmez; yeni kalıcı taslak vaadi yoktur.
- Eylem hedefi en az 48 birim yüksekliğinde; büyük metinde çubuk büyüyebilir. Odaklanılan alanı veya sohbet eylemlerini örtmez.
- Sohbette mevcut composer + sayaç + Send klavyenin üzerinde kalır. Done çubuğu eklendiğinde bu alanlar üst üste bindirilmez; klavye kapalıyken mevcut yerleşim korunur.
- Klavye yüzeyi platforma aittir; yeni bir özel klavye tasarımı veya yeni metin anahtarı eklenmedi.

## 2. Profil fotoğrafı

| Gerçek uygulama durumu | Çizim / anahtar | EN | TR |
|---|---|---|---|
| Yükleme sürüyor | photo-uploading / photoUploading | Uploading photo… | Fotoğraf yükleniyor… |
| İşleme sürüyor | photo-processing / photoProcessing | Processing photo… | Fotoğraf işleniyor… |
| Başarı doğrulandı | mevcut form-filled / photoUploaded | Photo uploaded. | Fotoğraf yüklendi. |

`photo-preparing` mevcut yerel hazırlama durumudur; sunucudaki işleme aşaması yerine kullanılmaz. `photo-selected` yalnız seçilmiş fotoğrafı temsil eder, yükleme başarısı değildir.

Yeni iki durumun her biri TR/EN × iOS/Android × %100/%200 olarak çizildi: **16 SVG + 4 PNG**. `photo-uploading` yükleme durum satırı ve doğrusal ilerleme göstergesi içerir; çizimdeki hareketli segmentin anlık görünümü bir yüzde değeri değildir. Gerçek ilerleme bilgisi varsa uygulama onu kullanır; yoksa belirsiz ilerleme göstergesi kullanılır. Süre, tahmini yüzde veya sahte tamamlanma üretilmez.

`photo-processing` ayrı durum metni ve mevcut 24×24 / 1,8 çizgili bekleme göstergesini kullanır. Yalnız transferin bitmesi, seçili fotoğrafın görünmesi veya zaman geçmesi `photoUploaded` için yeterli değildir; uygulamanın işlem başarısını doğrulaması gerekir. Başarı metni profil formunda fotoğrafın altında zaten vardır, değiştirilmedi.

Mevcut hata, tekrar deneme ve gezinme davranışları korunur; yeni iptal/yeniden deneme politikası veya backend durumu tanımlanmadı. Seçili görsel yerel önizlemedir; kayıt başarısı işareti değildir.

## 3. Doğum tarihi

- `profileBirthDate` serbest metin alanı değildir; dokunulunca platform tarih seçicisi açılır: **iOS çark / Android takvim**.
- Alan metin klavyesi açmaz; tarih seçicisi ve mevcut doğrulama kullanılır. Uygunluk ve görünürlük kuralları değişmez.
- Seçim sonrası okunur tarih gösterilir. Biçim örnekleri: **24 Sep 1995 / 24 Eyl 1995**. Bunlar örnek tarihlerdir; kullanıcıya varsayılan değer atanması anlamına gelmez.
- Katalogdaki tarih alanı zaten seçici oku ve okunur tarihle çizilmiştir. Mevcut form görselleri değiştirilmeden 56 form varyantının alan tanımına `readOnly`, `keyboardInput: false` ve platform seçicisi işlendi. Native çark/takvim burada özel çizimle taklit edilmedi.

## Dosyalar ve birleştirme

- Çizimler: `screens/svg/photo-uploading--*.svg`, `screens/svg/photo-processing--*.svg`; PNG karşılıkları `screens/png/`.
- Davranış devri: `contracts/profile-inputs.json` ve `specs/TASARIM-DEVRI.md`.
- Üç yeni anahtar: `photoUploading`, `photoProcessing`, `profileHiddenToOthers`. `photoUploaded` ve `selectionDone` mevcut metinleri aynen kullanılır.
- `l10n/cream-v2.2-patch_*.arb` ve `l10n/migration.json` ile yalnız yeni anahtarlar birleştirilir; canlı ARB'ler tam referansla ezilmez.
- Yeni iki durum `beta: true`; önceki beta kararları korunur. Toplam **298 durum / 2384 SVG / 596 PNG**; 291 beta / 7 sonraya kalan durum.
- Own-profile dışındaki mevcut ekran görselleri, logo ve tokenlar aynı; katalog, manifest, metinler ve ilgili devir notları güncellendi.

Bu teslim tasarım ve dosya doğrulamasıdır; gerçek cihazdaki klavye, yükleme/işleme ve native tarih seçicisi testlerinin yapıldığı anlamına gelmez.

## Founder ek kararı — kendi profilinden düzenlemeye geçiş

Profile sekmesinin giriş görünümü kendi profili: `view-own-visible` / `view-own-hidden`. Alt taraftaki `Edit my profile` düğmesi kaldırıldı. Üst sağda kalem, hemen sağında ayarlar dişlisi bulunur. Her hedef 48×48; kalem `form-edit` açar. Erişilebilir adlar mevcut `profileEdit` ve `settings` anahtarlarıdır. Marka işareti x=37 ve 40 birim olarak korunur.

Kullanıcı gizlediği yaş, cinsiyet ve mesleğini kendi profilinde görür; ilgili alanın altındaki kilit işareti ve açıklama yalnız kendisine gösterilir. Başkalarının görünümünde gizli alan tamamen yoktur; boş satır veya gizlilik işareti eklenmez.

| Anahtar | EN | TR |
|---|---|---|
| `profileHiddenToOthers` | Not visible to others | Başkalarına görünmez |

İki own-profile durumu × TR/EN × iOS/Android × %100/%200 = 16 güncellenmiş çizim. Toplam durum sayısı değişmedi.
