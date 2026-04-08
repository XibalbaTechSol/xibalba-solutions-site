
## 2025-03-18 - Missing Global Focus Styles
**Learning:** Found that this site was relying heavily on default browser focus states which, depending on the browser/system, were practically invisible against the dark background. A systemic approach to `:focus-visible` was missing.
**Action:** Added a global `:focus-visible` declaration leveraging the existing `--accent-secondary` color with an `outline-offset: 4px` to ensure accessibility outlines pop without disturbing the layout or being overly intrusive for mouse users.
