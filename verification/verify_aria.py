from playwright.sync_api import sync_playwright
import os

BASE_DIR = '/app'

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 375, "height": 667})

        url = f"file://{os.path.join(BASE_DIR, 'index.html')}"
        page.goto(url)

        hamburger = page.locator('.hamburger')

        # Initial state should be false
        aria_expanded = hamburger.get_attribute('aria-expanded')
        print(f"Initial aria-expanded: {aria_expanded}")
        assert aria_expanded == "false"

        # Click to open
        hamburger.click()
        aria_expanded = hamburger.get_attribute('aria-expanded')
        print(f"After click aria-expanded: {aria_expanded}")
        assert aria_expanded == "true"

        # Click to close
        hamburger.click()
        aria_expanded = hamburger.get_attribute('aria-expanded')
        print(f"After second click aria-expanded: {aria_expanded}")
        assert aria_expanded == "false"

        print("Verification passed!")
        browser.close()

if __name__ == '__main__':
    run()
