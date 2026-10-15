# d0 — durum matrisi

Her durum: EN/TR × %100/%200 × 390×844 / 412×915; 4× opak PNG. `--full` yalnız kaydırılan içerikte. Dar ekran: 320/%200 iOS + Android ölçümü.

| State | Davranış |
|---|---|
| d0-required | Cold-launch minimum-version gate. No back, profile, navigation or dismiss. Update opens configured OS store URL. |
| d0-opening | Store opener pending, spinner plus unchanged Update label; no success claim. Delete-account route remains available. Platform opener completion/failure ends pending state. |
| d0-store-failed | Store opener failed; Update remains retryable. No invented store URL. Delete link opens approved web deletion route. |
