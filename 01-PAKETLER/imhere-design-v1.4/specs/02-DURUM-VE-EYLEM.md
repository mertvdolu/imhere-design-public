# 02 — Check-in ve liste durum eşlemesi
Davranışın kaynağı mevcut controller ve v1.3 sözleşmesidir. Çizimler yeni domain enum’u/geri sayım/otomatik işlem tanımlamaz. `contracts/checkin-view-map.json`, `checkin-notices.json`, `test-keys.json` v1.3’ten byte düzeyinde korunmuştur.

| Görünüm | Durum | Kalan süre | Gerçek eylemler |
|---|---|---|---|
| 1 | INACTIVE | Yok | btn-checkin; backend yoksa pasif |
| 2 | ACQUIRING | Yok | btn-cancel |
| 3 | VERIFYING_SERVER | Yok | Yok |
| 3b | RESULT_UNKNOWN | Yok | btn-reconcile, aynı denemeyi sorgular |
| 4 | ACTIVE | Onaylı bitişten | btn-renew, btn-stop |
| 5 | RENEWAL_ACQUIRING | Önceki bitişten | btn-cancel yalnız aramada; btn-stop |
| 6 | STOPPED | Yok | btn-checkin; yenileme doğrulanıyorsa gizli |
| 7 | EXPIRED | Yok | btn-checkin; yenileme doğrulanıyorsa gizli |
| Ayrı ekran yok | REPLACED | Yeni ACTIVE'ten | Yeni oturum eylemleri |

## 12 uyarı
`notice-*` çizimleri her uyarının örnek kompozisyonudur; bağımsız domain ekranı değildir. Uygulama notice’ı gerçek durumla birleştirir, çizimin örnek domain’ini backend sonucu gibi kullanmaz.
- noFix: konum doğrulanamadı / zaman aşımı için mevcut controller sınıflaması; key korunur, yeni timeout enum’u/süre göstergesi icat edilmez. İzin/servis hatasına dönüştürülmez.
- permission: yeniden istenebilir izin; kullanıcı check-in eylemiyle tekrar dener. permissionForever: uygulama ayarları. servicesOff: cihaz konum ayarları. Bu üç hâl birbirine karıştırılmaz; diğer sekmeler ve harita açık.
- precise: hassasiyet açıklaması; metre/koordinat yok. Ayar yolu platform davranışına bağlı; yeni yetki veya otomatik konum işlemi yok.
- renewalFailed: ACTIVE ve önceki bitiş sürer; eski süre eklenmez. oldExpiredVerifying: EXPIRED + uyarı, kalan süre ve yeni check-in butonu yok; yeni onaya kadar başarı görünümü yok.
- verifying: RESULT_UNKNOWN; reconcile yeni deneme başlatmaz. network ve server: ana durum eylemleriyle; istemci sonuç uydurmaz.
- stopPending: ACTIVE + eski süre; offline olmaya dayanarak “görünmezsin/durduruldu” denmez. Mevcut controller’ın yeniden denemesi korunur.
- stopSuperseded: yeni oturum ACTIVE; eski durdurma onu kapatmaz.

## Süre ve yaşam döngüsü
Sunucu saatinden mevcut sona erişim; pozitif dakikalar yukarı yuvarlanır. Her saniye görsel güncelleme mevcut davranış, her saniye sesli anons yok. Yaklaşık 10 sn arama bir animasyon süresi veya zorunlu minimum bekleme değildir; bitiş controller’dan. 25. dk hatırlatma/30 dk sınır değiştirilmez. Ön plana dönünce otomatik yeni konum/yenileme yok. Cache, başarı veya güncel kişi varlığı kanıtı değildir.

## Kişi listesi bağımsız durumları
`nearby-loading/empty/offline/failed`: check-in ACTIVE örneği üzerinde çizilmiştir; kişinin varlığını sürekli doğrulamaz. Ağ hatası tek başına ACTIVE’i iptal etmez. Sunucu uygunluğunu doğrulayamayan eski profilleri güncelmiş gibi sunma; uygulamanın veri geçerliliği sözleşmesi üstün gelir. Tasarım TTL/refresh/retry politikası eklemez. Liste hatası ile check-in notice aynı olay olarak birleştirilmez.

## Key / Semantics
Test Key gerçek Text/Button widget’ında kalır; dekoratif wrapper’a taşınmaz. Orb’un tek tıklanabilir hedefi vardır. Uyarının referans verdiği aksiyon mevcut butonsa ikinci kopya açılmaz. status her zaman, remaining yalnız izin verilen aktif hâllerde, notice yalnız varsa. dev-banner üretimde yok.
