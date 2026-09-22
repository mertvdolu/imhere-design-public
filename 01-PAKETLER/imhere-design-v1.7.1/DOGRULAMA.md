# v1.7.1 doğrulama

- 2012 statik kontrol geçti: 8 görünüm, 64 SVG, 16 PNG; TR/EN anahtar ve parametre eşitliği; tuval içi metin sınırları.
- §7'nin üç metni mevcut uygulama ARB'leriyle birebir doğrulandı. pendingSlots used/max int; yaş age int. 399 eski metin ve ilgili metadata aynı, yalnız pendingSlots değişti.
- Üç kişi durumunda gönderim pasif; açıklamalar doğru. Gizli varyantlarda yaş/cinsiyet/meslek ve bunların metni yok. Cooldown süre/neden/geri sayım içermez.
- Bekleyen istek ayrıntısına giriş ve Mesajlar'a dönüş mevcut eylemlerdir; bu ekte kabul veya Sohbete geç açılmadı.
- 19/20 ve 20/20 sayaç görselleri eski v1.7 ile byte-aynı; yalnız metin parametre bağlantısı güncellendi.
- Token/font dosyaları aynı. Kabul edilmiş v1.6/v1.7/v1.8 paketlerinin manifest SHA-256 değerleri doğrulandı, eski dosyalar değişmedi.
- TR iOS normal ve EN Android %200 üçlü görseller gözle incelendi; açıklama düğmenin altında, metinler kesilmiyor.
- Dosyadan önizleme: 6 ana akış kartı / 8 toplam görünüm / 2 bölüm; EN Android %200 görselleri açıldı; dış ağ isteği veya sayfa hatası yok.

Bu kontroller tasarım dosyaları içindir. Uygulama kodu değiştirilmedi; Flutter derleme, gerçek cihaz, VoiceOver/TalkBack, sunucu/state geçişi testi yapılmadı. M06 gerçek durum bağları ve M10 native yerleşim kontrolü yazılım tarafındadır. §7 ile mevcut kodun not konumu farkı spec ve Manager notunda açıkça belirtildi.
