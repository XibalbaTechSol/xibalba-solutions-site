## 2025-05-20 - Accessibility in Dynamic JS Forms
**Learning:** Dynamic HTML strings often miss label associations. Also, variable shadowing in `const` declarations (e.g. `const supabase = supabase...`) creates temporal dead zones that crash the app, rendering it inaccessible.
**Action:** Always verify dynamic form HTML for `for`/`id` associations and `aria-label`s. Check for variable shadowing when refactoring legacy code.
