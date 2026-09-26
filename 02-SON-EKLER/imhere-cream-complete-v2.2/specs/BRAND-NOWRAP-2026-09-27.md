TASARIMCIDAN MANAGERE MESAJ

# Büyük yazıda marka başlığı — v1.0

Karar: bölünmez boşluk ONAY. Mevcut appTitle yazımı korunur; yalnız U+0020 → U+00A0. EN/TR aynı: `I’M\u00A0HERE` (U+2019 kesme işareti mevcut metindeki gibidir). Bu değişiklik telefon uygulama adı IM HERE veya Firebase e-posta metinlerini değiştirmez.

Delta: l10n/brand-nowrap-patch_en.arb ve _tr.arb. Yalnız appTitle + metadata birleştirilir; tam ARB üzerine yazılmaz. Uygulamada gerçek U+00A0 bulunmalı; ekranda literal \u00A0 gösterilmez.

Yerleşim: kelime sınırından bölme önlenir. Bu tek başına dar alanda taşmayı çözmez. Erişilebilir metin büyütmesi korunur; fontu küçültme, FittedBox ile sıkıştırma, ellipsis/kırpma kullanma. Yatay alana sığmazsa çevresindeki yerleşimi genişlet veya başlığa ayrı tam genişlikli satır ayır; metni karakter ortasından bölme. iOS yaklaşık%194 ve%200, Android büyük metinde Code gerçek genişlikle doğrular. Bu teslim cihaz doğrulaması değildir.

Yerel commit; aktarım Code. Yeni ürün davranışı veya marka yazımı kararı yok.
