## 2026-03-07 - Select Input Appearance in Dark Mode Forms
**Learning:** Applying `appearance: none;` to `<select>` elements without adding a custom dropdown arrow (e.g. via background SVG chevron) removes the native indicator, causing the dropdown to visually mimic a standard text input. This degrades the UI clarity.
**Action:** When restyling select elements in the future, either retain the native appearance or ensure a custom indicator is explicitly provided before overriding `appearance`.
