import pytest
import os
from playwright.sync_api import Page, expect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

def test_contact_form_loading_state(page: Page):
    # Go to contact page
    page.goto(get_file_url("contact.html"))

    # Fill in required fields
    page.fill("input[name='name']", "Test User")
    page.fill("input[name='email']", "test@example.com")

    # Prevent actual form submission to avoid navigation,
    # but allow the submit event to bubble so our handler runs.
    # We add this listener *after* the page loads, so it should run.
    # Note: Event listeners are executed in order.
    # Our handler in js/main.js is added on DOMContentLoaded.
    # This one will be added later, so it runs later?
    # Or we can just ensure it doesn't navigate.
    page.evaluate("""
        const form = document.querySelector('form[action]');
        form.addEventListener('submit', (e) => {
            e.preventDefault(); // Stop navigation
        });
    """)

    # Locate the submit button
    submit_btn = page.locator("button[type='submit']")

    # Click submit.
    submit_btn.click()

    # Check state
    expect(submit_btn).to_have_text("Sending...")
    expect(submit_btn).to_be_disabled()
