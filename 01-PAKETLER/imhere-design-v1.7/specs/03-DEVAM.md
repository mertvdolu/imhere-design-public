# 03 — Bağlantıyı devam ettir: özel karar
Sohbette sakin bir ikincil eylem; pulse, zamanlayıcı, hak doldurma hedefi veya “diğeri seni bekliyor” baskısı yok. Karar erken verilebilir. İlk görünümde seçili varsayılan/otomatik EVET/HAYIR yok.

## Kullanıcının kendi durumları
| Durum | Sunum |
|---|---|
| Henüz karar yok | Açıklama + Devam etmek istiyorum / Devam etmek istemiyorum; Sohbete dön |
| EVET gönderiliyor | İşlem açıklaması; çift işlem pasif; kaydedildi başarısı yok |
| Kendi EVET'i onaylı | Tercihin kaydedildi + yalnız kendi Devam etmek istiyorum metni; geri al ve Sohbete dön |
| EVET geri alınıyor / hata | Gerçek sonuca kadar son onaylı kendi EVET durumu korunur; işlemin ayrı açıklaması vardır |
| EVET geri alındı | Mevcut continueWithdrawn; yeniden kendi kararını seçebilir |
| HAYIR son onay | Kararın geri alınamaz olduğu önceden yazılır; kullanıcının kendi eylemini doğrulayan onay; karşı taraf onayı değildir |
| HAYIR gönderiliyor / hata | Sunucu sonucu olmadan sona erdi denmez; hata aynı kullanıcı eyleminde tekrar denemeye izin verir |
| HAYIR gerçek başarı / mevcut kapalı durum | Nötr Bağlantı sona erdi. Sebep veya karar saati yok; kararı değiştir/geri al eylemi yok |

HAYIR finali, başarılı sunucu sonucundan sonra geçerlidir; işlemin başarısız olması alınmış final kararı varmış gibi gösterilmez. Son onay ekranındaki metin yeni bir karşı-taraf onay mekanizması değildir. Önceki End Connection için kendi-eylemi onayı kabulü korunur; bağımsız güvenlik işlemlerinin tamamı Paket 4'tedir.

## Karşı karar gizliliği
Karşı tarafın tek başına EVET/HAYIR seçimi, karar verip vermediği veya zamanı gösterilmez. Sayaç, rozet, bekliyor etiketi, oran, yazı/ikon/rengin değişmesi, push veya accessibility ile sızıntı yok. Kullanıcının kendi kaydedildi/geri alındı metni karşı tarafa yayınlanmaz. `continue-yes-saved` sadece kendi durumudur; diğer kişi hakkında çıkarım yaptıran durum satırı yok.

HAYIR karşıya yalnız nötr bağlantı sona erdi sonucu üretir; kim bitirdi/ne zaman/hangi tercih gibi sebep açılmaz. Bu sonuç engelleme değildir; mevcut ürün davranışını UI yeniden tanımlamaz.

## Karşılıklı EVET ve yarış durumları
Sunucu karşılıklı EVET koşulunu doğruladığında normal sohbet yazma alanı kapanır, ayrı contact formu açılabilir. Bu noktada eski geri-al düğmesi kullanılabilir gösterilmez; normal kalan mesajlar tüketilmez. İki oyu ayrı gösteren tablo/rozet eklenmez; UI yalnız açılan iletişim paylaşımı yetkisini sunar.

EVET geri alma işlemi ile karşılıklı sonuç aynı anda gelirse gerçek nihai durum esas: başarılı geri alma, karşılıklı salt-okunur/contact veya kapanmış/kullanılamıyor sonucu. UI “geri alındı” mesajını varsaymaz ve başarısızlığın nedenini karşı kişinin kararıyla açıklamaz. Karar verileri karşı kullanıcıya tahmin ettirilmez.

Yükleme/hata/offline ayrı çizimlerdir. Yükleme hatası “henüz karar vermedin” olarak yorumlanmaz; boş varsayım üzerinden eski tercih ezilmez. Gerçek veri gelene kadar yeni onay üretmeyen durum görünümü kullanılır.
