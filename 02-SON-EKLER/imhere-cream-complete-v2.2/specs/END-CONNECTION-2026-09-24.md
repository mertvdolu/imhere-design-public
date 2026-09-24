TASARIMCIDAN MANAGERE MESAJ

# End connection — Founder telefon turu, 24 Eylül 2026

Güncel karar önceki kapalı kartı listede tutma kararını geçersiz kılar.

## Metinler

| Anahtar | EN | TR |
|---|---|---|
| `endConfirm` | End this connection? | Bağlantıyı bitir? |
| `endConfirmBody` | This chat will leave your chat list; its message history will be kept for safety for 30 days, then deleted. You can reconnect if you both want to. | Bu sohbet sohbet listenden kalkar; mesaj geçmişi güvenlik için 30 gün saklanır, sonra silinir. İkiniz de isterseniz yeniden bağlantı kurabilirsiniz. |
| `endReportInstead` | Report instead | Bunun yerine şikâyet et |

Düğme sırası: **End connection / Bağlantıyı bitir** (ana, mürekkep dolgulu), **Report instead / Bunun yerine şikâyet et** (ikincil), **Cancel / Vazgeç** (ikincil). Ana eylem ve iptal mevcut `endConnection` / `cancel` anahtarlarını kullanır. Başlık `endConfirm` güncellenir; `endConfirmBody` ve `endReportInstead` yenidir.

## Davranış ve çizim

- `end-confirm`: onay diyaloğu, TR/EN × iOS/Android × %100/%200. Büyük metinde içerik kaydırılır; üç eylem eksilmez, yazı küçültülmez. Kendi onayı gerekir; karşı tarafın onayı istenmez.
- Report instead aynı kişinin6 kategorili şikâyet formuna gider. **Bağlantıyı bitirmez**; şikâyet ve bitirme birlikte gönderilmez. Şikâyet sonrası mevcut ayrı engelleme sorusu korunur. Geri dönüşte kaynak hâlâ erişilebilirse bu onay bağlamı geri gelir.
- Cancel ve sistem geri hareketi mutasyon yapmadan kapatır. Dış boşluğa dokunma bitirmez.
- Kart yalnız sunucu bitişi doğruladığında listeden çıkar. Hata/offline/belirsiz sonuçta kart erken kaldırılmaz; mevcut tekrar deneme/sonuç kontrolü sürer.
- `connections-open-closed` kaldırıldı; yerini `connections-after-end` aldı. Örnekte yalnız kalan açık bağlantı bulunur. Son bağlantı bittiyse mevcut `messages-connections-empty` kullanılır. Toplam durum sayısı298, beta kararları korunur.
- Mesaj hakkı dolması veya karşılıklı devam/contact nedeniyle salt okunur olmak tek başına “ended” değildir; bu kartları bu kural nedeniyle kaldırma.
- Listeden kalkma geçmişin anında silinmesi değildir. Metin Founder’ın30 günlük güvenlik saklama kararını anlatır; saat, sayaç veya otomatik yeniden bağlantı vaat etmez. Mevcut saklama başlangıcını sıfırlayan yeni bir kural tanımlanmaz. Yeniden bağlantı yalnız iki taraf isterse, mevcut uygunluk kuralları içinde olur.
- Eski “kapalı kart listede kalır” hareket kuralı `ended-card-removal` ile değiştirildi. Önceki ham kaynak plan arşivdir; güncel motion haritası ve bu not geçerlidir.

## Birleştirme

Yalnız `l10n/end-connection-patch_en.arb` ve `..._tr.arb` deltalarını `migration.json` yönlendirmesiyle birleştir. Tam ARB’ler değiştirilmedi ve üzerine yazılmamalı. Katalog, CHANGELOG, MANIFEST ve hareket notları güncel. Yerel commit; native uygulama değişikliği yapılmadı.
