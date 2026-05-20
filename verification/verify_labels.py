from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://localhost:8000/contact.html')

    # Verify label-input pairing for name
    page.locator("label[for='contact-name']").click()
    assert page.evaluate('document.activeElement.id === "contact-name"')

    # Verify label-input pairing for email
    page.locator("label[for='contact-email']").click()
    assert page.evaluate('document.activeElement.id === "contact-email"')

    # Verify label-select pairing for interest
    page.locator("label[for='contact-interest']").click()
    assert page.evaluate('document.activeElement.id === "contact-interest"')

    # Verify label-textarea pairing for mission
    page.locator("label[for='contact-mission']").click()
    assert page.evaluate('document.activeElement.id === "contact-mission"')

    browser.close()
    print("Verification passed")