## 2025-05-23 - Mobile Navigation Accessibility
**Learning:** Static HTML sites often lack dynamic accessibility attributes (like `aria-expanded`) on interactive elements because they rely on simple CSS toggles. Adding these via a small JS utility is a robust pattern that avoids manual updates across many HTML files.
**Action:** Always check `aria-expanded` and `aria-controls` on mobile triggers. If missing, a centralized JS initialization is cleaner than editing every HTML template.
