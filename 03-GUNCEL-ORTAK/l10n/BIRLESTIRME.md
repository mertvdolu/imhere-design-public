# Güncel referans sözlükleri / Cream & Ink v2.2

Bu klasör tam referanstır; canlı ARB üzerine yazılmaz. Önceki M09/M10 düzeltmeleri korunur. Ek anahtarlar ve değişen mevcut metinler aşağıdaki güncelleme notlarında belirtilir. `02-SON-EKLER/imhere-cream-complete-v2.2/l10n/cream-v2.2-patch_*.arb` ve aynı klasördeki migration.json ile birleştirilir. Önceki alias ve placeholder sözleşmeleri korunur. EN aktif, TR hazırlığı korunur fakat kapalıdır.

CH-138: `authEmailUnavailable` mevcut anahtarının TR/EN metni canlı uygulamayla hizalandı. Yeni anahtar yok. Güncel `cream-v2.2-patch_*.arb` değişen metni de içerir; yalnız bu anahtar birleştirilir. `authExistingAccount` metni değişmedi.

Doğrulama tekrar gönderimi için `authVerifyResending` eklendi (TR/EN). Yalnız `verify-resend-busy` kullanır; ilk gönderim `emailSending` olarak kalır. Ayrıntı: `02-SON-EKLER/imhere-cream-complete-v2.2/specs/CODE-SORULARI-CH138-ERT050.md`.

Founder telefon turu (2026-09-24): `photoUploading` ve `photoProcessing` eklendi (TR/EN). `photoUploaded` başarı sonrasında, `selectionDone` klavye kapatma çubuğunda mevcut metniyle kullanılır; eski çağrılar değiştirilmez. Yalnız iki yeni anahtar birleştirilir.

`profileHiddenToOthers`: EN “Not visible to others”, TR “Başkalarına görünmez”. Yalnız kendi profilinde gizli yaş/cinsiyet/meslek altında. `profileEdit` ve `settings` üst çubuk erişilebilir adları olarak yeniden kullanılır.
