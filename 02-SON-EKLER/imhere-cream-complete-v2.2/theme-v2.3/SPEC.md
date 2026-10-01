# Cream & Ink v2.3 — Hafif kabartma

2026-10-01 · Founder onaylı 02 varyantı · Tasarım teslimi

## Kaynak ve öncelik

Founder, üçlü karşılaştırmadaki **02 / Hafif kabartma** görünümünü tüm tema için seçti. Krem/siyah kimlik, Geist ve v10 sıkılaştırma yerleşimi sürer. Bu belge yüzey görünümünü günceller; yeni ürün davranışı tanımlamaz.

1. Ürün davranışı: son Founder/Manager kararları ve ilgili ek spesifikasyonlar.
2. Yerleşim: `compact-v10-v1.0/SPEC.md`; iletişim kartı için `contact-card-v1.1/SPEC.md`.
3. Yüzey: bu belge ve `tokens/theme.tokens.json` **2.3**.
4. Katalog: 299 temel durum / 2.392 SVG. Bu çizimlerin geometri ve metinleri korundu; son eklerdeki yerleşim üstünlüğü devam eder. Örneğin eski SVG'deki geniş düğme, v10'un küçük düğmesini geçersiz kılmaz.

Dosya yolu bilerek `imhere-cream-complete-v2.2/` olarak korunur: Code'un mevcut referansları bozulmaz ve 380 MB paket ikinci kez kopyalanmaz. Geçerli **görsel sürüm 2.3**; eski görünüm Git geçmişindedir. Klasör adındaki 2.2 sürüm önceliği değildir.

## Renk ve derinlik

| Rol | Değer |
|---|---|
| Krem zemin / kabartmalı yüzey / alan | `#F4F1E9` |
| Ana eylem, seçili çip, metin | `#191A17` |
| Siyah yüzey üstü metin | `#FCFAF5` |
| Yardımcı metin | `#696A62` |
| Alan ve etkileşimli kontrol kenarı | `#7C7D73`, 1 dp |
| Dekoratif kart kenarı | `#B7B3A9`, 1 dp |
| Koyu gölge | `#D6D2C8` |
| Açık gölge | `#FFFEFA` |

Gölge, bir kontrolün tek sınırı veya seçili olduğunun tek işareti olamaz. Kenarlar, etiketler ve seçili işaretleri korunur. Logo `brand/README.md` ölçüleriyle kalır.

| Yüzey | Koyu gölge x/y, bulanıklık | Açık gölge x/y, bulanıklık |
|---|---|---|
| Yükseltilmiş | +5/+5, CSS blur 10 / sigma 5 | −5/−5, CSS blur 10 / sigma 5 |
| İçe oturan alan | iç +3/+3, CSS blur 6 / sigma 3 | iç −3/−3, CSS blur 6 / sigma 3 |
| Siyah ana düğme | +4/+4, CSS blur 9 / sigma 4,5; renk `#CFCABE` | −3/−3, CSS blur 8 / sigma 4 |
| Düz | Yok | Yok |

Yayılma sıfır. Değerler metin ölçeğiyle büyütülmez. Flutter'da dış gölge yerleşik `BoxShadow`, iç gölge yerleşik `Canvas/CustomPainter` ile kırpılarak uygulanabilir. **Yeni uygulama bağımlılığı yok.** CSS blur ile Flutter blurRadius eşdeğer kabul edilmez; sigma ve görsel referansla eşleştirilir. Metnin kendisine gölge verilmez; yalnız arkasındaki yüzey çizilir. İç gölgenin üzerine keskin alan kenarı çizilir.

## Bileşenler

| Bileşen | Normal | Basılı / seçili | Pasif / hata |
|---|---|---|---|
| Ana düğme | Siyah, küçük yüzey, ana gölge | Siyah kalır, gölge kalkar | Pasif gölgesiz; mevcut etiket/koşul |
| İkincil düğme | Krem, ince belirgin kenar, hafif kabartma | İç gölge; ölçü değişmez | Pasif gölgesiz |
| Üst çubuk / harita simgesi | 36 görünen yüzey, 22 simge, 48 hedef | İç gölge | Etkin/pasif bilgisi anlamlı etikette |
| Form / mesaj alanı | Krem, iç gölge, 1 dp alan kenarı | Odakta ek 2 dp siyah çizgi, 3 dp açıklık | Mevcut hata satırı korunur; gölge hata işareti değildir |
| Seçim çipi | İnce kenar, küçük hafif yüzey | Siyah + mevcut seçili işareti, gölgesiz | Pasif düz |
| İletişim / bilgi kartı | Krem, hafif kabartma | Bağımsız tıklanabilirlik icat edilmez | Uyarı/sonuç metni aynen |
| Sohbet balonu | Düz; kendi balonu siyah | Yok | Gölge gönderildi/okundu anlamı taşımaz |
| Ayarlar / bağlantı satırı | Düz, ince ayırıcı | Mevcut geri bildirim | Her satır ayrı kabartmalı kutuya dönüşmez |
| Alt menü | Mevcut v10 biçimi + dış hafif gölge | Seçili alan düz, mevcut çizgi/etiket | Yerleşim ve görünürlük koşulları aynı |
| Logo / splash / OS bildirimi / harita renkleri | Düz / mevcut varlık | Yok | Kabartma uygulanmaz |

**Ölçüler:** Görünen küçük düğme yaklaşık 32–36 dp yüksekliğinde; etiket iki satır olduğunda yüzey içerikle uzar. Etkileşim hedefi en az **48×48 dp**, hedefler çakışmaz. Gölge hitbox'a dahil değildir. Eski tam genişlikte düğmeler için ölçü kaynağı v10'dur.

## Ekran grupları

- Giriş, kayıt, parola, doğrulama, başlangıç hataları: alanlar içe oturur; ana eylem siyah, tekrar deneme ikincil kabartmalı. Mevcut hata metinleri ve çıkış yolları korunur.
- Profil: mevcut alan/toggle/çip düzeni. Onaylanan küçük kontrol yüzeyi; tek fotoğraf, gizlilik, görünürlük ve Networking/Friends oranı değişmez.
- Yakındakiler/check-in: mevcut oturum durumları, **I'm still here** ve Stop eylemleri korunur. Kişi kartlarında yalnız yüzey; sahte kişi/mesafe eklenmez.
- Harita: tam alan harita, v10 sağ üst kontrolleri, dört renk aynı; renk katmanına gölge veya kişisel nokta eklenmez. `© OpenStreetMap contributors · OpenFreeMap` menü üstünde ayrı akış satırıdır.
- İstek/eşleşme: iki niyet, boş başlangıç, seçili siyah çip. Seçim yapılmadan kabul etkinleşmez. Bekleyen, cooldown ve bağlantı kuruldu metinleri korunur.
- Sohbet: küçük üst simgeler ve içe oturan composer. Send hedefi 48; sayaç sabit ve Your message'ın 8 dp üstünde. Klavye açıkken alt menü yok. Yazılabilir sohbette saklama satırı yok.
- İletişim kartı: mevcut onay, uyarılar, Received/Sent ve Report; küçük eylemler. Boş **Save etkin**, boş **Send pasif**. Son onaylı davranışın örnekteki uyumsuzluğu giderildi.
- Güvenlik, Ayarlar, bildirim ve Etkinlikler placeholder: mevcut eylemler/durumlar; özel olarak yeni kutu veya işlev eklenmez. Hukuki metinler ve şikâyet kategorileri değişmez.

## Erişilebilirlik ve hareket

- En az 48 hedef; %200 metinde içerik sarılır, ekran gövdesi dikey kayar. Büyük yazıda menü 2×2.
- `prefers-contrast: more` / native yüksek kontrast: gölgeler kaldırılır; açık kenar ve siyah odak çizgisi kalır.
- Şeffaflığı azalt: alt menü opak krem; blur kapanır. Harita atfı her iki durumda okunur.
- Hareketi azalt: basma sırasında yer değiştirme/ölçek yok. H0 hareket zamanlaması, azaltılmış karşılıkları ve sunucu-onayı tetikleme koşulları aynen.
- Yüzey basma geçişi mevcut motion.quick / 150 ms; azaltılmış hareketle anlık. Yeni titreşim veya döngü yok.
- H0 GIF'leri yüzey kataloğu değildir: hareket soyutlamalarıdır; içerik ve zamanlama değişmediğinden yeniden tasarlanmadı. Ekran bileşenleri bu yüzey spesifikasyonundan gelir.

## Metin deltası

`l10n/cream-soft-v23-patch_en.arb` + `_tr.arb`: **yalnız contactCardProfileHelp**. Önceki yardım cümlesindeki kaydetmede zorunlu alan izlenimi kaldırıldı; yalnız kullanıcıya görünür olma anlamı korundu. Bu, Manager'ın `88567c9` kararının tutarlılık düzeltmesidir. Tam ARB üstüne yazılmaz; mevcut anahtar güncellenir. HARBOR gönderim uyarıları birebir aynı.

## Native teslim sınırı

Bu dosyalar tasarım varlıklarıdır. Flutter kodu, derlemeler, sunucu ve mağaza başvuruları bu commit ile güncellenmiş sayılmaz. Code ortak bileşenleri uygular; iOS/Android cihazında gölge kırpılması, klavye, %200 yazı, menü şeffaflığı ve performansı ölçer. Mağaza kareleri yeni native çekimler geldikten sonra güncellenir; mevcut ekran görüntülerinin içi boyanmaz.
