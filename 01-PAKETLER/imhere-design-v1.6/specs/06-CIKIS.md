# 06 — Profil / Ayarlar / Çıkış
Talep edilen giriş noktası **Profil → Ayarlar → Çıkış yap**. Kabul edilen profil ekranları değiştirilmeden bırakılmıştır. `logout-*` ekranları yalnız Ayarlar altındaki çıkış bölümünü gösterir; tam Ayarlar menüsü veya onay bekleyen başka ayarlar olarak yorumlanmaz. Mevcut Ayarlar görünümüne bu bölüm eklenir; M10'da Ayarlar rotası Profil bağlamından açılır. Ayarlar yeni bir alt sekme olmaz; kabul edilen dört sekme ve sırası korunur. Yerel tema temelindeki geçici üç sekmeli geliştirme kabuğu ürün navigasyonu için kaynak alınmaz.

- `logout-ready`: Çıkış yap eylemi etkin. Profil sekmesi seçili. Önceki onaydan bağımsız yeni bir “hesabı sil” veya güvenlik ayarı yok.
- `logout-busy`: Mevcut çıkış işlemi sürer; eylem pasif, “Çıkış yapılıyor…” açıklaması vardır. Çift istek yok.
- Başarı: Gerçek auth state oturum kapalı olduğunda mevcut karşılama/giriş rotasına dönülür; geri gezinme korunan hesabın ekranını göstermez. Yeni bir başarı ekranı gerekmez.
- `logout-failed`: Gerçek işlem sonucu başarısızsa hata + tekrar kullanılabilir Çıkış yap. Kullanıcıya kapandı denmez. İşlem hata bildirse de auth state zaten kapalıysa gerçek kapalı oturum esas alınır.
- `logout-offline`: Offline açıklaması görünür; Çıkış yap etkin kalabilir. Yerel sağlayıcı çıkışının internet gerektirip gerektirmediğini tasarım değiştirmez; işlem sonucu belirleyicidir. Yeni ağ önkoşulu eklenmez.

Çıkış düğmesi kendi başına check-in sonlandırıldı, bağlantı kesildi, veri silindi veya gizlilik tercihi sıfırlandı iddiası taşımaz. Mevcut backend/session işlemleri korunur. Yeni onay diyaloğu ya da farklı iş kuralı dayatılmaz. Önceki `endConfirm` kabulü bağlantıyı sonlandırma işlemine aittir; bu çıkış eylemiyle karıştırılmaz.

TR/EN, iOS/Android ve %200 metin sürümleri vardır. Büyük metinde tab sırası Profil → Mesajlar → Yakındakiler → Etkinlikler 2×2 devam eder; native uygulanabilirlik M10 yazılım kontrolündedir. Çıkış kontrolü48+ hedef, açık etiket ve işlem/hata anonsu taşır.
