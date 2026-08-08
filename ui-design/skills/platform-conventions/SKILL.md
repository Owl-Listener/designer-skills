---
name: platform-conventions
description: Design to iOS and Android conventions — what each OS mandates, where they diverge, and when to unify. Use when shipping native apps. For breakpoint adaptation use `responsive-design`; for matching competitor patterns use `jakobs-law` (interaction-design).
---
# Platform Conventions

You are an expert in iOS Human Interface Guidelines and Material Design, and in the trade-offs between platform-native and cross-platform product design.

## What You Do

You identify which UI patterns are platform-mandated conventions, map the meaningful differences between iOS and Android, and help teams decide when to follow each platform vs. when a unified cross-platform design is appropriate.

## Why Platform Conventions Matter

Users spend the vast majority of their time in the OS and its native apps. They build strong muscle memory for navigation, controls, and interaction patterns. When your product departs from platform convention without clear reason, users spend cognitive budget understanding your product rather than using it.

## Key Differences: iOS (HIG) vs. Android (Material Design 3)

### Navigation

| Pattern | iOS | Android |
|---|---|---|
| Back navigation | Swipe right from left edge; back button top-left | System back gesture (swipe from either edge) or predictive back; back arrow in app bar |
| Primary structure | Tab bar at bottom; sidebar on iPad | Navigation bar at bottom or Navigation drawer (hamburger) |
| Navigation history | Stack-based; each tab has its own stack | Single back stack across the app; tabs do not maintain independent history by default |
| Bottom navigation | Up to 5 tabs; no labels required | 3–5 tabs; labels required |

**Design implication**: iOS users expect swiping from the left edge to always go back; reserve that gesture zone. On Android, the system back gesture handles this — in-app swipe-from-left can be used for a drawer without conflicting.

### Controls and Components

| Component | iOS convention | Android (Material 3) convention |
|---|---|---|
| Toggle switch | UISwitch — pill shape, right-aligned in lists | Switch — thumb-and-track, can appear inline or in lists |
| Destructive confirmation | Action sheet (bottom) with red destructive option | Dialog with text buttons; red/error tone for destructive |
| Date/time picker | Wheel picker or calendar inline | Calendar with text input alternative |
| Selection menus | Picker wheel or action sheet | Exposed dropdown or modal bottom sheet |
| Primary button | Filled rectangle, full-width in forms | Filled button (rounded corners by default in M3) |
| Floating action | Not a convention — use contextual buttons | FAB — primary surface action, bottom-right |
| Pull to refresh | Native UIRefreshControl | SwipeRefreshLayout — same gesture, different visual |

### Typography

| Attribute | iOS | Android |
|---|---|---|
| System font | SF Pro (text) / SF Compact (watch) | Roboto / Google Sans |
| Dynamic type | Required — users control text size system-wide | Scalable pixels (sp) — must respect system font scale |
| Type scale | iOS text styles (Large Title, Title 1–3, Body, etc.) | Material type scale (Display, Headline, Title, Body, Label) |

Both platforms require apps to respect the user's system font size preference. Hardcoded point sizes that do not scale are an accessibility failure on both.

### Interaction and Gesture Conventions

| Gesture | iOS behaviour | Android behaviour |
|---|---|---|
| Swipe to delete | Standard in table views | Swipe to dismiss/archive (context-dependent) |
| Long press | Peek / context menu (iOS 13+ context menus) | Contextual action mode; long press to select |
| Pull to refresh | Standard | Standard |
| Pinch to zoom | Standard in maps, images | Standard |
| Back swipe | Reserved — always navigates back | Predictive back gesture; apps can opt in to preview |

### Visual and Iconography

| Area | iOS | Android |
|---|---|---|
| Icon library | SF Symbols (thousands, variable weight, auto-scale) | Material Symbols (rounded, outlined, sharp variants) |
| Corner radius | Larger, "squircle" curves (superellipse) | Moderate — Material 3 uses prominent rounding on components |
| System colours | Dynamic colors that adapt to dark/light automatically | Material You dynamic color — generated from wallpaper |
| Modal presentation | Sheet that slides up from bottom, with grab handle | Bottom sheet (standard or modal) or full-screen dialog |

## Cross-Platform Design Decisions

### When to follow each platform strictly
- Native or near-native apps where platform fluency is a key quality signal (banking, health, utility apps)
- Apps that integrate deeply with OS features (share sheet, widgets, Siri/Google Assistant)
- Apps with a large base of platform-experienced power users

### When a unified design is appropriate
- Products with high feature parity across platforms where design consistency reduces maintenance cost
- Products where cross-device continuity matters (e.g. users switch between iPhone and Android or web)
- B2B tools where users interact primarily with the product's own design system, not OS affordances

### The hybrid approach
Most cross-platform products adopt a middle path: a unified visual and component language, but with platform-specific adaptations for navigation (system-level conventions), system controls, and gesture conflicts. The product looks like itself; it behaves like the OS.

## What Not to Do

- Do not use a bottom tab bar on Android if it uses the gesture navigation that conflicts with a swipe-up action
- Do not suppress the iOS swipe-back gesture — users who trigger it and nothing happens will be confused and trust drops
- Do not use iOS action sheets on Android or Android dialogs on iOS as primary decision patterns
- Do not ignore Dynamic Type / SP scaling on either platform — fixed text sizes are an accessibility failure
- Do not transplant the FAB pattern to iOS without justification — it has no native precedent there

## Best Practices

- Read the current platform guidelines before each major design phase; both iOS HIG and Material 3 update frequently
- Audit native apps on each platform for the interaction you are designing before proposing a solution
- Maintain a component mapping document: what the design system calls a thing, what iOS calls it, what Android calls it
- Test on real devices for each platform — simulator behaviour and gesture handling differ from physical devices
- When in doubt about a platform-specific pattern, use what ships in the OS: it is already tested, already familiar
