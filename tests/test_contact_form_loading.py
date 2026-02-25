import pytest
import os
from playwright.sync_api import Page, expect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

def test_contact_form_loading_state(page: Page):
    page.goto(get_file_url("contact.html"))

    # Fill required fields
    page.fill("input[name='name']", "Test User")
    page.fill("input[name='email']", "test@example.com")

    # Intercept form submission
    def handle_route(route):
        print(f"Intercepted: {route.request.url}")
        route.fulfill(status=204, body="")

    page.route("**/formspree.io/**", handle_route)

    submit_btn = page.locator("button[type='submit']")

    # Click submit
    submit_btn.click()

    # Wait for a tiny bit to ensure JS has fired if it exists
    page.wait_for_timeout(100)

    # Check for loading state
    expect(submit_btn).to_have_text("Sending...")
    expect(submit_btn).to_be_disabled()
