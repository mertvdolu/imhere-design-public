# 01 — Sonradan ek bilgi paylaşımı
## Giriş ve yerleşim
Mevcut contact ekranında **Bu bağlantıda paylaştıkların** bölümündeki mevcut alanların düzenle/geri çek eylemleri kalır. En az bir uygun, henüz paylaşılmamış alan varsa bölümün sonunda **Ek bilgi paylaş** görünür. Bu düğme kayıt göndermez; ayrı seçim görünümünü açar. Karşı tarafın paylaşmış olması şart değildir.

Örnek: E-posta ve Telefon zaten paylaşılmış. Ek bilgi görünümünde yalnız Instagram ve Diğer vardır; E-posta/Telefon seçiciye pasif seçenek olarak bile kopyalanmaz. Böylece bu akışta var olan değerler yanlışlıkla yeniden gönderilmez veya ezilmez. Mevcut değerlerin düzenlenmesi kendi ayrı eyleminde kalır.

Yeni seçici her girişte boştur. Uygun alanı seç, değerini açıkça gir, **Seçtiklerimi paylaş** ile onayla. Çizimdeki @ornek.iletisim ve adresler yalnız fixture; uygulamada otomatik dolum veya hesap e-postası kopyası değildir. Bir alanı doldurmak paylaşmak değildir. Hiçbir alan seçilmezse submit pasif; **Şimdi paylaşma** mevcut contact ekranına değişiklik yapmadan döner.

## Durumlar
| Görünüm | Anlam |
|---|---|
| partial | İki alan paylaşılmış; ek bilgi girişi var |
| empty | Yalnız iki uygun alan; ilk seçim boş |
| selected | Instagram seçilip açıkça yazılmış |
| sharing | Yalnız seçilen ek alan gönderiliyor; çift gönderim kapalı |
| failed | Ek alan başarısız; mevcut paylaşımlar aynen sürer |
| offline | Yeni gönderim kapalı; otomatik kuyruk yok |
| saved | Başarıyla Instagram da paylaşılmış; Diğer hâlâ eklenebilir |
| all | Dört alan paylaşılmış; ek bilgi girişi yok, düzenle/geri çek sürer |

İşlem başarıyla sonuçlanmadan ek alan paylaşıldı sayılmaz. Mevcut bilgiler toplu form değiştirme/silme işlemiyle temizlenmez. API çağrısı mevcut mühendislik sözleşmesine bağlıdır; tasarım yeni endpoint veya transaction biçimi tanımlamaz. UI'ın niyeti **yalnız yeni seçilmiş alanlara ekleme**dir.

Belirsiz ağ cevabı mevcut işlem kimliğiyle uzlaştırılır; kör yeni paylaşım yapılmaz. Kesin hata sonrası retry aynı açık formu kullanabilir. Ekranlar arası yeni kalıcı taslak özelliği yok. Başka oturumda alan o sırada paylaşılmışsa uygunluk yeniden değerlendirilir; “ekle” adı altında mevcut değer sessizce ezilmez. Gerçek durumu yenileyip kullanıcıyı mevcut edit/withdraw akışına bırakın.

Uygunluk mevcut yetkili contact verisinden gelir. Geçmişte geri çekilmiş bir alan için ayrıca yeni yasak veya otomatik yeniden paylaşma kuralı getirilmez; o anki sözleşmenin paylaşılmamış/uygun alan sonucu esas alınır. Engel veya erişim kalkması tüm contact içeriğini ve Semantics'i kaldırır; eski değer cache'den gösterilmez.

Her paylaşım/düzenleme/geri çekme bağlamında önceden görülmüş veya kaydedilmiş bilginin geri alınamayacağı korunur. Sonradan ek alan paylaşma karşılıklı kararın yeniden sorulmasına, yeni sohbete veya yeni mesaj hakkına yol açmaz.

# Devam ekranından salt okunura geçiş
Buradaki tetikleyici **devam akışında karşılıklı EVET'in doğrulanmasıdır**. İlk istek/eşleşme oluşması değildir: ilk eşleşme normal sohbeti açmaya devam eder. Kullanıcının tek taraflı EVET'i de bu geçişi başlatmaz; karşı karar ayrı rozet/metin olarak gösterilmez.

Karşılıklı sonuç doğrulandığı anda devam/geri-al eylemleri ve composer kaldırılır. Hedef sohbet içeriği henüz hazırlanıyorsa ayrı `continue-readonly-loading` durumu:
- `chatClosedReadOnly`: Bu sohbet şu anda salt okunur.
- `chatLoading`: Sohbet yükleniyor…
- `messagesReturn`: Mesajlara dön.

Hedef hazırsa doğrudan mevcut v1.7 `chat-mutual` ve contact girişine geçilir; zorunlu bekleme, yeni sayaç veya süre yok. Gösterilen spinner mevcut yüklemeyi anlatır, iki kişinin özel kararını açmaz.

Yükleme başarısızsa `continue-readonly-failed`: salt okunur açıklaması kalır, `chatLoadFailed` ve mevcut retry label'ı. Retry hedef veriyi yeniden yükler; devam kararını yeniden göndermez, sohbeti tekrar yazılabilir yapmaz. Geri navigasyonu eski composer'ı veya geri alınamayacak artık karşılıklı olmuş EVET eylemini canlandırmaz.

Bu arada bağlantı biter veya erişim kaldırılırsa yetkili güncel sonuç uygulanır. Karşılıklı EVET sonrası salt okunur olmak, engel/erişimsizlik kuralına istisna değildir. Contact yüklemesi ayrı mevcut loading/error durumuyla yönetilir; bu iki geçiş çizimi yeni veri saklama vaadi getirmez.

## Platform ve erişilebilirlik
Tüm varyantlar TR/EN, iOS/Android ve gerçek %200 metin ölçeğiyle. Uzayan alanlar ve açıklamalar kaydırılır; font küçültülmez. Dört sekme ve büyük metindeki 2×2 nav aynı. Ekranlar tam içerik artboard'udur; native safe area/klavye ve M10 uygulanabilirliği cihazda doğrulanır.

Seçiciler checkbox, ilk durumda hiçbiri seçili değil. Paylaşılmış alanın değeri veya eylemi bu seçim grubunun Semantics'ine taşınmaz. Busy sırasında alan seçimi ve submit kilitlenir; seçili taslak okunabilir. Geçişte odak salt okunur başlığa/duyuruya gider; yükleme sonucu bir kez duyurulur. Reduce Motion'da geçiş hareketi gerekmiyor.
