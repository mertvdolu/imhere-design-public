# 04 — Ayrı iletişim paylaşımı arayüzü
## Erişim ve alanlar
Yalnız mevcut backend'in karşılıklı EVET/contact yetkisiyle. Bu form sohbet composer'ı değildir; normal mesaj hakkı harcatmaz veya mesaj düzenleme yolu açmaz. Telefon / Instagram / E-posta / Diğer dört ayrı seçilebilir alan. Varsayılan seçimler ve değerler boş; bir, birkaç, dört veya hiçbir alan paylaşılabilir. Hiç paylaşmamak diğer kişinin paylaştığını görme şartı değildir.

Seçilen alanın girdisi açılır; kullanıcı değerini kendisi yazar. Hesap e-postası, profil veya cihaz rehberi otomatik doldurulmaz. Çizimdeki dolu örnekler başlangıç değeri değildir. Telefon klavyesi/e-posta klavyesi gibi platform girdileri kullanılabilir; kişi rehberi/fotoğraf/konum izni gerekmez. Ürünce verilmemiş ülke formatı, karakter uzunluğu, zorunlu alan veya “diğer” türü eklenmez; gerçek doğrulama mevcut sözleşmeden.

## Yazmak, seçmek, paylaşmak
Alan seçmek veya doldurmak henüz yayın değildir. **Seçtiklerimi paylaş** ayrı, açık onaydır; yalnız seçili ve mevcut doğrulamaya uygun değerler gönderilir. Seçimsiz görünümde yayınlama pasif, Şimdi paylaşma etkin. Şimdi paylaşma contact/okunur bağlamına döner; sahte boş kayıt başarı mesajı üretmez ve normal sohbeti açmaz.

Paylaşım merkezindeki `contactChooseDetails` yalnız seçim formunu açar; yayınlama işlemi yapmaz. `contactShare` yalnız formdaki açık gönderim eylemidir.

İlk paylaşım öncesinde “Daha önce görülmüş veya kaydedilmiş bilgiler geri alınamaz.” metni görünür. Paylaşılıyor/hata durumlarında gerçek kabul yoksa `contactSaved` gösterilmez. Başarısız isteğin taslağı ekran açıkken korunabilir; kalıcı kayıt veya otomatik retry vaadi yok.

## Paylaşılmış ve gelen bilgiler
İki ayrı bölüm: **Bu bağlantıda paylaştıkların** ve **Seninle paylaşılanlar**. Kullanıcı yalnız kendi mevcut yayınlanmış alanında Düzenle / Görünürlüğünü kaldır eylemlerini görür. Karşı tarafın paylaştığı değerde bu eylemler yok. Karşı tarafın boş bölümü yalnız “Şu anda paylaşılan bir bilgi yok.” der; özel karar, neden veya erteleme bilgisi çıkarmaz.

`contact-received` kullanıcının hiçbir şey paylaşmadan diğerinin yayınlanmış bilgisini görebildiğini gösterir. Bu yeni karşılıklılık şartı koymadığımızı görünür kılar. Görünürlük yine mevcut yetki/engelleme durumuna bağlıdır.

## Düzenleme
Kendi mevcut yayınlanmış değer gösterilir; altına değiştirilen taslak girilir. **Değişikliği paylaş** gerçek başarıyla tamamlanana kadar karşıya önceki onaylı değer görünür; yerel taslak yayınlanmış sayılmaz. Hata önceki paylaşımı geri çekmiş veya güncellemiş gibi sunulmaz. Vazgeç mevcut paylaşımı değiştirmez. Bu işlev gönderilmiş sohbet mesajını düzenlemez.

## Görünürlüğü kaldırma
Kendi alanı için ayrı onay, ilgili değer ve koşullu `contactWithdrawConsequence`: artık buradaki görünürlüğü kaldırılabilir; önceden görülmüş/kaydedilmiş kopyalar geri alınamaz. Bu kişinin kendi eylemidir; karşı tarafın onayı aranmaz.

Kaldırılıyor sırasında kaldırıldı başarısı yok. Hata durumunda gerçek görünürlük korunur; kaybolmuş gibi gösterilmez. Başarı sonrası alan artık diğer kişinin contact görünümünde ve accessibility ağacında yok; kendi arayüzünde `contactHidden` gösterilebilir. Önceden alınmış ekran görüntüsünü, kopyayı veya hatırlanan bilgiyi silebildiği iddia edilmez.

Genel “görülmüş bilgi geri alınamaz” metni paylaşım/düzenlemede `contactSeenNote` olarak kullanılır. “Bu bilgi artık burada görünmez” cümlesi henüz kaldırılmamış paylaşıma başarı gibi yazılmaz; `contactHideNote` başarılı kaldırma sonrasındadır; onaydan önce koşullu `contactWithdrawConsequence` kullanılır.

## Boş, hata, offline, engel
Boş seçim, hiç paylaşılmamış merkez, alan hatası, paylaşım/güncelleme/kaldırma işlemi, yükleme ve offline ayrı görsellerdir. Offline/erişimsiz görünümde cache'teki contact değerleri güncel görünürlük izni varmış gibi çizilmez. Engel tüm içerikten önce gelir: fotoğraf, kişi, contact alanı ve eski değerler kaldırılır; nötr kullanılamıyor. Eski route/deep-link bunu aşamaz.
