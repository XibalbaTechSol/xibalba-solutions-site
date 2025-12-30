import pytest
from playwright.sync_api import Page, expect

def test_index_page(page: Page):
    page.goto("file:///home/xibalbasolutions/Desktop/xibalba-solutions-site/index.html")
    expect(page).to_have_title("Xibalba Solutions | Local AI & Data Sovereignty")
    expect(page.locator("h1")).to_be_visible()

def test_about_page(page: Page):
    page.goto("file:///home/xibalbasolutions/Desktop/xibalba-solutions-site/about.html")
    expect(page).to_have_title("About Us | Xibalba Solutions")
    expect(page.locator("h1")).to_be_visible()
    expect(page.locator(".founder-avatar img")).to_be_visible()

def test_services_page(page: Page):
    page.goto("file:///home/xibalbasolutions/Desktop/xibalba-solutions-site/services.html")
    expect(page).to_have_title("Services | Xibalba Solutions")
    expect(page.locator("h1")).to_be_visible()

def test_solutions_page(page: Page):
    page.goto("file:///home/xibalbasolutions/Desktop/xibalba-solutions-site/solutions.html")
    expect(page).to_have_title("Solutions & Use Cases | Xibalba Solutions")
    expect(page.locator("h1")).to_be_visible()

def test_pricing_page(page: Page):
    page.goto("file:///home/xibalbasolutions/Desktop/xibalba-solutions-site/pricing.html")
    expect(page).to_have_title("Pricing | Xibalba Solutions")
    expect(page.locator("h1")).to_be_visible()

def test_contact_page(page: Page):
    page.goto("file:///home/xibalbasolutions/Desktop/xibalba-solutions-site/contact.html")
    expect(page).to_have_title("Contact | Xibalba Solutions")
    expect(page.locator("h1")).to_be_visible()
    # Check for form elements
    expect(page.locator("input[name='name']")).to_be_visible()
    expect(page.locator("input[name='email']")).to_be_visible()
    expect(page.locator("textarea[name='message']")).to_be_visible()
    expect(page.locator("button[type='submit']")).to_be_visible()

def test_navigation(page: Page):
    page.goto("file:///home/xibalbasolutions/Desktop/xibalba-solutions-site/index.html")
    
    # Test navigation to About
    # Clicking the link in the nav
    page.click("nav .nav-links a[href='about.html']")
    expect(page).to_have_url("file:///home/xibalbasolutions/Desktop/xibalba-solutions-site/about.html")
    
    # Test navigation back to Home
    # The logo is the link back to home
    page.click("nav .logo")
    expect(page).to_have_url("file:///home/xibalbasolutions/Desktop/xibalba-solutions-site/index.html")

def test_no_console_errors(page: Page):
    error_logs = []
    page.on("console", lambda msg: error_logs.append(msg.text) if msg.type == "error" else None)
    
    for filename in ["index.html", "about.html", "services.html", "solutions.html", "pricing.html", "contact.html"]:
        page.goto(f"file:///home/xibalbasolutions/Desktop/xibalba-solutions-site/{filename}")
    
    assert len(error_logs) == 0, f"Console errors found: {error_logs}"
