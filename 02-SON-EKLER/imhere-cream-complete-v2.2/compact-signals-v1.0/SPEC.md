> **Güncel yüzey dili: Cream & Ink v2.3 / hafif kabartma.** Ölçü ve davranışlar bu belgede; yüzey uygulaması `theme-v2.3/SPEC.md` ve ortak tokenlarda.

TASARIMCIDAN MANAGERE MESAJ

# Sürüm8 — kompakt oran ve okunmamış nokta v1.0

Kapsam: yalnız iki yeni öğe. Genel düğme/ekran sıkılaştırması bu teslimde yapılmadı. Kaynak: Manager’ın bu isteği; Code docs/surum8-plan.md Plan C ve design-handoff §0.A okunmamış nokta satırı. Plan C’nin “en güvenli yorum” olarak işaretlediği ürün davranışları aşağıda aynen korunur; burada yeni ürün kuralına dönüştürülmez.

## 1. Profil oran göstergesi

Kendi/başkasının profilinde mevcut profil bilgilerinin devamında, ilgi alanlarından önce çerçevesiz tek satır:
EN Networking 60% · Friends 40%
TR Networking %60 · Arkadaşlık %40
Örnek60/40 yalnız önizleme değeridir; canlıda sunucunun mevcut değeri kullanılır. Tamamlayanı100−Networking. Ayarlanmamışsa bütün satır gizli; boş yer, sahte50/50, yüzde0 yok.

Geist helper14/400/1.4, Ink#191A17; üst/alt8 dp. Kart, rozet, grafik, pasta veya ilerleme çubuğu yok. Metin büyütmede gerekirse iki satıra sarılır; sayı kesilmez ve font küçültülmez. Gösterge etkileşimli değil, yanında yeni büyük Düzenle düğmesi yok. Ekran okuyucu yüzdeyi ve iki etiketi birlikte okur; başarı/uyumluluk puanı diye sunulmaz.

## 2. Mevcut ayar/profil düzenleme ekranında tek kaydırıcı

Başlık18/500: Networking and friends / Networking ve arkadaşlık. Altında8 dp güncel oran14/400; altında kaydırıcının48 dp yüksekliğinde etkileşim alanı. Toplam içerik yaklaşık100–120 dp; yeni çevre kartı, büyük açıklama veya ayrı kaydet düğmesi yok. Mevcut ekranın kaydetme/commit akışı korunur; otomatik kayıt icat edilmez.

0 solda Friends,100 sağda Networking; 10’ar adım,11 durak. Görsel ray2 dp, aktif Ink, pasif inputBorder#7C7D73; tutamak16 dp Ink. Gerçek hedef en az48×48; küçük tutamak hedefin kendisi değildir. Uçlarda14/400 metin; büyük yazıda satıra sarılabilir. Native Slider kullan; yeni bağımlılık yok.

Kaydırıcının erişilebilir adı Networking percentage / Networking yüzdesi; değeri her iki oranı içerir. Artır/azalt10; klavye ve ekran okuyucu ile erişilebilir. Sayı önizlemesi gecikmeden değişir; dekoratif yay/haptik eklenmez. Hareketi azalt aynı görünüm.

Ayarlanmamış giriş: Not set / Ayarlanmadı; yayımlanmış oran gösterme. Native kontrolün geçici tutamak pozisyonu kaydedilmiş veri değildir. Kullanıcının ilk bilinçli ayarlaması, aynı konuma dokunsa bile taslak değeri belirler; hiç dokunulmazsa payload’a alan eklenmez. Varsayılan profil oranı oluşturma. Alanı temizleme/gizleme eylemi eklenmedi; kaynakta istenmemiş.

## 3. Okunmamış nokta

Founder’ın kırmızı nokta isteği bu öğeye özgü renk istisnasıdır: `colors.notificationUnread = #B63A32`. Harita densityRed kullanılmaz ve dört density token’ı değişmez. Bu renk yeni genel vurgu/hata/düğme rengi değildir.

- Sohbet/bağlantı satırı SAĞ: çap8 dp. Varsa chevron’ın12 dp solunda, satırın dikey merkezinde; yoksa mevcut sağ iç kenarda. Yeni satır yüksekliği yaratmaz. Ayrı dokunma hedefi değil; sohbet satırının hedefi korunur.
- Alt Messages: mevcut simgenin sağ üst köşesinde8 dp; çevresinde2 dp mevcut navigasyon yüzeyi halkası.24 dp ikonun sağ üst köşesi noktanın merkezi için ankrajdır. Sekme etiketiyle çakışmaz; 48 dp sekme hedefinin dışına çıkmaz. Büyük yazıda2×2 navigasyonda aynı ikon ankrajı.
- Sayı, titreşim, yanıp sönme veya büyüme yok. Hem okunmuş/okunmamış ikon geometrisi aynı; nokta gerçek okunmamış bilgisine göre var/yok.
- Ekran okuyucu: satırın mevcut adı + “Unread messages” / “Okunmamış mesaj”; sekmede “Messages, Unread messages”. Noktanın ayrı semantics düğümü yok. Okunmuşta ek ifade yok.
- Kaynak davranışı korunur: sohbet açılıp mesajlar gösterilince ilgili durum temizlenir; açık bağlantılarda herhangi bir okunmamış varsa sekme noktası kalır. Sekmeye dokunmak bütün sohbetleri okunmuş yapmaz. Bu tasarım karşı tarafa okundu bilgisi sunmaz.

## Dosyalar ve sınırlar

ONIZLEME.html: EN/TR,320/390/412 genişlik ve%200 metin, ayarlanmamış/0/50/100 oranları; okunmuş/okunmamış örnekleri. Demo oranı canlı veri değildir. catalog.json ek katalog; ana eski ekran SVG’leri yeniden çizilmiş sayılmaz. tokens.json yeni ölçüler, theme.tokens.json notificationUnread rengi. ARB delta5 anahtar; messagesUnread mevcut adı korunur, diğer isimler Code’da varsa migration ile eşlenir. Tam ARB üzerine yazılmaz.

Native uygulama değiştirilmedi; cihazda taşma/semantics doğrulaması Code’da. Yerel commit; aktarım Code.
