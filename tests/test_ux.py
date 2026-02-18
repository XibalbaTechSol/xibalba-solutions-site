import pytest
import re
import os
from playwright.sync_api import Page, expect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

def test_contact_form_ux(page: Page):
    # Navigate to contact page
    page.goto(get_file_url("contact.html"))

    # Verify Select styling
    select_element = page.locator("#interest")
    expect(select_element).to_be_visible()

    # Check that the inline style is removed
    style_attr = select_element.get_attribute("style")
    assert "appearance: none" not in (style_attr or "")

    # Verify it has form-control class
    expect(select_element).to_have_class(re.compile(r"form-control"))

    # Verify Required Labels
    name_label = page.locator("label[for='name']")
    expect(name_label).to_have_class("required-label")

    email_label = page.locator("label[for='email']")
    expect(email_label).to_have_class("required-label")

    # Verify Submit Button interaction
    page.fill("#name", "Test User")
    page.fill("#email", "test@example.com")

    # Prevent actual form submission to keep the page and button state visible for assertion
    page.evaluate("""
        const form = document.querySelector('form');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
        });
    """)

    submit_btn = page.locator("button[type='submit']")
    submit_btn.click()

    # Check if button text changes to "Sending..."
    expect(submit_btn).to_have_text("Sending...")
    expect(submit_btn).to_be_disabled()
    # Check for loading class
    expect(submit_btn).to_have_class(re.compile(r"loading"))

def test_veriphysics_form_ux(page: Page):
    page.goto(get_file_url("veriphysics.html"))

    # Verify Required Labels
    firm_label = page.locator("label:has-text('Investment Firm / Name')")
    expect(firm_label).to_have_class("required-label")

    email_label = page.locator("label:has-text('Work Email')")
    expect(email_label).to_have_class("required-label")
