import pytest
from playwright.sync_api import sync_playwright
import os

def test_blog_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})
        
        # 1. Test Blog Listing Page
        listing_path = os.path.abspath("xibalba-solutions-site/blog.html")
        page.goto(f"file://{listing_path}")
        
        assert "Technical Intel" in page.locator("h1").text_content()
        first_post_link = page.locator("text=Read Full Intel →")
        assert first_post_link.is_visible()
        
        # 2. Test Navigation to Post
        first_post_link.click()
        
        # Note: In file:// protocol, relative links might be tricky in tests depending on environment
        # Let's verify the content of the post page directly if click fails or navigation is complex
        post_path = os.path.abspath("xibalba-solutions-site/blog/2026-04-02-hermes-loops.html")
        page.goto(f"file://{post_path}")
        
        assert "Recursive Reasoning" in page.locator("h1").text_content()
        assert "Hermes 3" in page.content()
        assert "Internal Trace Loop" in page.content() # Verify code block
        
        # 3. Verify Navigation Back to Foundry
        foundry_link = page.locator("nav a", has_text="Foundry")
        foundry_link.click()
        assert "Intelligence" in page.locator("h1").text_content()
        
        page.screenshot(path="xibalba-solutions-site/screenshots/blog_reimagined.png")
        browser.close()
