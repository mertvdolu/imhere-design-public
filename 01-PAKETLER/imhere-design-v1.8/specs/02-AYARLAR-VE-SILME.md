# 02 — Ayarlar, bağlantılar ve gerçek hesap silme
## Geçici onaylı çalışma kapsamı
Founder'ın nihai Ayarlar listesi onayı bekleniyor; verilen geçici liste tasarıma uygulanmıştır. Profil altında: Dil, Bildirimler, Engellenenler, Gizlilik politikası, Şartlar, Hesabımı sil, Çıkış yap. Gizlilik/Şartlar iki ayrı web bağlantısı; aynı hukuki bölümün satırlarıdır. Ödeme, abonelik, tema, profil görünürlük tekrarı veya yeni tercih eklenmedi. Founder onayı bekliyor ifadesi yalnız teslim belgelerinde; ürün ekranında değil.

Dil mevcut cihaz/TR/EN seçimidir. Seçili durum gerçek tercihe bağlı; değişim yerel ve kalıcı mevcut locale controller üzerinden. Cihaz dili seçeneği önceki kabul edilmiş temel metinden devralınır; yeni dil yok. İşlem internet gerektirmez; ağ hatası uydurulmaz. Seçim sırasında metinler yeni dile döner, odak aynı kontrolde kalır. Ekran matrisi iki yerelleştirmedeki label ölçülerini göstermek için seçili tercihin olası anlık geçiş görünümünü de içerir.

Çıkış için 4 kabul edilmiş v1.6 ekranı byte-identical yeniden kullanıldı. Çıkış hesabı silmez; check-in, yerel tercihler veya profil verileri için yeni yan etki tanımlanmaz. Offline Çıkış yap mevcut auth davranışıyla kullanılabilir; salt internet yok diye yeni kilit getirilmez.

## Gizlilik politikası / Şartlar — M11 / PL-01
Founder bu belgelerin henüz olmadığını doğruladı. Ayarlar satırında dış bağlantı işareti bulunur. URL verilene kadar hedef yer tutucudur; sahte domain, sahte içerik veya sözleşme kabul kutusu yok. Dokunmada uygulama içi `legalUnavailable` durumu gösterilir, boş tarayıcı açılmaz. M11'de onaylı gerçek URL bağlandığında platformun web açma davranışıyla sayfa açılır. Dönüşte Ayarlar bağlamı korunur.

Paketin loading/failed/offline ekranları **web açma hazırlığı / uygulama tarafındaki açma hatası** durumlarını tarif eder; bu çizimler web sayfasının içeriği veya işletim sistemi tarayıcı arayüzü değildir. Dış tarayıcı açıldıktan sonraki internet/HTTP hatalarını o tarayıcı yönetir; uygulama bunları görebildiğini varsaymaz. Aynı şekilde açıldı sonucunu belge okundu/kabul edildi sanmaz. Hazırlık beklemesi gerekmeyen uygulamada loading kullanılmaz.

## Hesap silme: onaylı kısa metin
TR:
- **Hesabını silmek geri alınamaz.**
- Profilin, fotoğrafın, check-in kayıtların, isteklerin, sohbetlerin ve paylaştığın iletişim bilgileri erişiminden kalkar.
- Sınırlı kayıtlar yasal gereklilikle saklanabilir.

EN:
- **Deleting your account can’t be undone.**
- You’ll lose access to your profile, photo, check-in records, requests, chats and shared contact details.
- Limited records may be retained to meet legal requirements.

Altında belirgin, ayrı **Hesabımı sil / Delete my account** ve **Vazgeç / Cancel**. Başlık `deleteConfirm`, metin için üç yeni UI anahtarı; eski `deleteBody` sözlükte değişmeden kalır ancak bu onayda daha somut yeni metinler kullanılır. Silme kapsamı yeni bir tasarım kararı değildir; son Manager yanıtındaki Founder onaylı çerçevenin UI karşılığıdır. Master belge açılmadı.

## Silme durumları
| Görünüm | Gerçek anlamı | Eylem |
|---|---|---|
| Onay | Henüz işlem başlatılmadı | Hesabımı sil / Vazgeç |
| Yeniden giriş | Mevcut auth katmanı yeniden doğrulama istiyor | `authReauthRequired` → kabul edilmiş e-posta/parola girişi |
| Siliniyor | İşlem yürütülüyor | Tekrar gönderim yok; iptal edilmiş iddiası yok |
| İstek alındı | Silme talebi doğrulandı, silme henüz tamamlanmadı | Gerçek durumunu kontrol et |
| Tamamlandı | Hesap silme tamamlandığı doğrulandı | Hesap oturumundan çıkılmış karşılama bağlamı |
| Başarısız | Kesin başarısız sonucu | Mevcut güvenli yeniden deneme |
| Belirsiz | İstek gönderildi mi / tamamlandı mı henüz bilinmiyor | Durumu uzlaştır; kör yeni silme göndermesi yok |
| Çevrimdışı | Henüz gönderilemeyen işlem | Silme pasif, Vazgeç kullanılabilir |
| Açıklama yok | Onaylı açıklama yüklenemiyorsa | Tekrar dene; silme onayı verdirilmez |

Açıklama bu teslimde yerel TR/EN metin olarak hazırdır; “açıklama yok” yalnız içeriğin dinamik bağlandığı durumda savunmacı bileşen varyantıdır, zorunlu yeni ağ bağımlılığı değildir.

Yeniden giriş için yeni parola kuralı/formu yok: mevcut 19 canonical auth anahtarı, en az 8 karakter, generic hata. Yeniden giriş başarıyla bitince silme kendi onayına geri dönülür; yalnız giriş yapmak silmez. Önceden devam eden gerçek silme sonucu ayrıca uzlaştırılır. İşlem alındı durumu hesap silindi ekranı değildir; oturum geçersizleşmesi tek başına tamamlanma kanıtı sayılmaz. Sonucu auth oturumu kalktıktan sonra gösterecek mevcut mühendislik mekanizması M10'da doğrulanır; tasarım yeni backend API icat etmez.

Başarı, hesabı devre dışı bırakmak veya yalnız çıkış yapmak yerine **gerçek silme** sonucudur. “Her şey anında silindi”, belirli saklama süresi, karşıdaki kişinin gördüğü/kaydettiği kopyaların silindiği veya rapor kanıtlarının yok olduğu söylenmez. Bildirilen erişim kaybı kullanıcının kendi erişimidir. Hukuki açıklama hazırlanmış gibi davranılmaz.
