import pytest
import os
from playwright.sync_api import Page, expect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

def test_mobile_menu_interaction(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto(get_file_url("index.html"))

    nav_links = page.locator(".nav-links")
    hamburger = page.locator(".hamburger")

    # 1. Initially hidden
    expect(nav_links).not_to_be_visible()

    # 2. Click hamburger
    hamburger.click()

    # 3. Visible
    expect(nav_links).to_be_visible()

    # 4. Click again
    hamburger.click()

    # 5. Hidden again
    expect(nav_links).not_to_be_visible()
