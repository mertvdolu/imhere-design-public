# 05 — S-1…S-5 kapatma ve metin birleştirme
## S-1
Onaylanan temizlik kapsamında yalnız inputBorder değişti. Mevcut M05 ThemeData üretimi bu token değişikliğiyle güncellenmeli; tema/ortak bileşen dosyaları bu teslimde yeniden yazılmadı. Görsel karşılaştırma component-input, ölçüm contrast.json.

## S-2
navMap kaldırıldı. mapOpen “Bölge hareketliliği / Area activity” yalnız harita giriş eylemi; mapTitle başlık. navProfile/navMessages/navNearby/navEvents dört sekme. Eski navMap çağrısının rolünü kontrol et; başlıksa mapTitle, girişse mapOpen; hiçbir çağrı beşinci sekme oluşturmamalı.

## S-3
chatClosedReadOnly kanonik: “Bu sohbet şu anda salt okunur.” Süre/kapanma nedeni sözü yok. chatReadOnly çağrıları buraya. Mutual bağlamı ayrıca mutualTitle ile açıklanabilir; gizli karar ifşası yok. Block görünmezliği her zaman önde, salt-okunur ekran gerekçesiyle bloklu sohbet geri gösterilmez.
chatSoftTitle/chatSoftBody kanonik; chatSoftContactTitle/Body kaldırılır. Review/Send Anyway ayrı korunur.

## S-4
requestAccept → bağımsız niyet seçimi → requestSelectAccept. İlk buton backend kabulü yapmaz. FD-75 yalnız Arkadaşlık/Networking; boş başlangıç, min1/max2. Diğer tarafa kabul öncesi niyet gösterilmez. Asıl ekran tasarımı paket3’te.

## S-5
Eski envanter tahmini ~94, okunan mevcut uygulamada kesin **83** eksik anahtar. `missing-app-keys-audit.json` her anahtarı ekleme veya alias olarak izler. Bütün yeni/değişen metinler iki dilde `copy-diff.json` içinde.
- 26 hazır ilgi alanı + Diğer; yeni kategori yok.
- Genel alan/hata metinlerinde Türkçe karakterler, noktalama, marka apostrofu düzeltildi.
- Meslek/yaş/cinsiyet görünürlük metinleri hazır; varsayılanlar iletilen Founder kararıyla sözleşmede. Profil layout’u paket2.
- Teknik “sunucuda çıkarılır” ifadesi kullanıcıya “Gizlediğin alanlar diğer kişilerin profil görünümünde yer almaz” olarak yazıldı; veri davranışı değişmedi.
- errorAgeIneligible → genel profileBirthDateError; sebep/sınır açıklayan hata gösterilmez. dobHelp başlangıç açıklamasında 18+ kuralı açık kalır.

## Birleştirme güvenliği
Bu ARB’ler teslimin kanonik sözlüğüdür; canlı uygulama dosyasını körlemesine üzerine yazma. Önce mevcut ARB ve çağrıları envanterle. migration.json alias’larını, parametre isim/tiplerini ve iki locale’i birlikte güncelle. numbers: mevcut sözleşme sabitleri {min}/{max}/{limit} gibi parametrelerle geliyorsa koru; tasarımın örnek /20, 1–5, 30 değerleri yeni sabit kaynak değildir. charactersLeft.count ile profileCharactersRemaining.remaining aynı anlamı taşıdığı doğrulanmadan otomatik isim değişimi yapma. Üretilmiş localization dosyalarını elle düzenleme.

## Sonraki paketlere kayıt
Ayarlar içerik onayı paket4'e; davetsiz davet edinme metni paket2'ye; kapalı sohbet saklama süresi M11'e ait. Özetin End Connection “onay istemez” ifadesi ile eski endConfirm anahtarı paket4'te birlikte ele alınmalı; bu paket eski anahtarın varlığından akış kararı üretmez. Bu konular paket1'i engellemez.

## Kabul sonrası düzeltme
End Connection açık noktası kapanmıştır: karşı tarafın onayı aranmaz; kullanıcının kendi onay diyaloğu ve endConfirm korunur. Önceki açık nokta kaydı tarihsel olarak okunmalıdır.
