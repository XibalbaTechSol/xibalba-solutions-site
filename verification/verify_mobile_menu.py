import os
from playwright.sync_api import sync_playwright, expect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_file_url(filename):
    return f"file://{os.path.join(BASE_DIR, filename)}"

def verify_mobile_menu(page):
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto(get_file_url("index.html"))

    hamburger = page.locator(".hamburger")

    # 1. Take screenshot of closed menu (hamburger visible)
    page.screenshot(path="verification/mobile_menu_closed.png")

    # 2. Click hamburger
    hamburger.click()

    # 3. Wait for menu to appear (animation)
    page.wait_for_timeout(500) # Wait for animation

    # 4. Take screenshot of open menu
    page.screenshot(path="verification/mobile_menu_open.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_mobile_menu(page)
            print("Screenshots taken successfully.")
        finally:
            browser.close()
