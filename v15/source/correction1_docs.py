from pathlib import Path
import json

def prepare(B):
 summary=json.loads((B/'evidence/summary.json').read_text())
 p=B/'TOKENS.md';p.write_text(p.read_text()+'''\n## Yasak eşleşme — Düzeltme 1

**#696A62 yardımcı metin + #E5E9EF Networking açık yüzeyi YASAK: 4.490:1.** Normal metin eşiği 4.5:1 altında. Bu yüzeyde Ink (#191A17) kullanılır; yardımcı metin yalnız krem (#F4F1E9) zeminde kalır. Hiçbir renk değeri değiştirilmedi. Ekrandaki topluluk ikonu açık yüzeyinde yalnız kendi koyu rengi bulunur; yardımcı metin taşımaz.
''')
 p=B/'VALIDATION.md';p.write_text(p.read_text()+f'''\n## Düzeltme 1 — dikey kontrol

- Dikey blok çakışması: {summary['verticalOverlaps']}.
- Dikey metin taşması: {summary['verticalTextOverflow']}.
- Kaydırma başlangıcının üstünde erişilemeyen içerik: {summary['unreachableContent']}.
- Tüm durumlar measurementVersion=2 ile yeniden ölçülür. Normal akıştaki kardeş bölgeler ve metnin kendi alanına sığması kontrol edilir. Harita arka planı ve bilinçli kapsayıcı/çocuk örtüşmeleri hariçtir. Font Range ölçüsünün doğal üst/alt boşluğu için punto ×0.1 tolerans; bu tolerans D0’da tespit edilen 20–78 px taşmayı gizlemez.
- Dikey kaydırma hata değildir. D0 metni/bağlantısı küçültülmez, tam içerik ve 320/%200 kareleri ayrıca verilir.
- Kontrol sonuçları tasarım önizlemesidir; native cihaz/ekran okuyucu testi değildir.
''')
 rows=[
 ('1','HB-37 r6 / karar58','gecis/migration-linkedin-changed-{default,other,saving,failed,offline}; bağımsız LINK_CHANGED, kayıtlı Nobody, hata ve kapatmada kayıtlı ayar. Yeni v15LinkedinChangedBody aynen.'),
 ('2','Sohbet satırı','linkedin-chat-connection eski linkedin-connection yerine geçer; satır sohbet ekranında, Bağlantılar/readInbox listesinde değil. Eski HTML scene bağlantısı alias ile yeni duruma açılır.'),
 ('3','Hata ayrımı','settings-switch-failed = communitySwitchFailed; settings-failed = katıl/ayrıl communitySettingsChangeFailed.'),
 ('4','Katıl/ayrıl bekleme','settings-joining/leaving: metinsiz 24×24 spinner, stroke1.8. progressbar etiketi H1’den; yeni görünür metin yok.'),
 ('5','Check-in uyarısı','settings-switch-checkin/going: ikonlu communityCheckInEndsNote, gövdeden sonra.'),
 ('6','Meslek bağlamı','Profilde occupation H1, geri + mevcut Save; Atla yok. Kayıt occupation-signup-* örnekleri ayrı. Other unvan alanı seçilen Other satırının hemen altında.'),
 ('7','Tek görünür başlık','Geçiş (c) radiogroup hideLegend=true; erişilebilir grup etiketi korunur.'),
 ('8','LinkedIn kayıt başarısı','linkedin-saved: server-ack sonrası Skip yerine Continue; kart adımına gider.'),
 ('9','LinkedIn ilk ekleme','linkedin-settings-empty: kayıtlı link yok; profileLinkedinVisibilityDefaultNote mevcut, Everyone standart radyo seçimi, Atla yok.'),
 ('10','Ayarlar okuma kapıları','settings-loading/read-failed + linkedin-settings-loading/read-failed; eski/varsayılan veri gösterilmez, okuma hatası Retry ile yeniden okunur.'),
 ('11','Filtreli Yakındakiler','filters-not-enough/no-longer-enough: Nearby H1 + topluluk göstergesi + 2 filters on düğmesi; filtreler korunur.'),
 ('12','D0 %200','flex:1 0 auto, çocuklarda flex-shrink:0, safe center. measure.js dikey çakışma/metin taşması/erişilemeyen başlangıç ölçer.'),
 ('13','Katalog emekliliği','match-different tüm eski varyantları V15.ENABLED == false. Tarih silinmedi.'),
 ('14','Matris başlığı','Kök SCREEN-STATE-MATRIX.md: Bölüm / State / Görsel + ayırıcı satır.'),
 ('Ek','Yasak eşleşme','TOKENS.md ve tokens.json: #696A62 metin / #E5E9EF yüzey 4.490:1, kullanılmaz.')]
 table='| Madde | Konu | Uygulama |\n|---|---|---|\n'+''.join('| '+' | '.join(r)+' |\n' for r in rows)
 (B/'DUZELTME-1.md').write_text('''# TASARIMCIDAN MANAGERE MESAJ

TASK: V15-TASARIM-DUZELTME-1  
Depo / dal: imhere-design-public · design/v15-cream-ink-v23  
Temel teslim: 0aaa981d83241d30e24b28fcdc70a76ca48563bf

## Kapsam

14 madde + yasak renk eşleşmesi işlendi. Onay bekleyen renk, gösterge, meslek seçici, filtre satırı, Both kartı, ikon ve açılış görünüşleri yeniden tasarlanmadı. Yalnız istenen bağlam, durum, yerleşim ve doğrulama düzeltmeleri yapıldı.

'''+table+f'''
## Teslim

{summary['states']} durum · {summary['mainPng']} ana PNG · {summary['fullPng']} full PNG · {summary['measurements']} DOM ölçümü.
EN/TR × %100/%200 × 390/412; 320/%200 iOS+Android stres ölçümü.
Son dosya sayısı, boyut ve SHA256 MANIFEST’te; final commit/ls-remote teslim mesajında.

## Metin

Önceki 195 anahtarın EN/TR değerleri korunur. Tek yeni wording: v15LinkedinChangedBody (HB-37 r6 §15 / HB-41, karar58). Mevcut communitySwitchFailed ve occupation anahtarları artık kullanıldıkları için teslim copy listesine eklenir; toplam 198 anahtar. Yeni metin ÖNERİ’si yok; onaylı ARB değerleri yeniden yazılmaz.

## Doğrulama

Yatay taşma {summary['horizontalOverflow']}; 48×48 altı hedef {summary['smallTargets']}; yatay kesilen metin {summary['clippedText']}; dikey çakışma {summary['verticalOverlaps']}; dikey metin taşması {summary['verticalTextOverflow']}; erişilemeyen başlangıç {summary['unreachableContent']}.
`evidence/final-validation.json` kaynak-copy, dosya, boyut ve kapsam denetimidir. `evidence/correction1-*` yeni düzeltmelerin kanıtlarını içerir. `correction1-d0-before.json` düzeltme öncesi sorunu kaydeder; güncel başarı özeti değildir.

## Sınırlar

Yalnız v15/ ve EKRAN-KATALOGU.json. Uygulama deposuna dokunulmadı; main merge, force push, deploy, mağaza veya dış iletişim yok. Native doğrulama Code’da. Founder görsel kararları ayrı onay kapısı olarak korunur.
''')
 for f in ['README.md','HANDOFF.md']:
  p=B/f;p.write_text(p.read_text()+'\n## Güncel düzeltme\n\n[14 maddelik Düzeltme 1](DUZELTME-1.md) bu teslimin güncel fark listesidir.\n')
