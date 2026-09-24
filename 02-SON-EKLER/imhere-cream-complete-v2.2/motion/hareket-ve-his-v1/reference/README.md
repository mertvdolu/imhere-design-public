# Flutter referans kontrolü

Yerel SDK: Flutter3.47.3 / Dart3.13.3. `motion_primitives.dart` analizden geçti; eşlik eden testte3 test geçti (yay toleransları, iki OS hareket azaltma bayrağı, onaysız/tekrarlanan/arka plan olayını bastırma).

Tekrar kontrol için iki Dart dosyasını Flutter SDK kullanan ayrı bir test projesinin aynı test dizinine koyup `flutter test test/motion_primitives_test.dart` çalıştırın. `flutter_test` yalnız SDK test aracıdır; üretim uygulamasına yeni paket eklenmez. Ürün reposu/pubspec değiştirilmedi.

Bu testler native animasyonun bütün ekranlara entegre edildiğini veya cihazda60fps çalıştığını kanıtlamaz. İşlevsel tetikleyiciler gerçek domain olaylarına Code tarafından bağlanmalıdır.
