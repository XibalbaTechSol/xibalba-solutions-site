import pytest
import os
from playwright.sync_api import Page, expect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

@pytest.fixture(autouse=True)
def check_console_errors(page: Page):
    error_logs = []
    page.on("console", lambda msg: error_logs.append(msg.text) if msg.type == "error" else None)
    yield
    assert len(error_logs) == 0, f"Console errors found: {error_logs}"

def test_index_page(page: Page):
    page.goto(get_file_url("index.html"))
    # Updated title
    expect(page).to_have_title("Xibalba Solutions | Surgical Robotics Data")
    expect(page.locator("h1")).to_be_visible()
    # Check for investors link existence
    expect(page.locator("a[href='investors.html']").first).to_be_visible()
    # Check for new Recurring Revenue text
    expect(page.locator("body")).to_contain_text("Secure Local AI")

def test_about_page(page: Page):
    page.goto(get_file_url("about.html"))
    expect(page).to_have_title("About Us | Xibalba Solutions")
    expect(page.locator("h1")).to_be_visible()
    expect(page.locator(".founder-avatar img")).to_be_visible()

def test_services_page(page: Page):
    page.goto(get_file_url("services.html"))
    # Updated title
    expect(page).to_have_title("Secure AI & Software Services | Xibalba Solutions")
    expect(page.locator("h1")).to_be_visible()
    # Check for new content
    expect(page.locator("body")).to_contain_text("Secure Local AI & HIPAA Compliance")

def test_solutions_page(page: Page):
    page.goto(get_file_url("solutions.html"))
    expect(page).to_have_title("Solutions & Use Cases | Xibalba Solutions")
    expect(page.locator("h1")).to_be_visible()

def test_pricing_page(page: Page):
    page.goto(get_file_url("pricing.html"))
    expect(page).to_have_title("Pricing | Xibalba Solutions")
    expect(page.locator("h1")).to_be_visible()

def test_contact_page(page: Page):
    page.goto(get_file_url("contact.html"))
    expect(page).to_have_title("Contact | Xibalba Solutions")
    expect(page.locator("h1")).to_be_visible()
    # Check for form elements
    expect(page.locator("input[name='name']")).to_be_visible()
    expect(page.locator("input[name='email']")).to_be_visible()
    expect(page.locator("textarea[name='message']")).to_be_visible()
    expect(page.locator("button[type='submit']")).to_be_visible()

def test_investors_page(page: Page):
    page.goto(get_file_url("investors.html"))
    expect(page).to_have_title("Investors | Xibalba Solutions")
    expect(page.locator("h1")).to_be_visible()
    expect(page.locator("h1")).to_contain_text("Surgical Robotics")

def test_navigation(page: Page):
    page.goto(get_file_url("index.html"))
    
    # Test navigation to About
    # Clicking the link in the nav
    page.click("nav .nav-links a[href='about.html']")
    expect(page).to_have_url(get_file_url("about.html"))
    
    # Test navigation back to Home
    # The logo is the link back to home
    page.click("nav .logo")
    expect(page).to_have_url(get_file_url("index.html"))

    # Test navigation to Investors
    page.click("nav .nav-links a[href='investors.html']")
    expect(page).to_have_url(get_file_url("investors.html"))

