# STORE-IOS-14 — iPhone mağaza görselleri 1.4

**R2 · Gündüz çekimiyle üretildi · Copy: APPROVED — HARBOR HB-27 + Founder 13 Eki 2026.**

Cream & Ink v2.3 · Uygulama **1.4.0 (19)** · 6 native sahne × 3 çıktı ölçüsü = **18 PNG**.

- [HTML önizleme](ONIZLEME.html)
- [Altı karenin genel görünümü](review/iphone-6.9-contact-sheet.png)
- [Manager / Code teslim notu](HANDOFF.md)
- [Copy incelemesi](COPY-REVIEW.md)
- [Ölçü ve üretim notu](SPEC.md)
- [Doğrulama](VALIDATION.md)
- [Dosya / ölçü / SHA256 listesi](MANIFEST.json)

## Mağazaya alınacak klasörler

| Klasör | Ölçü | Adet |
|---|---|---|
| [iphone-6.9](app-store/iphone-6.9/) | 1320×2868 | 6 |
| [iphone-6.5](app-store/iphone-6.5/) | 1242×2688 | 6 |
| [iphone-dynamic-island-medium](app-store/iphone-dynamic-island-medium/) | 1206×2622 | 6 |

Yalnız `app-store/` altındaki PNG'ler mağaza yükleme adayıdır. `review/`, `source/` ve HTML mağazaya yüklenmez. iPad / Android ekranı bu pakette yok. Copy onayı Founder'ın STORE-IOS-14 R2 mesajıyla kayda alındı; mağazaya yükleme/yayın yapılmadı.

## Kaynak gerçeği

Kaynak: `is/IPHONE19` / `ee077b1`; iPhone 18 Pro Simülatör, iOS 27.0, en_GB, normal yazı; 13 Ekim 2026 sabah çekimi (`kosu-20261013-073348`, kayıt 07:38 +03). Durum çubuğu gerçek çekim saatini gösterir: 02'de 07:36 / Ends at 8:06 AM, 06'da 07:38 / Activity snapshot: 7:38 AM. Kurmaca Maya/Alex, yerel `demo-imhere`. Altı SHA256 Code kaydıyla eşleşir; `app/`, `fcb3a1c` ile bayt-aynıdır (Git ağaç kimlikleri doğrulandı). Native arayüz tam kadraj ve oranı korunarak kullanıldı.

İki mevcut fotoğraf yuvasına aynı sentetik Maya portresi yerleşti (02 / 04). İstek profilinde fotoğraf yuvası olmadığı için 03 portresizdir. Networking çipi gerçek native metninde kaldı; sohbetin kadraj dışındaki mesajı eklenmedi; etkinlik kapağının native yer tutucusu korunur. Haritanın native atfı görünür, ayrıca dış kompozisyonda `© OpenMapTiles` kredisi bulunur.

R2'de yalnız iki başlık değişti: **See who else is here.** / **Events from our team.** Diğer dört başlık, alt satır, marka yazımı, kompozisyon ve portre koordinatları aynı. Haritanın yeni native yakınlığı korunur.

Android çekimleri henüz teslim edilmedi: [Play hazırlık notu](../imhere-store-v1.4-play/NATIVE-CAPTURE-REQUEST.md). Play seti iPhone'dan sonra hazırlanacak.
