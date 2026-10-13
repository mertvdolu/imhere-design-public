# TASARIMCIDAN MANAGERE MESAJ — Google Play 1.4

STORE-IOS-14 EK1 görsel teslimi hazır.

- Dal: `design/store-play-14-v23`. Yerel commit kimliği son teslim mesajında; push yok.
- Konum: `03-MAGAZA/imhere-store-v1.4-play/`.
- `google-play/phone/`: 01-purpose, 02-nearby, 03-request-profile, 04-chat, 05-event-detail, 06-area-activity — her biri1080×1920, opak RGB PNG.
- `google-play/feature-graphic.png`: 1024×500, opak RGB PNG.
- [Önizleme](ONIZLEME.html), [contact sheet](review/contact-sheet.png), [copy](COPY-REVIEW.md), [SPEC](SPEC.md), [kontroller](VALIDATION.md), [SHA256](SHA256SUMS.txt) ve MANIFEST birlikte.

## Kaynak / korunmuş farklar

Altı Android kaynağı `kosu-20261013-080310`, kayıt13 Ekim08:08 +03, commit28880d1c, 1.4.0(19), API36/Pixel7, en_GB. Kaynak SHA256'ları doğrulandı; native PNG'ler değişmeden kopyalandı. Durum çubuğu gerçek saat, Android hareket çubuğu görünür. Maya/Alex kurmaca; Maya yalnız 02/04'teki var olan fotoğraf yuvalarında.

02'de Networking çipi uygulamadaki gibi. 03'te portre yuvası yok. 04'te dört mesaj görünür. 05'te kapak yer tutucu, Interested/Going görünür; daha aşağıdaki açıklama native alt menünün arkasına uzanır. 06'nın dört rengi, OpenStreetMap/OpenFreeMap atfı ve dış OpenMapTiles kredisi korunur. Uygulama arayüzü yeniden çizilmedi.

## Onay ve aktarım

Telefon başlıkları iPhone R2 ile aynı; iOS için HB-27 + Founder onayı kaynak olarak kayıtlıdır. Play kullanımı ve yeni feature graphic: **DRAFT — HARBOR + FOUNDER PLAY COPY APPROVAL REQUIRED**. Son onay sonrası bu yedi PNG mağaza alanlarına yerleştirilebilir. Bu çalışma mağazaya yükleme yapmadı.

Uygulama/ARB/token/ürün davranışı ve iPhone R2 dosyaları değişmedi. Önceki Play1.2 seti tarihçe olarak korunur. Code bu yerel commit'i mevcut yöntemle taşıyabilir.
