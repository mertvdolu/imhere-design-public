TASARIMCIDAN MANAGERE MESAJ

# Founder dev turu — H2 / H7 / H9 / H3

## H2 — Geri

Üst sayfası olan alt ekranlarda sol üst 48×48 geri hedefi; simge24, çizgi1.8, semantik/tooltip Back / Geri. Marka işareti bu alt ekranların üst çubuğunda geri düğmesine yer açar. Aynı gezinme eylemi iOS kenar kaydırma ve Android sistem geri ile çalışır. Geçerli önceki rotaya dönülür; ana sekmelerin köklerine yapay geri rotası eklenmez. Form/işlem devam ediyorsa mevcut iptal, taslak ve bekleyen işlem kuralları korunur; geri hareketi başarı veya iptal sonucu uydurmaz. Native kaydırmayı ayrıca tween ile oynatma.

**Founder teyitli istisna:** doğrulama, davet-tekrar ve ilk profil kurulumunda geri dönüş yok; mevcut authSignOut korunur. İlk profil formundaki eski görsel Back izi de kaldırıldı. Ortak form hata/busy durumları düzenleme bağlamında açılıyorsa mevcut üst form rotasının geri davranışını kullanır. Kendi profilinin sekme kökü geri düğmesi gerektirmez; başka profiller ve profil düzenleme alt sayfadır.

## H7 — Sohbet

(a) chat-empty içindeki chatEmptyBody kartı kaldırıldı. Anahtar silinmez; kullanılmayan eski metin olarak korunur. Bu karta bağlı empty-breathe hareketi de kaldırıldı.

(b) Composer bulunan dokuz durumda Send yazılı düğme yerine kutunun İÇİNDE sağ altta yukarı ok: simge24, hedef48×48, sağdan8, altta8. Mesaj metninin altında56 birim ayrılır; taslak simgenin arkasına girmez. Mevcut iç kaydırma/500 karakter sınırı ve gönderim uygunluğu değişmez. Erişilebilir ad EN Send / TR Gönder, mevcut chatSend; pasif/işleniyor durumları korunur. Başarı yalnız sunucu onayıyla. Composer, sayaçlar ve içindeki Send birlikte OS viewInsets üzerinden klavyeyi izler.

(c) **DESIGN RECOMMENDATION — FOUNDER APPROVAL REQUIRED**
Sayaçları yalnız son5 mesaj / son50 karakterde göstermek öneridir. Bu teslim sayaçları gizlemez veya eşik uygulamaz. Founder eşiği ve kapsadığı durumları onaylayana kadar mevcut görünürlük sürer. Önerilen uygulamada da 500 sınırı, son hak ve hata bilgileri kaybolmamalıdır.

## H9 — İletişim paylaşım daveti

Yeni durum: chat-contact-invite (TR/EN, iOS/Android, %100/%200). Salt okunur/contact-eligible sohbetten türetilmiştir; yeni bir karşı karar bilgisi açığa çıkarmaz.

EN chatContactSharedInvite: {name} shared their contact details. You can share yours if you’d like.
TR: {name} iletişim bilgilerini paylaştı. İstersen sen de paylaşabilirsin.
EN chatContactShareMine: Share my details
TR: Bilgilerimi paylaş

Kart yalnız sunucu karşı tarafın o anda paylaşılan bilgisi olduğunu doğruladığında, kullanıcının kendi paylaşımı boşken ve mevcut form erişimi varken görünür. Paylaşım geri çekilirse veya erişim kaybolursa kaldırılır. Çözülmemiş/yükleniyor veriden paylaşım sonucu çıkarılmaz. Tek düğme contact-empty formuna gider; otomatik paylaşmaz. Kartı kullanmak zorunlu değildir; modal, geri sayım veya bildirim yok. Örnek ad Deniz; çalışma anında gerçek profil görünen adı {name} olur.

## H3 — Profil kaydından dönüş

Mevcut profil düzenleme bağlamında sunucu kaydı doğruladığında düzenleme rotasını kapat ve güncel görünürlükle view-own-visible/hidden göster; ikinci bir profil rotası ekleme. 0ms: doğrulanmış veri hazır, kayıt başarılı; 0–150ms: görünüm opacity0→1 lineer. Yay/ölçek/Hero/titreşim eklenmez. Hareketi azalt: aynı150ms opacity. Hata/bekleme: form ve taslak korunur, erken dönüş yok. İlk kurulumun mevcut tamamlama kapıları atlanmaz. Motion v1 own-profile-edit ile uyumludur; profile-save-return notu eklendi.

## Dosyalar

- Katalog: contracts/screen-manifest.json ve repo kökü EKRAN-KATALOGU.json
- Metin ekleri: l10n/dev-tour-h-patch_en.arb / _tr.arb; yalnız iki anahtar ve metadata birleştirilecek, tam ARB üzerine yazılmayacak.
- Motion: motion/hareket-ve-his-v1/screen-motion-map.json
- H7(c) öneri olarak kalır; diğer maddeler uygulanmış çizim teslimidir.
- Native uygulama testi/uygulama değişikliği yapılmadı. Yerel commit; aktarım Code.
