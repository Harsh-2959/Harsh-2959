# Profile Updates (apply to the existing GitHub profile files)

Project: animated GitHub profile README (SVG files + README.md). Make these changes to the files already open. Do not redo parts that are not listed.

## 1. Palette (replaces the current cyan / violet / pink aurora)
| Role | Name | Hex | Share |
|---|---|---|---|
| Base | Deep Atlas Navy | `#0E1D61` | ~60% (card backgrounds) |
| Text | Ivory | `#E8E0D2` | ~30% (headings, body text, borders) |
| Accent | Gold | `#B89A5A` | ~10% (dividers, icons, key numbers, highlights) |

- Inner panels and chips: a slightly lighter navy `#162A7E`.
- Muted text: ivory at about 70% opacity.
- Gold is **never** used for small text on ivory (contrast is only about 2:1). Gold on navy is fine (about 5.7:1).
- Ivory on navy is about 11.7:1.

## 2. Scope
- Apply the palette to **everything** (hero, cards, tech stack, dashboard, ID badge, connect footer, README tables), **including the signature**.
- **Exception: the gaming avatars section ("Beyond the Code") keeps its own colors. Do not change it.**

## 3. Theme fix (GitHub light and dark)
- Problem: transparent SVGs with white text vanish on GitHub's light theme.
- Fix: every SVG gets a **solid navy rounded card background**, so it looks the same in both themes. No floating white text on a transparent background.
- Add a thin border: 1px `rgba(232,224,210,0.14)`.

## 4. Hero change
- **Remove** the headline ("Turning Ideas Into Reality") and the two description lines under it, in the left side of `hero.svg`.
- **Keep:** the stats row (10+ / 3+ / 100%), the chips (name, location, college), and Violet's viewfinder frame on the right.
- **Put the signature** (section 5) in the freed space. Keep a small gap between it and the stats row.

## 5. Signature
- File: `signature.svg`, 880x329 viewBox, transparent background (it sits on the navy card).
- It reveals the **original calligraphy image**, embedded as a base64 PNG. **Do not redraw, retrace or restyle the lettering.**
- Writing order: "Harsh", then "Patil", then the final "l" flows into the underline, which sweeps **right to left**. A small curl on the underline is drawn last.
- No pen or writing tool is shown.
- Color: ivory `#E8E0D2` for the name, blending into gold `#B89A5A` along the "l" tail and the underline.
- Timing: about 7 s loop (write about 4 s, hold, fade, repeat).
- Pure SVG with CSS animation only. No JavaScript.
- Embed it in `hero.svg` (scale it to fit the left column), or reference it as a separate image in the README if embedding is a problem.

## 6. Technical rules (from the original build guide)
- Only CSS and SMIL animation. GitHub strips JavaScript.
- Nothing loaded from the network. Fonts and images are inlined as base64. Use PNG, not WebP.
- Entrance animations use `fill-mode: both`, and the default (non-animated) state shows the finished card.
- Namespace ids when embedding other SVGs.
- Add `?v=2` to every image link in the README (bump again on each edit). Commit the SVG first, the README second.
- Keep each SVG under a few MB.

## 7. Postponed (do not do now)
- The gaming avatars will later change from a sprite sheet to an animated video. Leave as is for now.

## 8. Check before committing
- Open every SVG in a browser and check at several points in the animation.
- Check the profile in GitHub **dark** and **light** themes.
- Confirm the palette hex codes match the table above.
