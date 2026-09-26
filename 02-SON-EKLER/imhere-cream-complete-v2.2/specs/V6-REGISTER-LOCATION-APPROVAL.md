TASARIMCIDAN MANAGERE MESAJ

# Sürüm 6 — kayıt ve konum tasarım kararı v1.0

> GÜNCEL EK: V6-FINAL-COPY-APPROVAL.md; TR hitabı ve uzun konum metni bu yeni ekte. Önceki kısa metni geri yüklemeyin.

2026-09-26. İncelenen kaynak: `/Users/velio/Desktop/here/imhere/docs/design-handoff.md` §0.A ilk iki satır; app/lib/screens/auth_screens.dart, location_rationale_screen.dart, request_widgets.dart ve theme/im_here_theme.dart. Uygulama deposu değiştirilmedi. Bu, tasarım/metin kararıdır; hukuki uygunluk veya Play yayın onayı değildir. Cihaz görüntüsü bu turda ölçülmedi.

## 1. Kayıt bilgilendirmesi — metin ONAY; görünüş aşağıdaki düzeltmeyle ONAY

HARBOR’un aktarılan metni korunur. Yeni onay kutusu veya kayıt düğmesini kilitleyen koşul yok. Bütün register-* durumlarında Create account düğmesinden hemen önce aynı bilgilendirme bloğu.

| Anahtar | EN | TR |
|---|---|---|
|authConsentLine|By tapping Create account you agree to the {terms} and confirm you have read the {privacy}.|Hesap oluştur’a dokunarak {terms}’nı kabul etmiş ve {privacy}’nı okuduğunuzu onaylamış olursunuz.|
|authConsentTerms|Terms of Use|Kullanım Şartları|
|authConsentPrivacy|Privacy Policy|Gizlilik Politikası|

- Gövde: Geist helper14/400, satır1.4, #696A62. Bağlantı: aynı boyut/ağırlık, #191A17 ve altı çizili. Cream #F4F1E9 üzerinde bu renk seçimi uygundur.
- 24 yan kenar; metin blok olarak kaydırılabilir form içinde. “Tek satır” tek bilgilendirme bloğu demektir; fiziksel tek satıra sıkıştırılmaz. maxLines/ellipsis/metni küçültme yok, %200 metin serbest sarılır.
- **Düzeltme:** mevcut `_ConsentLine` TextSpan + TapGestureRecognizer yalnız glif alanını hedefliyor; 48×48 hedef eklemiyor. Her belge bağlantısını kendi en az48×48, birbiriyle çakışmayan etkileşim alanına al. Cümlenin placeholder sırası ve kelimeleri korunur; alanlar satıra sığmazsa sarılır. Örneğin aynı metin akışında WidgetSpan ile padding’li bağlantı kullanılabilir; büyük metinde taşma olmayacak. Ekran okuyucuda iki ayrı link adı ve eylemi korunur, cümle iki kez okunmaz. Bu uygulama yaklaşımı önerisidir; ölçü/erişilebilirlik sonucu zorunludur.
- Bilgilendirme bloğu → Create account arası16; hata metni ve form alanlarıyla mevcut akış korunur. Açılan belge mevcut Ayarlar yükleyicisini kullanır; hata/offline kurtarma yolları korunur.

Metin tasarımcı bekleyişi kapanabilir; bağlantı hedefi düzeltmesi Code doğrulamasına taşınır. Mevcut çizimi koşulsuz uygun diye işaretlemeyin.

## 2. Konum açıklaması — metin ve tarif edilen yerleşim ONAY

| Anahtar | EN | TR |
|---|---|---|
|checkInTitle (mevcut)|Check-in|Check-in|
|locationPermissionRationale|Your location is verified only when you start or renew a check-in. It isn’t tracked in the background.|Konumun yalnızca sen check-in başlattığında veya yenilediğinde doğrulanır. Arka planda takip edilmez.|
|locationRationaleContinue|Continue|Devam|

Başlık mevcut sayfa başlığı stilinde; gövde Geist body16/400, satır1.6, Ink#191A17. Yan kenar24; başlık-gövde16, gövde-Continue24. Düğme mevcut birincil Ink/açık metin, yarıçap12, en az48 yüksekliğinde; kullanılabilir içerik genişliği kadar. SafeArea ve kaydırma korunur; büyük metinde gövde ve düğme kesilmez.

Tek içerik eylemi Continue; ek Not now/çıkış düğmesi tasarlanmıyor. Sistem geri rıza değildir; kapı davranışı Founder kararı olarak aynen korunur. Açıklama ekranının kendisi konum okundu/izin verildi başarısı göstermez. HARBOR daha uzun metin seçerse yeni uzunluk için yerleşim tekrar kontrol edilir; bu onay yalnız tabloda yazan metindir.

## Delta / uygulama

`l10n/v6-register-location-patch_en.arb` ve `_tr.arb`: beş anahtar + metadata; mevcut checkInTitle yeniden tanımlanmaz. Placeholder adları terms/privacy değişmez. Tam ARB üzerine yazılmaz. kPendingDesigner uygulama listesine Code bu kararı aktarır; tasarım deposundaki teslim uygulama listesini kendi başına boşaltmaz.

Code kontrolü: kayıt bağlantıları iki dilde100/%200 ölçekte48×48 ve çakışmasız; odak/link semantiği; form ve Continue taşmasız; geri ile izin/rıza tetiklenmez. Yeni cihaz/Play testi bu teslimde yapılmadı.

## Mağaza işi ayrı teslim

Emoji var; linkler tıklanamaz düz metin teyidi alındı. Onaylanan tüm mağaza metinlerinin SVG/PNG yeniden üretimi ayrı commit ile takip edilir; bu sürüm6 teslimi mağaza varlıklarını değiştirmez.

Yerel commit; aktarım Code. Yeni ürün davranışı yok.
