# v1.7 — Kontroller ve sınırlar

## Dosya ve dil kontrolü
93 durumun her biri TR/EN × iOS/Android × normal/%200 varyantı içeriyor: 744 SVG ve 186 PNG. SVG'lerin ölçüleri, tuval içindeki yazı sınırları, çözümlenmemiş parametreler ve PNG dosyalarının açılması kontrol edildi. Tam sözlükler 400'er anahtar; 66 ek metin ve parametre metadata'sı iki dilde eşit. Kabul edilen 334 eski metin/metadata aynı.

## Kritik UI kuralları
- Her niyet seçicide yalnız iki seçenek; gönderme ve kabul boş başlangıçları seçimsiz, onayları pasif. Kabul öncesi karşı niyet seti yok. Seç ve Kabul Et ayrı eylem; ters istekte otomatik match yok. Boş kesişimde Sohbete geç etkin.
-19/20 ve kalan süre bekleyen istekte. Sohbet ve devam kararında zamanlayıcı yok; kendi kalan mesaj hakkı dışında sayaç açılmaz.500/501 taslak örnekleri ve 0 hak görünümü ayrı.
- Salt okunur/karşılıklı/erişimsiz sohbette composer ve Gönder yok. Yumuşak uyarıda Yine de gönder var. Gönderilmiş mesaj için düzenle/sil/geri al veya medya eylemi yok. Belirsiz gönderimde yeni mesaj tekrarı yerine durum kontrolü var.
- Karşı devam kararı manifest/görünümde yok; yalnız kendi onaylı EVET'i gösterilir. Nötr sona ermede karar değiştirme/geri alma yok. Karşılıklı EVET yalnız contact erişimi ve salt-okunur sonucu açar.
- Contact 0/1/2/4 seçimi; seçimsiz başlangıçta boş değerler ve Şimdi paylaşma; yazmak yayın değildir. Kendisi paylaşmadan karşıdan bilgi görebilme örneği mevcut. Karşı kişinin değerinde düzenleme/geri çekme eylemi yok. Kaldırma öncesinde kaldırıldı başarısı yok.
- Kullanılamıyor durumlarında kişi/mesaj/contact değerleri yok. Engelleme nedenini açıklayan metin bulunmaz. Bu davranış native uygulamada erişim kontrolüne ve Semantics'e de bağlanmalıdır.

## Görsel inceleme
Ana akış; özel EVET/HAYIR, alınan contact ve kaldırma; büyük metin; 500/501 ve 0 hak örnekleri gözle incelendi. Büyük metinde bölüm etiketlerinin bölünmesini önlemek için Bağlantılar/İstekler seçenekleri alt alta yerleştirildi. Uzun formlar ve konuşma çizimleri kaydırılabilir tam içerik olarak teslim edildi; native fixed-height ekran iddiası değildir.

Yerel HTML önizlemede 13 temel akış ekranı, 93 toplam görünüm, yedi bölüm filtresi ve EN Android %200 resim yüklemeleri kontrol edildi. Önizleme harici ağ isteği yapmıyor. Fontlar ve resimler yerel/gömülü.

## Korunan dosyalar
v1.6 ve v1.6.1 kabul edilmiş paketleri kendi teslim manifestleriyle karşılaştırıldı; değiştirilmedi. Token'lar, font/lisans, profil/auth sözleşmeleri ve v1.4 kabul eki aynıdır. v1.7 yeni UI çıktısıdır; eski paketleri yeniden tasarlamaz.

Statik ayrıntılar `evidence/validation.json`, önizleme sonucu `evidence/preview-check.json`, kaynak/baseline kaydı `evidence/source-and-baseline.json` içindedir. Yazı/alan başına kontroller uygulama test sayısı olarak sunulmaz.

## Yapılmayanlar ve M10 sınırı
Flutter/backend kodu değiştirilmedi; gerçek kullanıcıya istek/mesaj/contact gönderilmedi. Native build, Firebase akışı, fiziksel cihaz, gerçek klavye/parola yöneticisi, VoiceOver/TalkBack veya ağ yarışı testi yapılmadı. Bu teslim tasarım ve dosya kontrolüdür; çalışan ürün entegrasyonu değildir.

Gerçek grapheme/emoji sayımı, sunucu hakları/süreleri, eşzamanlı ters istek, idempotency, mesaj gönderiminin belirsiz sonucu, EVET geri-al/mutual yarışı ve açık ekranda engelleme M10 yazılım doğrulamasına bağlanır.2×2 ana navigasyonun native uygulanabilirliği önceki kabul notuyla yazılımda doğrulanacak. Kapalı sohbet saklama süresi M11 kararında; burada süre veya kalıcılık vaadi yok.
