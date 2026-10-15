# gecis — durum matrisi

Her durum: EN/TR × %100/%200 × 390×844 / 412×915; 4× opak PNG. `--full` yalnız kaydırılan içerikte. Dar ekran: 320/%200 iOS + Android ölçümü.

| State | Davranış |
|---|---|
| migration-intro | No inferred choice. Not visible in discovery until community selection. |
| migration-community | Reuses registration selection component. Initial selection ends previous check-in; no rate-limit cost. LinkedIn step only if stored. |
| migration-linkedin-everyone | Shown only when linkedinTransitionNeeded=true. FIRST uses v15LinkedinBody. Dismiss keeps the stored setting; first-transition fixture is Everyone. Failure restores the stored setting and stays here. Group legend is visually hidden but accessible. |
| migration-linkedin-connections | Shown only when linkedinTransitionNeeded=true. FIRST uses v15LinkedinBody. Dismiss keeps the stored setting; first-transition fixture is Everyone. Failure restores the stored setting and stays here. Group legend is visually hidden but accessible. |
| migration-linkedin-nobody | Shown only when linkedinTransitionNeeded=true. FIRST uses v15LinkedinBody. Dismiss keeps the stored setting; first-transition fixture is Everyone. Failure restores the stored setting and stays here. Group legend is visually hidden but accessible. |
| migration-linkedin-saving | Shown only when linkedinTransitionNeeded=true. FIRST uses v15LinkedinBody. Dismiss keeps the stored setting; first-transition fixture is Everyone. Failure restores the stored setting and stays here. Group legend is visually hidden but accessible. |
| migration-linkedin-failed | Shown only when linkedinTransitionNeeded=true. FIRST uses v15LinkedinBody. Dismiss keeps the stored setting; first-transition fixture is Everyone. Failure restores the stored setting and stays here. Group legend is visually hidden but accessible. |
| migration-linkedin-offline | Shown only when linkedinTransitionNeeded=true. FIRST uses v15LinkedinBody. Dismiss keeps the stored setting; first-transition fixture is Everyone. Failure restores the stored setting and stays here. Group legend is visually hidden but accessible. |
| migration-occupation | Optional one-time invitation. Equal button treatment. Existing free text is not mapped automatically. |
| migration-offline | Network failure keeps route and avoids inferred membership. |
| migration-linkedin-changed-default | Standalone LINK_CHANGED review, no intro/community steps. Stored setting Nobody; other-selection example Connections. Dismiss and failure retain stored Nobody; success only after server ack returns to the existing app. No transition if linkedinTransitionNeeded=false. |
| migration-linkedin-changed-other | Standalone LINK_CHANGED review, no intro/community steps. Stored setting Nobody; other-selection example Connections. Dismiss and failure retain stored Nobody; success only after server ack returns to the existing app. No transition if linkedinTransitionNeeded=false. |
| migration-linkedin-changed-saving | Standalone LINK_CHANGED review, no intro/community steps. Stored setting Nobody; other-selection example Connections. Dismiss and failure retain stored Nobody; success only after server ack returns to the existing app. No transition if linkedinTransitionNeeded=false. |
| migration-linkedin-changed-failed | Standalone LINK_CHANGED review, no intro/community steps. Stored setting Nobody; other-selection example Connections. Dismiss and failure retain stored Nobody; success only after server ack returns to the existing app. No transition if linkedinTransitionNeeded=false. |
| migration-linkedin-changed-offline | Standalone LINK_CHANGED review, no intro/community steps. Stored setting Nobody; other-selection example Connections. Dismiss and failure retain stored Nobody; success only after server ack returns to the existing app. No transition if linkedinTransitionNeeded=false. |
