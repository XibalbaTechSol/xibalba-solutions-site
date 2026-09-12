from playwright.sync_api import expect

def test_contact_form(page):
    page.goto('file:///app/index.html')

    # Assert elements exist
    expect(page.locator('form#contact-form')).to_be_visible()

    # Fill required fields
    page.locator('input#contact-name').fill('Test User')
    page.locator('input#contact-email').fill('test@example.com')
    page.locator('textarea#contact-message').fill('This is a test message')

    # Assert visually required fields have some indication
    # Not testing this explicitly in this adhoc test, just verifying the HTML
