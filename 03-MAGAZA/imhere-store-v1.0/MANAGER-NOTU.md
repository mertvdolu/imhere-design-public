# TASARIMCIDAN MANAGERE MESAJ

**Teslim: Mağaza görselleri v1.0 / Cream & Ink v2.2**

Konum: `03-MAGAZA/imhere-store-v1.0/`

- App Store: 6,9 inç için 1320×2868 ve 6,5 inç için 1242×2688; her sette 6 İngilizce kare.
- Google Play: aynı akışta 6 telefon karesi (1080×1920) + öne çıkan görsel (1024×500).
- Sıra: açılış/niyet, Yakındakiler, tam ekran harita, Bağlantılar, Sohbet, Profil.
- 19 opak RGB PNG; 19 düzenlenebilir SVG, yerel HTML önizleme, kaynak/üretim dosyaları, manifest ve doğrulama raporu.
- Maya ve Alex kurmaca, fotoğrafları sıfırdan yapay üretildi. Örnek içerik notu karelerde görünür.
- Haritada kişisel işaret/sayı/mesafe yok; dört renk ve attribution korunuyor. Şematik harita açıkça örnek olarak işaretli.
- Yazılabilir sohbet saklama satırı göstermiyor. İki niyet/boş başlangıç, kapalı bağlantının nötr görünümü ve son ürün kuralları korunuyor.

**Yayın öncesi:** Karelerin içindeki arayüzler v2.2 tasarım çizimleridir; native cihaz çekimi değildir. Güncel iOS/Android görüntüleriyle son karşılaştırma yapılmalı; fark varsa ekran alanı gerçek native görüntüyle değiştirilmelidir. Bu teslim uygulamayı veya mağaza kaydını değiştirmedi.

İnceleme: `ONIZLEME.html`, `review/app-store-contact-sheet.png`, `review/google-play-contact-sheet.png`.
Yüklenecek dosyalar: ilgili platform klasöründeki `.png` dosyaları; SVG/kaynak/inceleme dosyaları mağazaya yüklenmez.

## Güncel Google Play simgesi

Mağaza yüklemesinde [google-play/app-icon-512.png](google-play/app-icon-512.png) kullanılır: **512×512, RGBA**, güncel Cream & Ink v2.2 simgesinin yeniden boyutlandırılmamış, yeniden kodlanmamış birebir kopyası. Paket 19 tanıtım karesi + 1 uygulama simgesi içerir. Eski A-wordmark ve B-symbol kullanılmaz.
