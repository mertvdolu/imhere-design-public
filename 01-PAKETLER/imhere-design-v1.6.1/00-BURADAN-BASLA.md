# I'M HERE — v1.6.1 / Paket 2 düzeltmesi
**v1.6 kabul edildi. Bu teslim, kabul edilen pakete eklenecek parola ve metin anahtarı düzeltmesidir.** Küçük sürüm numarası bu defa Founder'ın açık isteğiyle v1.6.1 olarak kullanıldı.

## Değişenler
- Parola altında tek satır: **En az 8 karakter. / At least 8 characters.** Başka karakter şartı ve güç göstergesi yok.
- Yazılımcının listesine birebir uyan **19 auth anahtarı**; eski adlardan altısının yeni adlara eşlemesi migration içinde. Listede karşılığı olmayan 28 kabul edilmiş UI adı aynı metinlerle uyumluluk alias kaydı olarak korundu.
- Girişte yanlış parola / hesap bulunamadı ayrımı yapmayan tek hata. E-posta kullanım hatası hesap varlığını doğrulamaz. Deneme sınırı metni süre/eşik belirtmez.
- Sıfırlama sonucu her iki hesap-varlığı durumunda aynı: **“Bu e-posta adresi kayıtlıysa parola sıfırlama bağlantısı gönderildi.”**

## İnceleme
`ONIZLEME.html` çevrimdışı çalışır; dil, platform ve büyük metin filtresi vardır. Bu patch'te14 değişen durum +3 yeni hata sunumu: **17 durum, 136 SVG, 34 PNG**. Her durum TR/EN, iOS/Android, normal/%200 SVG içerir; PNG'ler TR iOS normal ve EN Android büyük metindir. Görünüm dosyaları yalnız düzeltme kapsamındadır; v1.6'daki diğer ekranlar aynı kalır.

`review/GENEL-BAKIS.png` özet görsel; `specs/01-PATCH.md` davranış/yerleşim; `l10n/ANAHTAR-ESLEMELERI.md` anahtar tablosudur. `DOGRULAMA.md` kontroller ve sınırları açıklar.

## Yazılıma aktarım
Önce `l10n/auth_tr.arb` / `auth_en.arb`: yalnız 19 kanonik auth anahtarı. `l10n/migration.json` alias'ları ve çağrı yeri kurallarını içerir. `app_tr.arb` / `app_en.arb` ise334 anahtarlı tam referans sözlüklerdir; **canlı ARB'lerin üzerine yazılmaz**. Metinleri mevcut dosyalara anlam bazında birleştirin. Uygulamaya özel anahtarları ve var olan localization metadata/API'lerini koruyun.

Tasarım arşivinde de v1.6'yı saklayın. Bu patch'teki aynı kimlikli ekranlar v1.6'daki karşılıklarını günceller; diğer ekranları silmez. Patch manifesti yalnız 17 durumu listeler; tam uygulama ekran envanteri yerine geçmez.

## Korunan kabul
Profil görselleri bu küçük arşivde tekrar edilmedi ve kaynak v1.6 dosyaları değiştirilmedi. Kabul edilen 27 profil durumu v1.6'da kullanılmaya devam eder. Profil sözleşmeleri, profil/platform/çıkış spesifikasyonları, görünürlük kuralları, token'lar, fontlar ve v1.4 kabul eki aynen korundu. Koruma hash'leri evidence içindedir. Tekrar gönderim hâlâ backend durumuna bağlıdır; sayaç yok. Davet edinme yolu hâlâ Founder'dadır.

## Gereksinim kaynağı ve devam
Tasarım Gereksinim Özeti **v1.0.2** okundu; §2 Firebase e-posta + parola, doğrulama e-postası, giriş/reset/çıkış akışıyla uyumludur. Dosya bu teslimin references klasöründedir; eski v1.0/v1.0.1 özetleri auth kaynağı değildir. Parolanın 8 karakter kuralı ve 19 anahtar listesi son Founder/Manager mesajından gelir. Önceden kabul edilen meslek görünürlüğü ve kendi eylemine ait endConfirm açıklamaları korunur.

Sonraki paket: **Paket 3 — istek/eşleşme, sohbet, devam ve contact.** Bu patch Paket3 ekran tasarımlarını içermez. Bu teslim UI/UX dosyasıdır; Flutter/backend kodu değiştirilmedi.
