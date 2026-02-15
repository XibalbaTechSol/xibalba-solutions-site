import pytest
import os
from playwright.sync_api import Page, expect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

def test_select_appearance_style_not_none(page: Page):
    page.goto(get_file_url("contact.html"))
    select_element = page.locator("#interest")
    expect(select_element).to_be_visible()

    # We want to ensure 'appearance: none' is NOT present in the style attribute
    # Initially, it IS present, so this test should FAIL.
    # Playwright's verify helper for attributes:
    style_attr = select_element.get_attribute("style")
    assert "appearance: none" not in (style_attr or ""), "Found 'appearance: none' in style attribute which breaks UX"
