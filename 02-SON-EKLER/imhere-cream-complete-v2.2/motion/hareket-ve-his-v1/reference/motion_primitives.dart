// Design reference, not application integration. Flutter SDK only.
import 'dart:math' as math;
import 'dart:ui' as ui;
import 'package:flutter/material.dart';
import 'package:flutter/physics.dart';
import 'package:flutter/services.dart';

abstract final class InkMotion {
  static const quick = Duration(milliseconds: 150);
  static const reducedDuration = Duration(milliseconds: 150);
  static const standard = SpringDescription(
    mass: 1, stiffness: 322.27279677026473, damping: 32.313524436923586,
  );
  static const expressive = SpringDescription(
    mass: 1, stiffness: 194.9551486634935, damping: 20.943951023931955,
  );
  static const tolerance = Tolerance(distance: .001, velocity: .01);

  // Re-evaluate on didChangeAccessibilityFeatures and MediaQuery changes.
  // No one-time cached setting: a user may enable reduced motion mid-flight.
  static bool reduced(BuildContext context) {
    final flags = ui.PlatformDispatcher.instance.accessibilityFeatures;
    return reduceFlags(
      iosReduce: flags.reduceMotion,
      disableAnimations: flags.disableAnimations,
      mediaQueryDisable: MediaQuery.disableAnimationsOf(context),
    );
  }
  static bool reduceFlags({
    required bool iosReduce,
    required bool disableAnimations,
    required bool mediaQueryDisable,
  }) => iosReduce || disableAnimations || mediaQueryDisable;

  static SpringSimulation spring({bool expressiveMotion = false,
    double position = 0, double target = 1, double velocity = 0}) {
    return SpringSimulation(expressiveMotion ? expressive : standard,
      position, target, velocity, tolerance: tolerance);
  }
  // AnimationController.animateWith(spring(...)); opacity is separately clamped.
  // With reduced motion: skip this simulation, use a 150ms opacity transition.
  static Duration itemDelay(int visibleNewItemIndex, {required bool reduced}) {
    if (reduced || visibleNewItemIndex < 0 || visibleNewItemIndex >= 6) {
      return Duration.zero;
    }
    return Duration(milliseconds: visibleNewItemIndex * 40);
  }
}

// Own this ledger outside rebuilds. Use existing operation/message/connection
// identity, never a generated timestamp. Lifetime is the active presentation
// session; dispose with it. Persisted events must not replay on route reentry.
class ConfirmedMotionEvents {
  final Set<String> _seen = <String>{};
  bool claim(String existingEventId, {required bool confirmed,
    required bool foreground, required bool newlyCommitted}) {
    if (!confirmed || !newlyCommitted || existingEventId.isEmpty) return false;
    // Mark even when backgrounded so there is no catch-up animation/haptic.
    if (!_seen.add(existingEventId)) return false;
    return foreground;
  }
}

abstract final class InkHaptics {
  static Future<void> selection() => HapticFeedback.selectionClick();
  static Future<void> success() => HapticFeedback.lightImpact();
  static Future<void> error() => HapticFeedback.mediumImpact();
  // Call only from committed event/input handling, never paint/build.
  // Hardware timing and user system settings remain platform-controlled.
}

class PresenceBoundaryPainter extends CustomPainter {
  PresenceBoundaryPainter({required this.elapsedMs, required this.activeConfirmed,
    required this.reduced, this.ink = const Color(0xFF191A16)});
  final double elapsedMs;
  final bool activeConfirmed;
  final bool reduced;
  final Color ink;
  @override
  void paint(Canvas canvas, Size size) {
    if (!activeConfirmed || size.isEmpty) return;
    final rect = Offset.zero & size;
    canvas.save();
    canvas.clipRect(rect);
    void contour(double inset, double opacity) {
      final paint = Paint()..color = ink.withValues(alpha: opacity.clamp(0, .12))
        ..style = PaintingStyle.stroke..strokeWidth = 1.8;
      canvas.drawRRect(RRect.fromRectAndRadius(rect.deflate(inset + .9),
        const Radius.circular(16)), paint);
    }
    if (reduced) {
      contour(0, .06); // Static boundary. No personal/location marker.
    } else if (elapsedMs < 1200) {
      for (final start in <double>[0, 240]) {
        final dt = elapsedMs - start;
        if (dt < 0 || dt >= 960) continue;
        final p = InkMotion.spring(expressiveMotion: true).x(dt / 1000).clamp(0, 1);
        contour(size.shortestSide * .1 * p, .12 * (1 - dt / 960));
      }
    } else {
      contour(0, .06 - .02 * math.cos(2 * math.pi * (elapsedMs - 1200) / 4000));
    }
    canvas.restore();
  }
  @override
  bool shouldRepaint(PresenceBoundaryPainter old) => old.elapsedMs != elapsedMs ||
    old.activeConfirmed != activeConfirmed || old.reduced != reduced || old.ink != ink;
}
// Wrap decorative painters in IgnorePointer and ExcludeSemantics.
// Stop input cancels loops immediately. Confirmed stop may fade a non-sensitive
// boundary decoration for150ms; never retain map data or claim physical deletion.
