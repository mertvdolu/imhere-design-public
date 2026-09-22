# 02 — Sohbet ve yumuşak iletişim uyarısı
## Yerleşim
Geri, kişi başlığı, kaydırılabilir konuşma, yalnız kendi kalan hak metni, sakin Devam eylemi, mesaj yazma alanı ve Gönder. Mevcut token'larla kendi balonu açık yeşil, karşı balon koyu yeşildir. Hizalama ve erişilebilir yazar bilgisi rengi destekler. Yazılıyor/çevrimiçi/son görülme/okundu rozeti eklenmez.

Alt ana navigasyon Mesajlar bağlamındadır. Tam kaydırma artboard'u yerleşimi açıklar; native uygulamada klavye üstündeki composer ve safe-area kendi platform düzenine bağlanır. Gövde ve büyüyen composer birbirini örtmez. Uzun taslakta composer içi kaydırma var; çizimde son üç satır görünür. Tam taslak manifestte fixture olarak bulunur, gönderim öncesi kesilmez.

##20 hak ve 500 karakter
Kullanıcı yalnız kendi `chatRemaining.remaining` değerini görür: yeni sohbette 20/20, örnekte 19/20, bitince 0/20. Karşı tarafın kalan hakkı, birleşik 40 hedefi veya ilerleme barı yok. Karşı tarafın hakkı bitse de kullanıcının kendi kalan hakkı devam eder. Sayaç gerçek kabul edilmiş mesaj sonucundan gelir; çift dokunuş veya retry ikinci kez hak tüketmiş gibi gösterilmez.

Mesaj en çok 500 grapheme; mevcut uygulamanın görünen karakter/normalizasyon hesabı kullanılır. UTF-16 kod birimi sayımıyla emoji sınırı değiştirilemez. Üretim sayacı mevcut `characters`/validator davranışına bağlanır; görsel fixture sayımı bir validator uygulaması değildir.500 görünümünde Gönder mümkün; 501 görünümünde hata+pasif Gönder. Metin sessizce kırpılmaz; kullanıcı düzenler. Boş taslakta gönderim pasif; whitespace/normalizasyon ayrıntısı mevcut sözleşmeden.

0/20 durumunda normal mesaj yazma/gönderme alanı yok; okuma ve özel devam kararı vardır. Sayaç alışverişe veya yenilenebilir hak vaadine bağlanmaz. Devam eylemi haklar bitmeden de kullanılabilir; sonraki karar için zorunlu 20 mesaj doldurma yok.

## İçerik
Yalnız metin, emoji ve link. Ek/kamera/mikrofon/GIF/fotoğraf/video/dosya düğmesi yok. Klavyenin standart emoji girdisi kullanılabilir; özel medya/sticker sistemi yok. Örnek emoji SVG'de basit vektör gliftir; üretimde platform emoji renderer'ı kullanılır. Link metin olarak görünür; otomatik medya kartı/unfurl özelliği talep edilmez.

Gönderilmiş mesajlarda düzenle, sil, geri al menüsü yok. Gönderilmemiş veya kesin başarısız olmuş taslağı düzenlemek, gönderilmiş mesajı düzenlemek değildir. Contact kayıtlarının sonradan düzenlenmesi ayrı arayüzde ve ayrı işlem olarak kalır.

## Gönderim ve hata
Gönderiliyor sırasında aynı draft/işlem için ikinci Gönder pasif. Kesin hata alanı ve metni korur, tekrar deneyebilme sunar. Sonuç belirsizse `chatSendUnconfirmed`: yeni mesaj üretmeden mevcut gönderim durumu kontrol edilir. Kalan hak bilinmiyorsa sayı uydurulmaz; “Kalan mesaj hakkın kontrol ediliyor…” açıklaması vardır. Sonuç uzlaşmadan körlemesine tekrar gönderim yok. Bu durum yeni backend endpoint'i gerektirmez; mevcut operasyon/idempotency katmanına bağlanır.

Offline sahte teslim/senkronizasyon vaadi vermez; otomatik gönderim kuyruğu eklenmedi. Ağ geri geldiğinde mevcut doğrulanmış konuşma/hak durumuyla devam edilir. Cache erişimi gizlilik/engel durumunu geçersiz kılamaz.

## Yumuşak iletişim uyarısı
Mevcut telefon/e-posta/Instagram tespitinin sonucu kullanılır; yeni regex veya tespit kapsamı icat edilmez. Taslak, `chatSoftTitle` / `chatSoftBody`, **Mesajı gözden geçir** ve **Yine de gönder** gösterilir. Gönderim engeli değildir; kullanıcı bilinçli devam edebilir.

Gözden geçir güncel taslağa döner. Taslak değişirse mevcut tespit yeniden uygulanır; önceki uyarı onayı başka içerik için otomatik izin sayılmaz. Yine de gönder aynı mesajın normal yetki, uzunluk ve kendi hak kontrollerini korur. Ağ/kapalı sohbet/limit hatasını atlatan yol değildir. Uyarı sonrası gönderiliyor/hata ayrı görsellerdir; başarısız taslak confirmed balon olarak eklenmez.

## Salt okunur, kapanma ve erişim
EVET+EVET sonucu sohbet salt okunurdur; kalan normal mesaj hakkı olsa bile composer/Gönder yok. `chatContactOpen` ayrı contact arayüzünü açar. Kapalı sohbet yalnız `chatClosedReadOnly` ve nötr kapanışla gösterilir; süre sayacı, saklama süresi veya kalıcılık vaadi yok. Check-in süresinin bitmesi sohbeti kendiliğinden kapatmaz.

Engel/erişim kaldırma üstün gelir: kişi, geçmiş mesaj, contact değerleri ve ilgili Semantics düğümleri görünmez; neutral unavailable gösterilir. “Salt okunur” engellenmiş içeriği cache'ten gösterme izni değildir.
