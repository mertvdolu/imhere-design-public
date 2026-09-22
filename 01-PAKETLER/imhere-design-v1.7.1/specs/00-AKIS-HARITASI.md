# Kişi durumu akışı
Yetkili mevcut durum → ilgili kişi görünümü. Cooldown → pasif gönderim + nötr açıklama. Bekleyen → pasif gönderim + mevcut isteği görüntüle. Bağlantı → pasif gönderim + Mesajlara dön. Erişim kaldırıldı → mevcut nötr erişimsizlik.

İsteği görüntüle kabul eylemi değildir; gelen istek incelemesi bağımsız boş niyet seçimini korur. Sunucu sonucunu görmeden yeni durum tahmin edilmez. `STATE_CHANGED` bağlı/engelli/soğuma nedeni olarak sınıflandırılmaz.
