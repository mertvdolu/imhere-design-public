# EMAIL-01 — tasarım spesifikasyonu v1.0

12 Ekim 2026 · Cream & Ink v2.3 / Hafif kabartma · yalnız EN-GB.

**Görsel tasarım teslimi. Copy PROPOSED — HARBOR + FOUNDER COPY APPROVAL REQUIRED.** Gönderim altyapısı ve son HTML Code'dadır.

## 1. Tasarım kararı

Tek sütun; mevcut iki daireli işaret + canlı metin olarak I'M HERE. Büyük, sola hizalı başlık; kısa gövde; tek kompakt ana eylem. Son kullanma ve kopyalanabilir URL, eylemin hemen altında. Ayrı sakin güvenlik notu, sonrasında neden alındığı + Help / Privacy + London footer. Ek kahraman görseli, resim içine yazı, pazarlama alanı veya ikon ailesi yok.

İşaret düz kalır. Hafif kabartma yalnız açık mod ana düğmesinde dekoratiftir; düz yedek de tam anlaşılır. E04 aynı ağırlıkta, tehlike kırmızısı yok. E-postanın tamamı doğal yükseklikte; viewport'a sığdırmak için metin küçültülmez.

## 2. Renkler

| Rol | Açık | Koyu |
|---|---|---|
| İçerik zemini | #F4F1E9 | #191A17 |
| Başlık/gövde/link | #191A17 | #FCFAF5 |
| Yardımcı/footer metni | #696A62 | #B7B3A9 |
| Ana eylem | #191A17 | #F4F1E9 |
| Eylem yazısı | #FCFAF5 | #191A17 |
| Dekoratif ayırıcı | #B7B3A9 | #7C7D73 |
| Logo işareti | #14161A (mevcut marka kaynağı) | #F4F1E9 |

Tümü mevcut v2.3/brand paletidir; mobil uygulamaya yeni koyu tema/token ailesi eklenmez. Gölge metin/sınır yerine geçmez. Kontrast hesapları VALIDATION.md'de. AA kontrolü bu belirlenmiş çiftler içindir; istemcinin zorunlu renk dönüşümü ayrıca ölçülür.

## 3. Ölçü ve tipografi

| Öğe | 375 px | 600 px |
|---|---|---|
| E-posta sütunu | 375, akışkan | üst sınır600 |
| İç yatay boşluk | 24 | 40 |
| Üst boşluk | 32 | 32 |
| Logo | 72×46; gerçek geometri oranı korunmuş | aynı |
| İşaret–canlı marka yazısı | 16 | 16 |
| Canlı marka yazısı | 22/600, 1.2 | aynı |
| Logo sonrası ayırıcı | üst28 / alt32 | aynı |
| Başlık | 34/600, 1.12; harf aralığı −1.1 | 40/600, 1.12; −1.3 |
| Gövde | 17/400, 1.6 | aynı |
| Güvenlik/süre/URL/footer | 16/400, 1.5–1.6 | aynı |
| Düğme | 16/600, 24 satır; 12×24 dolgu; en az48 yükseklik | aynı |
| Başlık → gövde | 24 | 24 |
| Gövde → CTA | 28 | 28 |
| CTA → süre | 16 | 16 |
| Süre → düz URL açıklaması | 28 | 28 |
| Link açıklaması → URL | 10 | 10 |
| Link alanı → güvenlik ayırıcısı | 28 | 28 |
| Güvenlik alanı | üst24 / alt28 | aynı |
| Footer | üst24 / alt32 | aynı |

Font sırası: `Geist, "Helvetica Neue", Arial, sans-serif`. Ana PNG'ler **Geist olmadan**, Helvetica Neue / Arial yığınıyla üretildi. Arial ve isteğe bağlı Geist ayrıca kontrol edilir. E-postanın çalışması web fontuna bağlı değildir; gönderilen pakete font gömmek gerekmez. Sentetik kalınlık nedeniyle satır kırılımları istemciye göre değişebilir; sabit başlık/satır yüksekliği ile kırpma yapma.

Düğme tam genişlik zorunlu değil; içerik genişliğinde ve üst sınır100%. Uzun etiket iki satıra sarılır, yükseklik büyür. 48 px minimum, 44 px brif sınırını karşılar. Köşe yarıçapı100 (pill); Outlook yedeğinde köşeli ve gölgesiz kabul. Açık ana eylem gölgesi: +4/+4 blur9 #CFCABE, −3/−3 blur8 #FFFEFA. Koyu modda gölge yok.

## 4. Logo varlıkları

Tek kaynak: `../02-SON-EKLER/imhere-cream-complete-v2.2/brand/README.md` ve `assets/imhere-mark-icon-weight.svg`. Daire merkezleri, stroke5.8, kesişim ve oranlar değişmedi. 144×92 tuvalde yalnız düşey0.34 boşluk eklendi; görüntü72×46.

`assets/logo-on-light.svg` + `logo-on-light@2x.png`; `logo-on-dark.svg` + `logo-on-dark@2x.png`. PNG144×92, saydam. Alt metin tam `I'M HERE`. Logo işaretinin yanında marka adı HTML metnidir; kelimeler PNG/SVG içine çizilmedi.

Koyu krem varyant, bu brifin açık isteğiyle **yalnız e-posta koyu zemini** için türetildi. Eski notification beyaz maske dosyası kaynak alınmadı; mobil logo/brand README politikası değiştirilmedi. En az12 px işaret çevresinde boşluk; kabartma, perspektif veya bozulma yok. Görseller kapalıyken alt metin + canlı marka adı ve bütün eylemler kalır.

PNG istemci teslimi için, SVG tasarım kaynağı için. SVG'nin e-posta istemcilerinde zorunlu çalışacağı varsayılmaz. Her e-posta tek logo gösterir; koyu/açık kaynak dosyalarının toplamı dahi 40 KB sınırının altındadır (MANIFEST).

## 5. Koyu mod ve basit yedek

- Tasarlanmış koyu hâl: aynı içerik ve aralıklar, yukarıdaki ters palet. Krem işaret ve krem CTA; metin resme dönüşmez.
- Apple Mail için `color-scheme: light dark` + `prefers-color-scheme` yönü; son CSS Code tarafından uygulanır/test edilir. [WebKit açıklaması](https://webkit.org/blog/8840/dark-mode-support-in-webkit/).
- Gmail'in resmi CSS listesinde ekran genişliği sorguları var; tüm koyu mod stratejisinin tek bir medya sorgusuyla çalışacağı varsayılmaz. Desteklenmeyen CSS yok sayılabilir. [Gmail CSS desteği](https://developers.google.com/workspace/gmail/design/css).
- Otomatik renk tersleme/partial inversion, tasarlanmış koyu PNG ile aynı test değildir. Logo değişmezken arka plan değişirse işaret görünmez kalmamalı; gerekiyorsa Code mevcut krem zeminli logo taşıyıcısını koruyabilir. Yeni marka rengi üretme. Görünür canlı wordmark yedeği her hâlde kalır.
- Outlook masaüstü için temel görünüm: açık krem/ink, tek tablo sütunu, gerçek metin, solid CTA; radius/gölge kaybı kabul. Koyu kaynak değişimi desteklenmiyorsa iki logo birlikte gösterilmez. Bu teslim Outlook render'ı doğrulamış sayılmaz.

## 6. Erişilebilirlik ve uzun içerik

E-posta `lang=en-GB`; bir H1, paragraflar ve anlamlı link metinleri. Yerleşim tabloları `role=presentation`; bütün metin canlıdır. Eylem gerçek bağlantıdır (form/button gönderimi değil). Ana eylem etiketi işi söyler; gizli, farklı bir erişilebilir isim eklenmez.

Kopyalanabilir URL tam görünür, seçilebilir; üç nokta/maskeleme ile işlem bağlantısı kesilmez. Uzun URL görsel satırlara sarılır; URL'ye boşluk, soft hyphen veya görünmez karakter eklenmez. Düğme href'i ile fallback href/metni aynı eylemi kullanır. `EMAIL`/`NEW_EMAIL` uzun olsa da gövde kırılır; satır yüksekliği sabitlenmez.

%200 örnekte marka yan yana sığmıyorsa alt alta, düğme gerektiğinde satır kırar; alt bölüm doğal akışta uzar. Gövde ve footer en az16 px. Fotoğraf, hareket, arka plan resmi ve takip pikseli eklenmedi.

## 7. Metin / karar kapıları

Brifin tüm verilen metinleri `copy.md` ve `copy.proposed.json` içinde aynen. E03/E04 preheader, ortak fallback açıklaması ve E04 güvenlik satırı ayrı öneri. E03/E04 süre satırı brifteki ortak cümleden tekrar kullanılır; gerçek süre bilinmiyor.

E04'te yeni adresin tam/maskeli gösterimi ve maskeleme algoritması HARBOR kararını bekler. Çizimde kurmaca alex@example.com var; uzun ve maskeli test örnekleri ayrıca bulunur. Help/Privacy için canlı URL tahmin edilmedi. Sender adresi veya Reply-to kararı üretilmedi.

`I'M HERE` bu brifin e-posta yazımıdır. Önceki Firebase copy dosyaları tarihsel kalır; burada yeniden yazılmaz. Son metin ve gerçek HTML Code/HARBOR/Founder kapısından geçmeden yayımlanmaz.
