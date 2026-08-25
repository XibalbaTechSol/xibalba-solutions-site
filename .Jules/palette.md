## 2026-08-07 - Adding Required Indicators to Forms
**Learning:** Found that required input fields in the contact form were missing a visual indicator before submission, despite having the 'required' HTML attribute. This is an accessibility issue because users should not have to attempt form submission to find out which fields are required.
**Action:** Always append an explicit visual indicator (e.g., `<span aria-hidden="true">*</span>`) to labels of required fields, utilizing existing design system classes (like `text-error`).
## 2026-08-25 - [Add Visual Feedback for Disabled Buttons]
**Learning:** While testing the contact form's async submission, the submit button became disabled but lacked a clear visual indicator. In this app's design system, adding opacity and 'not-allowed' cursor to disabled buttons provides immediate feedback and prevents user confusion during simulated syncing.
**Action:** Ensure all interactive elements have explicit disabled states to improve accessibility and perceived performance during async operations.
