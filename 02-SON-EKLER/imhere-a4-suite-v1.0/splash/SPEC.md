# Yerel açılış ekranı

Zemin #17251D; işaret #C3F5CE. B-symbol merkezde, görünür genişlik yaklaşık 128 mantıksal birim; 288×288 şeffaf varlık kutusu içinde. iOS 390×844 ve Android 412×915 çizimleri yerleşim referansıdır. Telefon adı IM HERE olarak kalır; ekranda yazı, slogan, düğme, progress veya yükleme yüzdesi yok. Bu nedenle TR/EN ve büyük yazı aynı görünümü kullanır.

iOS: launch-mark varlığı ortada aspect-fit olarak yerel launch screen içine bağlanır; düz zemin ayrı tanımlanır. Tam ekran önizleme PNG'si esnetilerek uygulama launch screen'i yapılmaz.
Android: launch-mark yerel splash icon varlığı olarak, 288 dp kutuda kullanılır; zemin ayrı #17251D. Uygulama ikonu karesi yerine şeffaf işaret kullanılır. Çift splash/ikinci logolu sayfa eklenmez. PNG çözünürlükleri mantıksal boyutla karıştırılmaz.

Açılış ekranı statik ve yereldir; ağ cevabı beklemek için yapay süreyle tutulmaz. İlk uygulama karesi hazır olduğunda mevcut boot akışı devralır. Ağ/sunucu başarısızlığı için önceki M10 'ulaşılamıyor + Tekrar dene' ekranı geçerlidir. Bu teslim yeni yönlendirme, bekleme süresi veya animasyon kuralı getirmez. Sistem animasyonları korunur. Önizlemeler status bar, notch veya gesture bar'ın tüm platform davranışını taklit etmez; native yerleşim Code tarafından doğrulanır.

Kaynaklar:
- https://developer.apple.com/documentation/xcode/specifying-your-apps-launch-screen/
- https://developer.android.com/develop/ui/views/launch/splash-screen
