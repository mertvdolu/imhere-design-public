# I'M HERE — TASARIM GEREKSİNİM ÖZETİ v1.0.2 (Designer için)

**v1.0.2 düzeltmesi:** §2 kimlik doğrulama yöntemi netleştirildi: e-posta + parola (ENG-09-02) + doğrulama e-postası; giriş, parola sıfırlama ve çıkış ekranları eklendi. v1.0.1 metni "yalnız e-posta" ifadesiyle parolasız akış gibi okunabiliyordu; Manager hatası.

**v1.0.1 düzeltmesi:** §1 sekme sırası Master 6.2'ye göre düzeltildi (Profil · Mesajlar · Yakındakiler · Etkinlikler). v1.0'daki sıra Manager hatasıydı.
**Tarih:** 2026-09-15 · **Hazırlayan:** Project Manager · **Kaynak:** Master Document Rev.9-B + FD-75 · **Statü:** Özet; kaynak değil. Çelişkide Master Document geçerlidir; soru Founder üzerinden Manager'a gelir.
**Amaç:** Designer'ın v1.3 üzerine M10 ekranlarını kurallara uygun tasarlaması. Ürün davranışı burada değiştirilemez; öneri "DESIGN RECOMMENDATION — FOUNDER APPROVAL REQUIRED" etiketiyle yazılır.
**Etiketler:** LOCKED = değişmez · NOT LOCKED = metin/yerleşim serbest, davranış sabit · TBD = Founder kararı bekliyor.

---

## 1. Navigasyon ve genel (LOCKED)
- **Dört sekme, bu sırayla:** Profil · Mesajlar · Yakındakiler · Etkinlikler (Master 6.2; v1.3/O-01 ile aynı). Harita ayrı sekme değil; Yakındakiler içinde.
- Yakındakiler başlangıç sekmesi; check-in + kişi listesi + heatmap aynı sekmede. Ayarlar Profil altında. Mesajlar = Bağlantılar + İstekler.
- Ürün ekranında teknik log/dashboard yok. Tek profil; kalıcı mod (dating/networking) yok; oyunlaştırma yok.
- Tüm ekranlarda loading / empty / offline / permission-denied / failed durumları ayrı tasarlanır (AC-MOB-04).
- Erişilebilirlik: ekran okuyucu, büyük metin, renkten bağımsız durum aktarımı (AC-UX-05).
- TR/EN eşit; ilk dil cihazdan (TR→TR, diğer→EN), Ayarlar'dan değiştirilebilir. Uzun metin/emoji taşması düşünülür.

## 2. Onboarding (LOCKED sıra)
Davet kodu → E-posta + parola ile hesap (ENG-09-02: Firebase e-posta/parola) → doğrulama e-postası (gelen kutusundaki bağlantıya dokunma) → Profil → İlk check-in. Telefon/SMS/sosyal giriş yok. Ayrıca gerekli ekranlar: mevcut kullanıcı girişi (e-posta + parola), parola sıfırlama (e-posta ile), doğrulanmamış hesap bekleme ekranı, çıkış. Yöntem (bağlantı/kod/parola) engineering kararıdır; ürün kuralı yalnız "gerçek e-posta doğrulaması".
- Davetsiz kullanıcı için "davet nasıl alınır" metni: TBD (R3, M10).

## 3. Profil (LOCKED envanter, 12.1)
| Alan | Kural | Görünürlük |
|---|---|---|
| Fotoğraf | Tam 1; galeri yok | Görünür |
| Ad | 2–30 karakter; gerçek ad şartı yok | Görünür |
| Doğum tarihi | Zorunlu, 18+ | Asla gösterilmez; **yaş** hesaplanır, varsayılan görünür, gizlenebilir |
| Cinsiyet | Kadın / Erkek / Non-binary / Belirtmek istemiyorum | Varsayılan görünür, gizlenebilir |
| Meslek | Zorunlu | Gizlenebilir (toggle) |
| Bio | Zorunlu, ≤150 | Görünür |
| İlgi alanları | 1–5, önceden tanımlı + Diğer | Görünür |
| Konuşulan diller | Opsiyonel | Görünür |
- Telefon/Instagram/e-posta profil alanı değildir. Konum, mesafe, koordinat, pin **hiçbir profilde/listede gösterilmez** (O-02, O-03).
- "Kiminle bağlanmak istersin" cinsiyet tercihi YOK.
- Başka kullanıcının profili: yukarıdaki görünür alanlar + istek gönderme eylemi (uygunsa).

## 4. Check-in ("Buradayım") (LOCKED davranış)
- Kullanıcı eylemiyle, ön planda; ~10 sn "konum doğrulanıyor" beklemesi; başarı → **30 dk ACTIVE**, kalan süre görünür, Durdur var.
- ~25. dakikada hatırlatma; CTA ile yeniden doğrulama → yeni 30 dk (süre birikmez). Otomatik yenileme yok.
- Ayrı durumlar (her biri ayrı ekran/uyarı): izin reddi (+ "Ayarları aç") · konum servisi kapalı · yetersiz hassasiyet · zaman aşımı · ağ hatası · erken yenileme başarısız (eski check-in bitişe kadar sürer) · eski süre doldu + doğrulama sürüyor.
- "Doğrulanıyor" → doğrulama başarısı olmadan "Buradasın" gösterilmez. Sürekli fiziksel varlık garantisi verilmez.
- Metinler: 6.5 tablosu ve v1.3 paketindeki 12 uyarı = öneri (NOT LOCKED); ayrım LOCKED.

## 5. Harita / yoğunluk katmanı (LOCKED, 16.1)
- Aggregate yoğunluk: 0–1 gösterilmez · 2–4 MAVİ · 5–9 SARI · 10–19 YEŞİL · 20+ KIRMIZI. Sayı, pin, kişi, mesafe gösterilmez.
- Harita gezmek referansı değiştirmez; kişisel işaret yok. Heatmap check-in olmadan da görülebilir (S1).
- Durumlar: PARTIAL ("yaklaştır"), EMPTY_NO_REGION, yükleniyor, boş, offline, hata, eski veri (v1.3'te iki kart var).

## 6. Yakındakiler listesi (LOCKED)
- Yalnız geçerli check-in'i olan ve ≤400 m'deki uygun kişiler; mesafe/sıralama ipucu yok.
- Engellenen kişiler görünmez.

## 7. İstek ve eşleşme (LOCKED, 19.x + FD-75)
- **Niyetler: Arkadaşlık, Networking** (FD-75; Flört kaldırıldı). Min 1, max 2, **varsayılan yok**.
- Gönderen istek öncesi kendi setini seçer. Alıcı gönderenin setini **görmez**; kendi setini seçip "Seç ve Kabul Et" der. Eşleşme sonrası iki set açığa çıkar; kesişim "Ortak noktanız: …" gibi gösterilebilir, boşsa nötr metin (NOT LOCKED metin).
- Aynı anda en fazla **20 bekleyen giden istek**; bekleyen ekranı "19/20" ve kalan süreyi (15 dk) gösterir; bu kredi/kota değildir.
- Karşı taraf aynı anda istek gönderdiyse ikinci deneme gelen isteğe yönlendirilir (auto-match yok).
- Sonuçlar: kabul → tek eşleşme · red · süre doldu · iptal (gönderen) · engel. Bekleme cooldown'ları arka planda (24 sa / ≥3 sa / 1 dk); UI'da sayaç zorunlu değil.

## 8. Sohbet (LOCKED, 20.x)
- Kişi başı 20 mesaj (toplam 40); kendi kalan hakkı görünür; karşı tarafın hakkı gösterilmez. Süre sayacı yok.
- Mesaj ≤500 karakter; metin + emoji + link. Medya, ses, dosya, GIF yok. Düzenleme/silme yok.
- Telefon/e-posta/IG tespitinde **yumuşak uyarı** + "Yine de gönder". Sert engel yok.
- **Bağlantıyı devam ettir** (private): sakin bir eylem; seçim karşıya tek başına gösterilmez; karşının kararına dair rozet/sayaç/baskı yok. EVET mutual olana kadar geri alınabilir; **HAYIR final** (karşı taraf nötr "bağlantı sona erdi" görür). EVET+EVET → sohbet **salt okunur** (O-04) + contact formu.
- Contact formu: Telefon / Instagram / E-posta / Diğer; bir/çok/hiç paylaşma; paylaşılanı düzenleme/geri çekme; "önceden görülmüş bilgi silinmez" dürüstçe yazılır. Hesap e-postası otomatik dolmaz.
- Kapalı sohbet: salt okunur, sınırlı süre; süre gösterilmez (TBD, M11).

## 9. Güvenlik (LOCKED, 21)
- Report: 5 kategori (Taciz, Spam, Uygunsuz içerik, Güvenlik endişesi, Diğer). Sonrasında ayrı soru: "Bu kişiyi ayrıca engellemek ister misin?" (rapor ≠ engel).
- Block: tek taraflı, anında; tüm yüzeylerde görünmezlik. Unblock var; eski sohbeti geri açmaz.
- End Connection: tek taraflı, onay istemez, engel değildir.
- Hesap silme: Ayarlar'dan; gerçek silme.

## 10. Bildirimler (LOCKED sınır, 17.x)
- Ambient keşif: günde en fazla 2, ≥3 sa ara; kişi/profil/konum/mesafe içermez.
- Hatırlatma ~25. dk, oturum başına 1. Direct istek/mesaj bildirimleri kotaya dahil değil.
- Bildirim izni reddi uygulamayı kapatmaz; nazik izin ekranı.

## 11. Etkinlikler (LOCKED)
- Yalnız placeholder: açılır, "yakında" tonu, sahte etkinlik/işlem yok, core loop'a dönüş kolay.

## 12. Ayarlar — türetilmiş liste (Founder onayı bekliyor)
Master Document tek tek listelemez; LOCKED işlevlerden türetilen minimum: Dil (TR/EN) · Bildirimler · Engellenenler (unblock için) · Gizlilik politikası / Şartlar (M11) · Hesabı sil. Fazlası Founder kararı.

---

## Açık noktalar (sahiplik)
| # | Konu | Sahip | Ne zaman |
|---|---|---|---|
| A1 | Ayarlar içeriği (§12 listesi) | Founder | Şimdi (tek kelime) |
| A2 | Davetsiz kullanıcı "davet nasıl alınır" metni (R3) | Founder → Designer | M10 |
| A3 | Kapalı sohbet saklama süresi | Founder + Manager (PL-01) | M11 |
| A4 | Mağaza ikonu / splash final | Designer | M10 sonu |
| A5 | Mapbox stil (taslak → final) | Designer + Code | M05 adım 7 |
| A6 | Erişilebilirlik cihaz doğrulaması | Code + Designer | M10 |
| A7 | navMap, çift anahtar, eksik TR metinleri | Designer temizler (v1.4) | M10 birleştirme öncesi |
| A8 | Form kenarlığı kontrastı | Designer | v1.4 |

## M10 tasarım sırası (öneri; milestone'larla hizalı)
1. **Ana yapı + Yakındakiler + check-in görünümleri + harita durumları** (M05/M06'ya kadar) 
2. **Giriş + profil** (M08 öncesi) 
3. **İstek/eşleşme + sohbet + devam + contact** (M06/M07 ile paralel) 
4. **Güvenlik + Ayarlar + bildirim + Etkinlikler placeholder** (M08/M09) 
Her paket: TR/EN, iOS/Android, boş/hata/offline/yükleme halleri, büyük metin.
