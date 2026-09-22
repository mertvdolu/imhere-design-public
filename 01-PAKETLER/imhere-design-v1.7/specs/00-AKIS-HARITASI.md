# 00 — Paket 3 akış haritası
```mermaid
flowchart TD
 Nearby[Yakındakiler / kişi profili] --> Send[Niyet seçimi: boş başlangıç]
 Send --> Pending[Bekleyen istek: 19/20 + kalan süre]
 Pending --> Result{Mevcut istek sonucu}
 Result -->|Kabul| Match[Eşleşme: iki niyet seti görünür]
 Result -->|Süre doldu / iptal / red| EndReq[İstek sonucu]
 Send -->|Ters yönde istek var| Incoming[Gelen isteğe yönlen]
 Messages[Mesajlar] --> Connections[Bağlantılar]
 Messages --> Requests[İstekler: gelen + giden]
 Requests --> Incoming
 Incoming --> Accept[Alıcının bağımsız boş niyet seçimi]
 Accept -->|Seç ve Kabul Et| Match
 Match --> Chat[Sohbet: yalnız kendi kalan hakkı]
 Connections --> Chat
 Chat -->|İletişim bilgisi olabilir| Soft[Yumuşak uyarı]
 Soft -->|Gözden geçir| Chat
 Soft -->|Yine de gönder| Chat
 Chat --> Choice[Özel devam kararı]
 Choice --> Yes[Kendi EVET tercihi]
 Yes -->|Karşılıklı olmadan geri al| Choice
 Choice -->|Kendi son onayıyla HAYIR| End[Bağlantı sona erdi: nötr]
 Yes -->|Sunucu karşılıklı EVET doğrular| ReadOnly[Salt okunur sohbet]
 ReadOnly --> Contact[Ayrı contact formu]
 Contact -->|Bir / çok / hiç| Shared[İletişim paylaşım alanı]
 Shared --> Edit[Kendi paylaşılan bilgisini düzenle]
 Shared --> Withdraw[Görünürlüğünü kaldır]
```

Çizim yönlendirme mantığını anlatır; sunucu işlemi veya otomatik seçim değildir. Her ok gerçek işlem sonucu ve mevcut erişim kontrolüne bağlıdır. Alıcının niyetleri kabul öncesinde bağımsızdır. Karşı tarafın devam kararı hiçbir ayrı düğüm/rozet olarak UI'a açılmaz; şemadaki karşılıklı koşul backend'in yetki verdiği sonuçtur.

Erişim kaldırılmış/engellenmiş içerik için tüm rotalarda nötr kullanılamıyor görünümü üstündür. Kapalı sohbet, ancak mevcut erişim/saklama koşulları izin verdiği sürece salt okunur gösterilir. “Sohbete dön” eski sohbeti yeniden açmaz.
