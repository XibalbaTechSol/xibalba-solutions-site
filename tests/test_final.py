import pytest
from playwright.sync_api import sync_playwright
import os

def test_about_ui_ux():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})
        path = os.path.abspath("xibalba-solutions-site/about.html")
        page.goto(f"file://{path}")
        
        assert "Jacob Vickers" in page.locator("p").first.text_content()
        assert page.locator(".feature-card").is_visible()
        
        page.screenshot(path="xibalba-solutions-site/screenshots/about_reimagined.png")
        browser.close()

def test_pricing_ui_ux():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})
        path = os.path.abspath("xibalba-solutions-site/pricing.html")
        page.goto(f"file://{path}")
        
        cards = page.locator(".feature-card")
        assert cards.count() == 3
        assert "$15,000" in page.content()
        
        page.screenshot(path="xibalba-solutions-site/screenshots/pricing_reimagined.png")
        browser.close()

def test_contact_ui_ux():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})
        path = os.path.abspath("xibalba-solutions-site/contact.html")
        page.goto(f"file://{path}")
        
        form = page.locator("form")
        assert form.is_visible()
        assert form.get_attribute("action") == "https://formspree.io/f/mqegdoyy"
        
        # Check for technical requirement placeholder
        assert "Define your niche use case" in page.locator("textarea").get_attribute("placeholder")
        
        page.screenshot(path="xibalba-solutions-site/screenshots/contact_reimagined.png")
        browser.close()
