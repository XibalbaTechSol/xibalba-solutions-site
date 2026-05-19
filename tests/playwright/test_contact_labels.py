import os
import pytest
from playwright.sync_api import Page, expect

def test_contact_form_accessibility_labels(page: Page):
    abs_path = os.path.abspath("contact.html")
    page.goto(f"file://{abs_path}")

    # Test name field
    page.locator("label[for='name']").click()
    assert page.evaluate('document.activeElement.id === "name"')

    # Test email field
    page.locator("label[for='email']").click()
    assert page.evaluate('document.activeElement.id === "email"')

    # Test select field
    page.locator("label[for='interest']").click()
    assert page.evaluate('document.activeElement.id === "interest"')

    # Test textarea field
    page.locator("label[for='message']").click()
    assert page.evaluate('document.activeElement.id === "message"')
