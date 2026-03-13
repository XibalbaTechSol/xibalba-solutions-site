from playwright.sync_api import Page, expect, sync_playwright
import os

BASE_DIR = '/app'

def verify_feature(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})
    url = f"file://{os.path.join(BASE_DIR, 'index.html')}"
    page.goto(url)
    page.wait_for_timeout(500)

    hamburger = page.locator('.hamburger')

    # Check initial state
    aria_expanded = hamburger.get_attribute('aria-expanded')
    print(f"Initial aria-expanded: {aria_expanded}")
    assert aria_expanded == "false"
    page.screenshot(path="/home/jules/verification/initial_state.png")

    # Click to open
    hamburger.click()
    page.wait_for_timeout(500)
    aria_expanded = hamburger.get_attribute('aria-expanded')
    print(f"After click aria-expanded: {aria_expanded}")
    assert aria_expanded == "true"
    page.screenshot(path="/home/jules/verification/opened_state.png")

    # Click to close
    hamburger.click()
    page.wait_for_timeout(500)
    aria_expanded = hamburger.get_attribute('aria-expanded')
    print(f"After second click aria-expanded: {aria_expanded}")
    assert aria_expanded == "false"
    page.screenshot(path="/home/jules/verification/closed_state.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(record_video_dir="/home/jules/verification/video")
        page = context.new_page()
        try:
            verify_feature(page)
        finally:
            context.close()  # Important: close context to save the video
            browser.close()
