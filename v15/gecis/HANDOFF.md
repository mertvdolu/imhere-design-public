# gecis — Code handoff

Önce SPEC + SCREEN-STATE-MATRIX. Copy dosyası inceleme/eşleme kaynağıdır; canonical ARB üzerine yazılmaz. Anahtarın onaylı kaynağı COPY-REVIEW’de. Başarı yalnız sunucu/işlem sonucu onayından sonra.

Karar 58: koşul linkedinTransitionNeeded; reason FIRST veya LINK_CHANGED yalnız sahibin readProfile verisinden gelir. LINK_CHANGED, eski istemciden link değişince bağımsız yeniden gösterilir; aynı link kaydı göstermez. Kaydetme işaret/ayar başarısı server-ack ile; hata eski ayarı korur. Kapatma mevcut ayarı değiştirmez. İlk geçiş örneğinde Everyone; yeni örnekte Nobody. Alt eylemler içeriğin sonunda, uzun içerik kaydırılır.

Flutter: SafeArea + ScrollView, doğal metin ölçüsü, yerleşik animasyon/CustomPainter. Yeni bağımlılık yok. Ekran okuyucuda H1 header, link link, tek seçim radiogroup; decorative icon excludeSemantics. Önizleme kabuğu OS cihaz testi değildir. Code VoiceOver/TalkBack, native Dynamic Type, Android font ölçeği, gerçek URL açıcı/ağ/yanıtları ayrıca ölçer.
