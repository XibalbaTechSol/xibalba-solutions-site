import pytest
import os
from playwright.sync_api import Page, expect

def test_products_pillars(page: Page):
    abs_path = os.path.abspath("ai-agents.html")
    page.goto(f"file://{abs_path}")
    
    # Force visibility of animated elements for testing
    page.add_style_tag(content=".animate-in { opacity: 1 !important; transform: none !important; transition: none !important; }")
    
    # 1. Validate Page Header
    expect(page.locator("h1")).to_contain_text("Sovereign Product Architecture")
    
    # 2. Validate the 4 Pillars
    pillars = [
        "Integrity Token (INTG)",
        "Hermes Agents",
        "Local AI Services",
        "Hermes Swarm"
    ]
    for pillar in pillars:
        expect(page.locator(f"h2:has-text('{pillar}')")).to_be_visible()
    
    # 3. Validate Visual Artifacts (Mermaid)
    sections = ["integrity-token", "hermes-agents", "local-ai", "hermes-swarm"]
    for section_id in sections:
        section = page.locator(f"section#{section_id}")
        expect(section).to_be_visible()
        # Wait for SVG to exist and be visible
        page.wait_for_selector(f"section#{section_id} .mermaid svg", state="visible", timeout=15000)
        expect(section.locator(".mermaid svg")).to_be_visible()
    
    # 4. Validate Sanctum Guard detail (Local AI)
    expect(page.locator("text=Sanctum Guard")).to_be_visible()
