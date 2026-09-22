# 02 — §7 metin hizalaması
Kaynak: `references/design-handoff-section-7.md`; mevcut mühendislik handoff'undan bölüm alıntısı. Master belge okunmadı. Kopya kaynak yolu ve SHA-256 `references/source.json` içindedir.

| Anahtar | TR | EN | İşlem |
|---|---|---|---|
| `pendingSlots` | `{used}/{max} bekleyen istek` | `{used}/{max} pending requests` | Mevcut anahtar + metadata güncelle |
| `profileAgeYears` | `{age} yaşında` | `{age} years old` | §7 kanonik yeni anahtar |
| `requestCooldown` | Şu an bu kişiye istek gönderilemiyor. | You can’t send a request to this person right now. | §7 kanonik yeni anahtar |
| `requestAlreadyPending` | Bu kişiyle bekleyen bir istek var. | There’s a pending request between you and this person. | Bu ekteki yeni UI adı; §7'den gelmedi |
| `requestAlreadyConnected` | Zaten bağlantıdasınız. | You’re already connected. | Bu ekteki yeni UI adı; §7'den gelmedi |

İlk üç metin mühendislikteki karşılıklarıyla birebir. Son iki NOT LOCKED UI metni kullanıcının istediği görsel durumlar için eklendi. `requestPending` / Yanıt bekleniyor ve `matchTitle` / Artık bağlantıdasınız küresel olarak değiştirilmez; kabul ekranının anlamı korunur.

## Parametreler
`used:int` kullanıcının güncel etkin giden bekleyen sayısı; `max:int` mevcut `contracts/founder-constants.json` → `limits.OUTGOING_PENDING_MAX`. Okunan sözleşmede 20; görsellerde 19/20 ve 20/20. Çeviri artık 20'yi sabitlemez; üst sınırı tasarım değiştirmez. Bu sayı mesaj hakkı, bakiye, satın alınabilir slot veya günlük kota değildir.

`age:int` erişime izin verilen profilin yaşı; örnek 28. Formdaki doğum tarihini dışarı açmaz. Gizlenen yaş için `profileAgeYears` hiç oluşturulmaz. Yaş sayımı/yuvarlama/zaman dilimi algoritması bu tasarımın kapsamı değil.

## Birleştirme sırası
1. İki dilde yalnız `v1.7.1-patch_*.arb` alanlarını anlamsal birleştir. `app_*.arb` tam referans dosyalarını canlı dosyaların üzerine yazma.
2. M06'da zaten olan üç canonical anahtarın değer/metadata'sını doğrula; aynı adla ikinci tanım üretme. Yeni iki durum anahtarını ekle. Önceki migration alias'ları ve v1.8/app-only anahtarlar kalır.
3. `pendingSlots` metadata'sında hem used hem max int. Lokalizasyon üretimi ve tüm çağrıların yeni imzaya geçişi birlikte: Mesajlar giden liste, bekleyen ayrıntısı ve dolu durum dahil. `max` mevcut sabitten, label parse ederek değil. `pendingSlots(used, max)` çağrısının gerçek üretilen parametre sırasını metadata/generated API ile doğrula.
4. Görünen profil yaşındaki sabit fixture metnini `profileAgeYears(age)` ile bağla. Gizli/null alanı çağırma. Mevcut submit/intent/route davranışını bu metin birleştirmesiyle değiştirme.
5. `requestClosed` / “Bu istek sona erdi.” aynen kalır; reddedilme ile engel/hesap sonlanmasını neden gösteren ayrı kartlara ayırma (FD-79). Eski `requestUnavailable` metnini global alias'la ezme; mevcut uygun bağlamı korunur.

400 v1.7 anahtarından yalnız `pendingSlots` metni/metadata'sı değişti; 399'u aynı. 4 ek anahtar ile bu ekin tam referansı 404. v1.8'deki 452 üzerine uygulandığında 456 tasarım anahtarı; app-only anahtar varsa canlı toplam farklı olabilir. Token, font ve diğer ürün davranışları değişmedi.
