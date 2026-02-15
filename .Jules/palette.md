## 2025-02-15 - Contact Form Select Affordance
**Learning:** Found a `<select>` element with `appearance: none` but no custom styling (like a background arrow). This removed the visual affordance that it was a dropdown, making it look like a text input.
**Action:** When inspecting form elements, always check if `appearance: none` is used without a replacement visual indicator. If so, remove it to restore native browser styles for better accessibility and usability.
