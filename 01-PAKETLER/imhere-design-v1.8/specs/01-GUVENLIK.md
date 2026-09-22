# 01 — Şikâyet, engelleme, engeli kaldırma, bağlantıyı bitirme
## Şikâyet
İlk görünümde radio seçimi boştur; Gönder pasif. Tam beş kategori: Taciz / Spam / Uygunsuz içerik / Güvenlik endişesi / Diğer. “Diğer” yeni zorunlu serbest metin, medya yükleme veya delil toplama formu eklemez. Tek kategori seçilince gönderim aktif; gönderilirken seçim ve tekrar gönderim kilitlenir. Çizimde seçili Taciz yalnız örnektir.

Şikâyet başarıyla alınmadan `reportSent` ve ayrıca-engelle sorusu görünmez. Başarıdan sonra **ayrı adımda** `reportAlsoBlock`: Engelle / Şimdi değil. Seçim önceden yapılmaz; rapor otomatik engellemez. Bu adımda Engelle zaten açık kendi eylem onayıdır; aynı soruyu ikinci kez tekrarlamaya gerek yok. Başarısız engellemede “Şikâyetin alındı” korunur, yalnız engel hatası gösterilir; tekrar rapor gönderilmez. Şimdi değil raporu geri çekmez.

Gönderilemedi kesin sonuçsa aynı kategoriyle yeniden denenebilir. Ağ cevabı belirsizse başarısız veya alındı denmez; `safetyUnknown` ve durum kontrolü. Çevrimdışı gönderim kuyruğu icat edilmez.

## Engelle
Doğrudan girişte `blockConfirm` ve `blockBody`, açık Engelle / Vazgeç. Karşı taraf onayı veya bildirim/cevap bekleme yok. Etkin engel keşif, istek, sohbet ve contact görünürlüğünü derhal kaldırır; görsel, semantik ağaç ve artık gösterilmemesi gereken cache içeriği birlikte ele alınır. Açık sohbet/derin bağlantı da aynı erişim denetimini uygular.

İşlem gönderilirken kişi verisi yerine işlem görünümü kullanılır; doğrulanmış sonuç olmadan “engellendi” başarısı gösterilmez. Mevcut backend'in effective-block sonucu tüm yüzeyleri bağlar. Başarısız/çevrimdışı işlem uzaktan engel koymuş sayılmaz; belirsiz sonuç önce uzlaştırılır. Retry yeni bir ürün kuralı veya offline kuyruk değildir.

## Engellenenler ve unblock
Boş, dolu, yükleme, hata, çevrimdışı durumları vardır. Yönetim satırındaki görünen ad yalnız kullanıcının kendi engel kaydını tanıyıp kaldırması içindir; kişi profilini, fotoğrafını, bio'sunu, sohbetini veya contact'ını açmaz. Satır mevcut güvenli engel-listesi verisine bağlanır; engellenmiş profili ayrıca çekme hakkı tanımaz.

Engeli kaldır kendi onayında ad + `unblockBody` yer alır: **eski sohbet veya bağlantı yeniden açılmaz.** Başarı yeni match, niyet, mesaj hakkı veya otomatik yeniden istek üretmez. Hata sonrası eski engel sürer; sonuç belirsizse kaldırıldı denmez. Başarı listeden ilgili kaydı kaldırır; son kayıt ise boş durum.

## End Connection
`endConfirm` kullanıcının **kendi eyleminin onayıdır**. “Onay istemez” karşı tarafın onayına ilişkin önceki Founder açıklamasıdır. `endBody` sonucu açıklar. İşlem tek taraflıdır; kişiyi engellemez. Kendi onayı → işlem → doğrulanmış `connectionEndedNeutral`.

Karşı tarafa neden, karar veya özel tercih gösterilmez. Eski sohbet varsa yalnız mevcut erişim ve saklama koşullarında salt okunurdur; engelleme bunu bastırır. Kapalı sohbetin saklama süresi eklenmez. Kesin hata yeniden deneme; belirsiz sonuç durum kontrolü. Sonuç ekranından Mesajlar'a dönüş eski sohbeti etkinleştirmez.

Tüm bu işlemler mevcut işlem kimliği/idempotency/erişim kontrolüyle bağlanır. Çift dokunuş ikinci işlem oluşturmaz. Yeni endpoint/hata kodu/süre veya şikâyet yaptırım politikası tanımlanmaz.
