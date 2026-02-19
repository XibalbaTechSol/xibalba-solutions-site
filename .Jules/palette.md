## 2025-02-09 - Mixed Form Handling Strategy
**Learning:** This project mixes standard static form submissions (Formspree on `contact.html`) with JS-handled async forms (Supabase on `dashboard.html`). Global scripts targeting forms must distinguish between them (e.g., by checking for the `action` attribute) to avoid conflicting with existing inline handlers.
**Action:** When adding global form behaviors, always scope selectors to avoid disrupting the `dashboard.html` SPA-like logic.
