---
name: Technical Precision Engine
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#41484b'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#71787c'
  outline-variant: '#c1c7cc'
  surface-tint: '#376476'
  primary: '#003747'
  on-primary: '#ffffff'
  primary-container: '#1f4e5f'
  on-primary-container: '#92bed2'
  inverse-primary: '#a0cde1'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fc'
  on-secondary-container: '#57657a'
  tertiary: '#003554'
  on-tertiary: '#ffffff'
  tertiary-container: '#004d77'
  on-tertiary-container: '#6fbfff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bce9fe'
  primary-fixed-dim: '#a0cde1'
  on-primary-fixed: '#001f29'
  on-primary-fixed-variant: '#1d4c5d'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#cce5ff'
  tertiary-fixed-dim: '#93ccff'
  on-tertiary-fixed: '#001d31'
  on-tertiary-fixed-variant: '#004b73'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '600'
    lineHeight: 44px
    letterSpacing: -0.03em
  headline-xl-mobile:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 34px
    letterSpacing: -0.025em
  headline-lg:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 26px
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: '600'
    lineHeight: 22px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: -0.005em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: '0'
  body-xs:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: 0.005em
  code-md:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: -0.005em
  code-sm:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: '0'
  label-md:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.03em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-desktop: 1.5rem
  margin: 1rem
  margin-tablet: 1.5rem
  margin-desktop: 2rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-lg: 1.25rem
  space-xl: 2rem
---

## Brand & Style

This design system embodies high-density utility, extreme clarity, and focused developer ergonomics. Rooted in modern engineering environments like Linear, Vercel, and GitHub, the interface treats UI as an unobtrusive framework for workflows, system telemetry, and code. 

### Aesthetic Pillars
- **Engineered Restraint**: Every element serves an operational purpose. Decoration is stripped down in favor of typographic rhythm, intentional alignment, and clean surface boundaries.
- **Instrumental Tactility**: Interactive elements feel fast, sharp, and mechanical. Low-latency visual feedback, micro-interactions, and tight bounding boxes evoke high-performance CLI and IDE tools.
- **Calibrated Neutrality**: The interface relies on a cold slate baseline to maximize reading endurance, punctuated by deep navy focal points and strict semantic status indicators.

## Colors

The palette leverages a technical balance: clinical slate surfaces paired with a dense, grounded primary navy (#1F4E5F).

### Palette Architecture
- **Surfaces**:
  - `canvas`: `#F8FAFC` (Slate 50) — Base background for navigation frames and full-window layout canvas.
  - `surface-raised`: `#FFFFFF` — Primary panels, code blocks, tables, cards, and modal dialogs.
  - `surface-subtle`: `#F1F5F9` (Slate 100) — Active selection states, hover fills, inline code chips, and keyboard shortcut housings.
- **Borders & Rules**:
  - `border-subtle`: `#E2E8F0` (Slate 200) — The fundamental structural hairline border across cards, sidebars, and dividers.
  - `border-strong`: `#CBD5E1` (Slate 300) — Interactive bounds, inactive form outlines, and nested table headers.
- **Accents & Roles**:
  - `primary`: `#1F4E5F` — Dominant action surfaces, primary CTA backgrounds, brand touchpoints, active sidebar highlights.
  - `secondary`: `#475569` — Neutral indicators, secondary button labels, icon states.
  - `telemetry-success`: `#059669` (text/icon), `#ECFDF5` (background), `#A7F3D0` (border) — Operational, deployed, healthy.
  - `telemetry-warning`: `#D97706` (text/icon), `#FFFBEB` (background), `#FDE68A` (border) — Degradation, rate-limited, warning.
  - `telemetry-danger`: `#DC2626` (text/icon), `#FEF2F2` (background), `#FECACA` (border) — Build failure, error, destructive action.
  - `telemetry-info`: `#0284C7` (text/icon), `#F0F9FF` (background), `#BAE6FD` (border) — Queued, syncing, informational note.

## Typography

Typography acts as the primary visual scaffold. Headings and interface copy use Inter with optical tracking compensations (negative letter spacing) to ensure compact, crisp display at high densities. JetBrains Mono is standard for metadata, runtime stats, commit SHAs, code diffs, and system tags.

### Implementation Guidelines
- **Numeric Data**: Always employ tabular figures (`font-variant-numeric: tabular-nums;`) across tables, counters, dashboards, and metrics.
- **Code & Labels**: Use `code-sm` inside pill badges for SHA tags, ports, and version numbers. Use `label-sm` with uppercase transforms exclusively for category headings in navigation sidebars and data table headers.

## Layout & Spacing

Layouts follow an asymmetric workbench model: fixed collateral sidebars (tree navigators, project scopes) paired with an elastic fluid content region.

### Grid & Structure
- **Global Canvas**: Fluid shell framed with a standardized 240px or 280px left rail (collapsible to 56px icon mode), a 1px vertical slate boundary, and an auto-spanning main panel.
- **Horizontal Density**: Tables and metrics grids adjust automatically between 1-column (phone/tablet) to 3- or 4-column balanced dashboards (desktop >1200px) with `gutter-desktop` (1.5rem).
- **Rhythm Rules**: Vertical stacks inside views utilize `space-md` (0.75rem) for linked forms and lists, while major structural section separations expand to `space-xl` (2rem).

## Elevation & Depth

This system avoids expressive drop shadows, relying on structural 1px borders, background tone contrast, and subtle ambient shadows for floating layers.

### Stacking Model
- **Level 0 (Flat Ground)**: Background surfaces (`#F8FAFC`) with hairline borders (`#E2E8F0`) defining panel areas. No shadow.
- **Level 1 (Cards, Panel Items)**: `#FFFFFF` fill bounded by a 1px `#E2E8F0` border. A micro-surface highlight gives a crisp edge: `0 1px 2px 0 rgba(15, 23, 42, 0.04)`.
- **Level 2 (Popovers, Dropdowns, Flyouts)**: Elevated floating context: `0 4px 6px -1px rgba(15, 23, 42, 0.07), 0 2px 4px -2px rgba(15, 23, 42, 0.05)`, bounded by 1px `#E2E8F0`.
- **Level 3 (Command Palettes, Modal Dialogs)**: High-altitude focus: `0 20px 25px -5px rgba(15, 23, 42, 0.08), 0 8px 10px -6px rgba(15, 23, 42, 0.04)` over a translucent tinted backdrop blur (`rgba(15, 23, 42, 0.3)` with `backdrop-filter: blur(4px)`).

## Shapes

The interface is defined by refined, tight radii that keep components compact and precise.

### Standard Token Application
- **Input Elements & Buttons**: Standard `0.375rem` (6px) or `0.5rem` (8px, `rounded-lg`) matching developer tool conventions.
- **Container Paneling**: Outer panel boundaries and cards standard at `rounded-lg` (8px). 
- **Keyboard Shortcuts (KBD) & Code Chips**: `0.25rem` (4px, `rounded-sm`).
- **Telemetry Pills & Status Avatars**: Fully rounded (`9999px`) for quick visual scanning.

## Components

### Buttons
- **Primary**: Solid `#1F4E5F` background, white label, 1px transparent border. Hover: `#163946`. Active: `#0F2730`. Focus-visible: 2px offset ring with `#1F4E5F`.
- **Secondary**: `#FFFFFF` background, 1px `#E2E8F0` border, `#1E293B` text. Hover: `#F8FAFC` background, `#CBD5E1` border. Active: `#F1F5F9`.
- **Ghost/Tertiary**: Transparent background, `#475569` text. Hover: `#F1F5F9` background, `#1E293B` text.
- **Destructive**: `#FEF2F2` background, 1px `#FECACA` border, `#DC2626` text. Hover: `#FEE2E2`.

### Inputs & Select Fields
- Base height: 32px (compact) or 36px (default).
- Background: `#FFFFFF`. Border: 1px `#E2E8F0`. Text: `#0F172A`, placeholder `#94A3B8`.
- Focus state: Border transitions to `#1F4E5F` with an ambient glow (`box-shadow: 0 0 0 1px #1F4E5F`).
- Monospaced Input: Supported for API keys, regex filters, and branch names using `JetBrains Mono` at `13px`.

### Status Badges & Chips
- Structure: 20px height, inline-flex, 6px horizontal padding, `rounded-full` or `rounded-sm` (4px) for tags.
- Success: Background `#ECFDF5`, text `#059669`, border 1px `#A7F3D0`. Includes a 6px solid `#10B981` status dot.
- Warning: Background `#FFFBEB`, text `#B45309`, border 1px `#FDE68A`.
- Danger: Background `#FEF2F2`, text `#B91C1C`, border 1px `#FECACA`.

### Cards & Grouped Containers
- Flat `#FFFFFF` canvas encased in a crisp 1px `#E2E8F0` border with an 8px radius.
- Headers are divided from body content using a horizontal 1px hairline border (`#F1F5F9`) with standard `space-md` internal padding.

### Lists & Data Tables
- Table headers: Uppercase `label-sm` in `#64748B`, height 32px, background `#F8FAFC`, bottom border 1px `#E2E8F0`.
- Rows: Height 40px, cell padding `8px 12px`, alternating hover fill `#F8FAFC`. Bottom hairline `#F1F5F9`.
- Monospace metadata cells right-aligned for instant scanning.

### Command Palette (Spotlight K-bar)
- Fixed center overlay, max width 640px.
- Container: `#FFFFFF` surface with Level 3 elevation and 8px radius.
- Search input: 48px height, 16px font size, borderless bottom divider 1px `#E2E8F0`.
- Action items: 36px height, rounded 6px inside list frame, active state `#F1F5F9` with keyboard shortcut badge `#E2E8F0` aligned right.