> **Güncel yüzey dili: Cream & Ink v2.3 / hafif kabartma.** Ölçü ve davranışlar bu belgede; yüzey uygulaması `theme-v2.3/SPEC.md` ve ortak tokenlarda.

# Sıkılaştırma v10 · tasarım eki v1.0

TASARIMCIDAN MANAGERE MESAJ

Bu ek, Cream & Ink v2.2 üzerine yerleşim revizyonudur. Önce/sonra HTML 12 örnek ekran içerir. Eski katalog SVG'leri tarihsel karşılaştırma kaynağıdır; bu teslim bütün 299 durumu yeniden çizmiş sayılmaz. Native uygulama değiştirilmedi. Code aktarımı için yerel commit.

## Kaynak ve öncelik

28 Eylül iş klasörü 0-MESAJ + 2-UYUM-LISTESI; seçilen 24 JPG ve 0-NOTLAR birlikte incelendi. Bu kaynakların hiçbiri depoya alınmadı. Son Manager yanıtı önceki “her ekran” kuralını daraltır:
- Giriş, doğrulama, ilk profil kurulumu: alt menü YOK.
- Kurulum sonrası ana ekranlar ve harita: alt menü VAR. Normal profil/ayar alt sayfalarında da görünür; erişim kuralları değişmez.
- Sohbette klavye açık: alt menü YOK; klavye kapanınca geri gelir.
- Tam ekran onay ve rapor pencereleri: alt menü YOK. İşlem tamamlanmadan sekmeyle çıkış eklenmez.
- Konum: HARBOR metni karakter karakter korunur; yalnız Continue. OS reddetme hakkı değişmez.

## Ölçüler

Geist ve mevcut renk token'ları aynen. Sayfa kenarı24; blok arası24; ilişkili etiket/alan8; liste bölümleri24. Bu düzeni sıkılaştırmak için bütün boşlukları azaltmıyoruz: büyük dolu yüzey ve yinelenen kart çerçevelerini azaltıyoruz.

| Bileşen | Görünür ölçü / davranış | Dokunma |
|---|---|---|
| Küçük ana/ikincil düğme | label14/500/1.4; yatay16/dikey8; içeriğe göre genişlik; pill | en az48×48; görünür boyadan ayrı |
| Next → | label14/500; sağa hizalı, çerçevesiz | en az48×48 |
| Simge |20–24; dairesel yüzey32–36 |48×48; hedefler kesişmez |
| Alan | body16/400/1.6; yatay12/dikey10; min48; inputBorder1 | tam alan; parola göz simgesi48 |
| Liste satırı | min56; dikey10; içerikle büyür; ayırıcı1 | tüm satır |
| Profil avatarı |64; yerleşim örneği | ayrı eylemi yoksa hedef gerekmez |
| Mesaj avatarı |48 | satır hedefinin parçası |
| Başlık | mevcut headline token korunur; örnekte28 yalnız yerleşim varyantı | token delta aşağıda |

28/500/1.15/−0.7 yalnız compactPageTitle token'ı olarak bu ekin parçasıdır; ana36 token'ı değiştirilmez. Diğer başlık18/500, yardımcı14/400. Hukuki içerik body16/400/1.6; “minicik hukuk yazısı” referanstan alınmaz.

## Yüzen menü

Sıra Profile → Messages → Nearby → Events. Kenarlardan16 (büyük metinde8), alttan16 + sistem safe area. Dış radius26, iç aktif alan20; içeride4. Normal dört sütun, her hedef min48×56. Etiket12/400, seçili500 ve2px çizgi; yalnız renk farkına dayanmaz. Büyük metinde etiket12×sistem ölçeği (200% için24) ve2×2; ikon üstte; satır sırası değişmez. Sığmayan yazı sarılır; ölçek küçültülmez.

Yüzey surface#FCFAF5 %94 + arka plan blur sigma16; kenarlık inputBorder#7C7D73. Ink metin. Aktif alan#E9E5DA opak. Sistem Şeffaflığı Azalt: background#F4F1E9 tamamen opak, blur yok. Native sistem bilgisinin mevcut köprüden alınması Code doğrulamasında; desteklenmeyen platformda güvenli varsayılan opak. Yeni bağımlılık eklenmez. Flutter yerleşik BackdropFilter/ClipRRect; blur yalnız menü dikdörtgenine kırpılır. Dekoratif devamlı hareket yok.

Menü yerleşimi görsel olarak yüzer; içerik altına gizlenmez. Scroll alanı gerçek menü yüksekliği+boşluk+safe area kadar inset alır. Harita atfı menünün ÜSTÜNDE ayrı, opak ve metne göre büyüyen satır. Harita ekranında kişisel işaret, sayı, mesafe, yer kartı ve niyet filtresi eklenmez. © OpenStreetMap contributors · OpenFreeMap korunur.

Sohbette sıralama: içerik → composer → menü → safe area. Klavye açık: içerik → composer → OS klavye; menü yok. viewInsets iki kez eklenmez. Büyük yazı ve klavye birlikte: composer gerekirse içeriden kayar; gönder hedefi görünür kalır, mesaj geçmişi kalan alanda kayar. Kaydırma/boş alana dokunma ile mevcut klavye kapatma davranışı korunur. iOS/Android sistem geri kuralları değişmez.

## Akış eşlemesi

### Kayıt ve ilk profil
Davet → e-posta taslağı → parola + mevcut hukuk metni ve48 hedefli bağlantılar → hesap oluşturma/verify → ilk profil. E-posta adımında Next sunucuya hesap oluşturma çağrısı YAPMAZ. Son eylem mevcut authCreateAccount; yeni hesap/kimlik kuralı yok. Mevcut parola kuralı8 karakter, güç göstergesi yok. Hata ilgili alanın altında; genel hata mevcut metniyle; offline taslağı silmez. Doğrulama/davet-tekrar/ilk profil authSignOut korunur. İlk profile geri navigasyon önceki kapıyı atlatmaz.

İlk profil alan sırası: fotoğraf → ad → doğum tarihi+yaş görünürlüğü → cinsiyet+görünürlük → meslek+görünürlük → bio → ilgi alanları → mevcut isteğe bağlı dil alanı → mevcut son kaydetme. Tek soru/ekran görsel bölünmedir; yeni zorunluluk veya yeni sunucu kaydı eklenmez. Alanların mevcut required/optional kararını Code kaynakları belirler. Başka mevcut alanlar (oran/iletişim gibi) kaldırılmaz; mevcut yerlerinde aynı bileşen ölçüsü uygulanır, yeni zorunluluk getirilmez.

Doğum tarihi native picker; cinsiyet mevcut dört radyo, her satır48. Fotoğraf none/uploading/processing/uploaded halleri ve metinleri korunur. İlk soru dışındaki adımlar arasında yerel taslak geri düzenlenebilir; onboarding dışına geri çıkma değil. Son Save my profile sunucu onayından sonra view-own; motion H3 değişmez. Önizleme ad adımını temsil eder; bütün adımlar ayrı çizilmiş değildir.

### Profil / Ayarlar
Kompakt üst blok64 avatar; bilgiler ve ratio çerçevesiz. Varsayılan iki eşit küçük eylem mevcut Edit / Settings. Bu işte kabul edilen iki küçük düğme sunumu, eski üst sağ kalem+dişli yerleşiminin yerini alır; davranışları aynı. Dar genişlik/büyük yazıda iki düğme sarılarak ekranı uzatacaksa tek48 “…” menüsü → Edit / Settings alternatifidir; ikisi birlikte uygulanmaz. HTML inceleme için alternatifi details ile ayrıca gösterir.

Ayarlar mevcut eylemleri gruplar; gizli Dil eklenmez. E-posta değiştirme Hesap altında; destek adres+kopyala. Account/Privacy/About grup etiketleri EN/TR delta. Sil/Çıkış alt ayrı grupta; yeni ayar veya bildirim davranışı yok. Toast yalnız mevcut başarı olayından sonra; mevcut profileSaved. Kritik hata/yeniden deneme toast'a taşınmaz.

### Messages / sohbet
Connections / Requests metin+alt çizgi; sekmeler48 hedef. Kapalı bağlantı listesi ve son mesaj önizlemesi eklenmez. Okunmamış nokta8 / #B63A32, mevcut semantics korunur. Boş durum mevcut cümle + kendi çizimimiz + Nearby sekmesine giden küçük eylem. Loading spinner24/1.8; hata/offline mevcut Try again kalır.

Sohbette üst sağ mevcut continue/safety ikonları48. Mesaj alanının içinde sağ alt32 görünüm/48 Send. Boş/gönderiliyor/yazılamaz hallerde mevcut etkinlik kuralları. Sayaç kalıcı ve Your message üstünde8. Karakter sayacı mevcut son50 kuralı; mesaj metni500 limiti değişmez. Hello kartı yok; yazılabilir sohbette saklama satırı yok. Gerçek gönderildi durumu yalnız sunucu onayı. Salt-okunurda composer tamamen kaldırılır, mevcut saklama/iletişim eylemleri korunur. Tam ekran rapor/onay: menü yok.

### Harita / açıklama
Mevcut area,zoom,legend eylemleri kenarda48 hedef,36 yüzey. Show my area pin çizmez. Mevcut legend dört renk ve sözlü adlarla; yeni sayısal eşikler yok. Bilgi sayfası veya sheet: ×20/48 sol üst; tam ekran olmayan bilgi sayfasında menü korunabilir, tam ekran onay/rapora bu kural uygulanmaz. Başlık/etiketler mevcut mapLegend/density*.

## UYARLANIR — ayrı öneriler, bu teslimde uygulanmadı

DESIGN RECOMMENDATION — FOUNDER APPROVAL REQUIRED

- Friendship/Networking harita filtresi: yeni filtre davranışı gerektiğinden bu pakete alınmadı.
- Uzak görünüm bilgi hapı: yeni bilgiye ihtiyaç kanıtı yok; eklememe önerisi. Sayı önerilmez.
- Intro carousel: ayrı onboarding kapsamı; mevcut kayıt akışına eklenmedi.
- Kapak fotoğrafı ve profil paylaşım linki: yeni veri/gizlilik kapsamı; Founder + HARBOR onayı gerekir.

ALINMAZ özellikleri yok. Referanstaki davet ekranının alınmaması, IM HERE mevcut davet kapısının silinmesi anlamına gelmez.

## Teslim ve doğrulama sınırı

ONIZLEME.html:12 örnek, EN/TR,320/390/412,100/200 yazı, opak/yüzen yüzey, sohbet klavye alanı. Kayıt/gönderim gerçek değildir; örnek kişiler metin olarak etiketlidir, portre içermez. Önce sütunu eski iOS çizimleri; Android aynı mantıksal ölçülere safe area uygular, native çizilmiş sayılmaz.

l10n/compact-v10-patch_en/tr.arb:5 yeni anahtar, tam ARB değiştirilmez. Mevcut HARBOR metni delta'ya tekrar yazılmaz; byte-eşit kaynak kopyası önizlemeye gömülür. Networking uçları680a480'de mevcut, tekrarlanmaz.

Code kabul turu: 320/390/412; EN/TR;100/200; tüm hedefler48; OS büyük yazı/ekran okuyucu; keyboard/composer; bottom inset; dört menü görünürlük istisnası; harita atfı; reduce transparency; düşük cihaz blur performansı. HTML görsel doğrulaması ve native test durumları validation.json'da ayrı raporlanır.
