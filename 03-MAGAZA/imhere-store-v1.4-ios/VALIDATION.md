# STORE-IOS-14 — Doğrulama

R2 · 13 Ekim 2026 · Görsel teslim kontrolü; App Store kabulü veya native uygulama testi değildir.

## Otomatik kontroller — PASS

- Altı kaynak PNG: **1206×2622**; yeni gündüz CEKIM-KAYDI.txt SHA256 değerleriyle eşleşiyor.
- **18/18** çıktı: doğru ölçü, PNG, RGB, alfa yok. Her klasörde aynı altı sahne.
- **18/18** SVG: gömülü native PNG'nin SHA256'sı kaynağıyla aynı. Native tam kadraj; en/boy oranı korunuyor, native üzerinde kırpma/renk filtresi yok.
- Yalnız 02 ve 04'te yetkili fotoğraf katmanı; her sette iki yuva. 03'e portre alanı eklenmedi.
- Dış başlık/alt notlar font ölçümüyle kompozisyon sınırları içinde. Altı başlığın tamamı en fazla beş kelime.
- Dış metin kontrastları: başlık **15.49:1**, alt not/kredi **4.85:1**. Native arayüzün kontrastları bu testle yeniden onaylanmış sayılmaz.
- R2 kapsam karşılaştırması: 18 SVG'nin tamamında yalnız yeni native bitmap ve onaylı 02/05 başlıkları değişmiş; geometri ve portre yerleşimleri R1 ile aynı. Copy JSON'da yalnız iki başlık/satır kırımı ve onay durumu değişti. Kanıt: [r2-scope-validation.json](evidence/r2-scope-validation.json).
- Kanıt: [export-validation.json](evidence/export-validation.json) ve [artwork-validation.json](evidence/artwork-validation.json).

## Görsel ve HTML kontrolü

- Altı kaynak tek tek açıldı. Üç çıktı setinin contact sheet'leri incelendi: başlık/kare kesilmesi yok; native alt menü, dört renk ve atıf korunuyor; iki Maya portresi yuvada.
- HTML'de üç çıktı ölçüsü seçildi; doğru altı PNG/SVG bağlantısına geçiş doğrulandı. Orijinal native görünüm düğmesi kaynak PNG'lere geçiyor ve geri dönebiliyor.
- Tarayıcıdaki altı ana görsel yüklendi; konsol hata kaydı görülmedi. Gözlenen dar pencere yerleşiminde yatay taşma yok. Bu, tüm tarayıcı/cihazlar için kapsamlı test iddiası değildir.
- Görsel yüklenmeden önce en-boy oranı ayrılarak önizlemede yerleşim sıçraması önlendi.

## Kaynaktan gelen sınırlar / onaylar

- 02'de metin **Networking**, “Here for Networking” değil. Gerçek görüntü korundu.
- 04'te dördüncü mesaj kaynak kadrajın dışında. Final üç görünür mesajı içerir.
- 05'te kapak yer tutucu. Interested/Going etiketleri görünür, düğmelerin alt kenarı native alt menünün arkasında kalır. Yeni kadraj istenirse Code'dan yeniden çekim gerekir; burada yerleşim oynanmadı.
- Yeni kaynak `ee077b1`, çekim kaydı 13 Ekim 07:38 +03; iki kaynak commit’in `app/` ağaç kimliği aynı. 02/04 portre yuvaları R1 ile piksel düzeyinde eşit; konumları değişmedi. Kanıt: source/evidence/portrait-slot-check-r2.json.
- 02: 07:36 / Ends at 8:06 AM; 06: 07:38 / Activity snapshot: 7:38 AM. Native saat pikselleri değiştirilmedi. Eski BENIOKU yalnız source/evidence/r1/ altında tarihsel kayıttır.
- Copy: **APPROVED — HARBOR HB-27 + Founder 13 Eki 2026**. App Store'a yükleme, inceleme/kabul ve üretimdeki etkinlik içeriğinin canlı doğrulaması yapılmadı.
- Android / Play kaynakları bekleniyor; iPhone çıktıları Play teslimi yerine kullanılmaz.
