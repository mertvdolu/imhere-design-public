# Google Play1.4 — Doğrulama

13 Ekim2026. Bu rapor görsel dosya doğrulamasıdır; native cihaz testi veya Google Play kabulü değildir.

## Otomatik — PASS

- 6/6 kaynak PNG, çekim kaydı SHA256 eşleşmesi; 1080×2400.
- 6/6 telefon çıktısı1080×1920 +1 feature1024×500; tamamı PNG/RGB/sRGB, alfa yok.
- 7 SVG'deki8 native gömme orijinal kaynak SHA256 ile aynı; tam kadraj ve tek oranlı ölçek. Native üzerinde kırpma/filtre yok.
- Portre yalnız02/04; feature graphic aynı iki sahneyi kullanır. Konumlar ayrı dosyada, orijinal PNG değişmez.
- Dış başlıkların tamamı≤5 kelime; alternatif metinler≤140 karakter; metin ölçümüyle taşma yok.
- Başlık kontrastı15.49:1; yardımcı/alt metin4.85:1. Native UI kontrastı bu çalışmada yeniden onaylanmış sayılmaz.
- Telefonlarda native alan%52.81; başlık bölgesi%12.24. Kaynaklar/donanım öğeleri Android'e ait.

Kanıt: `evidence/export-validation.json`, `evidence/artwork-validation.json`. `source/validate.py` yeniden çalıştırılabilir.

## Görsel kontrol

Altı native kaynak, contact sheet, öne çıkan görsel ve 02 çıktısı açılarak kontrol edildi. Başlıklar iki satır, portreler yerinde; harita dört rengi ve atfı görünür. Sohbette dört mesaj görünür. Etkinlikteki alt açıklamanın menü arkasına uzanması kaynaktadır; müdahale edilmedi.

HTML önizleme kontrolü `evidence/browser-review.json` içinde kaydedilir. MANIFEST bütün dosyaların SHA256 değerlerini; SHA256SUMS.txt yedi yükleme adayını listeler.

## Sınır

Copy ve yeni feature graphic, son HARBOR + Founder Play onayını bekler. Store yayını/yüklemesi yapılmadı. Örnek etkinlik geçmiş tarihe dönüştüğünde native çekim yenilenmelidir; görsel üzerinde tarih değiştirilmez.
