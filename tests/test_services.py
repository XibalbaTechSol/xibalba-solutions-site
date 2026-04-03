import pytest
from playwright.sync_api import sync_playwright
import os

def test_ai_agents_ui_ux():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})
        
        path = os.path.abspath("xibalba-solutions-site/ai-agents.html")
        page.goto(f"file://{path}")
        
        # 1. Validate Technical Section
        assert "Hermes 3" in page.locator("h2").first.text_content()
        
        # 2. Validate Architecture Diagram (CSS-based)
        loop_steps = page.locator("main .feature-card div")
        assert loop_steps.count() >= 3
        
        # 3. Validate Integration Highlights
        assert page.locator("text=OMNICHANNEL").is_visible()
        
        page.screenshot(path="xibalba-solutions-site/screenshots/ai_agents_reimagined.png")
        browser.close()

def test_local_ai_ui_ux():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})
        
        path = os.path.abspath("xibalba-solutions-site/local-ai.html")
        page.goto(f"file://{path}")
        
        # 1. Validate Compliance Focus
        assert "HIPAA" in page.content()
        
        # 2. Validate Tech Stack List
        stack_items = page.locator(".feature-card li")
        assert stack_items.count() == 5
        assert "HERMES" in stack_items.first.text_content() or "HERMES" in stack_items.nth(1).text_content()
        
        page.screenshot(path="xibalba-solutions-site/screenshots/local_ai_reimagined.png")
        browser.close()
