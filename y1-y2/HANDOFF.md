# Y1 / Y2 — Manager / Code teslimi v1.0

**TASARIMCIDAN MANAGERE MESAJ**

Tarih: 7 Ekim 2026. Depo:`mertvdolu/imhere-design-public`. Dal:`design/y1-y2-cream-ink-v23`. Tema:Cream & Ink v2.3 / Hafif kabartma.

## Önce oku

1. [SPEC.md](SPEC.md) — ölçüler ve mevcut akışa eşleme.
2. [ONIZLEME.html](ONIZLEME.html) —40 durum; EN/TR,%100/%200; iOS/Android kabukları.
3. [SCREEN-STATE-MATRIX.md](SCREEN-STATE-MATRIX.md) —160 ana PNG +63 tam içerik çıktısı.
4. [COPY-REVIEW.md](COPY-REVIEW.md) —62 proposed anahtar +12 mevcut etiket referansı.
5. [MANIFEST.json](MANIFEST.json) —dosya listesi/hash; [VALIDATION.md](VALIDATION.md) —320 tarayıcı yerleşimi +17 akış gözlemi, native sınırları.

## Teslim kapsamı

**Y1:** Events başlığının altında kompakt öneri/Önerilerim girişleri; görselsiz öneri formu ve alan hataları; tarih/saat seçici; gönderim; Pending/Accepted/Not accepted; Withdraw; boş/yükleme/hata/çevrimdışı; günlük3 ve aynı anda 3 Pending sınırı.

**Y2:** I’m here sonrası boş tek-seçimli amaç; pasif Continue; mevcut konum/check-in kapılarına devir; nötr amaç rozeti; iki amaçtan kişi gösterimi; farklı amaç uyarısı, iptal, bekleme, hata, sunucu doğrulamasından sonra 10 gün sonucu. İstek sırasında eski niyet seçimi kaldırılır. Aktif oturumun I’m still here düğmesi ve diğer istek uygunluk kuralları kalır.

## Önemli aktarım notları

- Yeni renk/ikon/bileşen ailesi yok; mevcut v2.3, v10 ve Events parçaları yeniden kullanıldı. Yalnız tasarım eki.
- Metin durumu **PROPOSED — HARBOR COPY REVIEW REQUIRED**. Founder'ın EN taslakları aynen. TR ve tamamlayıcı etiketler öneri. `l10n/y1-y2-proposed_en.arb` / `_tr.arb` ana ARB değildir; onay gelmeden birleştirme. Ortak etiketler için native mevcut anahtarlar kullanılır.
- Accepted, published anlamına gelmez; öneri ekibin taslağına gidebilir. Kullanıcı doğrudan yayınlayamaz. Karar push/ret nedeni/önereni herkese gösterme eklenmedi.
- Sunucu yanıtı gelmeden “gönderildi”, “geri çekildi” veya10 gün sonucu gösterme. Cancel işlem başlatmaz. Hata durumunda yeni bir 10 günlük dönem icat etme; Code sonucu uzlaştırır.
- Y2 amaç oturum boyunca sabit; yenileme aynı amacı korur. Amaçsız eski kayıt için rozet/amaç tahmini yok. Networking/Friends profil yüzdesi ayrı kalır.
- `request-sent` yalnız geçiş anıdır. Mevcut bekleyen ekranın sayacı/kalan süresi bu sade PNG ile değiştirilmez.
- Full PNG'ler kaydırmanın tamamını gösterir, telefon oranını değiştiren tasarım değildir. Native seçici/klavye/sistem geri/büyük yazı/ekran okuyucu ve gerçek sunucu koşulları Code'da ölçülür.
- Gerçek Events sürümüne yönelik tasarımdır; geçici gizlenmiş Events sekmesini kendi başına production'da açma onayı değildir.

## Dosyalar

`ONIZLEME.html`, `style.css`, `preview.js`, `catalog.json`/`.js`, `copy.proposed.json`/`copy.js`, `COPY-REVIEW.md`, `l10n/*`, `screens/png/*`, `OVERVIEW.png`, `SPEC.md`, `HANDOFF.md`, `SCREEN-STATE-MATRIX.md`, `VALIDATION.md`, `source/REFERENCES.json`, `evidence/*`, `MANIFEST.json`.

HTML ortak Events CSS + mevcut font/mark dosyalarına bağlıdır; depoyu bütün olarak aç. PNG ve belgeler bağımsız okunabilir. GitHub HTML dosyasını kaynak olarak gösterir; çalıştırmak için indirip aç veya yerel önizlemeyi kullan.

## Sorular / onay durumu

Ürün davranışıyla ilgili yeni açık soru yok. Metinlerin nihai HARBOR onayı bekleniyor. Karar paketindeki günlük sınır için saat/reset vaadi tasarlanmadı; UI sunucunun uygunluk durumunu kullanır. Canlı yayın, native uygulama veya backend tamamlandı iddiası yok.

Commit SHA, teslim mesajında verilir. Ana dala birleştirme bu teslimin parçası değildir.
