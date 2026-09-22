# I'M HERE — Tasarım teslimi v1.4 / Paket 1
15 Eylül 2026 · Durum: Founder tarafından kabul edildi. Kabul ekindeki notlar geçerlidir. Uygulamaya uygulanmış veya cihazda doğrulanmış değildir.

## Kapsam
Ana yapı, Yakındakiler, check-in görünümleri, 12 uyarı, kişi listesi ve harita durumları; S-1…S-5 temizlikleri. İlk paketin dışındaki ekranlar tasarlanmadı. Kaynak önceliği bu görevde iletilen Founder kararları + düzeltilmiş Tasarım Gereksinim Özeti v1.0.1 + bunlarla çelişmeyen onaylı v1.3’tür. Master okunmadı. İletişim Founder üzerinden; yazılımcıya doğrudan mesaj yok.

## Nasıl incelenir?
1. `ONIZLEME.html` dosyasını tarayıcıda açın. İnternet, Figma hesabı veya yayın bağlantısı gerektirmez. 34 görünümü dil/platform/metin ölçeğiyle inceleyin.
2. `screens/svg/`: 34 görünüm × 2 dil × 2 platform × 2 metin ölçeği = **272 bağımsız SVG**. Fontlar ve örnek görseller dosyalara gömülüdür.
3. `screens/png/`: her görünüm için TR/iOS/%100 ve EN/Android/%200 olmak üzere **68 PNG**, 2× raster çözünürlükte.
4. `specs/01-YERLESIM.md`, `02-DURUM-VE-EYLEM.md`, `03-HARITA.md`, `04-ERISILEBILIRLIK.md`: uygulama ölçüleri ve davranış eşlemesi.
5. `tokens/`, `l10n/`, `contracts/`: makine okunur teslim. `05-TEMIZLIK.md` ve `DEGISIKLIKLER.md`: değişiklik kapsamı. `DOGRULAMA.md`: yapılan ve yapılmayan kontroller.

## Çizim nasıl okunur?
Dosyalar kaydırılabilir içeriğin TAM BOY çizimleridir; tek ekran içine küçültülmüş maket değildir. Referans cihaz alanı iOS 390×844, Android 412×915 logical px. Gerçek uygulamada üst/alt sistem güvenli alanları cihazdan okunur; alt navigasyon sabit, orta içerik kaydırılır. Tam boy çizimde alt bar içeriğin sonunda gösterilir. %200 çizimler büyük metinde büyüyen içerik yüksekliğini gösterir; yazı küçültülmez.

Ürün ekranı dışındaki görünüm adları, örnek platform/saat etiketleri ve form karşılaştırma sayfası inceleme içindir. Harita geometrisi SADECE yerleşim örneğidir; gerçek H3 verisi/konum/kamera koordinatı değildir. © sağlayıcı satırı gerçek SDK attribution'ının yer tutucusudur; üretimde seçilen sağlayıcının tam yasal bileşeni kullanılmalıdır. Portre/ad/bio örnekleri tasarım fixture’ıdır; üretimde sahte kullanıcı olarak yüklenmez. 14:06/batarya çizimleri yalnız safe-area ölçüm yardımıdır.

## Onay kapsamı
v1.4, v1.3 üzerine eklenen tasarım önerisinin sürümüdür; bu dosyanın teslimi uygulama onayı anlamına gelmez. Kapsam dahilindeki metin/kontrast temizlikleri ve FD-75 uygulanmıştır. Başka ürün değişikliği önerilmedi. Önceki v1.4 devir değerlendirmesi bir rapordu; bu arşiv ilk ekran paketidir.
