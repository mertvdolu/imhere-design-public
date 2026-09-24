import 'package:flutter_test/flutter_test.dart';
import 'motion_primitives.dart';
void main() {
  test('spring coefficients reach tolerance at documented frame', () {
    final standard = InkMotion.spring();
    final expressive = InkMotion.spring(expressiveMotion: true);
    expect(standard.x(29/60), closeTo(1, .001));
    expect(standard.dx(29/60).abs(), lessThan(.01));
    expect(expressive.x(39/60), closeTo(1, .001));
    expect(expressive.dx(39/60).abs(), lessThan(.01));
    expect(standard.x(0), 0);
    expect(expressive.x(0), 0);
  });
  test('iOS and Android reduction independently disable spatial effects', () {
    for (var mask=0;mask<8;mask++) {
      expect(InkMotion.reduceFlags(iosReduce: mask&1!=0,
        disableAnimations: mask&2!=0, mediaQueryDisable: mask&4!=0), mask!=0);
    }
    expect(InkMotion.itemDelay(5,reduced:false).inMilliseconds, 200);
    expect(InkMotion.itemDelay(6,reduced:false).inMilliseconds, 0);
    expect(InkMotion.itemDelay(5,reduced:true).inMilliseconds, 0);
  });
  test('pending, replay, restored and background events cannot celebrate', () {
    final events=ConfirmedMotionEvents();
    expect(events.claim('a',confirmed:false,foreground:true,newlyCommitted:true),false);
    expect(events.claim('a',confirmed:true,foreground:true,newlyCommitted:true),true);
    expect(events.claim('a',confirmed:true,foreground:true,newlyCommitted:true),false);
    expect(events.claim('b',confirmed:true,foreground:false,newlyCommitted:true),false);
    expect(events.claim('b',confirmed:true,foreground:true,newlyCommitted:true),false);
    expect(events.claim('c',confirmed:true,foreground:true,newlyCommitted:false),false);
  });
}
