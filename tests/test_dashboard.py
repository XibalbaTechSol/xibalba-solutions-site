import pytest
import os
from playwright.sync_api import Page, expect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

@pytest.fixture(autouse=True)
def check_console_errors(page: Page):
    error_logs = []
    page.on("console", lambda msg: error_logs.append(msg.text) if msg.type == "error" else None)
    yield
    assert len(error_logs) == 0, f"Console errors found: {error_logs}"

def test_dashboard_login_form(page: Page):
    page.goto(get_file_url("dashboard.html"))
    # Wait for the login form to appear
    # The page might briefly show "Loading..." then "Admin Login"
    expect(page.locator("h2")).to_contain_text("Admin Login")

    # Check for labels
    expect(page.locator("label[for='email']")).to_have_text("Email")
    expect(page.locator("label[for='password']")).to_have_text("Password")

    # Check input visibility
    expect(page.locator("#email")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()
