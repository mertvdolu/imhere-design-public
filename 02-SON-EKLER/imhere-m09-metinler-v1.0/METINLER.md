# I’M HERE — M09 metin önerisi v1.0

Durum: inceleme için. Anahtar adları öneridir; yazılımcının mevcut adlarıyla eşlenebilir. Delta olarak birleştirilir; mevcut ARB üzerine yazılmaz.

## chatRetentionInfo

TR: Bu sohbet yazmaya kapandıktan sonra mesajlar en fazla 30 gün saklanır.

EN: Messages are kept for up to 30 days after this chat becomes read-only.

## chatRetentionWarning

TR: Bu yazışma yakında silinecek. Paylaşılmış iletişim bilgileri varsa, ihtiyacın olanları kaydedebilirsin.

EN: These messages will be deleted soon. If contact details have been shared, you can save any you need.

## chatRetentionDeleted

TR: Saklama süresi dolduğu için bu yazışmadaki mesajlar silindi.

EN: The messages in this chat were deleted because their retention period ended.

## Kullanım

- Bilgi satırı sohbet ekranında kalıcıdır; sayaç, geri sayım veya kesin silinme saati içermez.
- Sürenin başlangıcı ürünün yetkili yazılabilirlik durumundan alınır. UI yeni bir başlangıç anı hesaplamaz. Kullanıcının ilettiği kapanma, karşılıklı devam + iletişim paylaşımı ve hakların dolması kuralları değiştirilmez.
- Yaklaşan silinme uyarısı yalnız sistem bu durumu doğruladığında gösterilir. Bu teslim yeni gün eşiği tanımlamaz. Paylaşım veya iletişim bilgilerine erişim hakkı kazandırmaz.
- Silinmiş metni ancak saklama süresi nedeniyle silinme doğrulandığında gösterilir; yükleme hatası, çevrimdışı durum veya boş yeni sohbet için kullanılmaz.
- Silinme mesaj içeriği içindir; profillerin silindiği ima edilmez.
- Yeni ürün davranışı veya tasarım önerisi yoktur; bu teslim yalnız metindir.
