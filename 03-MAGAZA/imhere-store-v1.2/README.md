# IM HERE — native mağaza kareleri v1.2 (kısmi teslim)

Kaynak: IM_HERE_MAGAZA_NATIVE_teslim.zip, 2026-09-27; iPhone18 Pro Simülatörü ve gerçek A13 test telefonu. Ürün/cihaz bilgisi Code’un BENIOKU’sundadır; `source/native/BENIOKU.md` kopyası korunur. Veriler yerel kurmaca sahnedir.

## Hazır

- app-store/iphone-6.9/:01–05,1320×2868.
- app-store/iphone-6.5/:01–05,1242×2688.
- google-play/phone/:01,04,05,1080×1920.
- Toplam13 SVG +13 PNG. İki toplu önizleme review/ altında; boş alanlar eksik kare demektir, mağazaya yüklenecek görsel değildir.

Maya sentetik portresi yalnız gerçek fotoğraf yuvasına eklendi. Native görüntü tümüyle, oran korunarak ölçeklenir; kesilmez, esnetilmez, metin/ikon yeniden çizilmez. Kaynak görüntüdeki saat/batarya/sistem çubuğu korunur. “Fictional profiles · Illustrative content” etiketi her kişi karesinde; haritada “Illustrative map · Not live data”, native OpenStreetMap/OpenFreeMap atfı ve dış çerçevede OpenMapTiles kredisi korunur. Fotoğraf bindirmesi nedeniyle nihai kare ham screenshot değil, açıkça etiketlenmiş kompozisyondur.

## Bekleyenler — yayın için set tamamlanmadı

1. Android02 Nearby ve03 harita: sanal cihaz çekimi gelecek.
2. 06 kendi profil: fotoğraf yuvası olmayan çekim kullanılmadı. Founder, Alex fotoğraflı native çekimi beklemeyi seçti. iOS/Android kaynakları gelince3 çıktı üretilecek.
3. Dil başlığı düzeltilmiş ek Maya profili gerekiyorsa Code yeniden çeker; mevcut ek görüntü kullanılmadı.

Bu klasörde eksik dosyalar yerine eski çizim yok. Önceki imhere-store-v1.0 tarihsel pakettir; onun eski telefon içlerini yeni native setle karıştırmayın. Öne çıkan1024×500 illüstratif kompozisyon ve512 Play simgesi mevcut v1.0 paketinde korunur; v1.2 tam bağımsız mağaza yükleme paketi değildir. Son tam teslimde bir araya getirilecek.

## Üretim ve kanıt

source/build.py native görüntü + portrait-placements.json + mevcut sentetik varlıkları SVG olarak birleştirir. source/render.cjs Sharp ile opakRGB PNG üretir. Pillow ve Sharp mevcut çalışma araçlarıdır, uygulamaya bağımlılık eklenmez.

DELIVERY.json her çıktı için native kaynak yolu/SHA256, boyut, portre dikdörtgeni ve bekleyenleri listeler. source/native/ içindeki17 PNG teslimle bayt eşitliğinde korunur. evidence/export-validation.json boyut/renk çıktıları; evidence/native-validation.json kaynak/kapsam doğrulaması. Önizlemeler görsel kontrolden geçirildi. Gerçek native çekimlerin kaynağı Code; bu teslim yeni bir cihaz test turu değildir.

Sayaç onayı ve dil deltası: 02-SON-EKLER/imhere-cream-complete-v2.2/specs/NATIVE-STORE-COUNTER-LANGUAGES-2026-09-27.md (depo köküne göre).

Yerel commit; aktarım Code.
