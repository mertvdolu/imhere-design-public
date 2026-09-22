# 06 — Birleştirme ve kaynaklar
- Baseline v1.7 kabul edildi. 400 metin ve metadata aynen kalır; 52 ek metin ile 452. `v1.8-additions_tr/en.arb` delta, `app_tr/en.arb` referanstır. **Canlı ARB dosyalarını değiştirmeyin: migration ile anlamsal birleştirin.** App-only anahtarları silmeyin.
- v1.6.1 auth canonical anahtarları ve alias'ları, parola kuralı, generic auth hata/conditional reset metinleri aynı. Report gönderimi için auth hata metni veya check-in handler kopyalanmaz. `checkInRetry` yalnız ortak Tekrar dene label'ıdır, eylem bağlamı ayrıdır.
- `endConfirm` kendi onayı olarak kullanılır. `deleteBody` referans sözlükte korunur; v1.8 delete-confirm callsite'ı `deleteIrreversible`, `deleteAccessScope`, `deleteLimitedRetention` üç anahtarını kullanır. Eski anahtar global olarak yeni paragrafa alias edilmez.
- Token JSON/font/lisans/kabul eki byte-identical. Yeni global token yok. Önceki teslimler değişmedi. Çıkış ekranları v1.6'dan byte-identical kopyalandı; yeniden uygulamak değil mevcut eylemi Ayarlar satırına bağlamak gerekir.
- Contracts UI davranış açıklamasıdır; yeni backend enum/API veya hata kodu değildir. String key ≠ widget Key ≠ endpoint. İşlem sonuçları ve erişim mevcut yetkili katmana bağlanır. Tasarım uygulama kodunu değiştirmez.
- `notificationRequestSample/MessageSample` genel içerik örneğidir; mevcut payload/key eşlemesi varsa yeniden adlandırmadan mevcut sözleşmeyle bağlanır. Ambient/reminder kuralları değişmez.

## Kaynak önceliği
Güncel Founder/Manager Paket 4 talimatı ve son hesap silme açıklaması; Tasarım Gereksinim Özeti v1.0.2 §9–12; geçmişte kabul edilmiş endConfirm/çıkış/metin/token sözleşmeleri. Master 22.8'in kendisi okunmadı; kullanıcının ilettiği onaylı özet kullanıldı. Bu teslim kaynak belgeyi yeniden yorumlayarak iş kuralı değiştirmez.

## Karar ve entegrasyon bekleyenler
1. Founder'ın Ayarlar listesi nihai onayı. Şimdiki liste üzerinde çalışılması açıkça yetkilendirildi.
2. M11 / PL-01 gerçek Gizlilik/Şartlar içeriği ve web URL'leri. Metin/URL tasarımcı tarafından uydurulmadı.
3. M10 gerçek cihaz/backend doğrulaması: silme aşamaları, erişim kaldırma, izin dönüşleri, blocked-list minimal identity, büyük metin nav. Test sonuçları bu paket tarafından garanti edilmez.

Hesap silmenin davranış çerçevesi artık açık nokta değildir; onaylı kapsam metne uygulandı. Sınırlı kayıtların saklama süresi tasarıma dahil edilmedi. Ek ürün kararı önerilmedi.
