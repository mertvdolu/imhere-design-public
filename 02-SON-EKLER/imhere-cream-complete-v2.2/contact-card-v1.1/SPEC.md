# Sürüm 9 · İletişim kartı tamamlayıcı teslim v1.1

TASARIMCIDAN MANAGERE MESAJ

Öncelik sürüm9; v10 uygulamasına bağımlı değildir. contact-card-v1.0'daki ilk onay, boş gönderim ve sonraki gönderim kuralları korunur. Bu ek dört eksik parçayı ve ilgili sonuç/hata durumlarını tanımlar. Native uygulama dosyaları değiştirilmedi.

## 1. Kendi profilinde kart bölümü

Mevcut kendi profil içeriğinin ardından24 dp; başlık contactCardTitle18/500;8 dp altında contactCardProfileHelp14/400/1.4;12 dp altında Edit card ikincil küçük düğme. Yeni çevre kartı/kocaman dolu blok yok. Alan değerleri burada tekrar listelenmez. Başkasının profilinde bu bölüm, alanlar ve düzenleme girişi hiç oluşturulmaz; gizlenmiş kart yer tutucusu bile yok.

Yardım: en az bir telefon/e-posta/Instagram bilgisi; göndermeden önce yalnız sahibi görebilir. Kaydetmek paylaşmak değildir. Kart alıcısının aldığı kopya, sahibinin profilini herkesin görebildiği bir iletişim profiline dönüştürmez.

## 2. Kart düzenleme

Başlık → yardım → Phone → Email → Instagram → Save card → sonuç/hata satırı. Sayfa kenarı24; alanlar arası24, etiket-alan8. Body16/400/1.6; alan min48, kenar inputBorder1, dolgu input, radius12. Telefon klavyesi/email klavyesi native; Instagram metin. Yeni telefon formatı, regex, ülke seçici veya doğrulama kuralı icat edilmez; Code mevcut doğrulamasını kullanır. Hatalar contactFieldInvalid ile alanın altında.

Kart okuması başarıyla kartın hiç olmadığını bildirirse giriş e-postası yalnız taslağa ön doldurulur. Mevcut kartın boş e-postası sonradan yeniden doldurulmaz. Okuma hatası kart yokluğu değildir: contactLoadFailed + Try again. Okunurken contactLoading +24×24/1.8 spinner. Kullanıcı giriş e-postasını silebilir/değiştirebilir; telefon veya Instagram yerine geçebilir. Yeni kimlik doğrulama e-postası değişmez; arka planda otomatik kayıt/gönderim yok.

### Talep ile mevcut kod arasındaki fark

Bu teslimde Manager'ın “en az1 alan dolu olmalı” talebi düzenleme için de uygulanmıştır: trim sonrası bütün alanlar boşsa Save card pasif; yardım satırı koşulu açıklar. Mevcut contact_card_screens.dart _kaydet boş haritayı servise gönderebiliyor; Code bu farkı açıkça ele almalı. HARBOR §D eski önerisi yalnız gönderme anını zorunlu kılıyordu. Bu teslim onboarding'i zorunlu yapmaz, yeni veri toplamaz. Kartı tamamen boş kaydetmenin ayrıca korunması istenirse ürün kararı Manager tarafından netleştirilmeli; tasarımda sessizce iki farklı kural uygulanmamalı.

Kaydet sürerken ikinci istek yok; düğme pasif, yanında mevcut24 spinner; “Sending your card” KULLANILMAZ (bu paylaşım değil). Başarı contactCardSaved yalnız sunucu onayında, düğmenin altında8; otomatik ekran kapatma/sohbet gönderimi yok. Hata contactCardSaveFailed aynı konumda; taslak kalır, Save tekrar kullanılabilir. Yeni düzenlemede eski başarı/hata satırı temizlenir. Offline mevcut hata/offline metni, aynı yeniden deneme davranışı.

## 3. Sohbette kart girişi

Açık sohbet üst çubuğu: mevcut geri/karşı taraf kimliği ve Safety korunur; Continue'nun HEMEN SAĞINDA Material contact_page_outlined. Simge22, çizgi mevcut Material; hedef48×48. Tooltip + erişilebilir ad contactCardTitle. Düğme kart göndermez, mevcut önizleme/onay akışını açar. İstek aşamasında yok. Dar ekran ve büyük metin: eylemler küçülmez; başlık gerekirse alt satıra alınır, fotoğraf/isim elipsiyle anlam kaybı yaratılmaz.

Karşılıklı devam durumunda: mevcut salt-okunur ve geçerli saklama bilgisi → küçük birincil Contact card. Composer yok. Bu eylem için ikinci bir üst bar kart düğmesi tekrarlanmaz. Mevcut ilk gönderim onayı korunur; karşı tarafın onayı istenmez. Closed/blocked/report sonrası uygunluk kontrolünü mevcut ürün durumu belirler; yeni gönderim hakkı oluşturulmaz.

Gönderim sürerken contactCardSending, Send pasif. contactCardSendFailed başarısızlığı bildirir, mevcut güvenli retry davranışı kullanılır; kendi kendine tekrar yok. contactCardChanged başarı bildirimi değildir: sürüm değişti, gönderim tamamlanmadı. Güncel dolu alanlar yeniden gösterilir; yeni Send gerekir. İlk gönderimde tam HARBOR onayı; sonraki gönderimde sabit warning aynen kalır.

## 4. Sohbette kart satırı

Gelen: Received14/500 → yalnız dolu alan etiket/değerleri → Report ikincil48 hedef. Dolu alan sırası Phone/Email/Instagram; boş alan çizilmez. Kopya aldığı anda gönderilmiş değerleri gösterir; sahibinin daha sonra düzenlediği kartla sessizce değişmez. Değerler selectable text, uzun e-posta/handle sarılır; kısaltılmaz. Yeni telefon arama/mailto/Instagram derin bağlantısı tasarlanmıyor.

Giden: Sent14/500 + gönderilmiş dolu alanlar. Sağdan hizalı yüzey; gelenle aynı okunaklı açık surface. Sent yalnız sunucunun kabul ettiği gönderim içindir; okundu/görüldü/karşı cihaz teslimi iddiası değil. Giden kendi kartında Report yok. Received ve Sent renk dışında metinle ayrışır.

Surface#FCFAF5, Ink#191A17; border#D9D5CB dekoratif1, radius15,padding16; arada12. Alan etiketi14/400 secondary, değer16/400. Report mevcut şikâyet akışına bu kart/sohbet bağlamıyla gider, otomatik engel/onay davranışı eklenmez.

## HARBOR önceliği — §H son hal

§H, §G'nin30 gün şikâyet istisnasını açıkça geçersiz kılar:
- Şikâyet önce: gönderilmiş kart kopyaları şikâyet dosyasıyla90 gün; karşı taraf göremez; sonra silinir. Sonradan engelleme kanıtı silmez.
- Herhangi bir şikâyetten önce engel: aradaki kart kopyaları hemen silinir. Sonraki şikâyet silinmiş kopyayı geri getirmez; mesajlar kanıt olarak tutulur.
- Diğer durum: sohbet yazılamaz olduktan30 gün sonra gönderilmiş kopyalar silinir.
- Sahibinin kayıtlı kartı ayrı veri: değiştirene/kaldırana/hesabı silene kadar.

Bunlar teslim kaynağının davranış notlarıdır; yeni hukuki metin veya backend doğrulaması değildir. Alıcının önceden görmüş/kopyalamış olabileceği bilgiyi geri alamayız: §E tam onay ve “Sent details can't be taken back.” uyarısı aynen. Uygulama içi kopyanın silinmesini “daha önce görülmemiş oldu” gibi sunmayız. Bu12 anahtara yeni süre vaadi eklenmedi.

## Boyut, erişilebilirlik, hareket

Küçük buton label14/500; yatay16/dikey8 görünür dolgu, gerçek hedef en az48×48. Düzenleme ve uyarılar scroll akışında; alt sabit blok metni örtmez. System text200%: metin sarılır, buton büyür, font küçültülmez. EN/TR ve iOS/Android aynı hiyerarşi; native safe area/geri/klavye Code'da. Yeni animasyon/bağımlılık yok. Busy spinner mevcut bileşen. Durum metni polite live region; hata ilgili alanla ilişkilendirilir; kartın alanları ekran okuyucuda etiket+değer olarak gruplanır.

Bu ek v10 cam alt menüsünü sürüm9'a taşımıyor. Önizleme ekran/kart kesitidir; mevcut uygulama kabuğu korunur. v10 geldiğinde aynı bileşen ölçüleri o kabukla kullanılabilir.

## Dosyalar / birleştirme

- ONIZLEME.html + style.css + copy.js:16 seçilebilir örnek, EN/TR,320/390/412,100/200.
- ../l10n/contact-card-complete-patch_en.arb + _tr.arb: tam12 istenen anahtar, Code isimleri aynen. Mevcut yer tutucu kopyalar yeni deltadan güncellenir; tam ARB üzerine yazılmaz.
- Eski contact-card-v1-patch anahtarları korunur. Tam onay ve sent-warning byte eşitliğinde doğrulanır.
- catalog.json: tamamlayıcı durumlar. Ana tarihsel SVGler yeniden üretilmiş sayılmaz.
- validation.json: dosya ve tarayıcı kontrolleri; native cihaz testleri ayrı.

Code kontrolü: own/other ayrımı; exists=false ön doldurma; read failure; boş kaydetme farkı; invalid/saved/failure/busy; üst çubuk sırası48 hedef; mutual read-only; Received/Report + Sent; değişmiş kart sürümü ve onay; §H görünürlük/retention testleri. Referans/private kaynak belgeleri depoya kopyalanmadı.
