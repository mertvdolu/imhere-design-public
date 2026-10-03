# TASARIMCIDAN MANAGERE MESAJ

## Events V1 · Cream & Ink v2.3 · tasarım eki v1.0

36 HTML durum teslimi: liste/detay, üç kategori, NONE/INTERESTED/GOING, seçim geçişi/geri çekme/hata, üçer başlangıç-kilidi/iptal/değişiklik varyantı, yükleme/boş/hata/offline/ulaşılamıyor, görsel hatası, uzun içerik, takvim/harita açılış ve hata.

**Önce:** `SPEC.md` → `SCREEN-STATE-MATRIX.md` → `ONIZLEME.html` → `COPY-REVIEW.md`.

**Konum:** `02-SON-EKLER/imhere-events-v1.0/`.

**Tasarım dalı:** `design/events-v1-cream-ink-v23`. Kaynak tema SHA: `58bf8c4380c9e2b8487b32d5d94f6f1e683ad649`. Teslim SHA commit sonrasında handoff mesajında verilir; kendi SHA'sını içeren dosya üretilmez.

### Uygulama kararları

- Yalnız kullanıcının kendi tek tercihi; başka kişi/sayı/avatar yok. Going check-in veya doğrulanmış katılım değildir.
- Başlangıçtan önce Interested ↔ Going ↔ Withdraw. Sonuç yalnız sunucu onayıyla; beklerken eski seçim korunur.
- Başladıktan sonra yalnız RSVP kilitli; iptalde bütün etkinlik eylemleri pasif. Geri ve alt menü çalışır.
- İptal listede 24 saate kadar görünür, sonra normal listeden çıkar; istemci sayaç veya arşiv eklemez.
- Değişiklikte güncel içerik ve mevcut RSVP; yeni onay zorunluluğu yok.
- Takvim tek seferlik aktarım; harita cihaz haritası. Check-in/Nearby/heatmap davranışı değişmez.
- EN/TR; iOS/Android; dar ekran ve %200; 48 hedef, gölgesiz yüksek kontrast, opak menü ve azaltılmış hareket seçenekleri.

### Metin kapısı

**52 yeni EN/TR anahtar PROPOSED. Founder onayı gerekir.**
`l10n/events-v1-proposed_en.arb` ve `_tr.arb` otomatik birleştirme listesine alınmadı. Tam ARB üzerine yazılmaz. Founder onayından sonra Code mevcut ARB'ye anahtar bazında birleştirir; çakışan anahtar varsa önce karşılaştırır. Mevcut navigation/retry metinleri yeniden tanımlanmaz.

Hatırlatma: yalnız GOING, başlangıçtan 1 saat önce. Değişti bildirimi: title/start/end/venue; description/image/category bildirim üretmez. Öneri bildirimler adsızdır, mekân/etkinlik adı taşımaz. Kanal/ses/ön plan politikası yeniden tanımlanmadı.

### Karar ve doğrulama sınırı

Founder'dan tasarımla ilgili beklenen karar yeni metinlerin onayıdır. Mühendislik taslağındaki 80/1000 içerik sınırları ve timezone önerileri bu teslimle canonical yapılmadı; finalized sözleşme esas. Saklama/üretim izni tasarım tarafından belirlenmedi.

299 eski durum ve production placeholder sessizce değiştirilmedi; bu ayrı bir geliştirme eki. Flutter/backend/store varlığı değiştirilmedi. HTML doğrulamaları `evidence/validation.json`; native iOS/Android, VoiceOver/TalkBack ve gerçek sistem takvim/harita dönüşleri Code tarafından doğrulanacak.
