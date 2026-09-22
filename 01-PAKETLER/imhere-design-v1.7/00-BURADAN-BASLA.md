# I'M HERE — v1.7 / Paket 3
**İstek/eşleşme · sohbet · özel devam kararı · iletişim paylaşımı.** Kabul edilmiş v1.6.1 üzerine yeni ekran paketi; önceki giriş/profil paketlerinin yerine geçmez.

## Önce incele
1. `ONIZLEME.html`: Çevrimdışı önizleme. Önce ana akış, ardından tüm durumlar veya bölüm seçilebilir. TR/EN, iOS/Android, normal/%200 metin filtresi vardır. Ekranlar statik tasarım çizimleridir; uygulama işlemi başlatmaz.
2. `review/GENEL-BAKIS.png`: Akışın temel ekranları. `specs/00-AKIS-HARITASI.md`: Ekranlar ve geçişler.
3. `specs/01-ISTEK-ESLESME.md`, `02-SOHBET.md`, `03-DEVAM.md`, `04-CONTACT.md`: Yerleşimler ve kilitli davranışların UI karşılığı.
4. `l10n/v1.7-additions_tr.arb`, `v1.7-additions_en.arb` + `migration.json`: Yazılıma birleştirilecek metinler. **Canlı ARB'lerin üzerine yazılmaz.**
5. `DOGRULAMA.md`, `specs/05-DURUMLAR-PLATFORM.md`, `specs/06-BIRLESTIRME.md`: Durum kapsamı, entegrasyon notları ve kontrol sınırları.

## Teslim kapsamı
**93 durum × 2 dil × 2 platform × 2 metin ölçeği = 744 SVG.** Her durum için TR iOS normal ve EN Android büyük metin olmak üzere 186 PNG. SVG'lerde fontlar ve kullanılan portreler gömülüdür; internet gerekmez. Artboard'lar tam kaydırma içeriğidir; referans cihaz alanı manifestte ayrıca belirtilir.

66 yeni UI metni iki dilde eklendi; tam referans sözlükler 400'şer anahtar. v1.6.1'in 334 metni ve metadata'sı değişmedi. Auth anahtarları ve alias'ları aynen korundu. Onaylı orman/nane renkleri, Geist, token'lar ve kabul eki aynı. Yeni global token veya ürün kuralı yok.

## Kritik kabul noktaları
- Mesajlar = Bağlantılar + İstekler. İstekler içinde gelen/giden bölümleri var; beşinci alt sekme yok. Uygulama açılışı Yakındakiler olarak kalır.
- Niyet yalnız Arkadaşlık/Networking; ilk seçimler boş. Alıcı, kabul öncesinde gönderenin niyetini göremez. “Tanışmak isterim” seçim ekranını açar; “Seç ve Kabul Et” seçili kendi niyetlerini gönderir.
- Bekleyen ayrıntısı 19/20 ve kalan istek süresini gösterir. Bu bir kredi veya günlük kota değildir. Kesişimi olmayan eşleşme sohbeti engellemez.
- Yalnız kendi 20 mesaj hakkı ve 500 karakter sınırı; metin/emoji/link. Medya, gönderilmiş mesajı düzenleme/silme yok. İletişim bilgisi uyarısı yumuşaktır; Yine de gönder bulunur.
- Devam kararı özeldir; karşı karar, rozeti veya bekleme baskısı yok. EVET karşılıklı olana kadar geri alınır. HAYIR finaldir; nötr sona erme görünür. EVET+EVET → salt okunur sohbet ve ayrı contact formu.
- Contact Telefon/Instagram/E-posta/Diğer; bir, çok veya hiç paylaşma. Yazmak paylaşmak değildir. Hesap e-postası otomatik dolmaz. Düzenleme/geri çekme yalnız ayrı contact kayıtlarına aittir. Önceden görülmüş/kaydedilmiş bilgiler geri alınamaz.

## Kaynak ve teslim sınırı
Güncel Tasarım Gereksinim Özeti v1.0.2 §7–8 ve Founder'ın son mesajı esas alındı. Referans kopyası pakettedir. Eski mühendislik envanterindeki üçüncü niyet FD-75 ile geçersizdir; yeni ekranlara taşınmadı. Master belge okunmadı. Yazılımcıya doğrudan mesaj gönderilmedi.

Uygulama/Flutter/backend kodu değiştirilmedi. Görsellerdeki kişi, mesaj, kod, sayı ve iletişim adresleri tasarım örneğidir; üretim verisi değildir. Örnek linkler yalnız metindir. Doğrulanmış sunucu sonucu olmadan gönderildi/kabul edildi/paylaşıldı başarısı gösterilmez. Ürün cihaz testleri M10 yazılım doğrulamasıdır.

Paket 4'ün tam güvenlik/Ayarlar/bildirim/Etkinlikler ekranları bu teslimin kapsamı değildir. Engellemenin mevcut tüm yüzeyleri gizleme üstünlüğü ve önceki endConfirm kabulü burada korunur. Kapalı sohbetin saklama süresi hâlâ M11 kararıdır; süre vaadi eklenmedi.
