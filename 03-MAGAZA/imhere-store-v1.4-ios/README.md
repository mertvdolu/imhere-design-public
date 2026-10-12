# STORE-IOS-14 — iPhone mağaza görselleri 1.4

**Görsel üretimi tamam · Pazarlama copy'si TASLAK — HARBOR + Founder onayı bekliyor.**

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

Yalnız `app-store/` altındaki PNG'ler mağaza yükleme adayıdır. `review/`, `source/` ve HTML mağazaya yüklenmez. iPad / Android ekranı bu pakette yok. Copy onayı ve yayın işlemi bu teslimle yapılmış sayılmaz.

## Kaynak gerçeği

Kaynak: `is/IPHONE19` / `fcb3a1c`; iPhone 18 Pro Simülatör, iOS 27.0, en_GB, normal yazı, 09:41; kurmaca Maya/Alex ve yerel `demo-imhere`. Altı orijinal PNG'nin SHA256'sı Code çekim kaydıyla eşleşir. Native arayüzün tamamı oranı korunarak kullanıldı.

İki mevcut fotoğraf yuvasına aynı sentetik Maya portresi yerleşti (02 / 04). İstek profilinde fotoğraf yuvası olmadığı için 03 portresizdir. Networking çipi gerçek native metninde kaldı; sohbetin kadraj dışındaki mesajı eklenmedi; etkinlik kapağının native yer tutucusu korunur. Haritanın native atfı görünür, ayrıca dış kompozisyonda `© OpenMapTiles` kredisi bulunur.

Android çekimleri henüz teslim edilmedi: [Play hazırlık notu](../imhere-store-v1.4-play/NATIVE-CAPTURE-REQUEST.md). Play seti iPhone'dan sonra hazırlanacak.
