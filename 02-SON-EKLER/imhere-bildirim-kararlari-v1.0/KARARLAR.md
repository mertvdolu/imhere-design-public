# I'M HERE — Bildirim ayrıntıları v1.0

## 1. Android genel bildirim kanalı
EN: Updates
TR (Türkçe yeniden açıldığında): Güncellemeler

Mevcut genel/varsayılan kanalın kullanıcıya görünen adı için önerilen anahtar: notificationChannelUpdates. Bu ad yeni kanal ayrımı veya yeni Ayarlar seçeneği getirmez. Hatırlatma kanalının adı ayrı kalır.

## 2. Ses
Tasarım varsayılanı iki platformda da sessiz. Yeni özel ses veya titreşim deseni yok. Kullanıcının sistemde yaptığı tercihler geçerlidir; sessiz varsayılan, cihazın her koşulda sessiz kalacağı vaadi değildir. Mevcut kurulumlara geçişi mühendislik doğrular; bu belge sesin kodda değiştirildiğini iddia etmez.

## 3. Android küçük simge
Bu teslimde özel nihai bildirim simgesi yok. Mevcut uygulama simgesinden türetilmiş geçici tek renkli sürüm uygundur. Harf/uygulama adı ve zemin karesi kullanılmasın; ayırt edici ana işaret şeffaf zeminde sadeleştirilsin. Küçük boyutta okunurluk cihazda doğrulansın. Mağaza ikonu/splash final tasarımının kabulü anlamına gelmez.

## 4. İstek bildirimine dokunma
Mevcut hedef korunur: ilgili isteğin görüldüğü ekran. Bu v1.8'in güncel auth/erişim/durum doğrulamasıyla açılır. Eski bildirim iptal edilmiş veya erişilemeyen isteği yeniden canlandırmaz; mevcut nötr durum kullanılır. Dokunmak isteği otomatik kabul etmez ve yeni istek göndermez. Ürün akışı değişikliği istenmiyor.

## 5. Check-in kanalının kaynağı ve görünen adı
İncelenen v1.8 specs/03-BILDIRIMLER.md, hatırlatma başlığı/gövdesini tanımlar; Android kanal adı tanımlamaz. Yerel uygulamada app/lib/notifications/native_notification_port.dart içinde 'Check-in' sabit adı bulunuyor. Bu nedenle tasarım paketinden gelen bir kanal adı olarak gösterilemez. Tarihsel olarak geçici amaçla konulduğu mevcut kanıtla doğrulanmıyor.

Bundan sonraki görünen ad:
EN: Check-in reminders
TR: Check-in hatırlatmaları
Önerilen anahtar: notificationChannelCheckInReminders.

Yalnız görünen ad kararıdır; kanal kimliği, hatırlatma zamanı, gönderim sayısı ve tıklama davranışı değişmez.

## Önceki kararların kapsamı
Yakınlık bildirimi başlıksızdır ve uygulama açıkken gösterilmez. Bu foreground kararı diğer bildirim türlerine genellenmez. Bu belge tasarım teslimidir; uygulama/backend değiştirilmedi. Kanal adları TR/EN metin dosyalarında verilmiştir; canlı ARB üzerine yazmadan birleştirilir.
