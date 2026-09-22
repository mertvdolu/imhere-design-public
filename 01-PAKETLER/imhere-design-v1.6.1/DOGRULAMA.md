# v1.6.1 — Kontrol ve sınırlar

- Kanonik auth dosyaları yazılımcının 19 anahtarını birebir içeriyor; TR/EN eşit. Tam referans sözlükler 334'er anahtar. Altı eski ad alias eşlemesinde; eşleşmeyen 28 UI adı migration uyumluluk kayıtlarında ve tam sözlüklerde aynı metinle korunuyor.
- Parola kuralı normal ve %200 TR/EN çizimlerinde alan altında tek satır. Karakter türü şartı ve güç göstergesi yok. Başarısız girişte parola zayıflığı/hesap yok ayrımı gösterilmiyor.
- 14 değişen durum ve 3 yeni hata sunumu; 136 SVG ve 34 PNG. Yazıların tuval sınırları, dosyaların açılması ve parametreler kontrol edildi. Normal ve büyük metin örnekleri gözle incelendi.
- Kayıtlı ve kayıtsız adres reset sonuçları aynı anahtara bağlı. Deneme sınırı metni sayı, süre veya eşik içermiyor. Sıfırlama isteğinin gerçek ağ/işlem hatası ayrı kalıyor.
- Kabul edilen v1.6 paketindeki dosyalar kendi teslim manifestine göre değişmedi. Profil sözleşmeleri, token/fontlar ve kabul eki aynı. Profil görselleri bu patch'te yeniden üretilmedi.
- Yerel önizlemenin dil/platform/metin/grup filtreleri ve resim yüklemesi kontrol edildi. Kontrol çıktıları evidence klasöründedir.

Tasarım Gereksinim Özeti v1.0.2 okundu; §2 auth akışıyla uyumlu. Kaynak dosyanın SHA-256 kaydı ve referans kopyası pakettedir.

Bu kontroller statik tasarım dosyalarına aittir. Uygulama/backend kodu, canlı ARB'ler ve Firebase ayarları değiştirilmedi; gerçek kullanıcı hesabı veya reset e-postası oluşturulmadı. Native klavye/parola yöneticisi, VoiceOver/TalkBack, auth entegrasyonu ve cihaz doğrulaması M10 yazılım aşamasındadır. Backend hata kodları burada icat edilmedi.
