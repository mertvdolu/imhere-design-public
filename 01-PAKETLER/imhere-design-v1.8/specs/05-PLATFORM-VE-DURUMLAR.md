# 05 — Platform, durum ve erişilebilirlik
## Ortak tasarım
Kabul edilmiş renk/token, Geist 400/500/600, iç ekran başlığı 24, ana vurgu 31, gövde 16, label 14, metadata 12; dış boşluk 24. Kart 16, input 12, CTA 28 köşe; aktif hedefler en az 48 logical px. Silici eylem mevcut danger rengi ve açık eylem metniyle ayrılır; renge tek başına anlam yüklenmez. Yeni global token yok.

iOS 390×844 / Android 412×915 referans görünüm. SVG ve PNG tam kaydırma içeriği; uzun çizim uzun cihaz demek değildir. Native ekranda gövde kaydırılır, güvenli alan ve geçici sheet/dialog yerleşimi platforma göre bağlanır. Başlık/uyarı/buton %200'de çok satıra büyür, font ölçeği kısılmaz. Her adımın onayı tek ekran mantığıdır; büyük metinde tam sayfa uyarlanabilir.

## Durum matrisi
| Alan | Boş | Yükleme / işlem | Kesin hata | Offline | Özel durum |
|---|---|---|---|---|---|
| Report | Seçim yok | Gönderiliyor | Gönderilemedi | Gönderim pasif | Belirsiz; alındı sonrası ayrı engelleme |
| Block / end / unblock | Hedef yoksa nötr erişimsizlik | İşlem sürüyor | İlgili eylem hatası | İşlem gönderilmez | Gerçek sonuç / belirsiz |
| Engellenenler | Liste boş | Liste yükleme | Liste hatası | Güncel liste iddiası yok | Eski sohbet açılmaz |
| Ayarlar / dil | Sabit liste; boş uygulanmaz | Yerel; yapay yükleme yok | Ağ hatası uygulanmaz | Kullanılabilir | Tercih gerçekten kalıcı |
| Bildirim izni | Henüz karar yok | Durum okunuyor | Okuma/ayar açma hatası | Yerel izin yönetimi sürer | Ret uygulamayı engellemez |
| Hukuki bağlantılar | URL henüz yok | Gerekiyorsa web açma hazırlığı | Açılamadı | Açılmadı | İçerik M11, sahte belge yok |
| Hesap silme | Hedef hesap yoksa mevcut auth'a dön | İşlem / istek alındı | Silinemedi | Yeni istek gönderilmez | Reauth / belirsiz / gerçek tamamlandı |
| Etkinlikler | Placeholder'ın kendisi | Yerel; uygulanmaz | Ağ hatası uygulanmaz | Aynı placeholder | Sahte etkinlik/işlem yok |

Çıkış 4 mevcut kabul edilmiş varyantıyla devralındı. Tüm uygulanabilir durumlar TR/EN ve iki platformda büyük metinle çizildi. “Uygulanmaz” işaretleri atlanan tasarım değil, ağ gerektirmeyen yerel UI'da sahte hata üretmeme kararıdır.

## Erişilebilirlik ve odak
Report radio grubu kategori adı, selected durumu ve tek seçim anlamını taşır. Busy durumda seçim ve gönderim etkileşimi kapalı; görsel seçim korunur. Başarı/hata bir kez anlamlı canlı bölge duyurusu; spinner metnin yerine geçmez. Ayrı engelleme sorusunda odak yeni başlığa geçer; rapor sonucunu tekrar gönderim gibi okutmayın.

Kendi onayını açınca odak başlık/açıklamada; destructive butona otomatik odak/otomatik onay yok. Vazgeç geri dönünce çağıran kontrol odağını alır. İşlem başladıktan sonra geri hareketi “iptal edildi” sonucu üretmez; devam eden sonucu mevcut controller uzlaştırır. Yeniden açış çift işlem doğurmaz.

Engellenme/erişim kaldırma eski görseli ve Semantics bilgisini kaldırır; yalnız opacity ile gizleme yetmez. Yönetim listesinin minimal adı public profile erişimine dönüşmez. Settings linkleri web açacağını erişilebilir etikette bildirir. Ürün içindeki teknik durum isimleri kullanıcıya okunmaz.

Native iOS VoiceOver / Android TalkBack, sistem yazı ölçeği, klavye ve gerçek permission sheet testleri M10'da. Büyük metinde 2×2 nav uygulanabilirliği önceki kabul gereği yazılım tarafında doğrulanır. Reduce Motion'da gereksiz geçiş yok; hata/işlem bilgisi animasyona bağımlı değil.

## M10 doğrulama örnekleri
Ağ cevabı rapordan sonra kaybolur; report başarılı ama block başarısız; unblock sonrası eski chat deep-link'i; açık contact sırasında engel; own end confirm iptali; izin ret ve Ayarlar'dan dönüş; offline cihaz izin okuma; eski reminder ile check-in; silme talebi alındı fakat henüz bitmedi; reauth başarı/başarısız; auth oturumu kalkınca gerçek silme sonucu; silme çift dokunuş; iki dil uzun metin; küçük cihaz ve %200. Bunlar çalıştırılmış native test sonucu değildir.
