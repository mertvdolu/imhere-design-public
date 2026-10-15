# TASARIMCIDAN MANAGERE MESAJ

TASK: V15-TASARIM-DUZELTME-1  
Depo / dal: imhere-design-public · design/v15-cream-ink-v23  
Temel teslim: 0aaa981d83241d30e24b28fcdc70a76ca48563bf

## Kapsam

14 madde + yasak renk eşleşmesi işlendi. Onay bekleyen renk, gösterge, meslek seçici, filtre satırı, Both kartı, ikon ve açılış görünüşleri yeniden tasarlanmadı. Yalnız istenen bağlam, durum, yerleşim ve doğrulama düzeltmeleri yapıldı.

| Madde | Konu | Uygulama |
|---|---|---|
| 1 | HB-37 r6 / karar58 | gecis/migration-linkedin-changed-{default,other,saving,failed,offline}; bağımsız LINK_CHANGED, kayıtlı Nobody, hata ve kapatmada kayıtlı ayar. Yeni v15LinkedinChangedBody aynen. |
| 2 | Sohbet satırı | linkedin-chat-connection eski linkedin-connection yerine geçer; satır sohbet ekranında, Bağlantılar/readInbox listesinde değil. Eski HTML scene bağlantısı alias ile yeni duruma açılır. |
| 3 | Hata ayrımı | settings-switch-failed = communitySwitchFailed; settings-failed = katıl/ayrıl communitySettingsChangeFailed. |
| 4 | Katıl/ayrıl bekleme | settings-joining/leaving: metinsiz 24×24 spinner, stroke1.8. progressbar etiketi H1’den; yeni görünür metin yok. |
| 5 | Check-in uyarısı | settings-switch-checkin/going: ikonlu communityCheckInEndsNote, gövdeden sonra. |
| 6 | Meslek bağlamı | Profilde occupation H1, geri + mevcut Save; Atla yok. Kayıt occupation-signup-* örnekleri ayrı. Other unvan alanı seçilen Other satırının hemen altında. |
| 7 | Tek görünür başlık | Geçiş (c) radiogroup hideLegend=true; erişilebilir grup etiketi korunur. |
| 8 | LinkedIn kayıt başarısı | linkedin-saved: server-ack sonrası Skip yerine Continue; kart adımına gider. |
| 9 | LinkedIn ilk ekleme | linkedin-settings-empty: kayıtlı link yok; profileLinkedinVisibilityDefaultNote mevcut, Everyone standart radyo seçimi, Atla yok. |
| 10 | Ayarlar okuma kapıları | settings-loading/read-failed + linkedin-settings-loading/read-failed; eski/varsayılan veri gösterilmez, okuma hatası Retry ile yeniden okunur. |
| 11 | Filtreli Yakındakiler | filters-not-enough/no-longer-enough: Nearby H1 + topluluk göstergesi + 2 filters on düğmesi; filtreler korunur. |
| 12 | D0 %200 | flex:1 0 auto, çocuklarda flex-shrink:0, safe center. measure.js dikey çakışma/metin taşması/erişilemeyen başlangıç ölçer. |
| 13 | Katalog emekliliği | match-different tüm eski varyantları V15.ENABLED == false. Tarih silinmedi. |
| 14 | Matris başlığı | Kök SCREEN-STATE-MATRIX.md: Bölüm / State / Görsel + ayırıcı satır. |
| Ek | Yasak eşleşme | TOKENS.md ve tokens.json: #696A62 metin / #E5E9EF yüzey 4.490:1, kullanılmaz. |

## Teslim

147 durum · 1176 ana PNG · 552 full PNG · 2316 DOM ölçümü.
EN/TR × %100/%200 × 390/412; 320/%200 iOS+Android stres ölçümü.
Son dosya sayısı, boyut ve SHA256 MANIFEST’te; final commit/ls-remote teslim mesajında.

## Metin

Önceki 195 anahtarın EN/TR değerleri korunur. Tek yeni wording: v15LinkedinChangedBody (HB-37 r6 §15 / HB-41, karar58). Mevcut communitySwitchFailed ve occupation anahtarları artık kullanıldıkları için teslim copy listesine eklenir; toplam 198 anahtar. Yeni metin ÖNERİ’si yok; onaylı ARB değerleri yeniden yazılmaz.

## Doğrulama

Yatay taşma 0; 48×48 altı hedef 0; yatay kesilen metin 0; dikey çakışma 0; dikey metin taşması 0; erişilemeyen başlangıç 0.
`evidence/final-validation.json` kaynak-copy, dosya, boyut ve kapsam denetimidir. `evidence/correction1-*` yeni düzeltmelerin kanıtlarını içerir. `correction1-d0-before.json` düzeltme öncesi sorunu kaydeder; güncel başarı özeti değildir.

## Sınırlar

Yalnız v15/ ve EKRAN-KATALOGU.json. Uygulama deposuna dokunulmadı; main merge, force push, deploy, mağaza veya dış iletişim yok. Native doğrulama Code’da. Founder görsel kararları ayrı onay kapısı olarak korunur.
