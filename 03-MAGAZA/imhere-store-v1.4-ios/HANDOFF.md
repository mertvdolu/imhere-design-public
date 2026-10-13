# TASARIMCIDAN MANAGERE MESAJ — STORE-IOS-14

**R2 · iPhone seti yeni gündüz çekimleriyle yeniden üretildi. Copy: APPROVED — HARBOR HB-27 + Founder 13 Eki 2026.**

## Teslim

- Uygulama 1.4.0 (19), Cream & Ink v2.3; altı sahne, üç ölçü, 18 opak RGB PNG.
- Konum: `03-MAGAZA/imhere-store-v1.4-ios/`.
- İlk bakış: [ONIZLEME.html](ONIZLEME.html) / [contact sheet](review/iphone-6.9-contact-sheet.png).
- Yükleme adayları: `app-store/iphone-6.9/`, `app-store/iphone-6.5/`, `app-store/iphone-dynamic-island-medium/`.
- Kaynak SVG'ler, üretim betikleri, font lisansı, copy, SHA256 MANIFEST ve doğrulama raporu pakette. Ana altılı setin özeti: [SHA256SUMS-iphone-dynamic-island-medium.txt](SHA256SUMS-iphone-dynamic-island-medium.txt).
- Branch: `design/store-ios-14-v23-r2`. Commit kimliği son teslim mesajında verilir; yerel commit, push yok; geçmiş değiştirilmez.
- 02 başlığı: “See who else is here.”; 05 başlığı: “Events from our team.”. Diğer copy, tasarım ve üretim yolu aynen.

## Native kaynak ve farkların kararı

| Konu | Bu sette yapılan |
|---|---|
| Kaynak | `is/IPHONE19` / `ee077b1`; 1.4.0 (19); iPhone 18 Pro Simülatör, iOS27.0, en_GB; `kosu-20261013-073348`, kayıt 13 Ekim 07:38 +03. Altı SHA256 eşleşti; `app/`, `fcb3a1c` ile bayt-aynı (Git ağaç kimlikleri eşit). |
| 02 Networking | Gerçek **Networking** çipi korundu. Görsel etiket “Here for Networking” yapılmadı. |
| Portre | 02/04 yuvaları R1 ile piksel düzeyinde aynı; koordinatlar değişmedi. Maya yalnız bu iki yuvada. 03'te fotoğraf yuvası yok: yeni yuva çizilmedi. |
| 04 sohbet | Üç görünür mesaj korunur. Dördüncü mesaj kadraj dışında; ekran kaydırılmadı, mesaj eklenmedi. |
| 05 etkinlik | İzin verilen etkinliğin yerel kopyası; native kapak yer tutucusu korunur. Interested/Going'nin alt sınırını alt menü örttüğü kaynak kadraj da aynen kalır; düğmeler taşınmadı. About gövdesi görünmüyor. |
| 06 harita | Bir kademe yakın yeni native kadraj; dört renk, kontroller, native `© OpenStreetMap contributors · OpenFreeMap` ve dış `© OpenMapTiles` korunur. |
| Saat | Gerçek native çekim saati: 02'de 07:36 / Ends at 8:06 AM / 30 min left; 06'da 07:38 / Activity snapshot: 7:38 AM. Saatler boyanmadı. |
| Çekim kaydı | Yeni CEKIM-KAYDI.txt ve altı PNG esas. Eski BENIOKU, `source/evidence/r1/` altında tarihsel kanıt; güncel çekim kaydı değil. |

## İnceleme / sonraki adım

HARBOR HB-27 + Founder copy onayı [COPY-REVIEW.md](COPY-REVIEW.md) içinde kaydedildi. “Fictional profiles · Illustrative content” tüm karelerde görünür. Bu teslim uygulama ARB'lerini veya ürün davranışını değiştirmez.

Görseller App Store Connect'e yüklenmedi. Native kadraj farkları bu görsel çalışmasında düzeltilmiş gibi sunulmaz; 05 için daha açık bir alt kadraj istenirse Code'un yeni native çekimi aynı üretim yoluna alınabilir. Yeni çekim mevcut teslimin üretilmesini engellemez.

**Play:** Android kaynakları hazırlanıyor; Play çıktıları henüz üretilmedi. Ayrı klasörün [hazırlık notu](../imhere-store-v1.4-play/NATIVE-CAPTURE-REQUEST.md) mevcut. iOS karelerinden Android arayüz türetilmeyecek.
