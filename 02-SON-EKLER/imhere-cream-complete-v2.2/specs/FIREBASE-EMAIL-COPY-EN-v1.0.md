TASARIMCIDAN MANAGERE MESAJ

# Firebase e-posta metinleri — EN v1.0

Gönderen adı: **IM HERE**

Doğrulama konusu: **Confirm your email for IM HERE**

Şifre sıfırlama konusu: **Reset your IM HERE password**

## Şifre sıfırlama gövdesi

```text
Hi there,

We received a request to reset your IM HERE password. Use the link below to choose a new password.

%LINK%

If you didn’t request this, you can ignore this email.

IM HERE
```

Üç cümle; %LINK% aynen korunacak. Gönderen/konu marka adı mevcut kesme işaretsiz IM HERE kararıyla tutarlı tutuldu. TR bu teslimde yok. Doğrulama gövdesi düzenlenmedi ve alternatif gövde üretilmedi.

Makine okunur dosya: `../email/firebase-email-copy_en.json`.

Kapsam yalnız metin teslimidir. Konsola aktarımı Code/Founder yapar. Gönderen e-posta adresi uydurulmadı; useimhere.com yapılandırması/deploy/test e-postası bu teslimde yapılmadı. Yerel commit.
