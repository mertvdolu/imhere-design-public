# 04 — Ölçüler, platform ve erişilebilirlik
## Ölçüler
24 yatay dolgu; input iç16, min56; çok satırlı bio min120 ve içerikle büyür. Etiket14/1.4 kalıcı, metin16/1.6; başlık31/1.16, metadata12/1.5. Radius input12, kart16, foto18, CTA28. #637D5A sınır v1.4'ten değişmedi. Focus mint2px, hata danger1px + inline açıklama. Disabled eylemde label korunur; “işlem yapılıyor” metni yalnız gölge/renkten anlaşılmaya bırakılmaz.

Normal/büyük çizimler gerçek ölçek1/2 ile; formun tamamı aynı ekrana sığdırılmaz. Seçici listelerde üst başlık/alt Tamam eylemi uygulamada safe-area ve klavyeyi örtemez; gövde scroll. %200'de etiket satırları, kartlar, butonlar büyür. Klavye açılınca `viewInsets` kadar kaydırma alanı sağla, odaklanan alan ve hatası görünür olsun; tuş takımını tasarım görüntüsü olarak çizme.

## iOS/Android
Yerel e-posta metin girdisi, date-only giriş ve tek fotoğraf picker. iOS VoiceOver/Dynamic Type, Android TalkBack/text scaling ve platform geri davranışı korunur. Sistem izin diyaloğu uygulama içi maket değildir; fotoğraf aksiyonundan bağımsız izin talebi yok. Girişte konum izni istenmez; ilk check-in Paket1 kullanıcı eylemidir. E-posta bağlantısı uygulamaya dönünce backend/auth durumu otoritedir.

## Semantics
Alan label+value+error birlikte; placeholder etiket yerine geçmez. Hata sonrası ilk hataya odak; tüm mesajı her tuşta tekrarlama. Kontroller en az48 logical px. Switch checked değeri, görünür/gizli metni ve ismi tek erişilebilir hedef. Cinsiyet radio, ilgi checkbox/toggle seçimi; sayı ve seçili durum erişilebilir. Fotoğraf dekoratif tekrarlı isim yerine bir “Profil fotoğrafı” açıklaması alır. Public gizli alanların Semantics düğümü de yok.

Giriş sırası üstten alta; selector açılırken odak başlık/seçili öğeye, kapanınca açan alana döner. Fotoğraf preview yanında seç/değiştir ayrı eylem; thumbnail yeni bir gizli aksiyon içermez. Konuşulan dillerin boş olması hata anonsu üretmez. Kaydet/spinner sonucu bir kez duyurulur; fake başarı anonsu yok.

## Navigasyon
Girişte alt sekme yok. Kendi profil kökü Profil seçili; başka profil detayında gelinen Yakındakiler bağlamı korunur. Başka bir giriş kaynağı varsa mevcut route bağlamı geçerlidir, tasarım evrensel selected index2 dayatmaz. 2×2 büyük metin düzeni v1.4 kabulüyle aynı sıra; native uygulanabilirlik M10'da yazılım kontrolü. Form modal/detay açıkken tab bar gösterimi platform route düzenine göre; bu çizimler formu izole tam sayfa gösterir.

## Hareket
Mevcut giriş250ms/basma180ms; Reduce Motion'da yer değiştirme kapalı. Karşılama halkası dekoratif, konum takibi iması yok. Bekleme tamamlanma yüzdesi/zamanı göstermez. SVG/PNG statiktir; uygulama animasyonu henüz test edilmedi.
