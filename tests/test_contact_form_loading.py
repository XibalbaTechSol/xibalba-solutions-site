import pytest
import os
from playwright.sync_api import Page, expect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

def test_contact_form_loading_state(page: Page):
    page.goto(get_file_url("contact.html"))

    # Fill form
    page.fill("input[name='name']", "Test User")
    page.fill("input[name='email']", "test@example.com")
    page.fill("textarea[name='message']", "Test message")

    # Intercept the form submission request to prevent actual navigation/unload
    # and keep the page state for assertion.
    page.route("**/formspree.io/**", lambda route: route.fulfill(status=204))

    # Click submit
    page.click("button[type='submit']")

    submit_button = page.locator("button[type='submit']")

    # Check for loading state
    expect(submit_button).to_have_text("Sending...")
    expect(submit_button).to_be_disabled()
    expect(submit_button).to_have_css("opacity", "0.7")
