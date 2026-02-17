
import pytest
import os
from playwright.sync_api import Page, expect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

def test_select_styling(page: Page):
    # Check contact.html
    page.goto(get_file_url("contact.html"))
    select_contact = page.locator("select#interest")

    # Check computed style
    appearance_contact = select_contact.evaluate("el => getComputedStyle(el).appearance")
    bg_image_contact = select_contact.evaluate("el => getComputedStyle(el).backgroundImage")

    print(f"Contact appearance: {appearance_contact}")
    print(f"Contact bg_image: {bg_image_contact}")

    # Check veriphysics.html
    page.goto(get_file_url("veriphysics.html"))
    select_veriphysics = page.locator("select[name='interest']")

    appearance_veriphysics = select_veriphysics.evaluate("el => getComputedStyle(el).appearance")
    bg_image_veriphysics = select_veriphysics.evaluate("el => getComputedStyle(el).backgroundImage")

    print(f"Veriphysics appearance: {appearance_veriphysics}")
    print(f"Veriphysics bg_image: {bg_image_veriphysics}")

    # Assertions for FIXED STATE
    # Contact has appearance: none and background image
    assert appearance_contact == "none"
    assert bg_image_contact != "none"
    assert "data:image/svg+xml" in bg_image_contact or "url(" in bg_image_contact

    # Veriphysics also has appearance: none and background image
    assert appearance_veriphysics == "none"
    assert bg_image_veriphysics != "none"
    assert "data:image/svg+xml" in bg_image_veriphysics or "url(" in bg_image_veriphysics
