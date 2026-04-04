import pytest
import os
from playwright.sync_api import Page, expect

def test_homepage_integrity(page: Page):
    # Use a clean context without base tag interference for local testing
    abs_path = os.path.abspath("index.html")
    page.goto(f"file://{abs_path}")
    
    # 1. Validate Hero Title
    expect(page.locator("h1")).to_contain_text("Sovereign Intelligence Foundries")
    
    # 2. Validate Mermaid Flowchart (The Trust Vacuum)
    # Wait for the first mermaid diagram to render
    page.wait_for_selector(".mermaid svg", timeout=10000)
    expect(page.locator(".mermaid svg").first).to_be_visible()
    
    # 3. Validate Feature Cards & Interactivity
    # Find the Integrity Protocol card by its heading specifically
    integrity_card = page.locator("article", has=page.locator("h3:text('Integrity Protocol')"))
    expect(integrity_card).to_be_visible()
    expect(integrity_card).to_have_css("cursor", "pointer")
    
    # Check that clicking works (even if local file navigation is tricky in headless)
    # We check the 'onclick' attribute instead of actual navigation to avoid 'file://' errors
    onclick = integrity_card.get_attribute("onclick")
    assert "integrity-protocol.html" in onclick
    
    # 4. Validate Latest Dispatches
    dispatch_header = page.get_by_role("heading", name="Latest Dispatches")
    expect(dispatch_header).to_be_visible()
