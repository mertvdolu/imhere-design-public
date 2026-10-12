# EMAIL-01 — Manager / Code teslimi v1.0

**TASARIMCIDAN MANAGERE MESAJ**

12 Ekim 2026 · Cream & Ink v2.3 · yalnız EN-GB.

## Önce oku

1. [SPEC.md](SPEC.md) — ölçü, renk, logo, koyu mod ve yedek görünüm.
2. [ONIZLEME.html](ONIZLEME.html) — dört e-posta, açık/koyu,375/600; ek font/uzun içerik kontrolü.
3. [SCREEN-MATRIX.md](SCREEN-MATRIX.md) —16 ana PNG + ek kanıtlar.
4. [copy.md](copy.md) — brif metinleri ve ayrı öneriler; [copy.proposed.json](copy.proposed.json).
5. [VALIDATION.md](VALIDATION.md), [MANIFEST.json](MANIFEST.json).

## Dört eylem

| E-posta | Alıcı | Ana eylem / fallback |
|---|---|---|
| E01 Confirm email | Kayıt adresi; Resend aynı şablon | ACTION_URL |
| E02 Reset password | Hesap adresi | ACTION_URL |
| E03 Confirm new email | Yeni adres; onaydan önce | ACTION_URL |
| E04 Email changed | Eski adres; değişiklikten sonra | REVERT_URL |

E04 geri-alma davranışı Founder brifinden gelir. Tasarım yeni geri-alma süresi/başarı ekranı icat etmez. URL ve tokenlar Code'daki işlem sözleşmesinden gelir.

## HTML'e çevirirken

- Sütun en çok600;375 örneğinde yatay24,600'de40. Tüm mesaj doğal yüksekliğinde.
- Tek canlı HTML ana bağlantı,48 px; görsel düğme yok. Gölge ve yuvarlatma kaybolsa da eylem okunur.
- Temel görünümü inline CSS / presentation table ile kur; client CSS desteğini ayrıca ölç. JS, form, canvas, animasyon veya font yüklenmesine bağımlılık yok.
- `prototype/01-confirm-email.html` yalnız isteğe bağlı yapı örneğidir; üretime hazır/istemcilerde test edilmiş HTML değildir. ONIZLEME/preview.js inceleme aracıdır, e-posta olarak gönderilmez.
- Gönderilecek mesajda yerel göreli varlık URL'lerini Code onaylı host/CID ile değiştirir. E-posta için PNG kullan; SVG kaynak olarak kalır. Logo toplamı~40 KB altında. Son gerçek HTML102 KB altında ayrıca ölçülür; preview klasör boyutu bunun ölçüsü değildir.
- Logo altı I'M HERE; yanında canlı marka yazısı. Görseller bloklansa da başlık, metin, eylem ve fallback tam kalır. Dark-mode logo takası başarısızsa iki logoyu birden gösterme.
- CTA ve düz URL aynı ACTION_URL/REVERT_URL olmalı. Değerleri HTML/attribute bağlamında encode et; URL'ye satır ayırmak için karakter ekleme. Uzun adres/URL kırpma/ellipsis yok.
- Multipart plain text karşılığı aynı sıra ve aynı eylem URL'sini taşır. Gönderim/alan adı yapılandırması bu tasarım tesliminde yapılmadı.

## Copy kapısı / açık kararlar

**PROPOSED — HARBOR + FOUNDER COPY APPROVAL REQUIRED.** Verilen wording aynen, ek4 metin ayrı öneri. Metinler onaylı veya canonical sayılmaz.

1. E04 NEW_EMAIL tam mı maskeli mi? HARBOR karar verecek. Her iki yerleşim desteklenir.
2. E03/E04 preheader, E04 güvenlik notu, ortak fallback ve E03/E04 expiry kullanımı onay bekler.
3. Her eylemin gerçek EXPIRY değeri ve onaylı Help/Privacy URL'leri Code/Founder'dan gelir.

Bunlar tasarımı durduran sorular değil; gönderim öncesi kapanması gereken alanlardır.

## Code'un gerçek istemci kontrolü

Gmail web/iOS/Android; Apple Mail iOS/macOS; Outlook web ve masaüstü. Her birinde light/dark, images off, fallback fonts, uzun URL, uzun NEW_EMAIL, zoom, çalışan CTA/fallback, doğru alıcı ve doğru action türü. E04 doğru eski alıcıya gider. Süre gerçek token sözleşmesine uyar. Outlook sade görünüm kabul; kaybolan eylem/metin kabul değil.

PNG'ler ve tarayıcı kontrolleri gerçek Gmail/Outlook testidir iddiası taşımaz. Spam/gelen kutusu sonucu, alan adı doğrulaması, gönderim veya Firebase şablon değişikliği bu commit'in çıktısı değildir.

## Dosyalar

`ONIZLEME.html`, `preview.css/js`, `copy.js`, `copy.md`, `copy.proposed.json`, `SPEC.md`, `HANDOFF.md`, `SCREEN-MATRIX.md`, `VALIDATION.md`, `MANIFEST.json`, `OVERVIEW.png`, `assets/` SVG+PNG, `screens/png/`, `evidence/`, `prototype/01-confirm-email.html`.

Dal: `design/email-01-cream-ink-v23`. Yalnız `email-01/` ve kök README/CHANGELOG güncellenir. Main'e merge ve üretim gönderimi bu teslimin parçası değildir. Commit SHA teslim mesajında verilir.
