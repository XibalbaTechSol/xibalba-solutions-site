import pytest
from playwright.sync_api import Page, expect

# Xibalba Solutions: Site-Wide Footer Validation
# Source of Truth: Centered 'Xibalba Solutions LLC. All rights reserved.' 
# and sitemap presence.

PAGES = [
    "index.html",
    "ai-agents.html",
    "integrity-protocol.html",
    "whitepaper.html",
    "business-plan.html",
    "blog.html"
]

@pytest.mark.parametrize("page_path", PAGES)
def test_sovereign_footer(page, page_path):
    # Load the local file
    import os
    abs_path = os.path.abspath(page_path)
    page.goto(f"file://{abs_path}")
    
    footer = page.locator("footer")
    expect(footer).to_be_visible()
    
    # Validate Centered Copyright
    meta = footer.locator(".footer-meta")
    expect(meta).to_contain_text("Xibalba Solutions LLC. All rights reserved.")
    
    # Ensure treasury address is REMOVED (Reimagined Footer requirement)
    treasury = page.locator(".eth-address")
    expect(treasury).not_to_be_visible()
    
    # Validate Sitemap Links
    sitemap_links = [
        "Hermes Agents",
        "Hermes Swarm",
        "Integrity Protocol",
        "Technical Whitepaper",
        "Strategic Business Plan",
        "Technical Dispatches"
    ]
    for link_text in sitemap_links:
        link = footer.get_by_role("link", name=link_text)
        expect(link).to_be_visible()
