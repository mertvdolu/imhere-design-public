# EMAIL-01 — doğrulama

12 Ekim 2026 · **PASS — tarayıcı görsel kontrolü**.

## Ölçülenler

- 16 ana PNG: dört e-posta × açık/koyu ×375/600;2× çıktı, doğal yükseklik.
- 4 ek PNG: uzun adres/URL, maskeli adres, görseller kapalı/düz yedek ve320/%200 büyük yazı.
- 46 yerleşim:16 ana;8 Arial375/uzun;8 Arial320/%200/uzun;8 Geist375;2 görselsiz/düz600;4 E04 maskeli375/600.
- Yatay taşma0; taşan metin0; bir H1 ve bir ana eylem. Ölçülen en küçük CTA50 px, gövde/not/footer en küçük16 px. İşlem URL'si ile fallback slotu aynı; E04 REVERT_URL.
- Logo alt metni I'M HERE; görsel yüklü;144×92 kaynak. Görselsiz mod uygulama içi bir inceleme simülasyonudur, gerçek client image-blocking testi değildir.
- Brifte bulunan23 copy alanı birebir kontrol edildi. Dört ek öneri ayrı. Süreler, canlı URL'ler ve alıcı gizleme kararı varsayılmadı.

## Kontrast (sRGB)

| Mod / rol | Ön plan | Zemin | Oran | AA normal metin |
|---|---|---|---|---|
| light / body | #191A17 | #F4F1E9 | 15.49:1 | PASS |
| light / secondary | #696A62 | #F4F1E9 | 4.85:1 | PASS |
| light / button | #FCFAF5 | #191A17 | 16.76:1 | PASS |
| dark / body | #FCFAF5 | #191A17 | 16.76:1 | PASS |
| dark / secondary | #B7B3A9 | #191A17 | 8.35:1 | PASS |
| dark / button | #191A17 | #F4F1E9 | 15.49:1 | PASS |

Dekoratif ayırıcı normal metin olarak sayılmaz. Otomatik istemci renk dönüşümü bu hesapta yok; gerçek Mail/Gmail/Outlook ölçümü Code'da.

## Dosya ağırlığı

SVG+PNG dört logo varlığı toplam **8801 byte** (<40 KB). Tek gösterilen logo bundan küçüktür. Örnek HTML **4612 byte** (<102 KB). Nihai gönderilecek HTML, gerçek URL ve Code değişiklikleri sonrasında yeniden ölçülür; bu sayı gönderim garantisi değildir.

## Kanıt ve sınır

`evidence/capture-*.json`, `stress-layouts.json`, `extra-captures.json`, `contrast.json`, `sources.json`, [summary.json](evidence/summary.json). PNG'ler tarayıcıdan alınmıştır. Son kaynak renkleri ve gövde17 px / not16 px ayrımı ölçüldü.

Gmail web/iOS/Android, Apple Mail iOS/macOS, Outlook web/masaüstü ile gerçek gönderim yapılmadı. Sunucu, DNS, Firebase şablonu ve hesap davranışı değiştirilmedi; gelen kutusuna düşme/spam sonucu iddiası yok. Koyu PNG istemcinin zorunlu renk çevirmesinin testi değildir. Asıl mail client matrisi HANDOFF'ta Code'a bırakıldı.
