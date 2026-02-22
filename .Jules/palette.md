## 2025-05-15 - Async Loading States
**Learning:** Users lack confidence in form submissions (like Formspree) when there is no immediate visual feedback, leading to multiple clicks or early abandonment.
**Action:** Always intercept form `submit` events for async actions to disable the button and update text (e.g., "Sending...") immediately, even before the network request completes.
