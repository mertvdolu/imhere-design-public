# ikonlar — Code handoff

Önce SPEC + SCREEN-STATE-MATRIX. Copy dosyası inceleme/eşleme kaynağıdır; canonical ARB üzerine yazılmaz. Anahtarın onaylı kaynağı COPY-REVIEW’de. Başarı yalnız sunucu/işlem sonucu onayından sonra.

SVG’ler assets/svg altında; Flutter yerleşik CustomPainter ile aynı path koordinatları çizilebilir, SVG runtime bağımlılığı ekleme. Hedef en az 48; görünen simge 16/20/24, boşlukla hedef. Kategori simgesi decorative; aynı etiket okunur. Topluluk düğmesi a11y label/hint kullanır.

Flutter: SafeArea + ScrollView, doğal metin ölçüsü, yerleşik animasyon/CustomPainter. Yeni bağımlılık yok. Ekran okuyucuda H1 header, link link, tek seçim radiogroup; decorative icon excludeSemantics. Önizleme kabuğu OS cihaz testi değildir. Code VoiceOver/TalkBack, native Dynamic Type, Android font ölçeği, gerçek URL açıcı/ağ/yanıtları ayrıca ölçer.
