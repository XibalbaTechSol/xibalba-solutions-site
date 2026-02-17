## 2025-05-15 - Dark Mode Select Inputs
**Learning:** When using `appearance: none` on `<select>` elements in a dark theme, browser defaults for `<option>` elements often remain white/light, causing jarring contrast or unreadable text.
**Action:** Always explicitly set `background-color` and `color` on `select option` to match the theme, even if the parent select is styled.

## 2025-05-15 - Invisible Dropdowns
**Learning:** Found an instance of `style="appearance: none"` inline without any accompanying background image, rendering the dropdown indistinguishable from a text input.
**Action:** Audit all usages of `appearance: none` to ensure a custom arrow indicator (SVG background) is present.
