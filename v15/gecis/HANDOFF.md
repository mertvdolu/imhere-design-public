# gecis — Code handoff

Önce SPEC + SCREEN-STATE-MATRIX. Copy dosyası inceleme/eşleme kaynağıdır; canonical ARB üzerine yazılmaz. Anahtarın onaylı kaynağı COPY-REVIEW’de. Başarı yalnız sunucu/işlem sonucu onayından sonra.

K-L2: eski link, geçiş gösterilmeden bağlantılar/filtrede açılmaz. Mevcut üyelik kaydından geçiş adımı ilerletilir; kullanıcıdan tahmin yapılmaz. Hata görünürlük Everyone değerini geri getirir; ekran kapanmaz. Offline genel offline metni. Uzun açıklama ve seçenekler tek ScrollView; alt eylemler içeriğin sonunda, tümüne erişilir.

Flutter: SafeArea + ScrollView, doğal metin ölçüsü, yerleşik animasyon/CustomPainter. Yeni bağımlılık yok. Ekran okuyucuda H1 header, link link, tek seçim radiogroup; decorative icon excludeSemantics. Önizleme kabuğu OS cihaz testi değildir. Code VoiceOver/TalkBack, native Dynamic Type, Android font ölçeği, gerçek URL açıcı/ağ/yanıtları ayrıca ölçer.
