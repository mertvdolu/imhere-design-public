# 01 — Ana yapı ve Yakındakiler
## Ölçü ve yapı
- iOS referans: 390×844 logical px; Android: 412×915. Dar ekran kabul kontrolü 320 logical px. SafeArea üst/alt değerleri runtime’dan; çizimde sırasıyla 54/34 ve 32/24 referans alınmıştır, uygulamaya sabitlenmez.
- Ortak yatay dolgu 24; içerik genişliği `viewport - 48`. Dikey aralıklar yalnız mevcut 4/8/12/16/20/24/32/40/48 skalasından. Tablet için yeni ekran tasarımı bu paketin dışında.
- Yapı: güvenli alan → marka → eyebrow/başlık → (pasifte açıklama) → Bölge hareketliliği → Buradayım alanı → status → varsa kalan süre → varsa notice → duruma uygun eylemler → presence note → kişi listesi → gizlilik metni.
- Harita eylemi üstte, check-in’den bağımsız erişilebilir. Dokununca aynı sekmenin alt sayfası açılır. Harita dönüşü oturum/referans değiştirmez. Başlık eylemi, sayfa başlığı ve sekme ayrı rollerdir.
- Başlık 31/1.16, gövde 16/1.6, etiket 14/1.4, metadata 12/1.5; Geist yerel gömülü. Çizim satırları gerektiğinde genişler. Native uygulama token’ların satır yüksekliklerini kullanır.

## Orb ve durum alanı
- Bölge minimum 244, orb çapı 160, halkalar merkezden 98/117. Gradient, tonlar ve halka opaklıkları v1.3’ten. Aktif check yalnız sunucu onayıyla. Aramada nötr spinner; radar/kişi/konum nabzı yok.
- Pasifte orb gerçek `btn-checkin` hedefidir; semantik label checkInStart. Görsel halkalar tıklanabilir değildir. %200'de etiket sığmadığı için dekoratif orb + altında tam genişlik checkInStart butonu kullanılır; yalnız alttaki gerçek buton Key taşır. Yalnız bir erişilebilir eylem vardır.
- Aktifte orb dekoratif durum işaretidir. Kalan süre yalnız status altındaki bir satırdadır; ekranda veya ekran okuyucuda çift sayaç yok. Yenileme ve durdurma ayrı, minimum 52 yüksekliğinde butonlar.
- Tüm butonlar `minHeight:52`, hedef minimum 48; metin uzadığında yükseklik büyür. %200'de eylemler dikey kalır. Kalıcı izin/servis kapalı örneğinde orb pasif, doğru ayar eylemi görünür. Backend bağlanmamış durum geliştirme kabul örneğidir; üretim akışı değildir.
- ImHereNoticeRow dilini sürdür: ikon + metin, en az 16 iç dolgu, köşe 16; tehlike yalnız renkle anlatılmaz. `checkin-status`, `checkin-notice`, `checkin-remaining` ayrı gerçek widget'lardır.

## Kişi kartı ve liste
- Kart 16 radius, 12 dolgu; tek fotoğraf 60×75 cover crop, isim ve bio/ilgi alanları. Büyük metinde satırlar ve kart büyür; bilgi kırpılmaz, yaş/cinsiyet/meslek görünürlüğü veri sözleşmesinden gelir. Örnek kartta bu opsiyonel bilgiler çizilmemiştir.
- Kartın tamamı minimum 48 hedefli profil açma eylemidir; chevron ayrı ikinci erişilebilir hedef değildir. Sıralama veriyi geldiği gibi kullanır; tasarım mesafe/rütbe/sayı ima etmez.
- Geçerli check-in olmadan profil listeleme kapalı açıklaması; yükleme, gerçek boş, offline ve hata ayrı. Kapalı listede fake skeleton kişi/örnek kullanıcı gösterilmez. Engellenen veya uygun olmayan profiller görünmez.

- **Kabul eki:** Yakındaki kişi kartında meslek, kullanıcı gizlediyse gösterilmez; boş etiket veya gizleme rozeti bırakılmaz.

## Dört sekmeli kabuk
Profil / Mesajlar / Yakındakiler / Etkinlikler. Seçili üçüncü sekme; renk + kalın yazı + selected Semantics. Normal bar: dört eşit sütun, ikon24, etiket12, minimum 60 + sistem inset. Diğer sekmelerin içerikleri sonraki paketlerdedir; bu teslim onların akışını taklit etmez.

Büyük metinde dört etiket tek satıra sığmıyorsa bar **2×2** yerleşir; okuma/dokunma sırası satır bazında aynı dört öğedir (Profil, Mesajlar / Yakındakiler, Etkinlikler). Her hücre 82 logical px minimum, iki satır toplam 164 + inset; metin sığmazsa hücre yüksekliği büyür. Bu bir beşinci sekme veya sıra değişikliği değildir. Gerçek textScaler ölçümüyle geçiş belirlenir, font ölçeği kapatılmaz. Focus/selected bilgisi yerleşim değişince korunur. iOS VoiceOver ve Android TalkBack sırası bu okuma sırasıdır.

**Kabul:** 2×2 büyük-metin navigasyonu kabul edildi; native uygulanabilirlik M10’da yazılım tarafınca doğrulanacak.
