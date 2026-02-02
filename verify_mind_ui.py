from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Emulate a mobile device to verify the "app" feel
        context = browser.new_context(
            viewport={'width': 390, 'height': 844}, # iPhone 12/13/14
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
        )
        page = context.new_page()

        # 1. Main View
        page.goto("http://localhost:8000/mind.html")
        expect(page.get_by_role("heading", name="Sovereign Mind")).to_be_visible()

        # Inject custom CSS to stop animations for consistent screenshots
        page.add_style_tag(content="""
            *, *::before, *::after {
                animation: none !important;
                transition: none !important;
            }
        """)

        # Take screenshot of main view
        page.screenshot(path="/home/jules/verification/mind_main.png", full_page=True)
        print("Captured mind_main.png")

        # 2. Loop Editor
        page.get_by_role("button", name="Edit").click()
        expect(page.locator("#loop-editor")).to_be_visible()
        page.screenshot(path="/home/jules/verification/mind_editor.png")
        print("Captured mind_editor.png")

        # 3. Rewrite Logic (Burn)
        page.reload() # Reset state
        page.add_style_tag(content="""
            *, *::before, *::after {
                animation: none !important;
                transition: none !important;
            }
        """)

        page.fill("#negative-thought", "I am limited")
        page.click("#btn-burn")
        # Wait for Step 2 to appear
        expect(page.locator("#rewrite-step-2")).to_be_visible()
        page.screenshot(path="/home/jules/verification/mind_rewrite.png")
        print("Captured mind_rewrite.png")

        browser.close()

if __name__ == "__main__":
    run()
