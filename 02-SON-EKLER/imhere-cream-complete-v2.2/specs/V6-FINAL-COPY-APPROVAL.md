TASARIMCIDAN MANAGERE MESAJ

# Sürüm 6 — kalan üç kalem onayı v1.1

2026-09-26. Üç tasarım kararı ONAYLANDI. Önceki d76a931’in kısa konum metni ve resmî TR hitabı bu ekle geçersizdir. Hukuki metnin sahibi HARBOR; bu teslim görünüş ve dil tutarlılığı onayıdır, hukuki uygunluk veya cihaz test sonucu değildir.

## 1. Kayıt satırı — ONAY

TR “sen” hitabı onaylı. ARB’de terms/privacy yer tutucuları korunur; belge adları değişmez. Uygulamanın mevcut tipografik kesme işareti ’ korunur.

## 2. HARBOR I-7 uzun konum açıklaması — yerleşim ONAY

Kaynak: uygulamanın güncel EN/TR ARB metni ve location_rationale_screen.dart, request_widgets.dart. Metin aşağıdaki gibi TAM korunur; kısaltma, üç nokta veya yazı küçültme yok. Mevcut kaydırılabilir RequestPage + SafeArea düzeni bu uzunluk için onaylıdır.

- Başlık mevcut checkInTitle. Gövde Geist16/400, satır1.6, Ink; yan kenar24.
- Başlık→gövde16; gövde→Continue24 (mevcut8 padding + ortak16 boşluk).
- Continue / Devam aynı birincil düğme, en az48 yüksekliğinde. Açıklamanın ardından akış içinde gelir, metnin üzerine sabitlenmez.
- %200 metinde gövde ve düğme birlikte kaydırılabilir; bütün metin ve düğmeye ulaşılır. maxLines, ellipsis, sabit gövde yüksekliği yok.
- Sistem geri rıza değildir. Ek Not now/çıkış eylemi yok; izin zaten var/kalıcı ret dalları mevcut davranışını korur.

Kontrol sınırı: güncel widget yerleşimi incelendi; uzun konum ekranının cihaz görüntüsü bu teslimde mevcut değildi. Bu onay uygulanacak yerleşim içindir; EN/TR ve büyük yazıda native taşma testi Code’un doğrulamasıdır. Yeni tasarım kararı beklemiyor.

## 3. Harita erişilebilirlik etiketi — ONAY

mapShowMyArea: EN “Show my area” / TR “Bölgemi göster”. Bu ad tam konum noktası vaadi taşımaz; mevcut check-in bölgesine gitme eylemini tarif eder. Etkileşim hedefi48×48; ekran okuyucu/tooltip aynı etiket. GPS okuma, kişisel pin veya mesafe eklenmez; mevcut davranış değişmez. Bu teslim yeni simge veya kontrol konumu kararı değildir.

## Onaylı metinler

### `authConsentLine`

EN: By tapping Create account you agree to the {terms} and confirm you have read the {privacy}.

TR: Hesap oluştur’a dokunarak {terms}’nı kabul etmiş ve {privacy}’nı okuduğunu onaylamış olursun.

### `locationPermissionRationale`

EN: To check in, I’M HERE uses your phone’s location once, now. It is used only to show you to people nearby for 30 minutes and is never shown to anyone. Erasure starts when your check-in ends. It is not tracked in the background.

TR: Check-in için I’M HERE telefonunun konumunu şimdi, bir kez kullanır. Konumun yalnızca 30 dakika boyunca yakınındakilere görünmen için kullanılır ve kimseye gösterilmez. Check-in bitince silme başlar. Arka planda takip edilmez.

### `mapShowMyArea`

EN: Show my area

TR: Bölgemi göster

## A13 kayıt bağlantıları — mevcut hâl kabul

İncelenen görüntü: `docs/evidence/m11/cihaz-surum6/v6-kayit-baglantilari-a13-en-100.png` (Code deposu). Metin ve altı çizili bağlantılar okunur; satırların geniş aralığı48 dp bağlantı kutularından kaynaklanıyor. Önceki istekteki48 hedefler korunur; bu hâl tasarım açısından yayın engeli değildir.

İsteğe bağlı sıkılaştırma: yalnız bilgilendirme bloğunun altı→Create account aralığı16→8 dp. Metnin helper14/400/1.4 stili, bağlantıların48×48 hedefi ve birbirinden ayrı erişilebilirlik alanları aynı kalır. Negatif satır aralığı, üst üste gelen hedef veya font küçültme kullanma. Diğer form boşluklarını topluca değiştirme. Bu öneri uygulanmasa da tasarım onayı geçerli.

## Aktarım

`l10n/v6-final-copy-patch_en.arb` ve `_tr.arb` üç anahtarı günceller. Önceki v6-register-location deltası ardından uygulanır; tam ARB üzerine yazılmaz. authConsentTerms/Privacy ve locationRationaleContinue değişmez. migration sırası kaydedildi.

Üç kPendingDesigner metin kaydı bu onayla kapatılabilir; uygulama listesini Code günceller. Uygulama deposuna yazılmadı. Yerel commit; aktarım Code.
