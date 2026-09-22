# 05 — Durum envanteri ve platform
| Grup | Durum | SVG | PNG |
|---|---:|---:|---:|
| messages | 10 | 80 | 20 |
| intents | 12 | 96 | 24 |
| requests | 13 | 104 | 26 |
| match | 5 | 40 | 10 |
| chat | 18 | 144 | 36 |
| continue | 14 | 112 | 28 |
| contact | 21 | 168 | 42 |
| Toplam |93|744|186|

SVG'lerin tümü TR/EN, iOS 390×844 / Android 412×915 referans cihaz alanı ve metin ölçeği 1/2 içerir. Artboard yüksekliği tam kaydırma içeriğine göre büyür. PNG örnekleri TR iOS normal + EN Android %200. Ayrıntılı ölçüler/alanlar/aksiyonlar `contracts/screen-manifest.json` içindedir.

## Ortak durumlar
- Bağlantılar ve istek listeleri: dolu, boş, yükleme, hata, offline.
- Gönderme/alıcı niyet seçimi: boş, tek, iki, işlem, hata, offline. Alıcı her yeni kabulde bağımsız boş başlar.
- İstek ayrıntıları: gelen/red işlemi; 19/20 bekleyen; 20/20 sınır; iptal işlemi/hatası; süre doldu/iptal/sona erdi; ters istek; kullanılamıyor.
- Eşleşme: ortak/ortaksız niyet, yükleme/hata/offline.
- Sohbet: boş/aktif/taslak; 500/501; gönderiliyor/kesin hata/belirsiz sonuç; yükleme/hata/offline; 0 hak; yumuşak uyarı ve gönderim durumları; salt okunur/contact/kullanılamıyor.
- Devam: boş karar; kendi EVET'i kayıt/geri alma/sonuç; HAYIR son onay/kayıt/hata/sona erdi; veri yükleme/hata/offline.
- Contact: 0/1/2/4 seçim; alan hatası; paylaşım; kendi ve diğerinin yayınlanmış değerleri; düzenleme; görünürlüğü kaldırma; boş merkez; yükleme/hata/offline/kullanılamıyor.

Bu paket kamera/mikrofon/konum/rehber izni istemez. Dolayısıyla uydurma cihaz permission-denied ekranı eklenmez. Bildirim izni reddi uygulamanın bu bölümlerini kapatmaz; bildirim izin ekranı Paket 4'tedir. İşlem/erişim reddi nötr kullanılamıyor veya ilgili işlem hatasıyla temsil edilir; engellenme nedeni açılmaz.

## Ölçü ve tipografi
Geist 400/500/600, başlık 31, gövde 16, label 14, metadata 12.24 dış dolgu; input iç 16/min 56; CTA min 52; kart 16/input 12/CTA 28 köşe. Tüm aktif hedefler en az 48 logical px. Mevcut token değerleri değişmedi. Niyetin rengi kendi anlamı için; seçili tik ve state renk dışında bilgi sağlar. Balonda yazar/hizalama okuma anlamını korur.

## Büyük metin ve native davranış
%200 çizimler fontu gerçekten 2× uygular; yatay sığmayan kart, kontrol, hata ve buton çok satıra büyür. Mesajlar'ın iki bölüm kontrolü normal metinde yan yana, büyük metinde alt alta yerleşir; dört ana sekme onaylı 2×2 düzenindedir. Native uygulanabilirlik M10'daki yazılım kontrolüne aittir.

Uzun konuşma/forma bir ekrana sığma zorunluluğu getirilmez. Native uygulamada gövde kaydırılır, composer klavye üstünde kalır, focused contact alanı ve hatası `viewInsets`/safe-area ile görünürdür. Girişte gelen sistem klavyesi veya işletim sistemi paylaşım arayüzü yeniden çizilmez. Sistem yazı ölçeği kısılmaz.

## Erişilebilirlik
Bölüm seçicisi seçili sekme anlamı; niyet/contact seçenekleri checkbox; label/değer/hata ilişkilendirilir. Seçilmemiş niyetin arka plan rengi tek sinyal değildir. Mesaj yazarını ekran okuyucu belirtir; geri-al/sil/düzenle gizli aksiyonu yok. Karşı tarafın niyet/karar/mesaj hakkı görünmemesi Semantics için de geçerlidir.

Uyarı açılınca odak başlıkta; Gözden geçir taslak alanına döner. Son onay kapanınca odak onu açan kontrole döner. Başarı/hata bir kez anlamlı anons edilir. Bekleyen istek süresi her saniye live-region olarak bağırmaz; odakla güncel kalan süre duyulur. Chat/continue zamanlayıcısı yok. Reduce Motion'da geçiş hareketi azalır; spinner bilgi metninin yerine geçmez.

## M10 örnekleri
TR İ/ı/ş/ğ, aile/ten rengi emoji ve birleştirici işaret; 500/501 grapheme; çok uzun link; uzun ad; 0 ve 20 hak; 19/20 ve 20/20; eşzamanlı ters istek; yinelenen dokunuş; kabul anında süre dolması; gönderim sonucu belirsizliği; EVET geri alma/mutual yarışı; contact kaydetme/geri çekme hatası; açık ekran sırasında engel. Bunlar çalıştırılmış native test iddiası değildir; yazılım doğrulamasının kapsamını tarif eder.
