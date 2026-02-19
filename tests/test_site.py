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

def test_contact_form_submission_state(page: Page):
    page.goto(get_file_url("contact.html"))

    # Fill out the form
    page.fill("input[name='name']", "Test User")
    page.fill("input[name='email']", "test@example.com")
    page.fill("textarea[name='message']", "This is a test message.")

    # Inject a listener to capture the state AFTER the main.js handler has run
    # and prevent the actual submission so the page doesn't unload.
    page.evaluate("""
        const form = document.querySelector('form');
        form.addEventListener('submit', (e) => {
            // Capture the state of the button
            const btn = form.querySelector('button[type="submit"]');
            window._btnText = btn.innerText;
            window._btnDisabled = btn.disabled;
            window._btnOpacity = btn.style.opacity;
            window._btnCursor = btn.style.cursor;

            // Prevent actual submission to keep the page state
            e.preventDefault();
        });
    """)

    submit_btn = page.locator("button[type='submit']")
    submit_btn.click()

    # Retrieve captured values
    btn_text = page.evaluate("window._btnText")
    btn_disabled = page.evaluate("window._btnDisabled")
    btn_opacity = page.evaluate("window._btnOpacity")
    btn_cursor = page.evaluate("window._btnCursor")

    # Assertions
    assert btn_text == "Sending...", f"Expected 'Sending...', got '{btn_text}'"
    assert btn_disabled is True, "Button should be disabled"
    assert btn_opacity == "0.7", f"Expected opacity '0.7', got '{btn_opacity}'"
    assert btn_cursor == "wait", f"Expected cursor 'wait', got '{btn_cursor}'"
