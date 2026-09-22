# v1.7.3 ekran ve uygulama notları

## 1. Contact düzenleme başarısı
contact-update-success: Mevcut alanın düzenlenmesi sunucu tarafından başarılı olarak doğrulandığında contactUpdated, mevcut başarı geri bildirim bileşeniyle gösterilir. Yeni değer aynı ekranda görünür. Gönderim başında, başarısızlıkta veya sonucu belirsiz işlemde başarı gösterilmez. Mevcut contactUpdating/contactUpdateFailed halleri korunur. Paylaşımda contactSaved, kaldırmada contactHidden kullanımı değişmez. Başarı ekran okuyucuya bir kez nazikçe duyurulur; odak zorla taşınmaz. Yeni otomatik kapanma süresi tanımlanmaz.

## 2. Kendi paylaşımları boş
contact-own-empty: contactYourDetails başlığı korunur; altında contactNothingShared bulunur. İfade TR: “Şu anda paylaşılan bir bilgi yok.” Mevcut EN karşılığı aynen kullanılır. Bu durum yalnız yüklemesi tamamlanmış, erişime izin verilen ve kendi paylaşılan alan sayısı sıfır olan içerik içindir; yükleme/hata/erişim yok durumlarının yerine gösterilmez.

contact-last-withdrawn: Son alanın kaldırılması doğrulanınca contactHidden başarı geri bildirimi ile aynı boş durum birlikte gösterilir. Başarı bildirimi geçince boş durum kalır. Silinen değer ekrandan ve erişilebilirlik ağacından çıkarılır. Karşı tarafın hâlâ erişilebilir paylaşımları ayrı başlık altında korunur; kendi alanlarının boş olması karşı tarafın alanlarını temizlemez. Çizimde bunun için örnek e-posta gösterilmiştir.

Ek bilgi paylaş girişi v1.7.2 davranışını kullanır: yalnız mevcut yetkili durumda paylaşılmamış ve paylaşılmasına izin verilen alanlar; boş ilk seçim, açık paylaşım onayı. Erişim/uygunluk yoksa giriş gösterilmez. Önceden görülmüş veya kaydedilmiş bilgi uyarısı korunur. Kaldırılmış bir alan otomatik yeniden paylaşılmaz.

## 3. Bağlantılar listesinde kapalı kart
connections-open-closed: Aynı listede açık Deniz ve kapalı Emre örnekleri. Kapalı kartın adının altında mevcut connectionEndedNeutral (“Bağlantı sona erdi.”) ikinci satır olarak görünür. Durum yalnız renk farkıyla anlatılmaz; metin %200'de satır kırar ve kart yüksekliği artar. Yeni renk/token, kapanma nedeni, kimin kapattığı, karar, süre veya yeniden başlatma eylemi eklenmez.

Kartın mevcut erişim ve açılma davranışı değiştirilmez. Kart çiziminde ayrı bir kapalı sohbet CTA'sı eklenmemiştir; bu, mevcut kart tıklamasını devre dışı bırakma talimatı değildir. Ekran okuyucu kart adı ve nötr durumu birlikte okur. Kimlik/fotoğraf sadece mevcut yetkili liste verisi izin veriyorsa gösterilir; block/unavailable halinde eski kimlik/cache geri getirilmez. Karşılıklı EVET ile salt okunur olmuş ama devam eden bağlantı, sırf mesaj yazılamıyor diye “sona erdi” etiketini almaz: etiket gerçek kapalı bağlantı durumuna bağlanır.

## Kapsam ve M10
TR/EN ve iOS/Android normal/büyük metin çizimleri teslimdir. Önceki yükleme, hata, offline ve erişilemez durumlar geçerlidir. Bu ek yeni ürün davranışı tanımlamaz. Klavyenin Gönder'i örtmesi M10 yerleşim işidir. Gerçek cihaz, ekran okuyucu, kart tıklaması ve değişen sunucu durumları yazılım entegrasyonunda doğrulanır.
