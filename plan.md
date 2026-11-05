1. Modify `css/style.css` using `replace_with_git_merge_diff` to add the `.spinner` class animation.
```
<<<<<<< SEARCH
/* ── Utility ── */
=======
.spinner {
    display: inline-block;
    width: 1em;
    height: 1em;
    border: 2px solid rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    border-top-color: currentColor;
    animation: spin 1s ease-in-out infinite;
    margin-right: 0.5rem;
    vertical-align: text-bottom;
}
@keyframes spin {
    to { transform: rotate(360deg); }
}

/* ── Utility ── */
>>>>>>> REPLACE
```
2. Modify `css/style.css` using `replace_with_git_merge_diff` to center the button content.
```
<<<<<<< SEARCH
.btn {
    display: inline-block;
    padding: 1rem 2.5rem;
=======
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 1rem 2.5rem;
>>>>>>> REPLACE
```
3. Modify `js/main.js` using `replace_with_git_merge_diff` to update the loading state text to an HTML string including the spinner.
```
<<<<<<< SEARCH
            // Show loading state
            btn.textContent = 'Synchronizing...';
            btn.disabled = true;
=======
            // Show loading state
            btn.innerHTML = '<span class="spinner" aria-hidden="true"></span> Synchronizing...';
            btn.disabled = true;
>>>>>>> REPLACE
```
4. Add a journal entry to `.Jules/palette.md` using `run_in_bash_session` to append the new entry:
`cat << 'EOF' >> .Jules/palette.md
## 2026-10-27 - Async Form Loading State
**Learning:** Submitting forms without a visual loading indicator (e.g. spinner) can cause user uncertainty. Simply changing button text is often not enough visual feedback to indicate an active network request.
**Action:** Always include a visual loading indicator (like a CSS spinner) alongside text changes for async form submissions to improve feedback and reduce user friction.
EOF`
5. Verify the changes locally by checking the diff using `run_in_bash_session` with command `git diff`.
6. Use `write_file` to create a script at `/app/verification/verify_loading.py`.
```python
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(record_video_dir="/app/verification/videos")
    page = context.new_page()
    page.goto("file:///app/contact.html")

    page.fill("#name", "Test User")
    page.fill("#email", "test@example.com")

    # Intercept network request to simulate slow loading
    page.route("https://xibalba-solutions-site.onrender.com/contact", lambda route: None)

    page.click("button[type='submit']")

    expect(page.locator(".spinner")).to_be_visible()

    page.screenshot(path="/app/verification/screenshots/loading.png")

    context.close()
    browser.close()
```
7. Verify the contents of the newly created script using `run_in_bash_session` with `cat /app/verification/verify_loading.py`.
8. Execute the verification script using `run_in_bash_session` with `python /app/verification/verify_loading.py`.
9. Use `run_in_bash_session` with `ls /app/verification/screenshots` and `ls /app/verification/videos` to discover the exact paths of the generated media files.
10. Call `frontend_verification_complete` with the discovered screenshot path.
11. Clean up the script and artifacts using `run_in_bash_session` to remove `/app/verification/verify_loading.py`, `/app/verification/screenshots/loading.png`, and the specific generated video `.webm` file discovered in step 9.
12. Run tests using `run_in_bash_session` with `python -m pytest tests/playwright/`.
13. Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
14. Submit the change with `submit`.
