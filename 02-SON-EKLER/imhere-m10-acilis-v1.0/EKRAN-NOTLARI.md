# M10 — Açılışta hesap durumuna ulaşılamıyor / v1.0

## Ekran
Mevcut Geist, koyu yeşil yüzey, nötr bilgi kartı ve açık yeşil birincil düğme. 24 px yatay kenar boşluğu; kart ile düğme arasında 16 px. Tek eylem checkInRetry. Geri, çıkış, giriş yap, destek, sekme çubuğu veya başka eylem yok. Üst marka simgesi dekoratiftir, etkileşimli değildir. iOS/Android ve %100/%200 metin için 16 SVG, 4 PNG. Uzun içerik gerektiğinde kayabilir; güvenli alanlar korunur.

- startup-unreachable: nedeni doğrulanmamış ağ/sunucu erişim sorunu için mevcut messagesUnavailable. TR: “Bu içerik şu anda kullanılamıyor.” EN karşılığı paketten aynen gelir.
- startup-offline: çevrimdışı olduğu doğrulanmış durumda mevcut offline. Doğrulanmamış sunucu hatası “İnternet bağlantısı yok.” diye sunulmaz. Hata türü ayrıştırılmıyorsa nötr varyant kullanılır.

İki çizim aynı açılış hâlinin metin varyantıdır. Yeni açılış metni veya anahtar üretilmedi. messagesUnavailable adı tarihsel olarak mesajlara bağlı olsa da bu çizimde yalnız mevcut genel metin yeniden kullanılır; mesajlar sekmesine yönlendirme değildir.

## Davranış bağlantısı
Tetikleyici mevcut açılış hesap-durumu okumasının başarısız olmasıdır. Tekrar dene aynı okumayı yeniden başlatır; çıkış, hesap oluşturma veya veri silme işlemi başlatmaz. Başarılı okumadan sonra mevcut yönlendirme kuralları kullanılır. Tekrar deneme sırasında mevcut boot/yükleme hâli geçerlidir; yinelenen istek oluşturulmaz. Yeni zaman aşımı, otomatik deneme veya yönlendirme kuralı tanımlanmaz.

Mesaj kullanıcıyı suçlamaz; hesap/veri kaybı veya oturumun bittiği iddia edilmez. Ekran okuyucu bilgi satırını ve düğmeyi okur; dekoratif ikonlar ayrıca okunmaz. Tekrar gösterimde odak döngüsü oluşturulmaz. Dokunma hedefi en az 48 px, düğme yüksekliği en az 52 px. Native erişilebilirlik ve cihaz doğrulaması M10 entegrasyonundadır.

## Birlikte verilen metinler
l10n/patch_tr.arb ve patch_en.arb önceki üç mesaj saklama metni ile nearbyLimited metnini aynen içerir. Bu teslim onların ürün onayı aldığı iddiasında bulunmaz. Önceki kullanım notları metin-notlari/ altında bulunur. Açılış ekranının mevcut anahtarları ayrı existing-screen-keys dosyalarında salt referans olarak verilir.

Delta birleştirme yapılır; canlı ARB üzerine dosya yazılmaz. visibilityHelp için ayrı iletilmiş düzeltme korunur; bu teslim onu geri almaz. Önceki paketler, uygulama kodu ve web sitesi değiştirilmedi.
