from playwright.sync_api import sync_playwright, expect
import os

def verify_contact_form(page):
    abs_path = os.path.abspath("/app/contact.html")
    page.goto(f"file://{abs_path}")

    # Check that both labels now contain the asterisk
    name_label = page.locator("label[for='name']")
    email_label = page.locator("label[for='email']")

    expect(name_label).to_contain_text("Identity / Organization *")
    expect(email_label).to_contain_text("Secure Transmission Channel (Email) *")

    page.screenshot(path="/app/verification/screenshots/contact_labels.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(record_video_dir="/app/verification/videos")
        page = context.new_page()
        try:
            verify_contact_form(page)
        finally:
            context.close()
            browser.close()