## 2026-03-04 - Form Accessibility: Label & ID Associations
**Learning:** Forms in dashboard and veriphysics lacked explicit 'for' and 'id' pairings or aria-labels, making them inaccessible for screen readers. Dynamic elements generated via JS (like in dashboard.html) also need these.
**Action:** Always verify proper pairing between <label for="x"> and <input id="x"> or provide aria-label when visual labels are omitted.
