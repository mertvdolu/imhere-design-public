# ERT-098 — Hesap durumu bilgi ekranı v1.0

2026-10-06 · Cream & Ink v2.3 / 02 — Hafif kabartma · Tasarım teslimi

## 1. Tek şablon, iki içerik

`DELETION_PENDING` ve `ACCESS_DISABLED` aynı zemin, başlık, gövde ve eylem bölgesini kullanır. Başlık/gövde üstten başlar; eylemler güvenli alanın üzerinde altta kalır. İkinci varyantta yalnız kopyalama eylemi ve başarılı kopyalamadan sonra mevcut bilgi satırı eklenir. Görsel önem, renk ve tipografi değişmez.

- `DELETION_PENDING`: yalnız **Sign out / Çıkış yap**, etkin birincil düğme.
- `ACCESS_DISABLED`: **Sign out / Çıkış yap** birincil; hemen altında **Copy email address / E-postayı kopyala** ikincil.
- Geri oku, alt menü, profil/ayar girişi, logo, durum ikonu, iptal/geri alma, neden/kategori, tarih veya sayaç yok.
- Silmenin tamamlandığına dair yeni ifade veya görsel yok. Onaylı gövdedeki mesaj silinmesi açıklaması aynen korunur.

## 2. Ölçü ve bileşen eşlemesi

Tüm değerler mantıksal dp/px; PNG'ler 2× çıktı. Yerleşim için v10, yüzey için v2.3 kullanılır; yeni ortak token veya bileşen ailesi eklenmez.

| Öğe | Kaynak / ölçü |
|---|---|
| Ekran | v2.3 düz krem zemin `#F4F1E9`; opak |
| Güvenli alan | Gerçek cihazın SafeArea değerleri; örnek PNG 390×844, üst 59 / alt 34 |
| İçerik | Yan 24; güvenli alan sonrası üst 32; gövde bölgesi alt 24 |
| Başlık | Mevcut kompakt başlık: Geist Medium, 28 / 500, satır yüksekliği 1,15; harf aralığı −0,7; ink `#191A17` |
| Başlık → gövde | 24 |
| Gövde | Mevcut body: Geist Regular, 16 / 400, satır yüksekliği 1,6; ink `#191A17`; sola hizalı |
| Eylem bölgesi | Yan 24, üst/alt 16; güvenli alanın içinde; düğme hedefleri arasında 8 |
| Birincil | v10 kompakt düğme + v2.3 siyah ana düğme yüzeyi; içerik genişliği; sola hizalı |
| İkincil | v10 kompakt düğme + v2.3 kabartmalı krem yüzey; 1 dp `#7C7D73` kenar |
| Düğme etiketi | Geist Medium, 14 / 500, satır yüksekliği 1,4; birincilde `#FCFAF5`, ikincilde ink |
| Düğme geometrisi | En az 48×48 hedef; görünen yüzey yaklaşık 36 yüksek; yatay iç boşluk 15 + 1 kenar, dikey 7 + 1 kenar; mevcut pill yarıçapı |
| Kopyalandı | Contact us içindeki `ImHereNoticeRow` deseni; mevcut onay işareti, body 16; simge/metin arası 8; ikincil hedef sonrası 8 |

Kabartma, gölge renkleri ve basılı hâller [v2.3 SPEC](../02-SON-EKLER/imhere-cream-complete-v2.2/theme-v2.3/SPEC.md) ile aynıdır. Gölge hedef alanına dahil değildir. Normal metinde küçük yüzey kullanılır; metin büyüyünce yüzey içerikle uzar.

## 3. %200 ve erişilebilirlik

- Başlık 56, gövde 32, düğme etiketi 28; metin küçültme, üç nokta ve satır sınırı yok. Sabit boşluklar ve gölge değerleri ikiye katlanmaz.
- Başlık ve gövde tek dikey kaydırma alanındadır. Alttaki eylem bölgesi ayrı akış alanı kaplar; metnin üzerine bindirilmez. Metnin sonuna kaydırılarak ulaşılır.
- Düğme metni gerektiğinde sarılır, yükseklik büyür. 320 dp / %200 EN kopyalama düğmesi iki satırdır; hedef yüksekliği 106,375 dp. Çıkış hedefi %200'de 67,1875 dp. Yatay taşma yok.
- Başlık ekran okuyucuda başlık; okuma sırası başlık → gövde → çıkış → varsa kopyala → başarı geri bildirimi. Kopyalama sonucu canlı bilgi satırı olarak duyurulur.
- Gövdedeki `info@useimhere.com` okunabilir ve seçilebilir düz metindir. Metin gerektiğinde sarılır. Bağlantıya dönüştürülmez, `mailto:` yok.
- Yüksek kontrastta mevcut kural: kabartma gölgeleri kalkar, belirgin kontrol kenarı ve odak çizgisi kalır. Zemin zaten opak; Şeffaflığı Azalt için yeni davranış yok.
- Yeni animasyon/titreşim yok. Native basılı yüzey mevcut `motion.quick` / azaltılmış hareket karşılığını kullanır.

## 4. Kopyalama ve eylemler

Contact us ile aynı panoya kopyalama akışı: sabit destek adresi kopyalanır; **yalnız kopyalama başarılıysa** EN `Copied`, TR mevcut `Adres kopyalandı.` satırı görünür. E-posta uygulaması açılmaz. Kopyalama başarısızsa başarı satırı gösterilmez; adres seçilebilir, kopyalama düğmesi yeniden kullanılabilir kalır. Yeni hata metni uydurulmadı.

Başlıktaki durum sunucudan gelen hesap durumudur; tasarım yeni hesap durumu, bekleme süresi veya ek sunucu çağrısı tanımlamaz. Çıkış mevcut `authSignOut` eylemine bağlanır. HTML'de çıkış yalnız önizleme dışındaki notla simüle edilir; gerçek oturum kapatmaz.

## 5. Kilitli metinler

Tüm metinler [copy.locked.json](copy.locked.json) içindedir; HTML için aynı içeriğin `copy.js` kopyası kullanılır. Başlıklar, EN gövdeler, ACCESS_DISABLED TR gövde ve düğmeler Founder brifinden aynen alındı.

DELETION_PENDING TR gövde, `harbor/events-gizlilik-ve-silme-taslak.md` §2 / §5.3 içindeki Founder onaylı metinden aynen alındı. Kaynak özeti ve metin özeti-hash'i [copy-source.json](copy-source.json) içindedir. HARBOR belgesinin tamamı bu teslimde yayımlanmaz.

EN `Copied` ve TR `E-postayı kopyala` bu brifin tam ifadeleridir. Mevcut genel Contact us anahtarlarının farklı wording'i bunların yerine geçirilmez; genel anahtarlar bu teslimle değiştirilmez. Ana ARB'lere birleştirme yapılmadı.

## 6. PNG'ler ve doğrulama sınırı

8 ana görüntü: 2 durum × 2 dil × %100/%200. Ek 8 görüntü: her %200 durum için metin sonu ve bütün metni gösteren uzun çıktı. Ek 2 görüntü: EN/TR kopyalandı geri bildirimi. [Görüntü eşlemesi](SCREEN-STATE-MATRIX.md).

`*-200-full.png` uzun belge çıktısıdır; yeni bir cihaz yüksekliği veya farklı bir native yerleşim değildir. Başlangıç ve `*-end.png` aynı 844 dp ekranın iki kaydırma konumudur.

32 tarayıcı yerleşimi: 320/390 × EN/TR × %100/%200 × iOS/Android örnek güvenli alanı. Başlık semantiği, ≥48 hedefler, düğmelerin ekran içinde kalması, yatay taşma olmaması ve seçilebilir e-posta kontrol edildi. Metin sonuna erişim, kopyalama sonucu ve yüksek kontrast ayrıca kontrol edildi. Gerçek iOS/Android cihaz testi değildir; native entegrasyonda Code gerçek SafeArea, Dynamic Type ve ekran okuyucu akışını ölçer.

## ÖNERİ

Yok. Metin değişikliği veya ek ürün davranışı önerilmiyor.
