import pytest
import os
from playwright.sync_api import Page, expect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

@pytest.fixture(autouse=True)
def mock_supabase(page: Page):
    # Mock the Supabase CDN script loading to avoid network dependency
    # and provide the global object it would have provided.
    page.route("https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2", lambda route: route.fulfill(
        status=200,
        body="window.supabase = { createClient: () => ({ auth: { getSession: async () => ({ data: { session: null } }), onAuthStateChange: () => {} } }) };",
        headers={"content-type": "application/javascript"}
    ))

def test_dashboard_login_accessibility(page: Page):
    # Capture console errors to debug
    page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))

    page.goto(get_file_url("dashboard.html"))

    # Wait for login form
    # Note: If the page crashes due to JS error, this will timeout
    expect(page.locator("#email")).to_be_visible()

    # Check accessibility
    expect(page.get_by_label("Email")).to_have_id("email")
    expect(page.get_by_label("Password")).to_have_id("password")

def test_dashboard_editor_accessibility(page: Page):
    page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))
    page.goto(get_file_url("dashboard.html"))

    # Manually trigger renderEditor to skip login
    # This requires renderEditor to be defined (script executed successfully)
    page.evaluate("renderEditor()")

    expect(page.locator("#post-title")).to_be_visible()

    # Check labels
    expect(page.get_by_label("Title")).to_have_id("post-title")
    expect(page.get_by_label("Slug (URL)")).to_have_id("post-slug")
    expect(page.get_by_label("Content (Markdown)")).to_have_id("post-content")
