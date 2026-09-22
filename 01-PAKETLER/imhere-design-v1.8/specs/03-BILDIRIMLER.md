# 03 — Bildirim izni ve içerik
## İzin
Nazik uygulama ön ekranı: istek ve mesajlardan haberdar olma açıklaması; Bildirimlere izin ver / Şimdi değil. İzin zorunlu değil. İzin isteği yalnız açık dokunmayla işletim sisteminin gerçek istemine gider; işletim sistemi diyaloğu çizimle taklit edilmez. Kullanıcının yanıtı mevcut platform API sonucundan okunur, yerel kabul varsayılmaz.

İzin açık, reddedilmiş, kontrol ediliyor, durum okunamadı, cihaz ayarları açılamadı ve çevrimdışıyken reddedilmiş durumları bulunur. Ret ekranında uygulamaya devam açık kalır. Retten sonra sürekli sistem istemi tetikleme, otomatik Ayarlar'a zorlama veya tüm ekranı kapatan bariyer yok. Cihaz bildirim ayarları kullanıcı tarafından isteğe bağlı açılır. Ayarlar'dan dönüşte izin yeniden okunur; açmayı başarmak izin verildi demek değildir.

İzin durumu yerel OS verisidir; internet olmadan okunabilir ve cihaz ayarları açılabilir. Çevrimdışı UI yalnız ağ durumunu belirtir; çekirdek ekranlara erişimi bildirim iznine bağlamaz. Android/iOS farklı ara statüler mevcut native izin modelinden gelir; izin verilmemiş/ertelenmiş durumu “açık” diye göstermeyin. Sistem tarafından sınırlı/provisional izin varsa gerçek etkin duruma göre bağlayın, yeni ürün tercihi üretmeyin.

Bu tasarım yalnız izin durumunu yönetir; ambient/mesaj/istek için yeni kategori toggle'ları, quiet hours veya bildirim zaman planlayıcısı eklemez. Founder Ayarlar onayıyla yeni kapsam gelirse ayrı değerlendirilir.

## Bildirim örnek bileşenleri
`push-*` çizimleri metin/payload inceleme bileşenidir. Uygulama ekranı, gerçek gelen push veya OS kilit ekranı tasarımı değildir. İki platform boyutunda ve büyük metinde içerik ölçüsü gösterilir; gerçek sistem kesme/gruplama/gizleme kuralları native OS'a aittir. 👀 SVG göz çizimi görsel temsildir; gerçek metin orijinal emojiyle kalır ve native emoji fontuyla çizilir.

- Ambient: kabul edilmiş `ambientNotification`. Kişi adı, fotoğraf, profil, konum, mesafe, kişi sayısı veya kişisel deep-link içermez. **En fazla 2/gün; en az 3 saat arayla.** Kota uygulamanın mevcut bildirim katmanında; kullanıcıya sayaç olarak gösterilmez.
- Check-in hatırlatması: mevcut `checkInReminderTitle/Body`, yaklaşık 25. dakika, en fazla 1/check-in. `checkInRenew` yeniden konum doğrulamasına gider; açmak/dokunmak check-in'i otomatik uzatmaz. Eski/geçersiz check-in için Paket 1'in gerçek mevcut durumuna yönlenir. Yeni süre uydurulmaz.
- Doğrudan istek/mesaj: ambient kotasına dahil değildir. Eklenen iki genel örnek metin yeni veri ifşası veya payload protokolü getirmez; mevcut onaylı gönderim sözleşmesi bağlanır. Yeni sayaç/kota yok.

Bildirimden açılışta güncel auth/erişim/istek/sohbet durumu yeniden doğrulanır. Engellenmiş/silinmiş/sona ermiş veriyi eski push üzerinden gösterme veya cache'den canlandırma yok. Yetkisiz kişiye bağlanan özel ekran yerine nötr mevcut görünüm. Hassas verinin eski sistem bildirimlerinden kaldırılması mevcut native yönetimin ayrıca doğrulanacak parçasıdır; tasarım sistemin önceden gösterdiği içeriği geri aldığını vaat etmez.
