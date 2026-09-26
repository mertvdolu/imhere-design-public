# BEACON GECE02 — Tasarımcı incelemesi v1.0

Tarih: 2026-09-26. Kaynak: Founder’ın ilettiği IM_HERE_GECE02_teslim.zip; G02-1 ve G02-4 §4. Karşılaştırma: yerel tasarım deposu, 3165944 tabanı.

## Sonuç

Renkler, temel tipografi ve ölçüler devralınabilir. Taslak mevcut hâliyle skill kaynağı yapılmamalı: kaynaksız logo ölçüleri ve pazarlama gözlemleri kesin ürün/tasarım kuralına dönüşmüş. Yanındaki `TASARIM-SISTEMI-DUZELTILMIS.md` bunları ayıran kaynak özetidir. Yeni ürün kararı, kurulu skill, uygulama değişikliği veya canlı site denetimi değildir.

## Bölüm bölüm işaretler

| Taslak bölümü | İşaret | Düzeltme / dayanak |
|---|---|---|
| Kaynaklar | EKSİK | Genel devrin üzerine gelen tarihli spesifikasyon ve ARB deltaları da okunmalı. Eski paketler güncel kural değildir. |
| §1 renkler | DOĞRU + EKSİK | Token değerleri doğru. Niyet yüzey token’ı seçili çipin tek görünümü değildir: T2 ince çipler, seçili Ink/açık metin. Mobil palet kuralları ayrı web projesine kendiliğinden yayılmaz. |
| §2 tipografi | DOĞRU + KAPSAM | 18/500,16/500,14/400 güncel token’lardır. `orbLabel` adı eski küreyi geri getirmez. Yerel font kuralının kaynağı mobil pakettir; tüm web projeleri hakkında denetim sonucu çıkarılmaz. |
| §3 logo | DÜZELT | 48 px ağırlık eşiği, yarıçap kadar koruma alanı, 24 px minimum güncel brand/README’de tanımlı değil; zorunlu kuraldan çıkar. Geri çekilmiş BEACON kılavuzunu veya bayt eşitliğini otorite yapma. Yeni kelime-logo çizme. Orijinal geometri ve verilen varlıklar kullanılır. |
| §3 splash / §6 hareket | AYIR | Native splash statik; H0’daki ilk Flutter karesi ayrı, 800 ms logo sahnesi. Uygulamanın hazır rotasını bekletme. |
| §4 yerleşim | EKSİK | %200 metinde 2×2 navigasyon; alt sayfalarda 48 hedefli geri, ilk kurulumda Çıkış yap istisnası. T1 geri alındı: aktif oturumda I’m still here + Stop korunur. T2–T4 ve H2/H7/H9/H3 eksik. |
| §5 harita | DOĞRU + NETLEŞTİR | Tam ekran, dört renk, kişisel işaret/sayı/mesafe yok; görünür attribution. Zoom bandın anlamını değiştirmez. Örnek harita canlı veri olarak sunulmaz. |
| §6 hareket | EKSİK | reduced token açıkça eklenmeli. 06 tek karşı taraf portresi; kendi fotoğrafı gerektirmez. Dalga yalnız haritada, Hello sent bekleyen ekranın üstünde bir kez; iOS rota geçişi sistemin. Yay tepki süresi ile yerleşme referansı aynı şey değildir. |
| §6 veri ve haptik | DÜZELT | “Başarı izlenimi vermez” yerine “başarı yalnız gerçek onaydan sonra gösterilir”. Her başarıda koşulsuz titreşim çıkarma; imza anın kendi tetik/haptik tablosu ve sistem tercihi geçerlidir. |
| §7 ton | DÜZELT | “Her zaman kesin sayı”, “her zaman 999”, “kendini ne olmadığıyla tanımla” evrensel tasarım kuralları değil. Sayılar yalnız ilgili sözleşmede; harita/cooldown kısıtları korunur. Acil numara hedef ülkenin onaylı içeriğine bağlıdır. |
| §7 dil | KAPSAM | İngiliz İngilizcesi bu mağaza metninin yereli olabilir; kabul edilmiş bütün EN ARB’lerini yeniden yazma talimatı değildir. EN aktif, TR teslimlerde korunur; Dil satırı şimdilik gizli. |
| §7 kelime yasakları | DÜZELT | Dayanaksız güvence ve romantik konumlandırma üretme. “match” gibi sözcüklerden mevcut dahili ID’leri değiştirme sonucu çıkmaz; Safety meşru ekran terimidir. |
| §8 yasaklar | AYIR | Harita gizliliği, uydurma referanslardan kaçınma, örnek içerik etiketi korunur. Stok fotoğraf/rakip adı/tüm dış betikler/tek yayın cümlesi gibi kapsamı belirsiz yasakları bu tasarım özetinden türetme. FD-84 gibi politika referansını ilgili onaylı belgeden doğrula; bu inceleme izin genişletmez. |
| §9 web | KAPSAM DIŞI | BEACON’un tarihli gözlemi; bu incelemede canlı CSS/font/istekler doğrulanmadı. Mobil skill’e ikinci tema ekleme. Plainly yeni ortak bileşen olarak onaylanmış değil. |
| §10 Ç-1 | KALDIR | Geri çekilmiş kılavuz nedeniyle Inter/Geist kelime-logo yeniden çizim işi açılmaz. Tek logo referansı brand/README. |
| §10 Ç-2/3/4 | AYRI İŞ | Web dönüşümü, hukuki marka yazımı ve web font barındırması otomatik tasarım değişikliği değildir. İlgili sahiplerin kapsamı; kaynaklar görülmeden uygunluk kararı yok. |

## G02-4 §4 — mağaza metni kararı

| Konum | Kullanılacak metin | Gerekçe |
|---|---|---|
| 02 başlık | People nearby. | Yakındakiler terimi; mesafe sıralaması veya aynı mekânda bulunma garantisi vermez. “People in the same place.” seçilmedi. |
| 02 alt yazı | Friendship or networking. Say hello. | Ortak ilgiye göre keşif/sıralama iddiasını kaldırır. |
| 05 alt yazı | Twenty messages each. Keep it simple. | Kişi başına 20 hak sözleşmesine dayanır. |
| 06 alt yazı | A profile that introduces you. | Fotoğraf/ilgi alanlarında ayrıca gizleme tercihi varmış izlenimini kaldırır. |
| Öne çıkan başlık | Friendship and networking. | “Common interests” üzerinden eşleştirme vaadi kurmaz. |
| Öne çıkan alt yazı | Start with a hello. | Kısa, mevcut eylemle uyumlu. |

01,03,04 başlıkları ve diğer alt yazılar korunur. 07/08 yeni kare önerileri bu incelemeyle iş kapsamına eklenmedi.

“Emoji/link hiçbir belgede yok” doğru değil: TASARIM-DEVRI §6 bunları açıkça içerir. Hukuki metinde sayılmaması tek başına uygulamada bulunmadıklarını kanıtlamaz. Code’un gerçek davranış teyidi ayrı; hukuki uygunluk onayı vermiyoruz. G02-4’ün platform politika yorumları bu incelemenin kapsamında doğrulanmadı.

**Teslim sınırı:** Bunlar sonraki mağaza dışa aktarımında kullanılacak metin kararlarıdır. Bu commit mağaza kaynak JSON’unu veya SVG/PNG’leri değiştirmez; mevcut mağaza görsellerinde eski metinler durur. Yeniden dışa aktarım ve native ekran karşılaştırması yapılmadan yeni metinler görsellere uygulanmış sayılmaz.

## Aktarım

Düzeltilmiş özeti skill’e dönüştürürken repo yollarını çalışılan checkout köküne göre çöz. Tarihli kararları kaynak olarak tut; güncel dosya ile çelişen gömülü bilgiyi sessizce uygulama. Ürün davranışı değişecekse Founder’a taşı. Bu dosyalar yalnız yerel commit olarak teslim edilir; aktarım Code tarafından yapılır.
