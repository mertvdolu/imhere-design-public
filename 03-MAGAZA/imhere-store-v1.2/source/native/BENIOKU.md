# Mağaza / site — portresiz native ekran görüntüleri (2026-09-27)

Tasarımcı'ya teslim (Manager kararı 1b: portresiz yerel görüntü; portreleri Tasarımcı çerçevede ekler).

| | |
|---|---|
| Kaynak kod | `surum-7` dalı (`0bcf10d` + sahne aracı yoğunluk dağılımı). Sürüm 7 sohbet sayacı konumu dahil. |
| Derleme | dev + yerel emülatör + **Sahne kipi** (`IMHERE_USE_EMULATORS`, `IMHERE_SAHNE`): DEBUG ve geliştirici şeridi yok. |
| Veri | Yalnız yerel emülatör (`demo-imhere`), kurmaca: `tools/dev-magaza-sahnesi.mjs` (Alex / Maya, metinler Tasarımcı mağaza paketiyle birebir). Üretime ve Founder cihazına dokunulmadı. |
| Fotoğraf | Yok (portresiz). Fotoğraf koruması (imzasız yol) değişmedi; emülatörde imzalı adres üretilmez. |
| iOS | iPhone 18 Pro Simülatörü, 1206×2622, konum Londra 51.5246,-0.0786, durum çubuğu 09:41 (simctl sabitleme). |
| Android | A13 test telefonu, 1080×2408, **yalnız konum dışı ekranlar** (Nearby ve harita A13'te çekilmedi; izleyici check-in'i sunucu tarafında Londra'da). |

## Dosyalar → mağaza karesi

| Kare | iOS | Android |
|---|---|---|
| 01 A hello starts here (istek ekranı) | `01-opening.png` (seçimsiz), `01-opening-secili.png` (Friendship seçili) | aynı iki dosya |
| 02 People nearby | `02-nearby.png` | — (yalnız Simülatör) |
| 03 Full-screen map | `03-full-screen-map.png` (dört bant) | — (yalnız Simülatör) |
| 04 Connections | `04-connections.png` | `04-connections.png` |
| 05 Chat | `05-chat.png` (4 mesaj), `05-chat-baslikli.png` (Maya başlığı görünür, 4. mesaj yarım) | `05-chat.png` (başlık + 4 mesaj + sayaç birlikte), `05-chat-baslikli.png` |
| 06 Profile | `06-profile.png` | `06-profile.png` |
| Ek | `ek-maya-profili.png` | `ek-maya-profili.png`, `ek-merhaba-gonderildi.png` |

## Tasarım karelerinden native farkları (Tasarımcı bilgisine)

1. **Kendi profili (06):** fotoğraf yoksa native'de fotoğraf yuvası hiç çizilmiyor; karedeki büyük portrenin yeri native'de yok.
2. **Kartlar (01, 02, 04, 05):** fotoğraf yuvası kişi simgeli gri kutu; portre oraya girer. İlgi alanları native'de kapsül değil düz metin ("Design · Coffee"); Nearby kartında ↗ yok.
3. **Sohbet (05):** sürüm 7'de "18/20 messages left" "Your message" başlığının hemen üstünde sabit. Native'de "Continue this connection" satırı ve "0/500" yok (karakter sayacı yalnız son 50 karakterde).
4. **Bağlantılar (04):** karedeki ikinci satır ("Alex — The connection has ended") izleyici de Alex olduğu için native'de üretilemedi; native yalnız Maya.
5. **Saat:** iOS durum çubuğu 09:41'e sabitlendi, ama uygulama içi zamanlar gerçek çekim saati ("Ends at 1:38 AM", "Activity snapshot: 1:19 AM").
6. **Başkasının profili (ek):** dil başlığı "Languages · Optional" (kendi profilinde "Languages spoken") — Code bulgusu olarak raporlandı.
