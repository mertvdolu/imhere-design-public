# ayarlar-topluluk — Code handoff

Önce SPEC + SCREEN-STATE-MATRIX. Copy dosyası inceleme/eşleme kaynağıdır; canonical ARB üzerine yazılmaz. Anahtarın onaylı kaynağı COPY-REVIEW’de. Başarı yalnız sunucu/işlem sonucu onayından sonra.

Katılma ve kullanılmayan topluluktan ayrılma aktif topluluğu değiştirmez; check-in bitirmez. Aktif değiştirme/aktiften ayrılma check-in’i bitirir. Eski sohbetler kalır. Going hatırlatmaları sürer. Yalnız server-ack sonrası In use/Joined/Left/Done. Fail eski üyelik ve active görünür; tekrar yolu açık. Başarılı geçişte eski liste/harita/etkinlik verisini anında temizle, yeni yükleme ayrı. Joining/leaving, Switching metnini ödünç almaz; görünür yeni metin yok. settings-switch-failed ve settings-failed ayrıdır. Read fail Retry okuma isteğini yeniden dener, işlem başarısı üretmez.

Flutter: SafeArea + ScrollView, doğal metin ölçüsü, yerleşik animasyon/CustomPainter. Yeni bağımlılık yok. Ekran okuyucuda H1 header, link link, tek seçim radiogroup; decorative icon excludeSemantics. Önizleme kabuğu OS cihaz testi değildir. Code VoiceOver/TalkBack, native Dynamic Type, Android font ölçeği, gerçek URL açıcı/ağ/yanıtları ayrıca ölçer.
