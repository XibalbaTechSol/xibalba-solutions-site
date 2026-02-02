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

def test_second_brain_page(page: Page):
    page.goto(get_file_url("second-brain.html"))
    expect(page).to_have_title("Second Brain | AI Goal Completion")
    expect(page.locator("h1")).to_contain_text("Turn Thoughts into")
    expect(page.locator("body")).to_contain_text("Gemini AI")
    # Expect login form or loading state since it's dynamic now
    # We accept "Loading Second Brain..." because Supabase might not connect in the test env
    expect(page.locator("body")).to_contain_text("Loading Second Brain")

def test_blog_index(page: Page):
    page.goto(get_file_url("blog.html"))
    expect(page).to_have_title("Blog | Xibalba Solutions")
    expect(page.locator("h2")).to_contain_text("Introducing Second Brain")
    # Click the link to the post
    page.click("a[href='blog/intro-to-second-brain.html']")
    expect(page).to_have_url(get_file_url("blog/intro-to-second-brain.html"))

def test_blog_post(page: Page):
    page.goto(get_file_url("blog/intro-to-second-brain.html"))
    expect(page).to_have_title("Introducing Second Brain | Xibalba Solutions Blog")
    expect(page.locator("h1")).to_contain_text("Introducing Second Brain")
    expect(page.locator("body")).to_contain_text("Frictionless Experience")
    # Check navigation back to blog index
    # Note: The nav link to blog is "Blog" -> "../blog.html"
    page.click("nav .nav-links a[href='../blog.html']")
    expect(page).to_have_url(get_file_url("blog.html"))

def test_products_page_link(page: Page):
    page.goto(get_file_url("products.html"))
    # Check for Second Brain section
    expect(page.locator("h2", has_text="Second Brain")).to_be_visible()
    # Click the link
    page.click("a[href='second-brain.html']")
    expect(page).to_have_url(get_file_url("second-brain.html"))
