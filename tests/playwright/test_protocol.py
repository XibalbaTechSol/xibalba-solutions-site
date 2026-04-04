import pytest
import os
from playwright.sync_api import Page, expect

def test_protocol_page_v8(page: Page):
    abs_path = os.path.abspath("integrity-protocol.html")
    page.goto(f"file://{abs_path}")
    
    # 1. Validate Tri-Metric Hero
    expect(page.locator(".metric-hero")).to_be_visible()
    
    # Use first() to avoid strict mode violation with text search
    expect(page.locator("text=$S_e$").first).to_be_visible()
    expect(page.locator("text=$S_g$").first).to_be_visible()
    expect(page.locator("text=$S_i$").first).to_be_visible()
    
    # 2. Validate Flowcharts (Wait for at least one)
    # Use nth(0) or first to avoid strict mode on wait_for_selector if needed, 
    # but wait_for_selector usually just needs the selector. 
    # The error was in wait_for_selector because multiple were found.
    page.wait_for_selector(".mermaid svg", timeout=15000)
    expect(page.locator(".mermaid svg").first).to_be_visible()
    
    # 3. Validate LaTeX Formula (KaTeX)
    # Use first() to avoid strict mode violation
    expect(page.locator(".katex").first).to_be_visible()
    
    # 4. Validate Audit Tiers Table
    table = page.locator("table.comparison-table")
    expect(table).to_be_visible()
    expect(table).to_contain_text("Tier III: Platinum")
    
    # 5. Validate SDK Manifest
    expect(page.locator("h2:has-text('SDK Manifest')")).to_be_visible()
