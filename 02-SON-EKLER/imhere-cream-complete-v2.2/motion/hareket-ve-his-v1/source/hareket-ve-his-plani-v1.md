# I'M HERE — Hareket ve His Planı v1

**Tarih:** 24 Eyl 2026
**Hazırlayan:** Manager (Sanat Yönetmeni rolüyle)
**Durum:** Founder onaylı yön. Tasarımcı çizer, Code uygular.
**Kaynak:** 2026 Apple Design Awards, iOS 26 / Liquid Glass, Material 3 Expressive, 2026 trend raporları ve projenin kendi belgeleri (Cream & Ink v2.2, katalog 295 durum, gizlilik 1.2.1).

---

## 1. Tek cümlelik ruh

> **"Kâğıda düşen bir mürekkep damlası: sakin, sıcak, gerçek."**

I'M HERE bir flört uygulaması değil. Yakınındaki gerçek insanlara "buradayım" deyip yüz yüze buluşmanın sessiz cesaretini anlatıyor. Bu yüzden hareket gösterişli olmayacak. **Varlık (presence)** hissi verecek: bir nefes, bir dalga, bir el sallama. Tema zaten "Cream & Ink": krem kâğıt, mürekkep siyahı. Hareket dili bu metaforun devamı olacak. Mürekkep yayılır, kâğıt yerine oturur, harfler kendini yazar.

## 2. Araştırmadan çıkan beş ders (2026)

1. **Hareket artık bir dil, süs değil.** 2026 trendlerinin ortak noktası, animasyonun durum değişikliğini ve sebep-sonucu anlatması. Her animasyon bir soruya cevap vermeli: "Ne oldu? Nereye gitti?"
2. **Yay (spring) fiziği standart oldu.** Material 3 Expressive, Android'de hareket sistemini sabit sürelerden yay fiziğine taşıdı. iOS zaten yay tabanlı. İki platformda da "yerine oturan", hafif esneyen hareket doğal hissettiriyor.
3. **Ödül alanlar tek bir güçlü tema etrafında tutarlı.** 2026 ADA kazananlarından Moonlitt ve Tide Guide, konularına özgü özel animasyonlar ve tutarlı bir tema dünyasıyla kazandı. Aldıkları ödüller Interaction ile Visuals and Graphics. Ders: her ekranda ayrı bir şov değil, tek bir imza dil.
4. **Erişilebilirlik ödül kriteri.** Pine Hearts, "hareket seçenekleri" ile Inclusivity ödülünü aldı. "Hareketi azalt" desteği artık bir artı değil, beklenti.
5. **Liquid Glass'ı kopyalamayacağız.** iOS 26'nın cam dili, Apple'ın yerel katmanlarında gerçek kırılma yapıyor. Flutter'da taklidi hem ağır hem sahte duruyor. Krem kâğıt dünyamızla da çelişir. Cam yerine **kâğıt derinliği** kullanacağız: yumuşak gölge, katman, hafif kalkma.

## 3. Değişmeyen kurallar ("bütün kurallar kalktı" dense bile)

Founder bütün tasarım sınırlarını kaldırdı. Aşağıdakiler tasarım kuralı değil; güvenlik, yasa ve kalite kuralı. Bunlar kalıyor:

- **Hareketi azalt:** iOS "Reduce Motion" ve Android "Animasyonları kaldır" açıksa her şey 150 ms'lik yumuşak geçişe iner. Döngü animasyonu olmaz.
- **Performans:** düşük seviye Android'de 60 fps. Takılan animasyon, animasyonsuzluktan kötüdür.
- **Dokunma hedefi ≥48, kontrast ve ekran okuyucu:** mevcut ölçümler bozulmaz.
- **Sahte veri yok:** yoğunluk kareleri, uydurma sayılar, "12 kişi yakında" gibi ölçülmemiş şeyler gösterilmez.
- **Metin sistemle aynı:** animasyon, sistemin yapmadığı bir şeyi ima etmez. Örneğin "gönderildi" animasyonu yalnız sunucu onayından sonra oynar.
- **Sıfır yeni bağımlılık:** Flutter'ın kendi animasyon araçları, CustomPainter ve platform titreşimi yeterli. Lottie ve Rive eklenmez.
- **Kritik yol korunur:** hareket katmanı kapalı testi ve Dilim 1 dağıtımını geciktirmez (bkz. §7).

## 4. Hareket belirteçleri (motion tokens)

| Belirteç | Değer | Kullanım |
|---|---|---|
| `motion.quick` | 150 ms, ease-out | Basış, seçim, küçük durum değişimi |
| `motion.standard` | yay: sönüm 0.90, tepki 0.35 s | Sayfa geçişi, kart, sekme |
| `motion.expressive` | yay: sönüm 0.75, tepki 0.45 s | İmza anlar (buradayım, merhaba, bağlantı) |
| `motion.stagger` | 40 ms, en fazla 6 öğe | Liste açılışı |
| `motion.reduced` | 150 ms opaklık | "Hareketi azalt" açıkken hepsinin yerine |

**Titreşim (haptics):** hafif, yalnız anlamlı anlarda.
- Seçim: `selectionClick`.
- Başarı (merhaba gönderildi, bağlantı kuruldu): hafif başarı titreşimi.
- Uyarı (hata): orta darbe.
- Liste kaydırmada titreşim yok.

## 5. İmza anlar (uygulamayı sevdirecek 7 an)

1. **Açılış: "Mürekkep imzası".** Founder logosu tek bir mürekkep çizgisiyle kendini çizer. 700–900 ms, yalnız soğuk açılışta. Sonra krem zemine yumuşakça yerleşir. Hareketi azalt açıksa logo doğrudan görünür.
2. **"I'm here" (konum paylaşımını başlatma): "Varlık dalgası".** Haritadaki kendi noktandan krem zemine 2 halka yayılır. Mürekkep rengi, %12 opaklık, 1.2 s. Hafif titreşimle birlikte. Oturum açık kaldıkça noktan çok yavaş nefes alır (4 s döngü). Durdurunca (Stop) halkalar içeri çekilir ve nokta söner. Bu, "erişim hemen kesildi" gerçeğini görsel olarak söyler.
3. **Yakındakiler listesi: "Kâğıt yerleşmesi".** Kartlar 40 ms arayla aşağıdan 8 px kalkıp yerine oturur (`standard` yay). Yenilemede yalnız yeni gelen kart bu hareketi yapar, bütün liste değil.
4. **Profil açma: "Fotoğraf kahramanı".** Karttaki fotoğraf, profil ekranının üstündeki büyük fotoğrafa akarak büyür (shared element / hero). Geri dönüşte yerine döner. Android'de "predictive back" ile kullanıcı geri hareketini sürüklerken ekran küçülerek önizlenir.
5. **Merhaba gönderme: "El yazısı".** Düğme bir an içeri çöker, sunucu onayı gelince "Hello sent" yazısı soldan sağa mürekkeple yazılıyormuş gibi açılır (maskeli çizgi, 500 ms). Başarı titreşimi. Onay gelmeden bu animasyon oynamaz, bekleme göstergesi görünür.
6. **Bağlantı kuruldu: "İki nokta".** İki kişinin küçük portresi iki yandan gelip ortada hafifçe dokunur, arkalarında tek bir mürekkep halkası yayılır. Konfeti yok, patlama yok. 1 s, sonra sohbete geçiş düğmesi belirir.
7. **Mesaj: "Yerine oturan kâğıt".** Gönderilen balon, yazma kutusundan çıkıp yay ile yerine oturur. Gelen mesaj soldan 12 px kayarak belirir. Klavye açılıp kapanırken yazma kutusu klavyeyle birlikte kayar, ayrı zıplamaz.

## 6. Ekran ekran his haritası

| Ekran | Hareket | Not |
|---|---|---|
| Kayıt / davet kodu | Alanlar arası geçişte odak çizgisi kayar; hata olursa alan 2 px sağa sola 2 kez sallanır + uyarı titreşimi | Kırmızı yanıp sönme yok |
| Profil düzenleme | Fotoğraf yükleme: avatarın çevresinde mürekkep halkası gerçek yüzdeyle dolar; "işleniyor"da halka yavaşça döner; bitince içeri oturur | Yüzde snapshotEvents'ten; uydurma yok |
| Doğum tarihi | Platform çarkı / takvim, kendi yerel hareketleri | Dokunma |
| Kendi profilim | Kalem (düzenle) basılınca 150 ms'de forma dönüşen geçiş; gizli alanların kilidi hafifçe belirir | |
| Harita (tam ekran) | Açılışta harita krem zeminden belirir, kendi noktan en son gelir | Yoğunluk karesi yok |
| Sekmeler | Alt çizgi göstergesi sekmeler arasında yay ile kayar | Mevcut çizgi korunur |
| Bağlantılar | Liste kâğıt yerleşmesi; bağlantı bitirilince satır yumuşakça daralarak kapanır | |
| Sohbet | §5-7 + okundu işareti opaklıkla belirir | |
| Güvenlik menüsü / şikâyet | Hareket en az: sade sayfa geçişi, gönderince sakin onay | Ciddi anlarda şov yok |
| Boş durumlar | Tek bir sakin öğe nefes alır (ör. mürekkep noktası), ekran başına en fazla 1 döngü | Hareketi azalt açıkken durur |
| Hata / bağlantı yok | Üstten ince bir şerit iner, düzelince geri çekilir | |
| Ayarlar / Contact us | Yalnız standart geçişler | |
| Hesap silme | Hareket yok denecek kadar az; onayda sakin kapanış | Duygusal manipülasyon yok |

## 7. Uygulama sırası (kritik yolu bozmadan)

Kapalı testte sürüm güncellemek serbest ve 14 günlük sayacı sıfırlamıyor. Bu yüzden hareket katmanı kapalı test sırasında güncelleme olarak gider.

- **H0 — Tasarım (şimdi, paralel):** Tasarımcı bu planı hareket spesifikasyonuna çevirir. Belirteçler, 7 imza an için kare kare zamanlama, "hareketi azalt" karşılıkları ve kısa önizleme videoları (MP4/GIF) hazırlar. Code'un zamanını almaz.
- **H1 — Temel (kapalı test paketi gittikten sonra, ~1 gün):** Motion belirteçleri, titreşim sarmalayıcısı, "hareketi azalt" altyapısı, sayfa geçişleri, Android predictive back, sekme çizgisi.
- **H2 — İmza anlar (~2 gün):** Varlık dalgası, merhaba el yazısı, bağlantı anı, fotoğraf kahramanı, mesaj yerleşmesi.
- **H3 — Cila (~1 gün):** Liste yerleşmesi, yükleme halkası, boş durumlar, hata şeridi, açılış imzası.

Her dilimin sonunda şunlar ölçülür:
- Düşük seviye Android'de kare süresi (jank %).
- "Hareketi azalt" açıkken her ekran (widget testi).
- Ekran okuyucu ve 48 px hedefler (mevcut ölçümler).
- Telefonda Founder turu.

## 8. Başarı ölçütü

- Founder'ın telefon turunda "bu uygulama güzel hissettiriyor" demesi.
- Kapalı testçilerin geri bildiriminde takılma veya "yavaş" şikâyeti olmaması.
- Hareketi azalt açıkken hiçbir işlevin kaybolmaması.
- Test sayısının artması, hiçbir mevcut testin zayıflamaması.

## Kaynaklar

- [Apple — 2026 Apple Design Awards kazananları](https://www.apple.com/newsroom/2026/06/apple-reveals-winners-of-the-2026-apple-design-awards/)
- [Apple Developer — Apple Design Awards](https://developer.apple.com/design/awards/)
- [Pixelmatters — 7 UI design trends to watch in 2026](https://www.pixelmatters.com/insights/7-UI-design-trends-to-watch-in-2026)
- [Wikipedia — Liquid Glass](https://en.wikipedia.org/wiki/Liquid_Glass)
- [Design Studio — 16 Mobile App UI/UX Design Trends 2026](https://www.designstudiouiux.com/blog/mobile-app-ui-ux-design-trends/)
