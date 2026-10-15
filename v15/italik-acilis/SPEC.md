# Açılış / tipografi

DESIGN RECOMMENDATION — FOUNDER APPROVAL REQUIRED

★ Yeni italik yönü: **yok**. v2.3 yerel pakette italik yok; 1.5 bilgi yoğunluğu artarken yeni vurgu ailesi ve lisanslı font paketi eklemeyi önermiyorum. Var olan üç Geist ağırlığı, TR glyphleri ve %200 yerleşimler bu teslimde ölçüldü. Hiçbir sahte italik uygulanmadı.

★ Yeni açılış yönü: **yok**, mevcut H0 aynen.

| Başlangıç–bitiş | Özellik | Eğri |
|---|---|---|
|0–620 ms|Kanonik logo konturu 0→1|Çizgi toplam uzunluğunda lineer|
|620–760 ms|Kesişim dolgu opaklığı 0→0.92|Mevcut quick|
|760–800 ms|Kanonik işaret|Sabit|

Titreşim yok. Sıcak dönüşte oynatılmaz. Reduce Motion: logo 0 ms’de tamamen görünür. Hedef ekran erken hazırsa açılış bekletilmez; dekorasyon iptal edilir; 150 ms opaklık geçişi kullanılır. Native splash krem + orijinal işaret; animasyon ilk Flutter karesindedir. Oran/path değişikliği: 0.

Normatif kaynak: ../../02-SON-EKLER/imhere-cream-complete-v2.2/motion/hareket-ve-his-v1/SPEC.md#01-ink-signature
