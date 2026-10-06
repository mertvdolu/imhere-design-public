# ERT-098 — Ekran / görüntü listesi

390×844 dp, 2× PNG (780×1688). EN/TR aynı şablon. 8 ana ekran + 8 kaydırma/tam metin kanıtı + 2 kopyalandı görüntüsü.

| Durum | Dil | Yazı | Ana PNG | Metin sonu | Tam metin |
|---|---|---|---|---|---|
| DELETION_PENDING | EN | %100 | [PNG](screens/png/deletion-pending-en-100.png) | — | — |
| DELETION_PENDING | EN | %200 | [PNG](screens/png/deletion-pending-en-200.png) | [PNG](screens/png/deletion-pending-en-200-end.png) | [PNG](screens/png/deletion-pending-en-200-full.png) |
| DELETION_PENDING | TR | %100 | [PNG](screens/png/deletion-pending-tr-100.png) | — | — |
| DELETION_PENDING | TR | %200 | [PNG](screens/png/deletion-pending-tr-200.png) | [PNG](screens/png/deletion-pending-tr-200-end.png) | [PNG](screens/png/deletion-pending-tr-200-full.png) |
| ACCESS_DISABLED | EN | %100 | [PNG](screens/png/access-disabled-en-100.png) | — | — |
| ACCESS_DISABLED | EN | %200 | [PNG](screens/png/access-disabled-en-200.png) | [PNG](screens/png/access-disabled-en-200-end.png) | [PNG](screens/png/access-disabled-en-200-full.png) |
| ACCESS_DISABLED | TR | %100 | [PNG](screens/png/access-disabled-tr-100.png) | — | — |
| ACCESS_DISABLED | TR | %200 | [PNG](screens/png/access-disabled-tr-200.png) | [PNG](screens/png/access-disabled-tr-200-end.png) | [PNG](screens/png/access-disabled-tr-200-full.png) |

## Kopyalama sonucu

- [EN · Copied](screens/png/access-disabled-en-100-copied.png)
- [TR · Adres kopyalandı.](screens/png/access-disabled-tr-100-copied.png)

`*-end.png`: aynı ekran, metnin sonuna kaydırılmış. `*-full.png`: bütün metni tek dosyada incelemek için uzun belge çıktısı; native ekran boyutu değildir.

Android güvenli alan örneği ve 320 dp kontrolü HTML seçicilerinde; ölçümler `validation.json` içinde.
