# Y1 / Y2 — Doğrulama

**PASS — tarayıcı tasarım önizlemesi.** Native uygulama/cihaz, ekran okuyucu, API, güvenlik veya üretim testi değildir.

## Ölçüm

| Matris | Kontrol |
|---|---:|
|40 durum × EN/TR ×100/200% ×390 iOS kabuğu |160 |
|40 durum × EN/TR ×200% ×320 iOS kabuğu |80 |
|40 durum × EN/TR ×200% ×320 Android kabuğu |80 |
| **Toplam** | **320** |

Her ölçümde: yatay taşma yok; telefon içindeki kontrol hedefleri en az 48×48; tek ekran başlığı; Geist hazır; kırık görüntü yok. Kaydırma miktarı kaydedildi. Uzun içerik için 63 full PNG mevcut. Dokunma ölçümü native dp dönüşümü veya fiziksel cihaz doğrulaması yerine geçmez.

`evidence/capture-*.json` ve `stress-*.json` ham ölçümler. `accessibility-modes.json`: üç temsilci ekranda yüksek kontrast gölgesiz yüzey ve opak menü (blur yok). Bunlar tam WCAG/VoiceOver/TalkBack uygunluk sertifikası değildir.

## Akış

`evidence/interaction-results.json` içinde 17 gözlem:

- Amaç boş başlangıç: 0 seçim, Continue pasif. Seçimden sonra işlem bekler.
- Başarısız check-in Friendship seçimini korur; başarıda iki amaç da görünür.
- Farklı amaç uyarısı işlemden önce; Cancel aynı kişiye döner. Bekleme sırasında sonuç iddiası yok; yalnız örnek olumlu yanıtla10 gün sonucu.
- Sonuçtan sonra yalnız ilgili kişi çıkar; aynı amaçlı diğer kişi görünür. Aynı amaçlı istekte eski niyet seçimi açılmaz; mevcut bekleyen ekrana geçiş.
- Boş formda7 alan/grup hatası; birleşik aile emojisi1/80 sayılır.
- Gönderim ve Withdraw bekler; hata form içeriğini korur; başarı/boş liste yalnız örnek yanıt sonrası.

Tarayıcının native tarih seçicisi ayrıca açılarak görüldü. iOS çark/Android picker ve klavye native cihazda Code tarafından ölçülmelidir. Örnek sunucu kontrolleri yalnız tasarım önizlemesidir.

## Varlık / metin

- 160 ana PNG: 780×1688.63 uzun içerik PNG +1 inceleme kolajı. Kaynaklar gerçek browser görüntüleridir; kolaj bu görüntülerden oluşturuldu.
- 62 yeni anahtar EN/TR eş; placeholder isimleri eş.18 Founder EN taslak anahtarı verilen wording ile birebir.12 mevcut ortak etiket yalnız referans.
-Canonical ARB, ortak tokenlar, eski Events/ERT teslimi ve Flutter/backend dosyaları değişmedi.
-Representative form, hata, amaç, Nearby ve farklı amaç görüntüleri görsel olarak incelendi; çıktı listesi SCREEN-STATE-MATRIX içinde.

## Native aktarımda kalanlar

Sunucu zaman/limit/grapheme doğrulaması; aynı işlem sonucunun uzlaştırılması; amaçsız eski oturumlar; görünmezliğin doğru iki kişiye uygulanması; konum kapıları; native seçici; klavye ve sistem geri; VoiceOver/TalkBack odak/anons; sunucudan gelen gerçek içerikle büyük yazı. Bunlar tasarım önizlemesinin tamamlanmış olmasıyla uygulanmış sayılmaz.
