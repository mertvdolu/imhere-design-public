# Üretim / kapsam

`states.json`, `copy-bank.json`, `occupation-catalog.json` bu teslimin dondurulmuş girdileridir.
`build.py` → browser/CUA ile `capture.mjs` → `finalize.py` → `validate.py` sırası kullanılır.
PNG yakalama yalnız belgelenmiş CUA tab + CDP köprüsüyle çalışır; bağımsız Playwright oturumu açmaz.
`capture.mjs` fonksiyonuna mevcut tab/CDP ve çıktı yolu verilir. `measure.js` yalnız DOM ölçer.

`add_*.py` ve `prepare_copy.py` tasarımın ilk üretim yardımcılarıdır; final girdileri yeniden üretmek için çalıştırılmaz. Son bağlam düzeltmeleri `states.json` içindedir. Canonical kaynakların yeni sürümü gelirse ayrıca incelenmelidir.

Bu HTML durum önizlemesidir; gerçek üyelik, LinkedIn, kart, filtre, harita, hesap veya ağ işlemi yapmaz. Üstteki başarı/hata düğmeleri yalnız tasarım incelemesi içindir. Veri girme/arama kontrolleri örnek etkileşim sağlar; tam uygulama modeli değildir.
