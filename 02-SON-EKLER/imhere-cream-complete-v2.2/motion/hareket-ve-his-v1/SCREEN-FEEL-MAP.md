# §6 — Netleştirilmiş ekran his haritası

Güncel normatif durum eşleştirmesi: `screen-motion-map.json` (297 durum). Aşağıdaki aile deseni açıklayıcıdır; JSON duruma özel referansları belirler.

| Ekran | Referans | Normal | Hareketi azalt | Katalog kapsamı |
|---|---|---|---|---|
|Kayıt / davet|form-focus-error|Odak150ms; yalnız başarısız gönderim denemesinde x=0,+2,−2,+2,−2,0 @0/40/80/120/160/200ms. Yeni hatada tek mediumImpact.|Sallanma yok;150ms opaklık.|register-* / login-* / invite-* / reset-*|
|Profil düzenleme|photo-progress|Gerçek bytes/total; total bilinmiyorsa yüzde yok. İşleniyor yalnız gerçek işleme süresince1200ms döngü; başarı onayından sonra scale.98→1 standard.|Statik işleniyor metni; ölçülen ilerlemeye doğrudan güncelleme.|form-* / photo-* / visibility-*|
|Doğum tarihi|native-date-picker|iOS çark / Android takvim sistem hareketi; ayrı animasyon katmanı yok.|OS erişilebilirlik ayarı.|form-* DOB alanı|
|Kendi profilim|own-profile-edit / profile-save-return|Kalem→form150ms opacity; doğrulanmış kayıttan sonra form pop, kendi profil150ms opacity.|Aynı150ms; Hero yok.|view-own-* / form-edit / form-saving|
|Tam ekran harita|02-presence-boundary|İki dalga viewport kenarından, kişisel nokta yok. Açılış150ms opacity; harita dört semantik rengi ve attribution korunur.|Statik kenar; döngü/halkalar yok.|map-* / checkin-*|
|Sekmeler|tab-indicator|Gerçek merkezler arasında standard; seçimde tek selectionClick. Büyük metin2×2 gerçek sınırları izler.|150ms çapraz opaklık.|Dört sekmenin kökleri|
|Bağlantılar|03-paper-list / ended-card-removal|Yeni gerçek ID girişleri40ms; doğrulanmış bitişte satır150ms silikleşir ve yuva150ms daralır. Etkileşim/semantics onayda kaldırılır.|150ms opacity; yuva animasyonsuz yeniden yerleşir.|messages-connections-* / connections-after-end|
|Sohbet|07-paper-message / keyboard-follow|Yalnız onaylanan mesaj; gelen yalnız yeni yetkili ID. Send içte48×48. Okundu yalnız sistem gerçekten destekliyorsa.|150ms opacity; ek klavye tween yok.|chat-* / continue-*|
|Güvenlik / şikâyet|safety-minimal|150ms opacity; doğrulanmış sonuçta sakin onay. Başarılı rapor+block güncel akışı.|Aynı150ms, gösteri yok.|safety-* / report-* / block-* / unblock-*|
|Boş durumlar|empty-breathe|Mevcut tek dekoratif öğe .55–.70 opacity /4000ms; insan/aktivite/konum ima etmez. chat-empty hariç.|Statik .65; döngü yok.|screen-motion-map.json içindeki empty-breathe eşleşmeleri|
|Hata / offline|error-strip|Mevcut durum alanı −4→0px /150ms + opacity. Retry erişilebilir; yeni veri gelmeden mesajı kaldırma.|Yalnız150ms opacity.|*-failed / *-offline / startup-*|
|Ayarlar / Contact us|settings-contact-minimal|Standart rota; adres+kopyala davranışı, kopyalandı yalnız clipboard başarısından sonra.|150ms opacity.|settings-* / support-* / contact-*|
|Hesap silme|deletion-minimal|150ms sakin durum geçişi; istek alındı/tamamlandı ayrımı korunur, kutlama/titreşim yok.|Aynı150ms.|delete-*|
