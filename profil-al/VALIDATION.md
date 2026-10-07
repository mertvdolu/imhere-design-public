# PROFIL-AL — validation

7 Ekim 2026 · Sonuç: **PASS (tarayıcı tasarım önizlemesi)**.

## Kapsam ve sonuç

- 35 durum; 140 ana PNG (EN/TR × %100/%200, 390×844 mantıksal alan, 4× çıktı).
- 92 uzun içerik PNG'si + OVERVIEW.png. Uzun içerik çıktısı tek ekrana sığdığı anlamına gelmez.
- 280 benzersiz yerleşim: 140 iOS kabuğu/390 (iki dil, iki ölçek) + 70 iOS kabuğu/320/%200 + 70 Android kabuğu/320/%200.
- Ek 3 yüksek kontrast + opak menü + hareket azaltma kontrolü (TR, 320, %200): purpose-active, confirm-paused, viewer-incoming. Gölge yok; menü varsa opak, blur yok.
- Yatay taşma 0; 48×48 altı görünür kontrol hedefi 0; kesilen/taşan metin düğümü 0; yinelenen ID 0. Telefon içeriğinde bir H1. Fontlar yüklü.
- Gelen istek varyantlarında amaç rozeti 0; bağlantı verisi yokken bağlantı/not yok; amaç ve onay/kaldırma sayfalarında alt menü yok.
- 34 proposed anahtarın EN/TR eşleşmesi; 16 kısa EN brif metni karakter karakter aynı. 27 ortak anahtar yeniden delta'ya eklenmedi.

## Etkileşim gözlemleri (17)

Onaysız Save pasif; açma hatasında onay yok; dönüşte üç bilgi paragrafı; Hayır sonrası pasif; Evet yalnız Save'i etkinleştirir; adres değişikliği beyanı sıfırlar; kaydetme bekler; sunucu onayından sonra saved; kaldırma bekler; kaldırma hatasında tekrar eylemi; onaydan sonra boş alan; ayarsız check-in boş; kayıtlı amaç önseçili; oturuma özel değişiklik varsayılanı yazmaz; aktif oturum notu kayıttan sonra kalır; gelen istekte link var/amaç yok; veri yokken satır/not yok.

Kanıt: [interaction-results.json](evidence/interaction-results.json). Bunlar HTML'deki inceleme kontrolleriyle simüle edilen akış gözlemleridir; gerçek sunucu çağrısı veya LinkedIn doğrulaması değildir.

## Görsel inceleme

Amaç seçimi, check-in notu, uzun LinkedIn formu/onayı, geçici kapalı TR %200, kaldırma ve gelen istek profili gerçek PNG'lerden incelendi. Gelen istekte kabul/ret hedefleri arasına mevcut spacing ölçeğinde 8/16 boşluk uygulandı; ilgili profil kareleri yeniden üretildi. Uzun metinler font küçültmeden kaydırılır; son eylemler full içerik çıktılarında görülebilir.

## Kanıt dosyaları ve sınırlar

`evidence/capture-*.json` ana yerleşimler; `stress-ios.json` ve `stress-android.json` dar ekran/büyük metin ölçümleri; `a11y-modes.json` ek modlar; [summary.json](evidence/summary.json) toplamlar. Bunlar tarayıcı ölçümleridir. VoiceOver/TalkBack, OS klavyesi, platform geri davranışı, gerçek dış açılış/dönüş ve izin/DTO sunucu kapıları Code'un native testinde kalır.

Copy durumu: **PROPOSED — HARBOR + FOUNDER COPY APPROVAL REQUIRED**. Canonical ARB veya uygulama koduna merge yapılmadı.
