from pathlib import Path
import json

def prepare(B):
 summary=json.loads((B/'evidence/summary.json').read_text())
 report=f'''# TASARIMCIDAN MANAGERE MESAJ

KİMDEN: Product Designer — I'M HERE Mobile  
KİME: Founder — Mert Dolu (→ Manager)  
TASK: V15-TASARIM · Son parça ve bütün teslim

## Konum ve kapsam

- Depo: https://github.com/mertvdolu/imhere-design-public
- Dal: `design/v15-cream-ink-v23`
- Klasör: `v15/`; ortak katalog: `EKRAN-KATALOGU.json`.
- {summary['states']} durum · {summary['mainPng']} ana PNG · {summary['fullPng']} uzun içerik PNG. Tam dosya sayısı ve SHA256: `MANIFEST.json`.
- 12 bölüm: d0, topluluk-kayit, gecis, ayarlar-topluluk, secici, meslek, linkedin, filtre, kart-adimi, ikonlar, professional, italik-acilis.
- İtalik/açılış bölümü yeni durum üretmez; mevcut H0 referansını ve “yeni yön yok” kararını içerir.
- HTML önizleme + kaynak HTML/CSS/JS, SVG ikonlar, Geist dosyaları/lisansı, PNG, SPEC, HANDOFF, COPY-REVIEW, katalog, matris ve ölçüm kanıtları dahildir.
- Son commit ve uzak SHA teslim mesajında bildirilir. Önceki parça commit’leri aşağıdadır.

## VALIDATION

{summary['measurements']} DOM yerleşim ölçümü: yatay taşma {summary['horizontalOverflow']}, 48×48 altı hedef {summary['smallTargets']}, yatay kesilen metin {summary['clippedText']}.
Her durum EN/TR × %100/%200 × 390/412 mantıksal boyut; ana PNG’ler 4×, opak RGB.
Her durumda ek 320 px / %200 iOS ve Android kabuğu ölçümü var. Uzun içerik dikey kaydırılır; `--full` kareler ayrıca verilir.

Ek kanıt: 5 yüksek kontrast/dar ekran kontrolü, 14 etkileşim senaryosu, protanopi/deuteranopi renk benzetimi. Son dosya/copy kontrolü `evidence/final-validation.json`.
Bunlar tasarım önizlemesi ölçümleridir; native uygulama, gerçek sunucu, VoiceOver/TalkBack ve mağaza kabulü kanıtı değildir.

## TOKENLAR

| Rol | Ana renk | On-color | Hafif yüzey | Ana/krem | On/ana | Ana/hafif |
|---|---|---|---|---|---|---|
| Networking | #344E78 | #FCFAF5 | #E5E9EF | 7.421:1 | 8.030:1 | 6.874:1 |
| Friendship | #315C46 | #FCFAF5 | #E5EBE4 | 6.766:1 | 7.321:1 | 6.304:1 |

Ink/krem 15.486:1; yardımcı metin/krem 4.847:1; kontrol kenarı/krem 3.693:1.
Hafif yüzeyler/dekoratif sınırlar anlamı tek başına taşımaz; metin, farklı ikon, standart radyo işareti ve yeterli kontrol sınırı korunur.
Cream & Ink v2.3 normatif yüzeyleri korundu: kabartma ve iç yüzey krem #F4F1E9; brief’teki #FCFAF5, Ink üstündeki açık metin rolündedir.

## 5 SORU — KARAR (★)

1. Koyu, bastırılmış mavi #344E78 ve yeşil #315C46. Kremde metin kontrastını sağlar; yoğunluk renklerinin pastel lekelerinden ayrılır. Etiket ve farklı ikon birlikte kullanılır.
2. Hap biçimli topluluk göstergesi (yalnız B). Haritada üst solda, konum eylemi sağda; atıf alt menünün üstünde ayrı satır. Dokunma yalnız Ayarlar → Topluluklar’a gider, doğrudan geçiş yapmaz.
3. Filtre tam ekran alt sayfa. 24 dp kenar ve dikey kaydırma, uzun TR/%200 içeriği taşır; beş seçim sınırı metinle, 50+ ayrı sayı sütunuyla gösterilir. Sıra seçim sırasında değişmez.
4. Beş ikon yeterli: Professional çanta, Social konuşma, Activity hareket çizgisi, Networking bağlı kareler, Friendship iki kişi. Kategori Ink; topluluk rengi yalnız etiketli topluluk kontrolünde. 16/20/24 görünür ölçüler, 1.8 çizgi, en az 48 hedef.
5. Yeni italik ve yeni açılış yönü yok. Yerel Geist’in üç ağırlığı ve onaylı H0 korunur. H0 zaten 620 ms çizgi + 140 ms dolgu + 40 ms sabit kare = 800 ms; sıcak dönüşte yok, azaltılmış harekette işaret anında görünür, uygulama açılışını bekletmez.

## KENDİ KARARLARIM (★)

- Tek topluluk göstergesi de dokunulur; aynı Ayarlar girişinden ikinci topluluğa katılma bulunur.
- “Both” kartı nötr Ink; üçüncü bir topluluk rengi yaratılmaz.
- Boş kartta Kaydet = Şimdi değil; boş başarı mesajı/kart kaydı oluşturulmaz.
- Seçim yapılmadığında mevcut genel “Please choose an option” değeri kullanılır (`errorGenderRequired`; anahtarın eski adı akışa yeni cinsiyet kuralı getirmez).
- LinkedIn kayıt adımında Atla; kayıtlı profil ayarında Vazgeç. Görünürlük seçenekleri eşit ağırlıkta, Herkes yalnız standart radyo noktasıyla seçili.
- Harita atfı mevcut 12 px lisans satırı olarak korunur; uygulama metni %200 ölçeklenir.

## YENİ BİLEŞEN — ONAY GEREKİR

- Community indicator: mevcut hap + ikon + etiket birleşimi.
- Grouped occupation selector: mevcut arama + açılır satır + radyo birleşimi.
- Counted filter row: mevcut onay kutusu + etiket + sayı birleşimi.
- Yeni topluluk renk tokenları ★ öneridir; yeni font, bağımlılık veya genel ikon ailesi yok.

## METİN

Onaylı değerden sapma hedefi 0; ölçülmüş sonuç `evidence/final-validation.json` içinde.
HB-37 dosyası artık **r5**: §14.1’deki son üç LinkedIn değeri aynen alındı. Önceki “METİN-EKİ BEKLİYOR” durumu bu kaynakta kapanmış.
Copy dosyasının `proposed` adı teslim standardıdır; mevcut onaylı metin statüsünü değiştirmez. Yeni wording önerisi yok. Canonical uygulama ARB dosyalarına merge yapılmadı.

## AÇIK / RİSK

- Code native Dynamic Type, OS erişilebilirlik ve gerçek yanıtları ayrıca doğrulayacak. Önizleme kontrollü durum örnekleridir; bütün form/veri işlemlerini taklit eden uygulama değildir.
- Filtrede “yaklaşık dakikada bir” notu yalnız backend gerçekten bu aralıkla yeniliyorsa kullanılmalı; Code teyidi gerekir.
- D0 ayrı 1.4.2 güncelleme kapısı; mağaza URL’si bulunmayan eski iOS yapıya eşik yükseltilmemeli (karar 42).
- Seçici ve Professional sahneleri ilgili bileşen yerleşimine odaklanır; mevcut check-in uzatma/Stop, Events RSVP/tarih/iptal akışlarını kaldırmaz.
- Eski 10 günlük kayıtlar kendi bitişinde sona erer; 1.5 yeni amaç uyuşmazlığı/10 gün akışını üretmez. Katalogda flag-off ve flag-on ayrımı işlendi.
- Yalnız tasarım dalına push. Main birleşimi, uygulama deposunda değişiklik, deploy veya mağaza gönderimi yapılmadı.

## Parça geçmişi

| Bölüm | Commit |
|---|---|
| D0 | 733db7975699128802af4051c64ed6d7b4b67d00 |
| Topluluklar 4-1…4-4 | 287188fb593fac15b6358e4863a5c6e896e2a339 |
| Meslek + LinkedIn | 7db8bca927e7482fa4c2336af88294df51ab1cc0 |
| Filtreler | aac07efbcc1f772c747453736c9d1d2728a65659 |
| Kart kayıt adımı | 0790ad8408512d5f62469246d686af92104a4a06 |
| İkonlar + Professional | 73e827dcc9707b63ac6bbd2573f6f9e38b9ad0dc |

Sonraki parça: yok; tasarım teslimi tamamlandı. Yeni bileşen/token ★ kararları Founder incelemesine, native uygulama ve ölçüm Code’a aittir.
'''
 (B/'TESLIM-RAPORU.md').write_text(report)
 for f in ['README.md','HANDOFF.md']:
  p=B/f;p.write_text(p.read_text()+'\n## Tek teslim raporu\n\n[Founder / Manager raporu](TESLIM-RAPORU.md) · [Son doğrulama](evidence/final-validation.json)\n')
 # Clarify canonical data and reproducibility without touching past deliveries.
 (B/'source/README.md').write_text('''# Üretim / kapsam

`states.json`, `copy-bank.json`, `occupation-catalog.json` bu teslimin dondurulmuş girdileridir.
`build.py` → browser/CUA ile `capture.mjs` → `finalize.py` → `validate.py` sırası kullanılır.
PNG yakalama yalnız belgelenmiş CUA tab + CDP köprüsüyle çalışır; bağımsız Playwright oturumu açmaz.
`capture.mjs` fonksiyonuna mevcut tab/CDP ve çıktı yolu verilir. `measure.js` yalnız DOM ölçer.

`add_*.py` ve `prepare_copy.py` tasarımın ilk üretim yardımcılarıdır; final girdileri yeniden üretmek için çalıştırılmaz. Son bağlam düzeltmeleri `states.json` içindedir. Canonical kaynakların yeni sürümü gelirse ayrıca incelenmelidir.

Bu HTML durum önizlemesidir; gerçek üyelik, LinkedIn, kart, filtre, harita, hesap veya ağ işlemi yapmaz. Üstteki başarı/hata düğmeleri yalnız tasarım incelemesi içindir. Veri girme/arama kontrolleri örnek etkileşim sağlar; tam uygulama modeli değildir.
''')
