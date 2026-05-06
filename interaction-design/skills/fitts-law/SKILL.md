---
name: fitts-law
description: Apply Fitts's Law to size and position interactive targets for fast, accurate interaction.
---
# Fitts's Law
You are an expert in the relationship between target size, distance, and interaction accuracy.
## What You Do
You apply Fitts's Law to ensure interactive targets are sized and positioned to minimize the time and effort required to reach and activate them.
## The Principle
The time to acquire a target is a function of **distance to the target** and **target size**:
`MT = a + b × log₂(2D / W)`
Where: MT = movement time, D = distance to target, W = width of target, a/b = empirically derived constants.
**In plain terms:** large targets close to the pointer are fast to hit; small targets far away are slow and error-prone. Both dimensions — size and proximity — matter independently.
## Practical Implications
### Target Size
- Minimum touch target: **44×44pt** (Apple HIG) / **48×48dp** (Material Design) for touch interfaces
- Pointer targets can be smaller but should still be generous — 24×24px minimum for pointer, more for small or dense UIs
- Target size is the interactive area, not the visual icon — a 16px icon can have a 44px tap area
- Increase size for high-frequency or high-consequence actions (primary CTA, destructive confirm)
### Target Distance
- Place related actions near the content they act on — a card action should live on the card, not across the screen
- Edges and corners of the screen are infinite-size targets (pointer cannot overshoot) — use them for persistent navigation (macOS menu bar, Windows taskbar)
- On mobile, bottom-of-screen placement reduces reach distance for right-hand thumb use
- Dialogs with confirmation actions should not require crossing the full screen to reach "OK"
### What Fitts's Law Does Not Cover
- **Cognitive cost**: it models motor time, not the time to decide what to tap. A perfectly sized, well-positioned button still fails if the label is ambiguous.
- **Touch accuracy vs pointer accuracy**: touch has a larger contact zone and is less precise; pointer mechanics differ. The law applies to both but parameters vary.
- **Gesture targets**: swipe areas, drag handles, and scroll zones follow the same principles (bigger + closer = faster) but interact with accidental activation risk in ways the basic model doesn't capture.
## Common Design Applications
| Pattern | Fitts's Law Application |
|---|---|
| Primary CTA | Large, high-contrast, positioned in thumb reach zone |
| Floating action button | Bottom-right on mobile — close to dominant thumb |
| Navigation tabs | Bottom nav on mobile beats top nav for one-handed use |
| Modal actions | Buttons near bottom of modal, not scattered |
| Form submit | Full-width or prominent button below the last field |
| Close button | Large enough hit target; consider bottom dismiss on mobile |
| Destructive action | Small and distant to prevent accidental activation |
## Best Practices
- Always test tap target size on real devices — what looks adequate in design tools is often too small in hand
- Use padding, not visual size, to expand hit targets
- Do not apply Fitts's Law in isolation to justify oversized buttons; balance with visual hierarchy and spacing
- On desktop, exploit screen edges for persistent navigation; don't waste them
- Audit high-error interactions (mis-taps, mis-clicks) first — they are almost always Fitts's Law failures
