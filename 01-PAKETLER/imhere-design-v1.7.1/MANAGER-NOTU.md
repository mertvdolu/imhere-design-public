v1.7.1 M06 küçük ekini inceleme için iletiyorum.

Kişi görünümünde üç durum hazır: cooldown'da pasif “Bir merhaba gönder” + “Şu an bu kişiye istek gönderilemiyor.”; bekleyen istek; zaten bağlantıdasınız. Görünür/gizli profil alanları, TR/EN, iOS/Android ve büyük metin varyantları var. Süre veya neden gösterilmez.

§7'deki pendingSlots → {used}/{max}, profileAgeYears ve requestCooldown kanonik ad/metinleri hizalandı. Üst sınır mevcut sözleşmeden; yeni limit yok. Bekleyen ve bağlantı durumları için iki yeni UI anahtarı ayrıca belirtildi. M06'da Sohbete geç açılmadı; bağlantı durumu generic STATE_CHANGED'dan çıkarılmıyor.

Bir yerleşim farkı: mevcut kod notu düğmenin üstünde çiziyor, §7 altında diyor. Ekte §7'deki alt yerleşim uygulandı; kod değiştirilmedi.

8 görünüm / 64 SVG / 16 PNG. Delta ARB + migration ile birleştirilecek; canlı ARB'ler üzerine yazılmayacak, v1.8 metinleri korunacak. Uygulama ve gerçek cihaz doğrulaması yazılım tarafında; dosya kontrolleri DOGRULAMA.md'de.
