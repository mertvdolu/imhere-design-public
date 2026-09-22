# 04 — Platform, büyük metin ve hareket
## Ortak
- %100 ve %200 varyantları tüm 34 görünüm için iki dilde/iki platformda var. Sabit yükseklikli metin alanı, ellipsis veya textScale kapatma yok. 320 logical px ve gerçek cihazın maksimum erişilebilirlik ölçeği ayrıca entegrasyonda sınanır.
- Standart hedef en az48; CTA min52. Metin arttıkça hedef büyür. Normalde 4 sütun olan navigasyon büyük metinde 2×2’ye geçer; sıra sabit. SafeArea ve sistem barları runtime’dan gelir.
- Renk tek işaret değildir: durum metni, bilgi/hata ikonu, seçili sekme Semantics bilgisi var. Ekran okuyucu metinleri ARB’den; dekoratif orb/halkalar/ikonlar/fotoğrafın tekrarlı açıklaması dışlanır. Profil kartı tek odak ve anlamlı ad/eylem içerir.
- Dialog açılmayan bildirimler odağı çalmaz. Durum değişikliği bir kez nazik anons edilir; saniyelik sayaç her saniye okunmaz. Kaydırılan ekran dönüşünde odak önceki giriş eylemine döner.
- PARTIAL ve no-region örnekleri dahil uzun TR/EN metinler otomatik sarılır. Emoji fallback sistemden; yeni emoji/ikon font paketi zorunluluğu yok.

## iOS
VoiceOver, Dynamic Type/textScaler, SafeArea ve yerel geri jesti korunur. Konum izni sistem diyaloğu kopyalanmaz; uygulama içi gerekçe + ilgili yerel ayar eylemi. Alt home indicator’ın üstü boş kalır. Sistem ayarından dönüş otomatik check-in başlatmaz.

## Android
TalkBack, sistem font ölçeği, geri hareketi/geri tuşu ve edge-to-edge insets. İzin reddi ile kalıcı ret mevcut controller sınıflamasından; geliştirici platform ayrımını korur. Sistem navigation gesture alanı alt barla çakışmaz.

## Hareket
v1.3 token’ları: giriş250ms, basma180ms, dekoratif orb nefesi5000ms. Geçişler opacity/çok küçük yer değişimi; kişi keşfi/radar veya canlı konum iması yok. Başarı check’i yalnız sunucu onayından sonra. Reduce Motion’da dekoratif nefes ve yer değiştirme kapalı; yükleme metni kalır, gerekiyorsa statik yükleme ikonu. Animasyon süreç süresini/başarıyı belirlemez. SVG/PNG teslimleri statiktir; hareket burada spesifike edilir.

## Kontrast
S-1 ölçümü `evidence/contrast.json`: eski sınır #506D46 → yeni #637D5A. Opak dolgu #1C3221 üzerinde ≥3:1; yüzey #17251D üzerinde ≥3:1. Focus/disabled/error durumları temanın mevcut ayrımlarıyla; aktif sınırın opaklığı düşürülmemeli. Dekoratif kart sınırına bu düzeltme yayılmadı.

## Cihaz kabul kontrolü (henüz yapılmadı)
TR/EN × iOS/Android × normal/büyük: odak sırası; tüm butonlara kaydırarak erişim; nav sıra/seçili durum; klavye/sistem bar örtüşmesi; uzun isim/emoji; permissionForever dönüşü; offline stop; belirsiz sonuç; eski sürenin yenileme sırasında bitmesi; harita attribution/jest ve 0–1 gizliliği; Reduce Motion. Gerçek simülatör/cihaz erişilebilirlik sonucu bu paketin kanıtı değildir.
