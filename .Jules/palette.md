## 2025-02-23 - Accessibility in Dynamic Forms & Variable Shadowing
**Learning:** JS-rendered forms often miss basic accessibility features like labels because they are constructed as strings. Also, learned that variable shadowing (naming a local variable `supabase` when `supabase` is the global library) can cause crashes in TDZ (Temporal Dead Zone), which breaks the entire page.
**Action:** Always check `for` attributes in dynamic forms and verify variable names against imported libraries to prevent shadowing crashes.
