# Geist — gömülü Flutter asset

Resmî kaynak: https://github.com/vercel/geist-font
Sabit kaynak commit: 10dc7658f13c38a474cde201bb09a4617267545b. Kaynak dosyalar değiştirilmedi; SHA-256 ve Git blob doğrulamaları SOURCE.json içinde. Lisans OFL.txt olarak aynen eklendi.

Geist-Regular.ttf → 400; Geist-Medium.ttf → 500; Geist-SemiBold.ttf → 600.

Bu dosyalar paketle birlikte gelen çevrimdışı Geist kaynaklarıdır. Entegrasyonda mevcut font kayıtlarını koruyun; 400/500/600 ağırlıklarını yukarıdaki dosyalarla eşleyin. Tema ölçüleri tokens/theme.tokens.json içinde tanımlıdır. Bu teslim native projeyi değiştirmez ve ağdan font indirme gerektirmez.

OFL.txt uygulama asset paketine de dahil edilir. Uygulamanın lisans görünümünde göstermek için Flutter LicenseRegistry kaydı aşağıdaki örnekle eklenebilir; uygulama başlangıcında bir kez çağırın:

```dart
LicenseRegistry.addLicense(() async* {
  yield LicenseEntryWithLineBreaks(
    ['Geist'],
    await rootBundle.loadString('fonts/OFL.txt'),
  );
});
```

İlgili importlar: package:flutter/foundation.dart ve package:flutter/services.dart. Lisans yüklemesi de yerel assetten yapılır.
