KİME: MANAGER
KONU: B-symbol seçimi + A4 devam teslimi v1.0

Konum: 02-SON-EKLER/imhere-a4-suite-v1.0/

- B seçimi kayda geçirildi; A arşiv, uygulanmayacak. Önceki simge tesliminde README/spec/SELECTION güncellendi, görseller değişmedi.
- notification/: B işaretinden doğrudan türetilmiş resmî tek renk şeffaf küçük simge. SVG, Android XML ve PNG yoğunlukları. Code'un görseli görülmediği için onun türetmesine onay verilmedi; bu resmî dosya alternatifidir.
- splash/: B ile uyumlu düz koyu zeminli, merkez işaretli yerel açılış tasarımı. Varlıklar ve iOS/Android yerleşim çizimleri; ek yazı/eylem/bekleme süresi yok.
- map/: EN/TR MapLibre v8 koyu OpenFreeMap alt harita JSON'ları. Mevcut renk katmanı ve iş kuralları korunur. Attribution zorunlu; ek kaynak kredisi korunur.
- KARAR-KAPANISLARI.md: Dil/L-93, iç panel ve bildirim görünümü sorularının önceki yanıtları bir araya getirildi.

Kanıt: tarayıcıda gerçek OpenFreeMap döşemeleriyle EN/TR çizim başarılı. Splash/simge varlıkları ve önizlemeler kontrol edildi. Native entegrasyon, cihaz/simülatör kanıtı henüz tasarımcı tarafından görülmedi. Uygulama kodu değiştirilmedi. Bir sonraki karşılaştırma Founder üzerinden iletilecek görüntülerle yapılır.

Dosyalar tek tek depoya yüklendi; CHANGELOG'a satır eklendi. Birleştirme: splash ve küçük simge kendi platform varlıklarına, map JSON mevcut adapter'ın style girişine bağlanır; tam eski paket üzerine kör kopyalama yapılmaz.
