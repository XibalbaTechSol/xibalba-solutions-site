## 2026-07-03 - Explicit Form Control Associations
**Learning:** The application's contact form components lacked explicit `for` attributes on labels and corresponding `id` attributes on inputs. This is a crucial accessibility oversight as it breaks click-to-focus behavior and impairs screen reader association.
**Action:** Ensure all new and existing form controls have strict, explicit associations using matching `id` and `for` attributes.
