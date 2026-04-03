import pytest
from playwright.sync_api import sync_playwright
import os

def test_index_ui_ux():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()
        
        # Load local file
        path = os.path.abspath("xibalba-solutions-site/index.html")
        page.goto(f"file://{path}")
        
        # 1. Validate Logo Centerpiece
        hero_logo = page.locator(".hero-logo")
        assert hero_logo.is_visible()
        # Ensure it has the correct class for centerpiece styling
        assert "hero-logo" in hero_logo.get_attribute("class")
        
        # 2. Validate Hero Text (Now below logo)
        hero_h1 = page.locator("h1")
        assert hero_h1.is_visible()
        assert "Intelligence" in hero_h1.text_content()
        
        # 3. Validate Centering
        # Check if the hero section is using flex column and centered
        hero_section = page.locator(".hero")
        display = hero_section.evaluate("el => getComputedStyle(el).display")
        align_items = hero_section.evaluate("el => getComputedStyle(el).alignItems")
        assert display == "flex"
        assert align_items == "center"
        
        # 4. Capture Screenshot for LLM Scrutiny
        os.makedirs("xibalba-solutions-site/screenshots", exist_ok=True)
        page.screenshot(path="xibalba-solutions-site/screenshots/index_centerpiece_logo.png")
        print("\nScreenshot saved to xibalba-solutions-site/screenshots/index_centerpiece_logo.png")
        
        browser.close()

if __name__ == "__main__":
    test_index_ui_ux()
