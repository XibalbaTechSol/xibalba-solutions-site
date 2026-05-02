## 2024-05-24 - Explicit Form Label Pairings
**Learning:** Form labels in `contact.html` lacked explicit `for` and `id` bindings to their corresponding inputs. While visual users can infer the relationship via proximity, screen readers require explicit `<label for="x">` and `<input id="x">` pairings to correctly announce fields.
**Action:** Always ensure every form input has an explicit `id` that matches the `for` attribute of its associated `<label>` to guarantee screen reader compatibility.
