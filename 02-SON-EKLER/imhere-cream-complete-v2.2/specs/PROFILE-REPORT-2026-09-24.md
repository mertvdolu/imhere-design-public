TASARIMCIDAN MANAGERE MESAJ

# Profilden güvenlik — CH-143 güncellemesi

Önceki üst sağ bayrak tasarımı yerine, profilin altında mevcut `safetyTitle` ikincil düğmesi kabul edildi. Backend yoksa gösterilmez. Düğme `safety-profile-menu` açar: Şikâyet / Engelle / Go back. End connection yoktur. Şikâyet onaylandığında engelleme de uygulanır; ayrı soru yoktur.

Kapsam: view-other-visible/hidden ve person-cooldown/pending/connected görünür/gizli varyantları. Kendi profilinde giriş yok. Ayrıntı: [güncel toplu devir](CODE-ALIGNMENT-CH141-143.md). Eski e1f4bbe bayrak + ayrı engelleme akışı bu kararla geçersizdir.
