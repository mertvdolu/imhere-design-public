# IM HERE — Cream & Ink v2.2

Son güncelleme: [CH-138 / ERT-050 / Code soruları](specs/CODE-SORULARI-CH138-ERT050.md).

Founder’ın bütün temayı krem/siyaha geçirme onayıyla hazırlanan **tam güncel tasarım paketi**.

- **296 ekran durumu / 2368 SVG**: TR + EN × iOS + Android × %100 + %200.
- Önceki güncel katalogdaki 287 durumun tamamı kapsanır; son ekler ayrıca çizilir.
- Her durum için EN/iOS/%100 ve TR/Android/%200 PNG önizlemeleri.
- `ONIZLEME.html`: bütün ekranların aranabilir, filtrelenebilir kataloğu. İnternetsiz açılır.
- `DENEYIM.html`: onaylı ana ekranların etkileşimli HTML referansı. Canlı harita internet ister.
- `tokens/theme.tokens.json`: ortak renk, tipografi ve bileşen ölçüleri, sürüm 2.2.
- `map/`: krem MapLibre/OpenFreeMap stili; gerçek veri katmanı içermez.
- `brand/`: gönderilen logo ile açık uygulama simgesi, splash ve Android bildirim maskesi.
- `l10n/`: tam referans sözlükleri, küçük metin deltası ve önceki alias/placeholder kurallarını koruyan migration.
- `specs/TASARIM-DEVRI.md`: yerleşim, durumlar ve uygulama notları.
- `evidence/validation.json`: doğrulamanın gerçek kapsamı; `MANIFEST.json`: dosya bütünlüğü.

Bu teslim tasarımı tamamlar. Flutter, sunucu veya mağaza derlemesi değiştirilmedi. Native entegrasyon ve gerçek cihaz doğrulaması ayrı adımdır. Eski yeşil paketler sürüm geçmişi/arşivdir; aktif görsel kaynak değildir.
