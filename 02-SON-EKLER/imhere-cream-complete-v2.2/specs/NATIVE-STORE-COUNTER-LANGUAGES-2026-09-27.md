TASARIMCIDAN MANAGERE MESAJ

# Native mağaza v1.2 / sayaç / dil başlığı

## Sayaç — ONAY

Sürüm7 design-handoff §0.A: chatRemaining (bilinmeyense chatCountPending) kaydırılan mesaj akışından ayrı sabit composer bloğunda, Your message başlığının hemen üstünde8 dp ara ile. Mesaj yazılabiliyorken görünür; klavyeyle birlikte üstte kalır. Hak0 ve composer yoksa mevcut sayaç + sınır uyarısı akışta kalır. Gelen/giden mesaj kaydırma davranışı değişmez. H7c’nin yalnız son5 mesajda gösterme önerisi bu Manager kararıyla geçersizdir; karakter sayacı son50 karakter kuralı değişmez.

Geist metadata12/400, satır1.5, textSecondary; başlıktan8 dp ayrı. Ekran okuyucu doğal sırayla sayaç→başlık→alan→Send; dekoratif çoğaltma veya her çizimde tekrar duyuru yok. Büyük yazıda sabit blok yüksekliği içeriğe uyum sağlar, mesaj alanını örten katman kullanılmaz. Gelen native iOS/A13 görüntülerinde konum uygun; klavye açık/büyük yazı hareketi bu durağan görüntülerle doğrulanmış sayılmaz.

## Başkasının profilinde dil başlığı — ONAY + delta

Yeni anahtar gerekmiyor: pakette ve uygulamada mevcut `profileLanguagesLabel` kullanılır.
EN: Languages spoken
TR: Konuşulan diller

other_profile_screen başlığının `languages` kullanımı → `profileLanguagesLabel`. Kendi profil aynı anahtarı kullanmaya devam eder. Formlardaki `languages` / Optional değiştirilmez; salt-okunur başlıkta Optional yok. Delta iki dilde mevcut değeri teyit eder, yeni değer icat etmez. Tek başına ARB birleştirmek call-site kullanımını değiştirmez; bunu Code bağlar.

## Native mağaza teslimi

`03-MAGAZA/imhere-store-v1.2/README.md` ana giriş. iOS01–05 her iki boyutta, Android01/04/05:13 kare. Kaynak PNG’ler aynen; Maya sentetik portresi SVG katmanı ile yalnız gri fotoğraf yuvalarında. Ekran içi metin/saatler değiştirilmedi; status/navigation bar kırpılmadı. 01 seçimsiz,05 dört mesajlı görüntü seçildi; başlıklı alternatifte yarım kalan mesaj nedeniyle o alternatif kullanılmadı.

Fotoğraf yuvası olmayan06 için Founder yanıtı: Alex fotoğraflı native çekim BEKLE. Android02/03 ayrıca bekliyor. Eski çizimler bu boşlukları doldurmaz. Maya portresi yerleştirildi; Alex yerleştirme işi doğru native kaynak gelene kadar bekler. Ek Maya profilinde eski Optional başlığı görüntü üzerinde boyanmaz; Code’dan düzeltilmiş çekim gerekir, bu ek görüntü mağaza setine konmadı.

Yerel commit; aktarım Code. Mağaza yüklemesi yapılmadı.
