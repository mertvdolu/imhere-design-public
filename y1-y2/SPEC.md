# Y1 / Y2 — Yerleşim ve davranış eşlemesi v1.0

**Cream & Ink v2.3 / 02 — Hafif kabartma.** Tasarım eki; uygulama, sunucu veya yayın teslimi değildir.

**Metin durumu: PROPOSED — HARBOR COPY REVIEW REQUIRED.** Founder brifindeki İngilizce taslaklar aynen kullanıldı. TR çeviriler, alan/hata/erişilebilirlik etiketleri ve Accepted açıklaması öneridir. `COPY-REVIEW.md` kaynak ayrımını gösterir. Ana ARB üzerine yazılmaz.

## 1. Kaynak ve bileşenler

- Founder'ın bu işteki kapsamı ve `ops/Y1-Y2-KARAR-PAKETI.md` esas. Kaynak karar tarihi ve teslim tarihi 7 Ekim 2026.
- `../02-SON-EKLER/imhere-events-v1.0/style.css`: mevcut Events kabuğu, kart, sekmeler, durum satırı, kompakt ana/ikincil kontrol, boş/yükleme hâli.
- `../02-SON-EKLER/imhere-cream-complete-v2.2/theme-v2.3/SPEC.md`: yüzey kuralları. `compact-v10-v1.0` sıkı yerleşim önceliği korunur.
- Yeni bileşen/ikon/renk ailesi yok: mevcut seçim çipi tek-seçimli radyo semantiğiyle, mevcut kategori satırı pasif amaç rozeti olarak, mevcut tam ekran onay yerleşimi farklı-amaç uyarısı olarak kullanıldı.
- Networking işareti Events'in çakışan iki çemberi; Friendship mevcut sohbet balonu. Metin her zaman görünür; ikon dekoratif. Haritanın dört yoğunluk rengi kullanılmaz ve değiştirilmez.

## 2. Ortak ölçüler

| Öğe | Ölçü / rol |
|---|---|
| Zemin / metin | `#F4F1E9` / `#191A17`; ikincil `#696A62`; ana eylem üstü `#FCFAF5` |
| Etkileşim kenarı / ayırıcı | `#7C7D73` / `#D9D5CB`; ayırıcı tek başına kontrol sınırı değildir |
| Yükseltilmiş yüzey | 5/5/10 `#D6D2C8`, −5/−5/10 `#FFFEFA`; mevcut v2.3 |
| Alan | radius12, 1px kenar, iç gölge3/3/6; yatay14/dikey12; min48 yükseklik |
| Sayfa | içerik kenarı24; başlık altı20; bölüm/alan arası24 |
| Başlık | Geist Medium 28 / 1.15; 200%: 56 |
| Bölüm / kişi adı | Geist Medium18 / 1.4 |
| Gövde | Geist Regular16 / 1.6 |
| Alan etiketi / kontrol | Geist Medium14 / 1.4 |
| Yardım / hata | Geist Regular14 / 1.5; hata kenarı2px ink; tehlike kırmızısı yok |
| Sayaç / rozet | 12 / 1.5; 200%: 24 |
| Dokunma | en az 48×48; görsel hap küçük olabilir, görünmeyen hedef küçülmez |
| Amaç rozeti | mevcut kategori/sınırlı yüzey: radius12, 1px kenar, padding4/8, ikon16, gap6; pasif |
| Seçim / eylem grubu | gap8, gerektiğinde sarılır; 200%'de dikey; seçili yüzey ink + açık yazı + radyo işareti |
| Alt menü | mevcut v10: edge16/radius26/inner4/label12; dört sekme; 200%'de 2×2, kenar8 |

Metin rollerinin boyutu iki katına çıkar, satır sayısı veya yüksekliği kilitlenmez. Ana içerik kayar; menü yüksekliği ayrı ayrılır. Düğmeler içeriğin sonunda kaydırılarak erişilir; metni kırpıp düğmeleri zorla aynı ekrana sıkıştırma. Tam ekran amaç/uyarı/sonuçta alt menü yok. Kurulum, klavye ve tam ekran onay istisnaları önceki teslimdeki gibidir. Native formda klavye açıkken alt menü gizlenir; ekran, odaklı alan ve gönderim eylemine kayabilmelidir.

Yüksek kontrastta gölge kalkar, kontrol kenarı korunur. Şeffaflığı Azalt: opak menü. Hareketi Azalt: dekoratif geçiş yok; mevcut işlevsel yükleme göstergesi devam eder. Başlık `h1`/native heading; etiket–alan–hata ilişkisi ve seçili radyo durumu ekran okuyucuda okunur. Sayaç her tuşta canlı bölgeyle anons edilmez.

## 3. Y1 — Events ve öneri formu

### Giriş

Başlık altında tek küçük ikincil **Suggest an event**, yanında/altında sakin **My suggestions** metin eylemi. Kartların içine yeni bir yayın/oluştur düğmesi eklenmez. Boş Events listesinde de bu girişler vardır. Bu tasarım gerçek Events sürümüne aittir; geçici gizli Events sekmesini kendi başına açma talimatı değildir.

### Form

Sıra: başlık → açıklama → kategori → başlangıç → 48 saat yardım satırı → bitiş → mekân adı → adres → günlük sınır yardımı → gönder. Görsel alanı yok. Kategoriler tek seçim; boş başlangıçta seçim yok.

| Alan | Sınır / kontrol |
|---|---|
| Başlık | 80 grapheme |
| Açıklama | 1000 grapheme; çok satırlı alan |
| Kategori | Networking / Social / Activity |
| Başlangıç | native tarih + saat seçici; en erken sunucunun şimdisinden48 saat sonra |
| Bitiş | native tarih + saat seçici; başlangıçtan sonra |
| Mekân | 120 grapheme |
| Adres | 200 grapheme |

Bu sınırlar mevcut Events doğrulaması ve Founder karar paketinden gelir. Bir birleşik emoji bir karakterdir; UTF-16 uzunluğu kullanılmaz. Sayaç sürekli alan altında sağdadır. Metni otomatik kesmek yerine aşımı ve alan hatasını göster. Boş alan, eksik kategori/tarih ve bitiş eşit/önce durumları ilgili alanın altında ink kenarlı kısa hata alır. Gönder denemesinde ilk hatalı alana odak/kaydırma; girilenler korunur.

Tarih/saat elle yazılmaz. HTML yalnız tarayıcının kendi seçicisini açar; native uygulamada mevcut platform seçicisi kullanılır. Geçmiş tarih ve 48 saatten yakın tarih aynı alan altı en-erken-başlangıç uyarısını kullanır. Sunucu saati, zaman dilimi ve tarih doğrulaması Code sözleşmesinden gelir. HTML'deki 7 Ekim12: 00 London referansı ve 24 Ekim örnekleri kurmaca yerleşim verisidir; gerçek takvim/sunucu doğrulaması değildir.

Gönderim beklerken çift gönderim önlenir; başarı yalnız olumlu sunucu yanıtı sonrası. Hata/çevrimdışında içerik korunur. Formun çevrimdışı çiziminde gönder pasif + Try again kurtulma yolu vardır. Yeniden bağlantıda aynı taslakla devam edilir; çevrimdışı kuyruk özelliği eklenmez. Başarıda **Suggestion sent.** + ekibin inceleyip yayınlamayabileceği taslak satır; My suggestions eylemi.

## 4. Y1 — My suggestions

- **Pending:** geri çekme eylemi yalnız bu durumda.
- **Accepted:** yayın garantisi/published rozeti/etkinliğe katıl düğmesi yok. Öneri ekibin taslağına dönüşebilir; ekip ayrıca yayınlar. Önerilen açıklama: “Acceptance does not mean the event is published.”
- **Not accepted:** neden/şikâyet/kategori açıklaması eklenmez. Nötr durum metni.
- **Boş:** sakin başlık + açıklama + öneri giriş düğmesi.
- **Günlük sınır:** günde 3 bilgisi; yeni gönderim girişi pasif. Pending öneri geri çekilebilir. Geri çekmenin günlük sayacı sıfırladığı söylenmez.
- **Bekleyen sınırı:** aynı anda 3; mevcut Pending satırlar ve Withdraw kalır. Yeni gönderime dönüşü sunucu uygunluk durumu belirler.
- Sayaç sıfırlanma saati, gece yarısı veya kalan süre icat edilmez; iki limit de sunucudan okunur. Form açıkken limit değişirse içerik korunarak ilgili limit metni gösterilir; sessiz başarıya dönülmez.
- Withdraw sırasında satır kalır; başarıdan sonra listeden çıkar. Hata durumunda Pending + tekrar Withdraw. Ayrı onay/geri alma davranışı eklenmedi.
- Liste yükleme/hata/çevrimdışı ayrı durumlar; başarısız/çevrimdışında Try again. Karar bildirimi push, öneren kişinin herkese görünmesi veya ret nedeni yok.

## 5. Y2 — oturum amacı

**I’m here → boş amaç seçimi → tek seçim → Continue → mevcut konum/check-in kapıları → sunucu onayı → aktif Nearby.** Seçim yapılmadan Continue pasif. Cancel oturum başlatmaz. Önceki amaç otomatik seçilmez.

Networking / Friendship seçenekleri aynı görsel ağırlıkta, ince kompakt radyo çipleri. %200'de alt alta. Başarısız check-in aynı seçimle tekrar denenir; başarısızlığı aktif oturum gibi çizme. Konum açıklaması/OS izni/diğer mevcut uygunluk kapıları atlanmaz veya yeniden yazılmaz.

Aktif oturumda mevcut **I’m still here + Stop** korunur; yenileme aynı amaçla. Amaç oturum boyunca sabit; değiştirmek için Stop ve yeni oturum gerekir. Profil Networking/Friends yüzdesi ayrı kalır.

Nearby kişi kartı: mevcut kişi satırında adın altında küçük metin+ikon rozeti. Her iki amaçtan kişiler görünür; rozet filtre veya topluluk ayrımı değildir. Eski amaçsız kayıtta rozet/amaç tahmini yapma; yokluğu mismatch sayma. Bu geçiş sözleşmesini Code yürütür.

## 6. Y2 — istek akışı / farklı amaç

Aynı amaç: mevcut kişi görünümü → **Send a hello** → işlem sürüyor → sunucu olumluysa mevcut bekleyen istek ekranı. Eski istek anındaki friendship/networking/both seçim adımı kaldırılır. Önceden var olan istek engelleri, hesap/güvenlik kontrolleri ve haklar korunur.

`request-sent` PNG'si yalnız **mevcut bekleyen ekrana geçiş anını** gösterir. Bekleyen ekranın mevcut hak sayacı/kalan süre/sonraki işleyişi bu ekte yeniden çizilmedi veya kaldırılmadı; bu sade geçiş karesini tüm bekleyen ekranın yerine uygulama.

Farklı amaç: aynı kişi görünümünden mevcut tam ekran onay şablonuna geç:

1. **Different reason**, {reason} ile tam taslak gövde, **Send anyway / Cancel**. Kırmızı veya korkutucu ikon yok.
2. Cancel → aynı kişi görünümü; istek/görünmezlik başlamaz.
3. Send anyway → bekleme; çift işlem önlenir. İstek gönderildi/check işareti gösterilmez.
4. Yalnız sunucu doğrulayınca **Request not sent. You won't see each other for 10 days.** Sonuç başlığı nötr; Nearby'ye dönüş eylemi.
5. Yanıt doğrulanamıyorsa sonuç/hide başladı iddiası yok; sakin hata ve tekrar deneme. Code aynı işlem sonucunu sunucuyla uzlaştırır; ikinci çağrının yeni bir 10 gün başlatacağı tasarlanmaz.

Görünmezlik bu iki kişi içindir; diğer amaçtaki herkesi gizleme. Canonical kapsam: Nearby, istek yolları/eski gelen istekler, yakınlık bildirimleri. Mevcut sohbet, report/block ve toplu harita yoğunluğu korunur. Süre geri sayımı veya gerekçe ifşası eklenmez.

## 7. Önizleme / PNG okuma

- `ONIZLEME.html`: 40 durum; EN/TR, 100/200%, 320/390/412 genişlik, iOS/Android kabuk örneği; erişilebilirlik seçenekleri.
- `screens/png/<state>--<lang>--<scale>.png`: 390×844 mantıksal alanın2× çıktısı.
- `--full.png`: kaydırılan içeriğin tamamı; uzun belge kanıtı, yeni telefon oranı veya tek ekrana sığma iddiası değil.
- Kurmaca isimler Example A/B / Örnek A/B; gerçek fotoğraf, kimlik, konum veya etkinlik yok. İnceleme etiketi önizleme çevresindedir.
- Önizleme sahne seçimi işlem yapmaz. “Başarılı/Hata yanıtı” araçları telefon dışındadır; canlı veri gönderilmez, görünmezlik uygulanmaz.
- Tarayıcı ölçümü native cihaz/VoiceOver/TalkBack kanıtı değildir. Code iki platformda native seçici, klavye, dinamik metin, odak ve sunucu sonucunu ayrıca doğrular.

## 8. Açık konu / ÖNERİ

Ürün davranışı için yeni öneri yok. Metinlerin nihai HARBOR onayı ve Code anahtar/sözleşme eşlemesi beklenir. Bu onay olmadan proposed ARB'ler canonical ARB'ye birleştirilmez. Yeni bağımlılık, yeni renk veya bileşen ailesi istenmedi.
