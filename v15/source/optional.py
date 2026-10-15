from pathlib import Path
import json,shutil,hashlib
from PIL import Image

def prepare(B):
 d=B/'italik-acilis';(d/'evidence').mkdir(parents=True,exist_ok=True)
 ref=B.parent/'02-SON-EKLER/imhere-cream-complete-v2.2/motion/hareket-ve-his-v1'
 gif=ref/'previews/01-ink-signature.gif';shutil.copyfile(gif,d/'reference-h0.gif')
 im=Image.open(gif);im.seek(im.n_frames-1);im.convert('RGB').save(d/'OVERVIEW.png')
 sha=hashlib.sha256(gif.read_bytes()).hexdigest()
 files={
 'README.md':'# İtalik / açılış — karar (★)\n\n**Yeni öneri: yok.** Geçerli Geist Regular/Medium/SemiBold ve onaylı H0 korunur. Yeni italik dosya, yazı tipi veya ek açılış süresi eklenmez.\n\nMevcut H0 zaten talep edilen çizgi açılışını 800 ms içinde yapar. Yeniden tasarlamak yerine normatif kaynağa referans verildi. `reference-h0.gif` mevcut varlığın bayt-aynı kopyasıdır; yeni animasyon teslimi değildir.\n\n[Referans önizleme](ONIZLEME.html) · [Zamanlama](SPEC.md)',
 'SPEC.md':'# Açılış / tipografi\n\nDESIGN RECOMMENDATION — FOUNDER APPROVAL REQUIRED\n\n★ Yeni italik yönü: **yok**. v2.3 yerel pakette italik yok; 1.5 bilgi yoğunluğu artarken yeni vurgu ailesi ve lisanslı font paketi eklemeyi önermiyorum. Var olan üç Geist ağırlığı, TR glyphleri ve %200 yerleşimler bu teslimde ölçüldü. Hiçbir sahte italik uygulanmadı.\n\n★ Yeni açılış yönü: **yok**, mevcut H0 aynen.\n\n| Başlangıç–bitiş | Özellik | Eğri |\n|---|---|---|\n|0–620 ms|Kanonik logo konturu 0→1|Çizgi toplam uzunluğunda lineer|\n|620–760 ms|Kesişim dolgu opaklığı 0→0.92|Mevcut quick|\n|760–800 ms|Kanonik işaret|Sabit|\n\nTitreşim yok. Sıcak dönüşte oynatılmaz. Reduce Motion: logo 0 ms’de tamamen görünür. Hedef ekran erken hazırsa açılış bekletilmez; dekorasyon iptal edilir; 150 ms opaklık geçişi kullanılır. Native splash krem + orijinal işaret; animasyon ilk Flutter karesindedir. Oran/path değişikliği: 0.\n\nNormatif kaynak: ../../02-SON-EKLER/imhere-cream-complete-v2.2/motion/hareket-ve-his-v1/SPEC.md#01-ink-signature',
 'HANDOFF.md':'# Code notu\n\nYeni italik font/bağımlılık/animasyon uygulama. Mevcut H0 sözleşmesi korunur. V15 istemcisi yeni geçiş kapılarına ek bekleme koymaz. Buradaki GIF yalnız referans, uygulama varlığı değildir. Logo şekli, native splash, azaltılmış hareket ve sıcak dönüş davranışı aynı. Karar (★): yeni yön yok. Geçerli H0’yı yeniden onaylanmış yeni tasarım diye yorumlama.',
 'SCREEN-STATE-MATRIX.md':'# Kapsam\n\nYeni ekran durumu: 0; yeni 390/412 PNG: 0. Bu seçenek isteğe bağlıydı; yeni yön önerilmedi. OVERVIEW mevcut referansın son karesidir; kaynak GIF ve orijinal H0 kare CSV’si normatif. Kopya, tema veya akış yeni durumu eklemez.',
 'VALIDATION.md':'# Validation\n\nN/A — yeni ekran/hareket önerilmedi. Mevcut H0 GIF kopya SHA256: `'+sha+'`. Kaynakla bayt-aynı. Yeni font: 0, geometri değişikliği: 0, ek bekleme: 0. Bu referans cihaz performansı kanıtı değildir.',
 'COPY-REVIEW.md':'# Copy review\n\nYeni kullanıcı metni yok. Ekranlara italik metin veya karşılama sözü eklenmedi.\n\n## ÖNERİ\n\nYok.',
 'ONIZLEME.html':'<!doctype html><html lang="tr"><meta charset="utf-8"><title>IM HERE — H0 mevcut referans</title><style>body{background:#F4F1E9;color:#191A17;font-family:system-ui;padding:32px;max-width:900px}img{max-width:100%}</style><h1>Yeni yön yok · mevcut H0 korunur</h1><p>İtalik font eklenmedi. Aşağıdaki önizleme onaylı H0 varlığının değişmemiş referansıdır.</p><img src="reference-h0.gif" alt="Mevcut H0 açılışı, normal ve azaltılmış hareket"><p><a href="SPEC.md">Zamanlama ve karar</a></p></html>'}
 for n,s in files.items():(d/n).write_text(s+'\n')
 (d/'copy.proposed.json').write_text(json.dumps({'status':'NO NEW COPY','entries':[],'proposals':[]},indent=2)+'\n')
 (d/'catalog.json').write_text(json.dumps({'states':[],'recommendation':'No new italic or opening; retain approved H0','sourceSha256':sha},indent=2)+'\n')
 (d/'evidence/reference.json').write_text(json.dumps({'copiedFrom':str(gif.relative_to(B.parent)),'sha256':sha,'byteIdentical':hashlib.sha256((d/'reference-h0.gif').read_bytes()).hexdigest()==sha},indent=2)+'\n')
 for n in ['README.md','SPEC.md','HANDOFF.md','SCREEN-STATE-MATRIX.md','COPY-REVIEW.md']:
  p=B/n;p.write_text(p.read_text()+'\n## 4-11 — isteğe bağlı yön\n\n[İtalik / açılış kararı](italik-acilis/README.md): yeni öneri **yok**; Geist ve onaylı H0 korunur.\n')
 p=B/'TOKENS.md';p.write_text(p.read_text().replace('★ İtalik ve yeni açılış: isteğe bağlı bölümde karar verilir. Yeni font/bağımlılık eklenmez.','★ İtalik / yeni açılış: yok. Yerel Geist’in üç ağırlığı ve mevcut 800 ms H0 korunur. Yeni font/bağımlılık yok.')+'\n## Renk algısı kanıtı\n\n`evidence/colors-none.png`, `colors-protanopia.png`, `colors-deuteranopia.png`: Chromium vision deficiency emülasyonu; yalnız tasarım kontrolü, tıbbi test değil. Etiket + farklı ikon + kenar anlamı renk ayrımına bağlamaz. Simülasyon yakalama sonunda sıfırlandı.\n')
