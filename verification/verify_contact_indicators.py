from playwright.sync_api import Page, expect, sync_playwright

def verify_required_indicators(page: Page):
    # Navigate to the local contact page
    page.goto("file:///app/contact.html")

    # Wait for the form to be visible
    expect(page.locator("form#contact-form")).to_be_visible()

    # Assert that the name label contains the red asterisk and it's visible
    name_label = page.locator("label[for='name']")
    expect(name_label).to_be_visible()
    expect(name_label).to_contain_text("Identity / Organization *")

    # Check that the asterisk has the text-error class
    asterisk = name_label.locator("span.text-error")
    expect(asterisk).to_be_visible()
    expect(asterisk).to_have_text("*")

    # Check the same for the email label
    email_label = page.locator("label[for='email']")
    expect(email_label).to_be_visible()
    expect(email_label).to_contain_text("Secure Transmission Channel (Email) *")
    email_asterisk = email_label.locator("span.text-error")
    expect(email_asterisk).to_be_visible()

    # Capture a screenshot showing the updated form labels
    page.screenshot(path="/app/verification/screenshots/contact_form_required_indicators.png", full_page=True)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use an appropriate mobile/desktop viewport to ensure visibility
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()
        try:
            verify_required_indicators(page)
        finally:
            context.close()
            browser.close()
