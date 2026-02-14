import pytest
import os
import re
from playwright.sync_api import Page, expect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

def test_contact_form_required_fields(page: Page):
    """
    Test that required fields in the contact form have visual indicators
    and correct attributes.
    """
    page.goto(get_file_url("contact.html"))

    # Check Name field
    name_label = page.locator('label[for="name"]')
    # expect(name_label).to_have_class(re.compile(r"required-label"))
    # Actually, to_have_class takes a string or regex. Regex is good.
    expect(name_label).to_have_class(re.compile(r"required-label"))
    name_input = page.locator('#name')
    expect(name_input).to_have_attribute("required", "")

    # Check Email field
    email_label = page.locator('label[for="email"]')
    expect(email_label).to_have_class(re.compile(r"required-label"))
    email_input = page.locator('#email')
    expect(email_input).to_have_attribute("required", "")

    # Check Select field (Usability improvement)
    # Ensure appearance: none is REMOVED so the native arrow is visible
    select_input = page.locator('#interest')
    # get_attribute returns the value of the attribute, or None if not present
    style_attr = select_input.get_attribute("style")

    # If style attribute exists, check it doesn't contain 'appearance: none'
    if style_attr:
        assert "appearance: none" not in style_attr

    # Also verify labels for non-required fields do NOT have the class
    company_label = page.locator('label[for="company"]')
    expect(company_label).not_to_have_class(re.compile(r"required-label"))

    # Verify the pseudo-element ::after content (Checking CSS application)
    # This requires evaluate because Playwright locators target DOM elements, not pseudo-elements
    # We check if the computed style has 'content' set to " *"
    # Note: getComputedStyle returns the value with quotes
    content = page.evaluate("""
        () => {
            const el = document.querySelector('.required-label');
            return window.getComputedStyle(el, '::after').getPropertyValue('content');
        }
    """)
    assert '" *"' in content or "' *'" in content
