import pytest
import os
from playwright.sync_api import Page, expect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

def test_contact_form_loading_state(page: Page):
    # Listen for console logs
    page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))

    page.goto(get_file_url("contact.html"))

    # Fill in required fields
    page.fill("input[name='name']", "Test User")
    page.fill("input[name='email']", "test@example.com")
    page.fill("textarea[name='message']", "Test message")

    # Use 204 No Content to prevent navigation and keep the page state
    page.route("**/formspree.io/**", lambda route: route.fulfill(status=204))

    # Click submit
    submit_button = page.locator("button[type='submit']")
    submit_button.click()

    # Now check the button state
    expect(submit_button).to_have_text("Sending...", timeout=5000)

    # Also check disabled state
    expect(submit_button).to_be_disabled()
