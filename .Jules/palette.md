## 2026-08-04 - Reusable Required Indicators
**Learning:** For forms where `required` attributes are present on inputs but lack visual indication, appending `<span class="text-error" aria-hidden="true">*</span>` to the `<label>` satisfies both sighted users and screen readers, leveraging existing utility classes.
**Action:** Always verify if a required input has a corresponding visual indicator on its label and add this pattern if missing.
