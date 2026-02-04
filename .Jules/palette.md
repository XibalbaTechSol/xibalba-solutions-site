## 2026-02-04 - Global Focus Styles
**Learning:** The application lacked consistent keyboard focus indicators, making navigation difficult for keyboard users.
**Action:** Added a global `:focus-visible` style in `css/style.css` using `outline: 2px solid var(--accent-secondary); outline-offset: 2px;`. This ensures accessibility across the site with a single CSS change.
