import pytest
import os
from playwright.sync_api import Page, expect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

def test_contact_form_accessibility(page: Page):
    """
    Verifies that the contact form has the correct accessibility attributes
    and UX enhancements.
    """
    page.goto(get_file_url("contact.html"))

    # 1. Verify the form ID exists
    form = page.locator("#contact-form")
    expect(form).to_be_visible()

    # 2. Verify Name input accessibility
    # Label should contain the asterisk
    name_label = page.locator("label[for='name']")
    expect(name_label).to_contain_text("*")
    # Input should have aria-required="true"
    name_input = page.locator("#name")
    expect(name_input).to_have_attribute("aria-required", "true")

    # 3. Verify Email input accessibility
    email_label = page.locator("label[for='email']")
    expect(email_label).to_contain_text("*")
    email_input = page.locator("#email")
    expect(email_input).to_have_attribute("aria-required", "true")

def test_contact_form_submission_state(page: Page):
    """
    Verifies that the submit button updates its text upon submission.
    Note: We prevent actual navigation to verify the DOM change.
    """
    page.goto(get_file_url("contact.html"))

    # Fill the form
    page.fill("#name", "Test User")
    page.fill("#email", "test@example.com")

    # Evaluate a script to prevent the form from actually submitting (and navigating away)
    # but still allow the submit event to bubble to our handler.
    # However, our handler is on the form. If we add another handler on the form that prevents default,
    # and it runs AFTER our handler, we can check the state.
    # The handler in main.js is added on DOMContentLoaded.
    # We can inject a script to prevent default.

    page.evaluate("""
        const form = document.getElementById('contact-form');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            // We prevent default here so we can assert the button state
            // without the page unloading.
        });
    """)

    # Click submit
    page.click("button[type='submit']")

    # Check button state
    submit_btn = page.locator("button[type='submit']")
    expect(submit_btn).to_have_text("Sending...")

    # The disabled state happens in a setTimeout(..., 0), so we might need to wait a tick.
    # Playwright's expect might retry, but let's see.
    expect(submit_btn).to_be_disabled()
