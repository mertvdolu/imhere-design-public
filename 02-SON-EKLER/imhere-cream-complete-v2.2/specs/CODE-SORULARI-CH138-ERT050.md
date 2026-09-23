TASARIMCIDAN MANAGERE MESAJ

# Code soruları — Cream & Ink v2.2 / CH-138, ERT-050, ERT-046

Yerel teslim; aktarımı Code yapacak. Flutter/backend dosyaları değiştirilmedi.

## 1. Tipografi

Üç mevcut çizim değeri hem paket hem ortak `theme.tokens.json` dosyasına eklendi. Mevcut tokenlar ve çizim ölçüleri değişmedi; `height` font boyutuna göre satır yüksekliği çarpanıdır.

| Token | Boyut | Ağırlık | Satır yüksekliği | Kullanım |
|---|---:|---:|---:|---|
| typography.sectionTitle | 18 | 500 | 1.4 | Bölüm başlığı |
| typography.status | 16 | 500 | 1.6 | Durum satırı |
| typography.helper | 14 | 400 | 1.4 | Yardımcı metin |

## 2. ERT-050 — register-too-many-attempts

Kayıt formuna, `login-too-many-attempts` karşılığı eklendi. Mevcut `authTooManyAttempts` metni kullanılır; süre, eşik veya sayaç yok. Hesap oluşturma ana eylemi giriş karşılığındaki gibi pasif çizilir; yeniden kullanılabilirlik uygulama/backend durumundan gelir. E-posta, gizli parola ve mevcut en az 8 karakter kuralı korunur. Yeni ürün kuralı veya metin anahtarı yok. %200 metinde uyarı ikonu metnin üstüne alınır; uzun sözcükler bölünmeden kartın tam iç genişliği kullanılır.

TR/EN × iOS/Android × %100/%200: 8 SVG ve 2 PNG. `EKRAN-KATALOGU.json` içinde yeni durumun tüm varyantları `beta: true`; önceki beta kararları aynı. Katalog: 296 durum, 2368 SVG, 592 PNG; 289 beta / 7 sonraya kalan durum.

## 3. CH-138 — register-email-unavailable

Kart metni canlı uygulamayla hizalandı:

- EN: This email can't be used to create a new account. If you already have one, sign in instead.
- TR: Bu e-posta ile yeni hesap oluşturulamıyor. Zaten bir hesabın varsa giriş yap.

Ana eylemin altında mevcut `authExistingAccount` ikincil düğmesi var: **I have an account · Sign in / Hesabım var · Giriş yap**. Hedef mevcut giriş ekranıdır. 8 SVG ve 2 PNG güncellendi.

## 4. İlk gönderim ve tekrar gönderim

İki durum kimliği korunur. `verify-sending` mevcut `emailSending` metnini kullanır. `verify-resend-busy` yeni `authVerifyResending` metniyle ayrılır:

- EN: Resending the verification link…
- TR: Doğrulama bağlantısı tekrar gönderiliyor…

Yalnız durum satırı değişir. Mevcut meşgul düğmeler, çıkış eylemi ve 24×24 / 1,8 çizgili bekleme göstergesi korunur. Gösterge uygulamada dönebilir (önceki tasarım onayı). Sayaç, yapay gecikme, yeni tekrar gönderim kuralı veya başarı iddiası eklenmez. 8 SVG ve 2 PNG güncellendi; ilk gönderim çizimleri aynı.

## 5. Material ikon eşlemeleri

Code'un önerdiği beş karşılık **onaylıdır**:

| Glif / kullanım | Material karşılığı |
|---|---|
| Geri | chevron_left |
| Gelen kutusu / boş durum | inbox_outlined |
| Sohbet balonu / boş durum | chat_bubble_outline |
| Uyarı | warning_amber_outlined |
| Harita | map_outlined |

Mevcut ikon ölçüsü, renk, erişilebilir etiket ve dokunma alanları korunur. Bu eşlemeler için ek çizim veya yeni varlık istenmiyor.

## 6. ERT-046 — yeniden deneme düğmeleri

`8078bfb`, yalnız `map-offline` değil, **nearby-failed, nearby-offline, map-failed ve map-offline** durumlarının tamamını kapsar. Dört durumun 32 SVG varyantında mevcut `checkInRetry` ikincil düğmesi ve 8 PNG karşılığı tekrar kontrol edildi. Bu teslimde o çizimler yeniden değiştirilmedi. Code'un dört ekranı da içeren commit'i esas alması yeterli.

## 7. Google Play simgesi

`03-MAGAZA/imhere-store-v1.0/google-play/app-icon-512.png` eklendi. Kaynak `brand/app-icon/master-1024-512.png`; 512×512 RGBA, byte düzeyinde aynı dosya. Mağaza önizlemesi, dosya listesi ve doğrulaması güncel. Eski A-wordmark ve B-symbol klasörlerine `ESKI-KULLANMA.md` ve eski paket girişine uyarı eklendi. Simge tasarımı değiştirilmedi.

## Dosyalar ve birleştirme

- Paket: `02-SON-EKLER/imhere-cream-complete-v2.2/`.
- Çizimler: `screens/svg/` ve `screens/png/`; kimlikler dosya adındadır.
- Ortak token: `03-GUNCEL-ORTAK/tokens/theme.tokens.json`; paket içi kopyayla aynıdır.
- Metin: `l10n/cream-v2.2-patch_en.arb`, `l10n/cream-v2.2-patch_tr.arb`, `l10n/migration.json`.
- Bu değişiklikte eklenen anahtar: `authVerifyResending`; değişen mevcut anahtar: `authEmailUnavailable`. `authExistingAccount` metni aynı.
- Tam referans ARB'ler uygulamadaki dosyaların üzerine yazılmaz; yalnız ilgili anahtarlar birleştirilir. CH-138 uygulamada zaten canlıdır.
- `contracts/screen-manifest.json`, `catalog.js`, kök `EKRAN-KATALOGU.json`, `MANIFEST.json`, `evidence/validation.json` güncellendi.

Kontrol kapsamı: TR/EN, iOS/Android, normal/büyük metin, SVG sınırları, düğme görünümü, durum farkları, katalog/beta ve dosya bütünlüğü. Native ve fiziksel cihaz testi bu teslimde yapılmadı.
