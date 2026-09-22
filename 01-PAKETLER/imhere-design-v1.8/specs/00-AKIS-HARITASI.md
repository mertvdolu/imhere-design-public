# 00 — Akış ve giriş noktaları
```mermaid
flowchart TD
 Profile[Profil] --> Settings[Ayarlar]
 Settings --> Language[Dil: Cihaz / TR / EN]
 Settings --> Notifications[Bildirim izni]
 Settings --> Blocked[Engellenenler]
 Settings --> Legal[Web bağlantıları: Gizlilik / Şartlar]
 Settings --> Delete[Hesap silme: kendi onayı]
 Settings --> Logout[Kabul edilmiş Çıkış]
 Context[Erişilebilir kişi veya bağlantı] --> Report[Şikâyet: 5 kategori, ilk seçim boş]
 Report --> Received[Gerçek şikâyet sonucu]
 Received --> Optional[Ayrı: ayrıca engelle?]
 Optional -->|Şimdi değil| Return[Geri dön]
 Optional -->|Engelle| Block[Engelleme işlemi]
 Context --> BlockConfirm[Kendi engelleme onayı]
 BlockConfirm --> Block
 Context --> EndConfirm[Bağlantıyı bitir: kendi onayı]
 EndConfirm --> End[Gerçek sonuç: bağlantı sona erdi]
 Blocked --> Unblock[Engeli kaldır: eski sohbet açılmaz]
 Delete --> Reauth[Gerekirse mevcut e-posta + parola girişi]
 Reauth --> Delete
 Delete --> DeletionReceived[Silme isteği alındı: henüz bitmedi]
 DeletionReceived --> Deleted[Gerçek silme tamamlandı]
 Notifications --> Native[Gerçek işletim sistemi izin diyaloğu]
 Native --> Allowed[İzin açık]
 Native --> Denied[İzin kapalı: uygulamaya devam]
 Events[Etkinlikler placeholder] --> Nearby[Yakındakiler]
```
Şema sırayı anlatır; her silme mutlaka gecikmeli çalışır veya yeniden giriş ister diye bir kural getirmez. Mevcut backend doğrudan tamamlanma döndürebilir; ara durum yalnız gerçekse gösterilir. Reauth başarısı tek başına silme değildir; kendi onayına geri dönülür. Sonucu belirsiz işlem önce mevcut işlem kimliğiyle uzlaştırılır.

Güvenlik menüsünün bağlantıyı bitir satırı yalnız mevcut bağlantı bağlamında vardır. Keşifteki bağlantısız profil için yalnız report/block sunulur. İşlem hedefi kişi/bağlantı sabit kimliğiyle taşınır; görünen ad işlem anahtarı değildir. Profil alanlarının görünürlük kuralları değişmez.

4 sekme sırası Profil → Mesajlar → Yakındakiler → Etkinlikler; başlangıç Yakındakiler. Ayarlar yeni ana sekme değildir. İşlem ekranı geçici tam sayfa/sheet olarak açılır; eski bağlam ve geri odağı korunur.
