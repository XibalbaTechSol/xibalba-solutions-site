from playwright.sync_api import sync_playwright
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

def verify_ux():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Contact Form
        page.goto(get_file_url("contact.html"))
        # Fill all required data to allow submission
        page.fill("#name", "Palette Verification")
        page.fill("#email", "palette@example.com")

        # Take screenshot of the form area
        form_locator = page.locator(".contact-form-container")
        form_locator.screenshot(path="verification/contact_form.png")

        # Take screenshot of the select dropdown specifically to show the arrow
        select_locator = page.locator("#interest")
        select_locator.screenshot(path="verification/contact_select.png")

        # 2. Button Loading State
        # Prevent default to stay on page
        page.evaluate("""
            const form = document.querySelector('form');
            form.addEventListener('submit', (e) => {
                e.preventDefault();
            });
        """)
        submit_btn = page.locator("button[type='submit']")
        submit_btn.click()
        # Wait for text change
        page.wait_for_function("document.querySelector('button[type=submit]').textContent === 'Sending...'")
        submit_btn.screenshot(path="verification/button_loading.png")

        # 3. Veriphysics Form
        page.goto(get_file_url("veriphysics.html"))
        # Take screenshot of the form area
        v_form_locator = page.locator(".contact-form-container")
        v_form_locator.screenshot(path="verification/veriphysics_form.png")

        browser.close()

if __name__ == "__main__":
    if not os.path.exists("verification"):
        os.makedirs("verification")
    verify_ux()
