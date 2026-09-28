TASARIMCIDAN MANAGERE MESAJ

# Kaydırıcı uç etiketleri v1.0 · 2026-09-28

Sonraki paket içindir; sürüm8 yayın engeli değildir. compact-signals-v1.0/SPEC.md’deki mevcut uç yerleşimini tamamlar, yön/değer davranışını değiştirmez.

| Anahtar | EN | TR | Yer |
|---|---|---|---|
| profileNetworkingMixFriendsLabel | Friends | Arkadaşlık | Sol: Networking0 / Friends100 |
| profileNetworkingMixNetworkingLabel | Networking | Networking | Sağ: Networking100 / Friends0 |

Mevcut14/400 uç etiketleri, Ink; büyük yazıda sarılabilir. Ayrı düğme veya ayrı dokunma hedefi değil. Kaydırıcının mevcut erişilebilir adı ve iki oranı anlatan değer korunur.

Delta: l10n/networking-endpoints-patch_en.arb ve _tr.arb. Yalnız iki yeni anahtar + metadata; tam ARB üzerine yazılmaz. Başka ekranda kullanılan intentFriendship/intentNetworking anahtarları yeniden adlandırılmaz.

Yerel commit; aktarım Code.
