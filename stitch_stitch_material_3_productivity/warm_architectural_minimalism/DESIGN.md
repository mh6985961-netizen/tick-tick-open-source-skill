---
name: Warm Architectural Minimalism
colors:
  surface: '#fcf9f3'
  surface-dim: '#dcdad4'
  surface-bright: '#fcf9f3'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ed'
  surface-container: '#f1eee7'
  surface-container-high: '#ebe8e2'
  surface-container-highest: '#e5e2dc'
  on-surface: '#1c1c18'
  on-surface-variant: '#4a463f'
  inverse-surface: '#31302d'
  inverse-on-surface: '#f3f0ea'
  outline: '#7c766e'
  outline-variant: '#cdc5bc'
  surface-tint: '#615e5a'
  primary: '#040302'
  on-primary: '#ffffff'
  primary-container: '#1f1d1a'
  on-primary-container: '#898580'
  inverse-primary: '#cbc6c1'
  secondary: '#625e56'
  on-secondary: '#ffffff'
  secondary-container: '#e6dfd5'
  on-secondary-container: '#67625a'
  tertiary: '#040301'
  on-tertiary: '#ffffff'
  tertiary-container: '#201d16'
  on-tertiary-container: '#8a847a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e7e1dc'
  primary-fixed-dim: '#cbc6c1'
  on-primary-fixed: '#1d1b18'
  on-primary-fixed-variant: '#494643'
  secondary-fixed: '#e9e1d8'
  secondary-fixed-dim: '#ccc6bc'
  on-secondary-fixed: '#1e1b15'
  on-secondary-fixed-variant: '#4a463f'
  tertiary-fixed: '#e9e1d6'
  tertiary-fixed-dim: '#cdc5ba'
  on-tertiary-fixed: '#1e1b14'
  on-tertiary-fixed-variant: '#4b463e'
  background: '#fcf9f3'
  on-background: '#1c1c18'
  surface-variant: '#e5e2dc'
typography:
  display-lg:
    fontFamily: Newsreader
    fontSize: 56px
    fontWeight: '400'
    lineHeight: 64px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Newsreader
    fontSize: 38px
    fontWeight: '400'
    lineHeight: 44px
    letterSpacing: -0.015em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 36px
    fontWeight: '400'
    lineHeight: 44px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: '400'
    lineHeight: 34px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Newsreader
    fontSize: 26px
    fontWeight: '400'
    lineHeight: 32px
    letterSpacing: -0.005em
  headline-sm:
    fontFamily: Newsreader
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 28px
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Hanken Grotesk
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
  label-lg:
    fontFamily: Hanken Grotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.02em
  label-md:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.04em
  label-sm:
    fontFamily: Hanken Grotesk
    fontSize: 10px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 3rem
  margin-mobile: 1.25rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.75rem
  space-xl: 3rem
---

## Brand & Style

This design system embodies the quiet discipline of Japanese paper craft (*washi*), lime-washed plaster, and honed warm stone. The aesthetic is strictly neutral, quiet, and deliberate. It avoids decorative ornament, high-energy chromatics, or synthetic neon highlights.

### Brand Personality & Emotional Response
- **Serenity & Stillness:** Interfaces feel like quiet gallery halls or tactile print publications, creating focus and lowering cognitive fatigue.
- **Architectural Rigor:** Hierarchy is conveyed strictly through spatial distribution, proportional scaling, and deliberate hairline dividers rather than saturated color signals.
- **Tactile Materiality:** Evokes porous mineral textures, untreated parchment, and matte limestone through nuanced off-whites and tinted charcoals.

### Design Movement
**Minimalist Editorial & Tactile Materiality:** Characterized by generous negative space, uncompromising typography pairings, fine architectural borders, and deliberate absence of all chromatic hues.

## Colors

The palette is strictly monochromatic and warm-toned. No chromatic accents (blues, greens, reds, yellows, purples) exist within the system. State changes, focus boundaries, and hierarchy rely solely on shifts between parchment, plaster, stone, and carbon tones.

### Palette Roles
- **Primary (`#1F1D1A` - Carbon Charcoal):** High-contrast editorial display headings, primary interactive surfaces, and key focus rings.
- **Secondary (`#767169` - Honed Taupe):** Secondary copy, captions, structural outlines, and inactive control icons.
- **Tertiary (`#B8B1A6` - Weathered Plaster):** Low-contrast borders, active container tints, disabled states, and hairline rules.
- **Neutral (`#EFECE6` - Warm Limestone):** Background canvas foundation, container fills, and elevated sheet backdrops.

### Canvas & Surface Hierarchy
- **Canvas Base:** `#F9F8F5` (Japanese Raw Silk / Off-White)
- **Surface Level 1 (Cards, Sheets):** `#F3F1EC` (Soft Washi Parchment)
- **Surface Level 2 (Inputs, Well Insets):** `#EBE8E1` (Lime Plaster)
- **Hairline Border Rule:** `#DED9CF` (Muted Sandstone Grain)

## Typography

The type system creates an intentional tension between an organic, literary serif (**Newsreader**) and a razor-sharp, balanced modernist sans-serif (**Hanken Grotesk**).

### Editorial Rules
- **Editorial Headings:** Use `Newsreader` in standard regular weight (`400`) or optical medium (`500`). Avoid heavy bold weights to preserve the delicate editorial character of Japanese book typography.
- **UI & Micro-copy:** Use `Hanken Grotesk` across all functional interfaces, form controls, tabular data, and navigational elements.
- **Letter Spacing:** Small labels (`label-sm`, `label-md`) utilize expanded letter spacing to ensure maximum clarity on textured, muted backgrounds.

## Layout & Spacing

The layout is grounded in a 12-column responsive fluid grid with generous margins reminiscent of wide book margins and Japanese *Ma* (negative space).

### Grid & Breakpoints
- **Desktop (1200px+):** 12 columns, `margin: 3rem`, `gutter: 1.5rem`. Maximum content container width capped at `1440px`.
- **Tablet (768px – 1199px):** 8 columns, `margin: 2rem`, `gutter: 1.25rem`.
- **Mobile (< 768px):** 4 columns, `margin: 1.25rem`, `gutter: 1rem`.

### Spatial Rhythm
Vertical rhythm follows strict multiples of `0.25rem` (4px base unit). Content groups should rely on expansive `space-lg` and `space-xl` gaps rather than card container boxing to organize thought and hierarchy.

## Elevation & Depth

This system avoids synthetic drop shadows, colored halos, and heavy dimensional skeuomorphism. Depth is produced strictly via surface tonality and hairline mineral rules.

### Tonal Stratification
- **Ground Floor (Base Canvas):** `#F9F8F5`.
- **Sub-surface (Inset wells, code blocks, form troughs):** `#EBE8E1`.
- **Raised Planes (Cards, drawers, modals):** `#F3F1EC`.

### Low-Contrast Outlines & Hairlines
- Surface boundaries are demarcated by `1px` solid hairlines tinted to `#DED9CF` (warm sandstone grain) or `#E3DFD7`.
- **No Drop Shadows:** Elevated overlays (popovers, flyouts, dialogs) achieve separation through a crisp `1px` border in `#B8B1A6` and an ambient, whisper-light warm occlusion: `0 8px 32px rgba(31, 29, 26, 0.05)`.

## Shapes

The shape system employs minimal, architectural softening. Corners are neither pin-sharp brutalist nor bubbly organic pills; they resemble precision-cut stone blocks with gently softened bevels.

### Shape Scale
- **Base Elements (Buttons, Inputs, Badges):** `0.25rem` (`4px`).
- **Cards, Sheets, & Panels (`rounded-lg`):** `0.5rem` (`8px`).
- **Full Modals & Floating Drawers (`rounded-xl`):** `0.75rem` (`12px`).
- Avoid pill radii (`rounded-full`) except for avatar masks and minimal circular icon toggles.

## Components

### Buttons
- **Primary:** Solid `#1F1D1A` background, `#F9F8F5` text, subtle `0.25rem` radius. On hover, background shifts to `#36332E`. Focus ring is a clean `1px` offset in `#1F1D1A`.
- **Secondary:** Transparent background, `1px` border in `#767169`, text in `#1F1D1A`. On hover, background transitions to `#EBE8E1`.
- **Ghost:** Borderless, text in `#767169`. On hover, text becomes `#1F1D1A` with a background fill of `#F3F1EC`.

### Input Fields & Textareas
- **Default:** Background fill `#EBE8E1`, `1px` border in `#DED9CF`, text in `#1F1D1A`, placeholder in `#767169`.
- **Focus:** Border shifts directly to `#1F1D1A` with no colored blur ring.

### Checkboxes & Radio Buttons
- **Unchecked:** `1px` outline in `#767169`, transparent background.
- **Checked:** Solid `#1F1D1A` fill with a `#F9F8F5` check or inner dot indicator.

### Chips & Tags
- Compact height (`24px` to `28px`), `0.25rem` corner radius.
- Background `#EBE8E1`, hairline border in `#DED9CF`, typography set in `label-sm` uppercase with expanded letter-spacing in `#767169`.

### Cards & Grouping Containers
- Solid background in `#F3F1EC`, edged with a `1px` hairline in `#DED9CF`.
- Padding strictly governed by `space-lg` (`1.75rem`) to maintain generous editorial breathing room.

### Dividers & Rules
- Minimal structural dividers use `1px` solid `#DED9CF`. For section breaks within long-form editorial views, center a solitary typographic bullet (`•`) in `#B8B1A6`.