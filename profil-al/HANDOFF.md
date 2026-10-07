# PROFIL-AL — Manager / Code teslimi v1.0

**TASARIMCIDAN MANAGERE MESAJ**

7 Ekim 2026 · Cream & Ink v2.3 / Hafif kabartma.
Depo: `mertvdolu/imhere-design-public`
Dal: `design/profile-purpose-linkedin-v23`
Başlangıç commit'i: `8bd0e29edf3c1ff10ee01ecca741c1f592e7b48d`

## Okuma sırası

1. [SPEC.md](SPEC.md) — ölçü/bileşen ve akış kuralları.
2. [ONIZLEME.html](ONIZLEME.html) — 35 durum; EN/TR, %100/%200.
3. [SCREEN-STATE-MATRIX.md](SCREEN-STATE-MATRIX.md) — her durumun PNG'leri; uzun içerik çıktıları.
4. [COPY-REVIEW.md](COPY-REVIEW.md) — 34 proposed anahtar, kaynak/fark listesi.
5. [VALIDATION.md](VALIDATION.md) · [MANIFEST.json](MANIFEST.json).

## A — varsayılan amaç

- Networking/Friends yüzde kaydırıcısı ve oran gösterimleri kalkar. Eski oran yeni amaca çevrilmez.
- Özel düzenleme alanında Networking / Friendship / Not set; mevcut radyo çipi ailesi. Kayıt mevcut profil Save akışında.
- Kendi profilinde ikinci bir varsayılan amaç baloncuğu **yok**. Başkasına varsayılan ayar gösterilmez.
- I’m here ekranı her seferinde açılır. Kayıtlı varsayılan varsa belirgin önseçim + okunur not. Kullanıcı bu oturum için değiştirebilir; ayar yazılmaz. Ayarsız/okunamayan durumda önceki boş seçim ve pasif Continue korunur.
- Aktif oturum amacı/yenileme değişmez; aktif oturum notu kayıttan sonra da görünür.

## B — LinkedIn

- Mevcut form, küçük düğme, bilgi satırı ve tam ekran onay bileşenleri kullanıldı. Genel dış bağlantı simgesi; logo/mavi marka rengi/doğrulandı rozeti yok.
- Open and check → başarılı dış açılış → uygulamaya dönüş → kanonik adres + üç bilgi paragrafı → Yes / No. **Yes yalnız Kaydet'i etkinleştirir; doğrudan kaydetmez.** Açılış hatasında onay yok. Adres değişince onay düşer.
- Kaydetme/kaldırma başarısı yalnız sunucu yanıtıyla. Kaldırmada contactSeenNote korunur. Hata/çevrimdışı ve görünürlüğün geçici kapalı olduğu hâller mevcut.
- Başkasında yalnız Yakındakiler kişi profili ve yanıt bekleyen gelen istek profili: LinkedIn metin bağlantısı + hemen altında izleyici notu. **Gelen istekte amaç rozeti/metni yok.**
- Yakındakiler liste kartı, giden istek, Bağlantılar, sohbet, eşleşme ve Engellenenler'e LinkedIn taşınmaz. Veri yoksa link/not/boş yer tutucu yok. Contact card'a kopyalanmaz.

## Metin kapısı

**PROPOSED — HARBOR + FOUNDER COPY APPROVAL REQUIRED**

- `l10n/profil-al-proposed_en.arb` ve `_tr.arb`: 34 öneri anahtarı. Canonical ARB değildir; tam ARB üzerine yazılmaz.
- Brifteki kısa EN taslaklar aynen korundu. TR ve üç uzun HARBOR v2 bilgi paragrafı onaylanmış sayılmadı.
- HARBOR v2'nin kısa metinlerle farkları `COPY-REVIEW.md > ÖNERİ` bölümünde: amaç açıklaması, biçim hatası, görünürlük notu ve tipografik kesme işaretleri. Nihai metin onayı bunları kapatmalı. Hazır dosyadaki “onaya hazır” ifadesi Founder onayı kabul edilmedi.
- Geçici kapatma notunun yanında yeniden görünürlüğü açıklayan öneri cümle var; “kayıtlı tutmak kalıcı gizlilik sağlar” izlenimi verilmez.
- 27 mevcut ortak anahtar referansı yeni ARB'ye tekrar eklenmedi.

## Dosya listesi

`SPEC.md`, `HANDOFF.md`, `README.md`, `ONIZLEME.html`, `style.css`, `preview.js`, `catalog.json` / `catalog.js`, `copy.proposed.json` / `copy.js`, `COPY-REVIEW.md`, `l10n/*`, `screens/png/*`, `OVERVIEW.png`, `SCREEN-STATE-MATRIX.md`, `VALIDATION.md`, `evidence/*`, `source/REFERENCES.json`, `MANIFEST.json`.

Görüntüler bölüm/akış odaklıdır; mevcut diğer profil alanlarını kaldırma talimatı değildir. HTML bütün depo içindeki ortak CSS/font dosyalarına bağlıdır. PNG ve belgeler bağımsız okunur.

## Sınırlar ve sorular

Ürün davranışı için yeni açık soru yok. Beklenen: HARBOR + Founder nihai metin onayı. Code; mevcut URL sözleşmesini, gerçek dış açılış/dönüşü, adres değişikliğinde onay sıfırlanmasını, görünürlük koşullarını, klavye/sistem geri/ekran okuyucuyu ve native cihazı ayrıca doğrular.

Örnek URL yalnız `linkedin.com/in/…` biçim yer tutucusudur; gerçek/geçerli profil değildir. Gerçek kişi adı/adresi/fotoğrafı yok. Bu HTML dış sayfaya gitmez ve profil kaydetmez. Tarayıcı doğrulaması native/backend/yayın tamamlandı anlamına gelmez.

Commit SHA teslim mesajında verilir. Ana dala birleştirme bu teslimin parçası değildir.
