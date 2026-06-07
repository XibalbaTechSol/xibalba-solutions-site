## 2026-06-07 - Add ARIA Labels and Explicit Form Associations
**Learning:** Found that custom forms often omit explicit `<label for="x">` and `<input id="x">` pairings, which are critical for screen reader compatibility and expanding the click target area for inputs. While adding simple `required` attributes is good, true accessibility requires programmatic association.
**Action:** Always ensure every form input, select, and textarea has a unique ID and is explicitly associated with a label using the `for` attribute.
