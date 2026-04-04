import pytest
import os
from playwright.sync_api import Page, expect

PAGES = [
    "index.html",
    "ai-agents.html",
    "integrity-protocol.html",
    "blog.html",
    "privacy.html"
]

@pytest.mark.parametrize("page_path", PAGES)
def test_final_footer_llc(page: Page, page_path):
    abs_path = os.path.abspath(page_path)
    page.goto(f"file://{abs_path}")
    
    footer = page.locator("footer")
    expect(footer).to_be_visible()
    
    # Validate the new centered LLC notice
    meta = footer.locator(".footer-meta")
    expect(meta).to_contain_text("Xibalba Solutions, LLC. All rights reserved.")
    expect(meta).to_have_css("justify-content", "center")
    expect(meta).to_have_css("text-align", "center")
    
    # Confirm treasury address is GONE
    expect(page.locator(".eth-address")).not_to_be_visible()
    
    # Confirm sitemap links are present
    expect(footer.get_by_text("Hermes Agents", exact=False)).to_be_visible()
    expect(footer.get_by_text("Technical Dispatches", exact=False)).to_be_visible()
