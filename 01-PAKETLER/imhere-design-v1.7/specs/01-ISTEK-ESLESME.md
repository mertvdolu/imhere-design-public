# 01 — Mesajlar, istek ve eşleşme
## Mesajlar yerleşimi
Alt sekmeler Profil → Mesajlar → Yakındakiler → Etkinlikler; burada Mesajlar seçili. Uygulamanın başlangıç sekmesi değişmez. Mesajlar başlığının altında Bağlantılar/İstekler iki bölüm kontrolüdür; ana sekme eklemez. Bağlantılar mevcut sohbet girişlerini, İstekler gelen/giden gruplarını gösterir. Geçişte mevcut liste/scroll bağlamı korunur; sıralama algoritması, okunma bildirimi veya yeni profil aktivite verisi tasarlanmaz.

İstekler kartında fotoğraf, görünen ad ve nötr istek durumu. Mesafe, konum, cinsiyet filtresi veya kabul öncesi gönderen niyeti yok. Gizli profil alanı eklenmez. Çizimde gelen Deniz ile giden Emre farklı örnek kişilerdir; aynı çifte çift bekleyen istek varsayılmaz. Liste örneği tüm 19 kaydı çizmek yerine ilgili kart sunumunu gösterir.

## İki niyet kartı
Arkadaşlık ve Networking; min 1/max 2. İlk girişte hiçbir seçenek seçili değildir. Kartlar checkbox anlamı taşır; bir veya ikisi seçilebilir. Seçim rengi mevcut friendship/networking token'ından, ayrıca tik ve erişilebilir selected durumundan anlaşılır. Başlık “Bu kişiyle neden bağlantı kurmak istiyorsun?”, açıklama “Birini veya ikisini seç.”

Gönderme onayı minimum bir seçim olmadan pasif. Kartlar kalıcı profil modu veya sonraki isteğe otomatik varsayılan oluşturmaz. Başarısız gönderimde açık ekranın kendi taslağı korunabilir; başka alıcıya veya kabul akışına taşınmaz. Kalıcı disk taslağı/otomatik gönderim vaadi yok.

## Bağımsız alıcı kabulü
Gelen ayrıntıdaki `requestAccept` yalnız alıcının niyet seçimini açar. Açılan seçici yine boştur. Gönderenin seti görsel, accessibility, önizleme, push veya istemci cache yoluyla gösterilmez. Alıcı kendi setini seçer, sonra `requestSelectAccept` / **Seç ve Kabul Et** ile kabul işlemini başlatır. Bu ikinci eylem olmadan match kurulmuş gibi davranılmaz. Seçim/gönderim sürerken aynı işlemin ikinci kez tetiklenmesi kapalıdır.

Red eylemi mevcut `requestDecline` ile; işlem/hata/success gerçek sonuca bağlı. Başarısız yanıt kartı reddedildi iddiası taşımaz. İstek bu sırada sona erdiyse sonuç ekranı uygulanır; eski karta kabul gönderimi sürdürülmez.

## Bekleyen ve sınır
Bekleyen ayrıntıda **19/20 bekleyen istek** ve `requestTimeLeft` ile **14: 32 örnek kalan süre** bulunur. Tam süre 15 dakikadır; sayaç gerçek isteğin gönderim/sonlanma verisinden hesaplanır. Görünümü yeniden açmak yeni 15 dakika başlatmaz; arka plandan dönüşte mevcut otoriteyle yenilenir. Bu sayaç sohbet veya devam kararına taşınmaz.

20/20 görünümünde mevcut `requestFull` açıklaması gösterilir. Mevcut bekleyeni iptal etmek mümkündür; yeni gönderim backend izin vermedikçe açılmaz. Sayaç kredi, günlük kullanım hakkı, satın alınabilir slot, ilerleme hedefi veya cüzdan değildir. Yeniden istek cooldown'ları mevcut kurala bağlı; yeni süre/yerel sayaç veya bypass eklenmez.

Çevrimdışı görünüm güncel 19/20 veya kalan süre iddiasını tekrar etmez. İşlem doğrulanmadığında kabul/gönderildi/iptal edildi başarısı oynatılmaz. Yeniden deneme mevcut işlem kimliği ve idempotency davranışını korur; belirsiz sonucu ikinci bir yeni istekle çözmeye çalışmaz.

## Ters istek, sonuç ve gizlilik
Aynı çiftte ters yönde bekleyen istek varsa ikinci gönderim `requestIncomingInstead` ile gelen isteğe yönlenir. Otomatik kabul/match yok; “Gelen isteği incele” sonra bağımsız boş seçici. Göndermede seçilmiş niyetler alıcının formuna otomatik doldurulmaz.

Süre doldu, kendi iptali ve diğer sona erme sonuçları ayrı görsellerdir. Red için kullanılan nötr sona erme, engel nedeni açıklamaz. Engelleme/erişim kaldırma durumu ise kimliği, fotoğrafı, istek verisini ve semantik ağacını kaldıran nötr `request-unavailable` görünümüne geçer.

## Eşleşme
Yalnız sunucunun doğruladığı tek match sonrasında iki set ve varsa kesişim görünür. Kesişim boşsa mevcut `matchNoCommon` nötr bilgisi gösterilir; Sohbete geç aktiftir. “Daha kötü eşleşme” puanı, yeni filtre veya yeniden eşleşme zorunluluğu yok. Yükleme/hata/offline ekranı match başarısını peşinen ilan etmez.
