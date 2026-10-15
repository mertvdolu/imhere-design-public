# gecis — validation

**PASS — browser design preview**

- 15 durum / 120 ana PNG / 72 full PNG.
- 252 gerçek DOM yerleşim ölçümü, EN/TR, %100/%200,390/412; ek320/%200 iOS+Android kabuğu.
- Yatay taşma: 0; <48 hedef: 0; yatay kesilen metin: 0. Dikey çakışma: 0; dikey metin taşması: 0; erişilemeyen başlangıç içeriği: 0.
- Her ekran tek H1; bütün fontlar yerel Geist.
- Ink/cream 15.486:1; secondary/cream 4.847:1; kontrol kenarı/cream 3.693:1. Metin≥4.5 ve kontrol≥3.
- PNG opak RGB, ana boyutlar1560×3376 ve1648×3660. Uzun metin için full kare ayrı; üst ekranın tek başına tüm içeriği göstermesi beklenmez.

Ölçüm: `evidence/<state>.json`, `evidence/summary.json`. Ürün, cihaz, VoiceOver/TalkBack, ağ ve backend doğrulaması değildir. Dikey kaydırma yetkili; font küçültme ve ellipsis yok.
