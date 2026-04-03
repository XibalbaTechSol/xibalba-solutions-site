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
        
        # 1. Validate Hero Impact
        hero_h1 = page.locator("h1")
        assert hero_h1.is_visible()
        assert "Intelligence" in hero_h1.text_content()
        
        # 2. Validate Navigation
        nav = page.locator("nav")
        assert nav.is_visible()
        
        # Check active link
        active_link = page.locator("nav .active")
        assert active_link.text_content() == "Foundry"
        
        # 3. Validate Technical Pillars
        features = page.locator(".feature-card")
        assert features.count() == 3
        
        pillar_titles = features.all_text_contents()
        assert any("Recursive Reasoning" in t for t in pillar_titles)
        assert any("OpenClaw Runtimes" in t for t in pillar_titles)
        assert any("Sanctum Guard" in t for t in pillar_titles)
        
        # 4. Validate Design Aesthetics (Glassmorphism & Gradients)
        # Check if gradient text class exists
        assert page.locator(".gradient-text").count() > 0
        
        # 5. Capture Screenshot for LLM Scrutiny
        os.makedirs("xibalba-solutions-site/screenshots", exist_ok=True)
        page.screenshot(path="xibalba-solutions-site/screenshots/index_reimagined.png")
        print("\nScreenshot saved to xibalba-solutions-site/screenshots/index_reimagined.png")
        
        browser.close()

if __name__ == "__main__":
    test_index_ui_ux()
