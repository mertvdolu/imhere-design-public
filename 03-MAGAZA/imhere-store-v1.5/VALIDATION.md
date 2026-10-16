# Store 1.5 — doğrulama

**PASS — görsel dosya doğrulaması.**

- 18 telefon PNG:6×1206×2622,6×1320×2868,6×1080×1920; RGB, alfa yok.
- 12 native kaynak SHA256 aynı; SVG içine gömülü PNG baytları kaynakla aynı. Kırpma, esnetme veya fotoğraf/saat/pil/UI örtüsü yok.
- Başlık ve alt satırlar Founder brief'ine birebir eşit. 03 özel alt açıklaması doğru; dış metinlerde LinkedIn yok.
- Geist gerçek font ölçümüyle başlık, alt satır ve açıklama yatay/dikey sığma kontrolü; çerçeveyle çakışma yok.
- 1.4 renkleri: Ink/krem ve yardımcı metin/krem kontrastı ≥4.5:1.
- Play feature 1024×500 RGB; 1.4 PNG SHA256 ile aynı, purpose ifadesi yok.
- Her platformun istek profili kendi native kaynağından gelir.
- 3 contact sheet görsel kontrol için; SHA256 ve boyutlar MANIFEST'te.

Kanıt: `evidence/artwork-validation.json`, `evidence/export-validation.json`, `source/capture-provenance.json`. HTML önizleme tarayıcı kanıtı `evidence/preview-validation.json` içindedir.

Bu kontrol native uygulama testi, HARBOR onayı veya App Store / Google Play kabulü değildir. Yeni native kaynakların build/commit bilgisi verilmedi; üretim sırasında icat edilmedi. Saatler kaynak haliyle korunur; dış çerçeve eski kaynaktaki bilgileri düzeltmez.
