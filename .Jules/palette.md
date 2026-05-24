
## 2026-05-24 - [Form Accessibility]
**Learning:** Found an accessibility issue pattern in the app's components where form inputs lacked explicit `<label for="">` and `<input id="">` pairings, making it difficult for screen readers to associate labels with inputs and reducing the click target area for users.
**Action:** Always ensure form inputs have explicit `id` attributes that match the `for` attribute of their corresponding `<label>` elements.
