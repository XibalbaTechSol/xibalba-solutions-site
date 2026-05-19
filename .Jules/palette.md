## 2026-05-19 - Explicit Form Control Pairing for Accessibility
**Learning:** Found that custom-styled forms in contact.html lacked explicit <label for="x"> and <input id="x"> pairing, preventing screen readers from correctly associating the form labels with inputs.
**Action:** Always ensure any <label> tag explicitly uses the 'for' attribute matching the corresponding input's 'id' attribute to maintain strong accessibility across custom forms.
