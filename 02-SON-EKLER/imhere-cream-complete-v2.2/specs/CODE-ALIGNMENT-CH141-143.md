TASARIMCIDAN MANAGERE MESAJ

# Code farkları — CH-141 / CH-142 / CH-143

Dört fark kabul edilip güncel kataloğa işlendi. Son Founder kararları eski çizim akışlarının yerine geçer.

1. **report-sent:** mevcut `reportSent` + `blockDone` satırları ve `safetyBack` (Go back / Geri dön) düğmesi. Ayrı engelleme sorusu, Block ve Not now yok. Eski `report-block-busy/failed/done` durumları aktif katalogdan çıkarıldı; yerine `report-sent`. Engelleme sonucu yalnız onaylı rapor sonucu ile gösterilir. Yeni metin gerekmedi.
2. **Kapalı kart:** kilit + nötr satır listeden silinsin. Bu zaten e1c7aed'de `connections-after-end` ile teslim edildi; son bağlantı gittiyse mevcut boş liste. `connectionEndedNeutral` ARB anahtarı silinmez: başka sonuç ekranlarında kullanılabilir.
3. **Yeniden merhaba:** sona ermiş bağlantı tek başına pasif sebebi değildir. `view-other-visible/hidden` etkin `requestSend` ile bu durumu da kapsar; yeni istek yine niyet seçimiyle başlar. `person-connected-*` yalnız AÇIK bağlantıdır. Engelleme/rapor kapısı, gerçekten bekleyen istek, cooldown veya erişim yokluğu aşılmaz; yeniden bağlantı otomatik değildir.
4. **Profil Safety:** alt ikincil düğme yerleşimi kabul. Önceki sağ üst bayrak kaldırıldı. Mevcut `safetyTitle` → yeni `safety-profile-menu`; Şikâyet + Engelle + Go back. Buradan End connection yok. Backend eylemleri sağlanmıyorsa giriş görünmez.

## Aynı teslimde beklenenler

- **End connection onayı hazır:** `screens/svg/end-confirm--*.svg`; başlık/body, End connection ana, Report instead ikincil, Cancel. Metin ve davranış: `specs/END-CONNECTION-2026-09-24.md`.
- **6. kategori hazır:** `reportChildSafety` — EN “Underage user or child safety”; TR “Reşit olmayan kullanıcı veya çocuk güvenliği”. Safety concern altında, Other üstünde.
- **Tek birleşik delta:** `l10n/code-alignment-patch_en.arb` ve `_tr.arb`. Önceki onaylı kategori + onay penceresi metinlerini bir araya getirir. Tam ARB üzerine yazılmaz; daha önce ayrı deltalar uygulandıysa aynı değerlerdir.
- Report instead tek başına end komutu göndermez; fakat son CH-141 kararı nedeniyle şikâyet başarıyla gönderilirse raporun engelleme etkisi uygulanır. Bu, eski “şikâyet sonrası ayrıca engelle” ifadesini geçersiz kılar.

Bu teslimde80 SVG /20 PNG üretildi (profil64, report-sent8, profil güvenlik menüsü8); eski rapor sonrası üç durumun24 SVG /6 PNG'si aktif paket içinden çıkarıldı. Güncel296 durum /2368 SVG /592 PNG. Eski sürüm arşivleri değiştirilmedi.

Katalog, motion durum eşleştirmesi, migration, CHANGELOG ve MANIFEST güncellendi. Native uygulama bu teslimde değiştirilmedi. Yerel commit; aktarım Code.
