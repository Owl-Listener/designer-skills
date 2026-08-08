---
name: localization-design
description: Design for multiple languages, writing directions, and cultural contexts — text expansion, RTL mirroring, and locale formats. Use when shipping beyond one locale. For the words themselves, use `ux-writing` (designer-toolkit).
---
# Localization Design
You are an expert in designing UI that works across languages, scripts, and cultures without requiring per-locale redesigns.
## What You Do
You apply localization-aware design principles to ensure components, layouts, and content can be adapted to any target locale without breaking — and that cultural differences in color, iconography, and conventions are accounted for.
## Text Expansion
The most common localization failure. English is compact; most target languages are longer:
| Language | Typical expansion vs English |
|---|---|
| German | +20–35% |
| French | +15–25% |
| Finnish | +30–40% |
| Arabic (translated) | −20–30% (but RTL and different script) |
| Japanese/Chinese | Often shorter, but very different typographic rules |
**Design for text expansion:**
- Never size containers to fit English copy — use flexible heights and widths
- Test layouts with German or Finnish translations as worst-case proxies before other locales exist
- Truncation with ellipsis is an acceptable last resort, but provide full text via tooltip/expand
- Buttons: use min-width, not fixed width; allow wrapping for extreme cases in narrow contexts
- Navigation labels: test all nav items together at 130% length to validate menu doesn't break
## RTL (Right-to-Left) Support
Arabic, Hebrew, Persian, and Urdu read right-to-left. The entire layout mirrors:
- **Content flow**: text, lists, and reading order reverse
- **Layout mirroring**: sidebars, navigation, and content areas flip; left margin becomes right margin
- **Icon mirroring**: directional icons (arrows, chevrons, back button) mirror; non-directional icons (camera, settings) do not
- **CSS logical properties**: use `margin-inline-start` instead of `margin-left`; `padding-block-end` instead of `padding-bottom` — these flip automatically with `dir="rtl"`
- **Text alignment**: use `text-align: start` not `text-align: left`
- **Numbers**: numerals remain LTR within RTL text in most contexts; don't mirror number displays
**What does not mirror in RTL:**
- Logos and brand marks
- Clocks and time displays
- Mathematical notation
- Images and illustrations (usually — context-dependent)
- Video player controls (debated; mirror directional but not play/pause)
## Typography for Non-Latin Scripts
- Arabic and Hebrew: cursive scripts with letter-joining rules; larger minimum font sizes (16px+) for readability
- CJK (Chinese, Japanese, Korean): square characters; different optimal line-height and letter-spacing than Latin; different measure rules
- Devanagari (Hindi) and other Indic scripts: complex ligatures; test with font stacks that include proper fallbacks
- Never fake-bold or fake-italic non-Latin scripts — use genuine weights from the font family
## Cultural Considerations
### Color
Color meaning varies significantly by culture:
| Color | Western association | Example alternative association |
|---|---|---|
| Red | Danger, error | Luck/prosperity (China), mourning (South Africa) |
| White | Clean, minimal | Mourning (many East Asian cultures) |
| Green | Success, go | Unfaithfulness (China), danger (some Middle Eastern contexts) |
- Don't rely on color alone for semantic meaning (this is also an accessibility requirement)
- Test color choices with cultural consultants for high-stakes or global products
### Iconography
- Hand gestures (thumbs up, OK sign) have offensive meanings in some cultures — avoid
- Postal and civic icons (mailbox, house, phone) vary by region — use abstract or universally-recognizable forms
- Religious and food symbolism is culturally loaded — avoid unless necessary and tested
### Date, Time, and Number Formats
- Date formats vary: MM/DD/YYYY (US), DD/MM/YYYY (UK/EU), YYYY-MM-DD (ISO)
- Use locale-aware formatting via `Intl.DateTimeFormat` / equivalent
- Currency: symbol position, decimal separator, thousands separator all vary
- Addresses: field order, required fields, and format vary significantly — use a locale-aware address form library
## Design System Implications
- All spacing, sizing, and layout should use logical CSS properties
- Text containers must be flexible-height and flexible-width
- Design token names should be semantic, not directional ("start" not "left")
- Components should be tested with at least one RTL locale and one long-expansion locale before being added to the system
- Provide localization guidance in component documentation: "This component has been tested with Arabic (RTL) and German (text expansion)"
## Best Practices
- Design with localization in mind from day one — retrofitting RTL support into a left-biased layout is expensive
- Create a pseudo-localization test string (replaces characters with extended lookalikes) to test expansion and special character handling before translations exist
- Partner with in-market users or cultural consultants, not just translators — translation handles words; localization handles meaning
- Audit icon and illustration libraries for cultural neutrality before internationalizing
