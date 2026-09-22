# v1.6 — Doğrulama ve sınırlar

## Tamamlanan kontroller
- 66 durumun her birinde TR/EN × iOS/Android × normal/%200 varyantı var:528 SVG. SVG'ler açıldı; çizim ölçüleri, yazı sınırları ve çözümlenmemiş parametreler kontrol edildi.
- 132 PNG dosyası açılıp doğrulandı. Kayıt, doğrulama, giriş, sıfırlama ve çıkış normal görünümleri; uzun hata mesajları ve %200 EN örnekleri gözle incelendi. İncelenen örneklerde taşma veya kırpılma görülmedi.
- Yerel HTML önizlemesi66 görünümü listeliyor. Dokuz grup filtresi ve EN Android %200 görüntülerinin yüklenmesi doğrulandı; sayfa hatası görülmedi.
- Kabul edilen profilin216 SVG +54 PNG dosyası v1.5 ile SHA-256 ve byte düzeyinde aynı. Profil sözleşmeleri, profil/platform spesifikasyonları, fontlar, token'lar, görsel varlıklar ve v1.4 kabul eki aynı.
- TR/EN sözlükleri330'ar anahtar; parametre ve metadata eşitliği kontrol edildi. Önceki301 anahtardan yalnız3 auth değeri değişti,29 auth anahtarı eklendi. Profil metinleri aynı.
- Yeni kayıt/giriş çizimlerinde maskeli parola alanı bulunuyor; doğrulama ve sıfırlama isteği çizimlerinde parola alanı yok. Auth giriş ekranlarında korunan uygulama sekmeleri yok. Doğrulama ekranında sayaç veya hesap adresi değiştirme eylemi yok.

Statik kontrol ayrıntıları `evidence/validation.json`; önizleme kontrolü `evidence/preview-check.json`; korunan ekran hash'leri `evidence/accepted-profile-manifest.json` içindedir. Tek tek yazı ve dosya kontrolleri uygulama testi sayısı olarak yorumlanmaz.

## Yapılmayanlar
Flutter/uygulama/backend kodu değiştirilmedi. Firebase'e gerçek kayıt/giriş/reset/resend/çıkış isteği gönderilmedi; gerçek e-posta teslimi, native cihaz, klavye, parola yöneticisi, VoiceOver/TalkBack veya derleme testi yapılmadı. Yerel mühendislik örnekleri yalnız yöntem doğrulaması için okundu. Bu teslim UI/UX dosyalarıdır; çalışan auth entegrasyonu değildir.

## M10'a taşınacak kontrol
Mevcut Firebase/auth state ile tüm başarı/hata/henüz doğrulanmamış geçişleri; hesap oluşup doğrulama e-postası gönderilemeyen durum; backend'e bağlı tekrar gönderim; tamamlanmış profille giriş; nötr reset cevabı; gerçek oturum durumuna bağlı çıkış ve korunan geri gezinme. Mevcut parola doğrulaması ve kaynak TR/EN hata metni entegrasyonda korunur. 2×2 büyük metin navigasyonunun native uygulanabilirlik kontrolü önceki kabul notuyla yazılımdadır.

## Beklenen bilgi
Founder mevcut parola kuralı/şifre gücü açıklamasını yazılımcıdan iletecek. Kullanıcının açık isteğiyle o zamana kadar parola alanında kural açıklaması ve güç göstergesi yok. Yeni limit veya karakter şartı tanımlanmadı; mevcut doğrulama kapatılmaz. Davet edinme yolu hâlâ Founder kararı bekliyor.
