import pytest
from playwright.sync_api import Page, expect

def test_mind_page_navigation(page: Page):
    """Test that the Mind link exists and works."""
    page.goto("http://localhost:8000/index.html")

    # Check for the link in the nav
    mind_link = page.get_by_role("link", name="Mind").first
    expect(mind_link).to_be_visible()

    mind_link.click()
    expect(page).to_have_url("http://localhost:8000/mind.html")
    expect(page).to_have_title("Sovereign Mind | Xibalba Solutions")

def test_mind_app_functionality(page: Page):
    """Test the core features of the Mind app."""
    page.goto("http://localhost:8000/mind.html")

    # Check Sections
    expect(page.get_by_role("heading", name="The Loop")).to_be_visible()
    expect(page.get_by_role("heading", name="The Vault")).to_be_visible()
    expect(page.get_by_role("heading", name="The Rewrite")).to_be_visible()

    # Test The Loop Editor
    page.get_by_role("button", name="Edit").click()
    expect(page.locator("#loop-editor")).to_be_visible()

    # Add a new affirmation
    textarea = page.locator("#loop-input")
    current_val = textarea.input_value()
    new_affirmation = "I am testing my mind."
    textarea.fill(current_val + "\n" + new_affirmation)

    page.get_by_role("button", name="Save Loop").click()

    # Verify it appears (might need to wait for cycle, but we can check the storage or immediate display if it's the first one)
    # The script starts the loop immediately.
    # We can check localStorage persistence
    loop_data = page.evaluate("() => localStorage.getItem('xibalba_mind_loop')")
    assert new_affirmation in loop_data

def test_mind_vault_add(page: Page):
    """Test adding an image to the vault."""
    page.goto("http://localhost:8000/mind.html")

    page.get_by_role("button", name="+").click()
    page.fill("#vision-url", "https://example.com/image.png")
    page.click("#btn-save-vision")

    # Check if image is added
    expect(page.locator(".vision-item img")).to_have_count(1)
    expect(page.locator(".vision-item img")).to_have_attribute("src", "https://example.com/image.png")

def test_rewrite_logic(page: Page):
    """Test the burn and imprint logic."""
    page.goto("http://localhost:8000/mind.html")

    # Step 1: Burn
    page.fill("#negative-thought", "I am weak")
    page.click("#btn-burn")

    # Step 2: Imprint (Wait for transition)
    expect(page.locator("#rewrite-step-2")).to_be_visible()
    page.fill("#positive-thought", "I am strong")

    # Handle the confirm dialog
    page.on("dialog", lambda dialog: dialog.accept())
    page.click("#btn-imprint")

    # Verify we returned to step 1
    expect(page.locator("#rewrite-step-1")).to_be_visible()

    # Verify the new thought was added to the loop
    loop_data = page.evaluate("() => localStorage.getItem('xibalba_mind_loop')")
    assert "I am strong" in loop_data
