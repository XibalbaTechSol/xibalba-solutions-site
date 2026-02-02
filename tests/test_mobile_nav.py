import pytest
import os
from playwright.sync_api import Page, expect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

PAGES = [
    "index.html",
    "about.html",
    "services.html",
    "solutions.html",
    "products.html",
    "investors.html",
    "hardware.html",
    "pricing.html",
    "contact.html",
    "cli.html",
    "crm.html",
    "veriphysics.html"
]

@pytest.mark.parametrize("page_file", PAGES)
def test_mobile_navigation_menu_all_pages(page: Page, page_file):
    # Set viewport to mobile size
    page.set_viewport_size({"width": 375, "height": 667})

    page.goto(get_file_url(page_file))

    hamburger = page.locator(".hamburger")
    nav_links = page.locator(".nav-links")

    # Initially, hamburger should be visible and nav links hidden/off-screen
    expect(hamburger).to_be_visible()

    # Check that nav_links is not in view
    expect(nav_links).not_to_have_class("nav-links active")

    # Click hamburger
    hamburger.click()

    # Now nav links should have class active
    expect(nav_links).to_have_class("nav-links active")

    # Click hamburger again to close
    hamburger.click()

    # Should not be active
    expect(nav_links).not_to_have_class("nav-links active")

def test_mobile_navigation_link_click(page: Page):
    # Set viewport to mobile size
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto(get_file_url("index.html"))

    # Open menu
    page.click(".hamburger")

    # Click a link
    page.click(".nav-links a[href='about.html']")

    # Should navigate
    expect(page).to_have_url(get_file_url("about.html"))
