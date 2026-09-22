# Geist — gömülü Flutter asset

Resmî kaynak: https://github.com/vercel/geist-font
Sabit kaynak commit: 10dc7658f13c38a474cde201bb09a4617267545b. Kaynak dosyalar değiştirilmedi; SHA-256 ve Git blob doğrulamaları SOURCE.json içinde. Lisans OFL.txt olarak aynen eklendi.

Geist-Regular.ttf → 400; Geist-Medium.ttf → 500; Geist-SemiBold.ttf → 600.

fonts/ klasörünü Flutter proje köküne kopyalayın. flutter/pubspec-fonts.yaml parçasını mevcut pubspec.yaml içindeki flutter bölümüne birleştirin; ikinci flutter bölümü oluşturmayın. Var olan asset/font kayıtlarını koruyun. ThemeData zaten Geist ailesini kullanıyor. Runtime font indirme, google_fonts veya ağ çağrısı eklemeyin.

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
