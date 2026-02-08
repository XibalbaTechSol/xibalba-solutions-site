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

def test_mobile_navigation(page: Page):
    # Set viewport to mobile size
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto(get_file_url("index.html"))

    # Hamburger should be visible on mobile
    hamburger = page.locator(".hamburger")
    expect(hamburger).to_be_visible()

    # Nav links should be hidden initially
    nav_links = page.locator(".nav-links")
    expect(nav_links).not_to_be_visible()

    # Click hamburger to open menu
    hamburger.click()

    # Nav links should be visible now
    expect(nav_links).to_be_visible()

    # Hamburger should have aria-expanded="true"
    expect(hamburger).to_have_attribute("aria-expanded", "true")

    # Click hamburger to close menu
    hamburger.click()

    # Nav links should be hidden again
    expect(nav_links).not_to_be_visible()

    # Hamburger should have aria-expanded="false"
    expect(hamburger).to_have_attribute("aria-expanded", "false")
