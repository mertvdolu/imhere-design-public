TASARIMCIDAN MANAGERE MESAJ

# İletişim kartı — üç durum v1.0 · 2026-09-28

Kaynak: Desktop/here/harbor/iletisim-karti-metinleri.md §E, boş kart metni §D. Yalnız kullanıcı tarafından istenen üç durum tasarlandı. HARBOR’un hukuki değerlendirmesi yeniden onaylanmadı; gizlilik/şartlar/site metinleri değiştirilmedi. Ön doldurma, onboarding zorunluluğu, günlük limit değeri veya yeni paylaşım davranışı tasarlanmıyor.

## 1. contact-card-confirm — ilk gönderim onay sayfası

Sohbet başına ilk gönderimde: başlık → gerçekten gönderilecek dolu alanların önizlemesi → HARBOR uyarısı → Send ana → Not now ikincil. Alan değerleri çalışma anındaki karttan gelir; boş alan gösterilmez. Önizleme etiket/değer biçiminde, kart surface#FCFAF5, radius15, padding16. Alanların gönderilecek kopyası ile önizleme tutarlı olmalı; değişirse eski önizlemeyle başka değer gönderilmez.

Tam sayfa, yan24, safe area; üst başlık Geist36/500/1.12; gövde16/400/1.6 Ink. Bölümler arası24; düğmeler arası12. Uyarı küçültülmez, kısaltılmaz. İki düğme metnin ardından aynı kaydırılabilir akışta; içerik üstüne sabitlenmez. İlk uyarı atlanarak gönderim yapılmaz. Not now göndermeden kapatır. Sistem geri göndermeye dönüşmez. Bu sayfa karşı tarafın onayını istemez.

## 2. contact-card-empty — Send pasif

Gönderilecek dolu alan yokken Send gerçek disabled semantiğinde. Altında8 dp: Add at least one detail to send / Göndermek için en az bir bilgi ekle. Stil helper14/400/1.4, textSecondary#696A62. Pasiflik yalnız renk değil, disabled erişilebilirlik durumu ile iletilir. Yardım satırı düğmeyle ilişkilendirilir. Yeni alan şartı veya hangi alanın zorunlu olduğu icat edilmez; en az biri gönderme şartıdır.

Önizlemedeki bu durum boş kart + düğme kesitidir; profil düzenleme akışının tamamı değildir. Mevcut kart düzenleme girişini değiştirmez.

## 3. contact-card-send-again — sonraki gönderim

Mevcut Send eylemi altında8 dp sabit bilgilendirme: Sent details can't be taken back. / Gönderilen bilgiler geri alınamaz. Helper14/400/1.4 textSecondary. Sabit = sürekli görünür yardımcı metin; toast değildir. “Tek satır” tek metin öğesidir; dar ekran/%200 yazıda sarılır, ellipsis yok. Tekrar onay sayfası eklenmez. Boş kartta pasif Send + boşluk yardım metni önceliklidir.

## Ortak

Düğme hedefi en az48×48; yükseklik metinle büyür, radius12. Krem#F4F1E9, Ink#191A17. EN/TR, iOS/Android aynı hiyerarşi; OS safe area/platform gezinme korunur. Ekran okuyucu sırası başlık→alanlar→uyarı→eylemler. Gönderildi sunucu onayından önce gösterilmez; mevcut pending/hata/offline davranışı bu üç durumla değiştirilmez.

## Metin / uygulama

l10n/contact-card-v1-patch_en.arb ve _tr.arb:6 anahtar + metadata. HARBOR’un EN/TR onay metni aynen; boş kart TR karşılığı tasarımcı çevirisidir. Tam ARB üzerine yazılmaz. Eski paylaşılan iletişim anahtarları silinmez; bu ek kart akışının anahtarlarıdır. Code eşdeğer anahtar oluşturduysa migration’da eşlesin; ikinci kopya üretmesin.

ONIZLEME.html:6 dil/durum örneği; yüzde200 ve telefon genişlikleri için kontroller. Köşeli alan açıklamaları tasarım yer tutucusudur, uygulama metni veya sahte kullanıcı verisi değildir. Native kod/cihaz testi yapılmadı. Ek katalog catalog.json’dadır; ana katalog eski SVG’leri bu ekle yeniden çizilmiş sayılmaz.

Yerel commit; aktarım Code.
