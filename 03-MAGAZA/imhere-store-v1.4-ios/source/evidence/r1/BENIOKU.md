# MAGAZA-NATIVE-14 — App Store iPhone native kareleri (STORE-IOS-14) · 2026-10-13

## DURUM: KARE YOK — NOT RUN (Code tarafında koşulmadı)

Bu klasörde henüz PNG yok. Kareler yerel Firebase emülatörü ister (`firebase emulators:exec`); Code ajan kuralında
`firebase` (deploy dahil) YASAK, bu yüzden Code emülatörü açmadı. Görev metnindeki yedek yol uygulandı: araçlar hazır,
kuru prova geçti, çekim Founder / Manager'ın **tek komutu**:

```bash
cd ~/Desktop/here/wt-IPHONE19 && bash tools/magaza-ios/cekim.sh
```

Komut bittiğinde bu klasöre `01-amac.png` … `06-harita.png` (1206 × 2622) + `CEKIM-KAYDI.txt` (+ varsa `KADRAJ-NOTLARI.txt`)
gelir. Üretime, gerçek cihaza ve Founder cihazına dokunmaz (yalnız `demo-imhere` emülatörü + Simülatör). Süre ≈ 10–15 dk
(ilk koşuda Simülatör cihazı ve bağımlılık hazırlığı dahil). Etkinliğin üretimdeki açıklama metni karede istenirse önce bir
dosyaya yazılıp `MAGAZA_ETKINLIK_ACIKLAMASI=<dosya> bash tools/magaza-ios/cekim.sh` ile verilir (verilmezse bkz. fark 3).

## Kaynak ve ortam

| | |
|---|---|
| Yapı | **1.4.0 (19)** (`app/pubspec.yaml`; iOS yalnız iPhone, `UIDeviceFamily` = `[1]`) |
| Kaynak | dal `is/IPHONE19` @ `fcb3a1c` (uygulama kodu = canlı aday `9a73c0e` + yalnız iPhone; `app/lib` farkı 0) |
| Derleme | `flutter build ios --simulator --debug --dart-define=IMHERE_USE_EMULATORS=true --dart-define=IMHERE_SAHNE=true --dart-define=IMHERE_EVENTS_V1=true` (dev + yerel emülatör + Sahne kipi: DEBUG şeridi ve geliştirici şeridi yok) |
| Simülatör | ayrı cihaz **"IM HERE Magaza"** (iPhone 18 Pro türü), iOS 27.0, 1206 × 2622, dil / bölge en-GB / en_GB, açık tema, normal yazı boyutu, durum çubuğu 09:41 + tam pil + Wi-Fi + hücresel (simctl sabitleme). Uygulama ana ekrandan açılır (sol üstte "geri" kırıntısı yok). Klavye açılmaz. |
| Veri | yalnız yerel emülatör `demo-imhere`, `tools/dev-magaza-sahnesi.mjs` (aşağıda). Gerçek kişi / e-posta / konum yok. |
| Fotoğraf | portresiz (emülatörde imzalı fotoğraf adresi üretilmez); yuvalar Tasarımcının sentetik portreleri içindir. |

## Kareler (dosya ↔ Tasarımcı adı ↔ durum)

| Dosya | Tasarımcı listesi | Ekran / sahne |
|---|---|---|
| `01-amac.png` | `01-purpose.png` | Nearby → I'm here → "Why are you here?": Networking / Friendship, seçim YOK, Continue pasif (izleyicinin varsayılan amacı yok, check-in yok). |
| `02-yakindakiler.png` | `02-nearby.png` | İzleyici Networking check-in → "Good, you're here." + People nearby'da TEK kart: Maya (Designer, Design · Coffee), amaç rozeti, gri fotoğraf yuvası. |
| `03-istek-profili.png` | `03-request-profile.png` | Maya → izleyici gelen istek (cevapsız): Messages › Requests › Maya → profil + "I'd like to connect" / "Not this time". |
| `04-sohbet.png` | `04-chat.png` | Kabul (sunucuda) + 4 kurmaca mesaj (Tasarımcı fixture'ı): sağ üst kalkan, sayaç, "Your message" yazma alanı; klavye kapalı. |
| `05-etkinlik.png` | `05-event-detail.png` | Events › "I'M HERE Coffee & Connect": Cumartesi 7 Kasım 2026 14:00–16:00 Londra, Royal Festival Hall, "Southbank Centre, Belvedere Road, London SE1 8XX", Social; Interested / Going, tercih verilmemiş. |
| `06-harita.png` | `06-area-activity.png` | Nearby › Area activity → tam ekran harita → Show my area: güncel kontroller, yoğunluk katmanı (adsız kurmaca üyeler, 400 m dışı), atıf satırı. |

Sahne kişileri: Alex (izleyici: "Coffee, design and new ideas. Always up for a good conversation.", Designer) ve Maya
(Designer) — Tasarımcı mağaza paketindeki kurmaca yetişkinler ("Maya and Alex are invented adults"). Mesajlar:
"Hello, I noticed you’re interested in design." · "Hello. I am! Especially the little details." · "Same here. The simple
things take the most thought." · "It’s nice to talk about new ideas." Etkinlik, yayındaki etkinliğin Manager görev
metnindeki bilgileriyle YEREL kopyasıdır (üretimden okunmadı).

## Native ile tasarım farkları (Tasarımcı bilgisine)

1. **Amaç rozeti (02):** kartta görünen metin **"Networking"** (+ iki çember simgesi); "Here for Networking" ekran okuyucu
   etiketidir. Rozet adın hemen altında.
2. **İstek profili (03):** fotoğraf yoksa kişi profili gövdesi fotoğraf yuvası ÇİZMEZ (yuva yalnız kart / liste satırı /
   sohbet başlığında). Gelen istekte amaç rozeti YOK (bilinçli, INV09). Fotoğrafsız ekrana yeni alan eklenmemeli.
3. **Etkinlik (05):** yerel kopyada kapak görseli yok → native yer tutucu görsel (takvim simgesi). Üretimdeki açıklama Code'da
   yok: verilmezse "About" bölümünde bilgileri yineleyen tek cümle; bölüm sayfanın en altında (büyük olasılıkla kadraj dışı).
   Tarih / saat biçimi uygulamanın kendi gösterimidir (en_GB, 24 saat).
4. **Saatler:** durum çubuğu 09:41 sabit; uygulama içi zamanlar (oturum bitişi, harita "anlık görüntü" saati) gerçek çekim
   saatidir.
5. **Harita (06):** görünen atıf satırı "© OpenStreetMap contributors · OpenFreeMap" + MapLibre ⓘ düğmesi (tam atıf orada).
   Kişisel konum işareti / kişi sayısı / mesafe yok; check-in sürerken haritada uygulamanın varlık dalgası animasyonu vardır.
6. **Gizlilik / Şartlar 1.4 duyurusu** (Nearby üstünde, cihazda bir kez) çekimden önce "Done" ile kapatılır; karelerde yok.
7. **Kadraj:** çekim yerleşimi değiştirmez; beklenen öğe ekranda değilse kare yine alınır ve `KADRAJ-NOTLARI.txt`'ye yazılır.

## Doğrulama (Code)

- Kuru prova GEÇTİ (`bash tools/magaza-ios/cekim.sh --kuru`, emülatörsüz; uygulama hiçbir sunucuya bağlanmaz): cihaz
  oluşturma, en_GB, 09:41 tam pil, ana ekrandan açılış, sekme / düğme bulma + dokunma, harita aç / geri, 1206 × 2622 kare.
  Kanıt: `ops/outbox/IPHONE19-kanit/kuru-prova/` (veri yok: "Check-in isn't connected in this build" bilerek).
- Araç kilidi testi `backend/functions/test/magaza-native-14.test.ts` (11/11; bozma 9/9 kırmızı).
- Koşulmayan: emülatörlü tam koşu. İlk koşuda bir adım tutmazsa test o adımda durur; teşhis
  `app/build/magaza-ios/el-sikisma-*/agac-*.txt` + `app/build/magaza-ios/teshis/*.png` (düzeltme küçük Code işi).
