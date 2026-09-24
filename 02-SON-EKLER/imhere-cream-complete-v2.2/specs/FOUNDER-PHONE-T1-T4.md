TASARIMCIDAN MANAGERE MESAJ

# Founder telefon turu — T1–T4

Önceki 18d189c tesliminde bu dört bulgu yoktu; bu ek teslimde tamamlandı.

## T1 — Aktif check-in

`checkin-04-active`, nearby-empty/loading/failed/offline ve aynı aktif kontrolü kullanan notice-renewalFailed/stopPending/stopSuperseded güncellendi. Tek `checkInStatusActive` satırı (bitiş saatiyle) + mevcut Stop. Büyük checkInRenew düğmesi ve ikinci geri sayım satırı kaldırıldı. Pasif oturumdaki checkInStart korunur. Sunucu süresi, stop hata/uzlaşma akışı veya devam eden isteğin iptali değişmez; otomatik yenileme icat edilmez. Eski renewal CTA yerleşimi bu kararla geçersizdir.

## T2 — Niyet seçimi

Gönderme ve kabul akışındaki 12 durum: checkbox içinde kart yerine 1 px çizgili ince çipler. Normal ölçekte aynı satır, 8 birim aralık, 48 yükseklik, 14/500. Seçili çip siyah dolgu üstüne krem yazı; seçilmemiş krem + siyah çizgi. Sıfır/bir/iki seçim ve gönderim sırasında devre dışı olma korunur. %200 büyük metinde 28/500, 56 yükseklik ve iki satır; kesme, küçültme veya yatay kaydırma yok. Semantics checked ve disabled durumlarını okur.

## T3 — Sohbet üst eylemleri

Continue eylemi bulunan 10 sohbet durumunda sağ üstte iki 48×48 dokunma alanı, aralarında 8; çizgi 1.8, simge 24. Solda Safety (kalkan; Flutter `shield_outlined`), sağda Continue (`link`). Erişilebilir ad/tooltip mevcut `safetyTitle` ve `continueTitle`. Safety mevcut bağlantı güvenlik menüsüne, Continue mevcut özel karar ekranına gider; dokunmak karar kaydetmez. Mevcut erişim/backend koşulları korunur. Kapalı/karşılıklı tamamlanmış sohbetlerde olmayan Continue eklenmez. Composer + sayaç + Send klavye üstünde sabitlenme davranışı korunur. Çizimler klavye kapalı hâlidir.

## T4 — Paylaşılan iletişim

contact-shared, contact-more-partial/all/saved ve contact-update-success: her kendi paylaşılan alan başlığının sağında 24 birim kalem (`edit_outlined`), dokunma alanı48×48. Tam genişlikte contactEdit düğmesi kaldırıldı. Erişilebilir ad/tooltip mevcut contactEdit + ilgili alan adı. Başkasının paylaştığı alanlarda kalem yok. Geri çekme ve ek bilgi paylaşımı değişmez.

## Teslim ve kontrol

35 durum, 280 SVG ve70 PNG güncellendi; tümünde TR/EN · iOS/Android · %100/%200. Katalog toplam296 durum, beta289 + ertelenen7 değişmedi. Yeni metin veya ARB delta yok; mevcut anahtarlar erişilebilir ad olarak kullanılır. Eski arşivler ve uygulama kodu değiştirilmedi. Yerel commit; aktarım Code.
