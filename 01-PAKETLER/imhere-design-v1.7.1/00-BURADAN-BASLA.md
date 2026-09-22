# I'M HERE — v1.7.1 / M06 kişi görünümü eki
Kabul edilmiş v1.7 üzerine küçük ek; v1.8'in yerine geçmez.

- `ONIZLEME.html`: Üç durum ve görünür/gizli profil varyantları; sayaç örnekleri. TR/EN, iOS/Android, %100/%200.
- `specs/01-KISI-DURUMLARI.md`: Yerleşim ve gerçek durum bağları.
- `specs/02-METIN-VE-MIGRATION.md`: §7 kanonik anahtarları, parametreler ve birleştirme.
- `l10n/v1.7.1-patch_tr.arb`, `v1.7.1-patch_en.arb` + `migration.json`: Birleştirilecek küçük değişiklik.
- `MANAGER-NOTU.md`: İletim notu. `DOGRULAMA.md`: Kontrol sonuçları.

**8 görünüm × 2 dil × 2 platform × 2 ölçek = 64 SVG; 16 PNG.** Altısı üç kişi durumunun görünür/gizli alan varyantları; ikisi 19/20 ve 20/20 sayaç entegrasyon örnekleri. Portre ve veriler fixture'dır.

4 yeni metin anahtarı; mevcut `pendingSlots` ve metadata'sı güncellendi. `app_*.arb` yalnız v1.7 + bu ekin 404 anahtarlı referansıdır. **Canlı ARB üzerine yazılmaz.** v1.8'in 52 ek metni ve uygulamaya özel anahtarlar korunur; v1.8 ile birleştirilmiş tasarım sözlüğü 456 anahtar olur.

Tema/token/font aynı; eski v1.6/v1.7/v1.8 teslimleri değiştirilmedi. Uygulama/Flutter/backend kodu değişmedi; web sitesi güncellenmedi. M06 durum bağları ve M10 gerçek cihaz yerleşimleri yazılım tarafında doğrulanır.
