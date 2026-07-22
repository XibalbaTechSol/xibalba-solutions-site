import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(record_video_dir="/app/verification/videos")
        page = context.new_page()

        # Determine correct path to contact.html
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = f"file://{os.path.join(base_dir, 'contact.html')}"

        print(f"Navigating to {file_path}")
        page.goto(file_path)
        page.wait_for_timeout(1000)

        # Scroll to form to make it visible
        page.locator("form#contact-form").scroll_into_view_if_needed()
        page.wait_for_timeout(1000)

        page.screenshot(path="/app/verification/screenshots/contact_form.png")

        context.close()
        browser.close()

if __name__ == "__main__":
    run()