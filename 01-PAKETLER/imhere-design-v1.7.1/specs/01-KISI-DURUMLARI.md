# 01 — Kişi görünümü ek durumları
## Korunan yapı
v1.6 kabul edilmiş başka kişi profili: tek fotoğraf, ad, görünürse yaş/cinsiyet/meslek, bio, ilgi alanları ve konuşulan diller. Profil görünümünün altındaki mevcut `requestSend` / “Bir merhaba gönder” etiketi korunur. M10 hedefinde Yakındakiler bağlamı ve kabul edilmiş dört sekme sırası aynı; M06'nın tam ekran rotası bu ekle yeniden yazılmaz.

Ekte her durum görünür ve üç alanı gizli örnekle çizilir. Bu iki fixture uç örnektir; yaş/cinsiyet/meslek gerçekte birbirinden bağımsız gizlenebilir. Gizli alana boşluk, maske, “gizli” rozeti veya erişilebilir metin konmaz. Doğum tarihi ve türetilerek bulunan gizli yaş kullanılmaz; yalnız izinli public DTO alanları.

## Durumlar
| Durum | Ana eylem | Altındaki metin | İkincil eylem |
|---|---|---|---|
| Cooldown | `requestSend`, pasif | `requestCooldown`: Şu an bu kişiye istek gönderilemiyor. | Ek CTA yok; mevcut geri/navigasyon kullanılabilir |
| Bekleyen istek | `requestSend`, pasif | `requestAlreadyPending`: Bu kişiyle bekleyen bir istek var. | `messagesViewRequest`: İsteği görüntüle |
| Mevcut bağlantı | `requestSend`, pasif | `requestAlreadyConnected`: Zaten bağlantıdasınız. | `messagesReturn`: Mesajlara dön |

Metin pasif düğmenin **altında**, 14 gövde/yardımcı metin stiliyle; kırmızı hata veya cezalandırıcı simge yok. Pasif CTA mevcut disabled bileşenle gösterilir. Süre, bitiş tarihi, neden, kim reddetti/iptal etti, tekrar deneme zamanı veya “yakında” vaadi yok. Accessibility açıklaması da aynı nötr metindir. Düğme dokunma/klavye/ekran okuyucu eylemiyle niyet seçiciyi açmaz.

## Verinin otoritesi ve gizlilik
- Cooldown yalnız gerçek `COOLDOWN_ACTIVE` sonucu sonrası gösterilir. Mevcut M06 akışı niyet ekranından kişi görünümüne bu sonuçla döner; sunucu cooldown'u önceden bildirmediği için tasarım yeni bir ön sorgu, yerel süre hesabı veya kalıcı sayaç istemez. Ekrana yeniden girişte uygunluğu sunucu belirler; cihaz saatiyle “artık gönderebilirsin” sonucu çıkarılmaz.
- Bekleyen durum yalnız gerçek, güncel ve erişilebilir isteğe dayanır. Alıcı/gönderen yönü metinde ima edilmez. İsteği görüntüle mevcut yönüne göre gelen inceleme veya giden bekleyen ayrıntısına gider; otomatik kabul, otomatik seçim veya yeni istek yok. Geçerli hedef elde yoksa bu yönlendirme varsayılmaz; mevcut yükleme/erişimsizlik davranışı kullanılır.
- Mevcut bağlantı yalnız doğrulanmış, erişilebilir ve kapanmamış bağlantıya dayanır. **Generic `STATE_CHANGED` hatasından “zaten bağlantıdasınız” çıkarılmaz.** Bu hata başka nedenler taşıyabilir. M06'nın genel hata akışı bu çizimle bilgi ifşa eden özel sonuca dönüştürülmez. M06'da Sohbete geç gizli kaldığı için CTA Mesajlara dön'dür; M07 özelliği bu ekle açılmaz.
- Cooldown, pending ve connected ekrandaki alternatif durumlarıdır; birden çok rozeti üst üste yığmayın. Öncelik ve yarış sonucunu mevcut sunucu/istek/bağlantı sözleşmesi belirler, tasarım yeni durum makinesi icat etmez. Erişim kaldırma/engel/hesap kullanılamıyor mevcut nötr erişimsizlik görünümünü uygular; bu ek kişiyi göstermeye devam etme izni değildir.

## M06 yerleşim farkı
Okunan `other_profile_screen.dart` nötr notu düğmenin üstüne koyuyor; `design-handoff.md` §7 düğmenin altını tarif ediyor. **Bu tasarım eki §7'deki alt yerleşimi esas alır.** Manager'a bildirilecek görsel hizalama; iş kuralı değişikliği değildir. Kod bu teslimde değiştirilmedi. Mevcut `other-profile-screen`, `btn-request-send`, `request-cooldown` widget Key'leri localization anahtarlarından ayrıdır; uygun yerleşime taşınırken korunur.

## Büyük metin ve durum kapsamı
Her durum %200'de gerçek 2× font, çok satıra büyüyen açıklama/buton ve kaydırılabilir gövdeyle çizildi. Font kısılmaz; normalde 4'lü, büyük metinde kabul edilmiş 2×2 ana navigasyon. Görseller tam içerik, native referans 390×844 / 412×915.

Bu küçük ek yeni yükleme/boş/offline/hata akışı tanımlamaz: v1.6 profil yükleme/boş alan/gizleme/hata/offline/erişimsizlik ve v1.7 işlem sonuçları devralınır. Çevrimdışılık cooldown sayılmaz; eski cache güncel pending/connection kanıtı değildir. Durum dönüşünde nötr mesaj bir kez duyurulur; odak pasif bir eyleme zorlanmaz. Native TalkBack/VoiceOver ve M10 nav uygulanabilirliği cihazda doğrulanacak.
