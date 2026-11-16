---
name: Monochrome Minimalist
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#45464c'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#575e70'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#141b2b'
  on-primary-container: '#7d8497'
  inverse-primary: '#c0c6db'
  secondary: '#555f6d'
  on-secondary: '#ffffff'
  secondary-container: '#d6e0f1'
  on-secondary-container: '#596372'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#151c25'
  on-tertiary-container: '#7d8490'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce2f7'
  primary-fixed-dim: '#c0c6db'
  on-primary-fixed: '#141b2b'
  on-primary-fixed-variant: '#404758'
  secondary-fixed: '#d9e3f4'
  secondary-fixed-dim: '#bdc7d8'
  on-secondary-fixed: '#121c28'
  on-secondary-fixed-variant: '#3e4755'
  tertiary-fixed: '#dce3f0'
  tertiary-fixed-dim: '#c0c7d3'
  on-tertiary-fixed: '#151c25'
  on-tertiary-fixed-variant: '#404752'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-xl:
    fontFamily: Geist
    fontSize: 56px
    fontWeight: '700'
    lineHeight: 64px
    letterSpacing: -0.04em
  display-xl-mobile:
    fontFamily: Geist
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.03em
  headline-lg:
    fontFamily: Geist
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
    letterSpacing: -0.03em
  headline-lg-mobile:
    fontFamily: Geist
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Geist
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: Geist
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.015em
  title-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
    letterSpacing: -0.01em
  body-md:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: -0.005em
  body-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0em
  label-lg:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
    letterSpacing: 0.02em
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.04em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.06em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-sm: 1rem
  gutter-lg: 2rem
  margin: 2rem
  margin-sm: 1rem
  margin-lg: 4rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system embodies austere precision, clinical clarity, and editorial rigor. It rejects decorative ornamentation, skeuomorphism, and extraneous visual weight to deliver an interface of distilled architectural purity.

The brand personality is intellectual, discerning, authoritative, and direct. The target audience comprises professionals, developers, designers, and thinkers who demand frictionless utility, rapid comprehension, and an uncompromising aesthetic standard. The interface evokes a feeling of sharp focus, structural integrity, and modern sophistication—comparable to high-end architectural monographs or precision measurement instruments.

The visual direction pairs extreme Swiss Modernist discipline with hyper-refined digital minimalism. Contrast is maximized to heighten legibility, negative space acts as an active structural element, and hairline dividers create geometric cadence without heavy visual drag.

## Colors

The color palette is strictly achromatic and cool-toned. Warm whites, cream, beige, and yellow-undertoned ivories are entirely prohibited. The background is unyielding, pure clinical white (`#ffffff`). Contrast is calibrated for AAA accessibility against pure charcoal and obsidian surfaces.

- **Primary (`#111827`)**: Deep rich charcoal. Applied to primary CTAs, active indicators, high-emphasis icons, and top-tier headers. Pure black (`#000000`) is reserved for display-level typographic punch.
- **Secondary (`#4b5563`)**: Cool graphite slate. Used for secondary body text, metadata, subtle active indicators, and secondary button borders.
- **Tertiary (`#9ca3af`)**: Neutral ash. Reserved for placeholder text, disabled UI states, and non-interactive iconography.
- **Neutral Surface Baseline (`#ffffff`)**: Absolute pure white. Used across primary canvases, elevated modal dialogs, and card surfaces.
- **Structural Outlines (`#e5e7eb` and `#f3f4f6`)**: Cool-grey hairlines providing crisp boundary definition without visual density.

## Typography

Typography relies on a dual-engine typographic setup: **Geist** for crisp, geometric, neo-grotesque structural typography, and **JetBrains Mono** for technical micro-labels, meta information, badges, and numerical readouts.

Tight negative letter-spacing on display headlines produces an editorial, publication-grade tone. Body copy maintains strict line-height hygiene (`1.5` to `1.6` ratio) to guarantee effortless scanning against pure `#ffffff` canvases. Labels and technical data points utilize uppercase monospaced styling with positive tracking to construct visual hierarchy without introducing secondary accent hues.

## Layout & Spacing

The layout model is anchored on an 8pt spatial grid deployed through a responsive 12-column layout on desktop (breakpoint `1024px+`), an 8-column layout on tablet (`768px - 1023px`), and a 4-column layout on mobile (`<768px`).

Negative space is utilized generously to isolate content nodes and define grouping. Rather than relying on background shading shifts, structure is articulated through strict alignment, hairline dividers (`1px solid #e5e7eb`), and generous white channels (`margin-lg`, `space-xl`).

Containers stay pinned to fixed max-widths on ultra-wide screens (`1280px` or `1440px`) to prevent excessive line lengths and maintain an editorial composition. Grid gaps collapse from `gutter-lg` on wide screens to `gutter-sm` on mobile viewports.

## Elevation & Depth

This design system avoids colored shadows, soft drop shadows, and blurred neomorphic layers. Elevation is flat and architectural:

1. **Ground Zero (Canvas)**: Pristine `#ffffff` base plane.
2. **Structural Delineation (Hairline System)**: Separation between modules is achieved entirely via `1px solid #e5e7eb` or `#f3f4f6` rules.
3. **Elevated Overlays (Modals, Popovers, Drawers)**: Retain pure `#ffffff` fill, paired with a razor-thin border (`1px solid #111827` or `1px solid #e5e7eb`) and an ultra-subtle, non-directional shadow: `0 8px 30px rgba(0, 0, 0, 0.06)`.
4. **Modal Backdrops**: Solid black at 40% opacity (`rgba(0, 0, 0, 0.40)`) with `backdrop-filter: blur(2px)` to maintain high contrast behind active sheets.

## Shapes

The shape vocabulary is strictly disciplined and architectural, using a level `1` (Soft) profile. 

- Micro-elements (tags, buttons, inputs): `0.25rem` (4px).
- Structural containers (cards, modals, dropdown panels): `0.5rem` (8px).
- Large viewports or hero panels: `0.75rem` (12px).

Rounded pill shapes and circular UI wrappers are prohibited, except for absolute circular status dots or user avatars. Sharp internal corners paired with subtle external radii preserve a balance between precision engineering and contemporary software design.

## Components

### Buttons
- **Primary**: Solid charcoal `#111827` background, pure white `#ffffff` text, 4px border radius. Hover state transitions to `#000000`. Active state applies `scale(0.99)`.
- **Secondary**: Pure `#ffffff` background with a crisp `1px solid #e5e7eb` border, `#111827` text. Hover state shifts border to `#111827` and background to `#f9fafb`.
- **Ghost**: Background transparent, `#111827` text. Hover state reveals `#f3f4f6` background.
- Padding: `0.5rem 1rem` for standard, `0.25rem 0.75rem` for compact. Typography set to `Geist Medium 13px`.

### Inputs & Text Areas
- Pure `#ffffff` fill, `1px solid #e5e7eb` perimeter border, 4px radius.
- Text: `#111827`. Placeholder: `#9ca3af`.
- Focus state: Border color snaps directly to `#111827` with a matching `1px` crisp inner outline (`box-shadow: 0 0 0 1px #111827`). Never use blue or colored glow halos.

### Cards & Panels
- Pure `#ffffff` background, bounded by `1px solid #e5e7eb`. No default shadow.
- Hoverable cards transition border to `#9ca3af` with zero vertical elevation shift.
- Internal padding adheres strictly to `space-lg` (`1.5rem`).

### Chips, Tags & Badges
- Background `#f9fafb` or `#ffffff`, enclosed in `1px solid #e5e7eb`.
- Monospaced typography via `JetBrains Mono` (`label-md` or `label-sm`), text color `#4b5563`.
- Active or selected chips shift background to `#111827`, text and border to `#111827`.

### Selection Controls (Checkboxes & Radios)
- Checkboxes: 16px square, 3px border radius, `1px solid #9ca3af`. Checked state fills `#111827` with a pure `#ffffff` check icon.
- Radios: 16px circle, `1px solid #9ca3af`. Checked state displays a solid `#111827` center dot (8px diameter).

### Lists & Data Tables
- Header row: `label-sm` in `JetBrains Mono`, tracking expanded, text `#6b7280`, bottom border `1px solid #e5e7eb`.
- Rows: Separated by `1px solid #f3f4f6`. Zero alternating zebra striping; visual separation relies on hover highlighting with `#f9fafb`.
- Cells: `body-md` in `Geist`, vertical padding `space-sm` to `space-md`.