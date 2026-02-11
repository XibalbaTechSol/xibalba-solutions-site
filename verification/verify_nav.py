from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{os.path.join(cwd, 'index.html')}"

        page.goto(file_path)

        # Set viewport to mobile
        page.set_viewport_size({"width": 375, "height": 667})

        hamburger = page.locator(".hamburger")

        # Initial state check
        expanded_initial = hamburger.get_attribute("aria-expanded")
        controls_initial = hamburger.get_attribute("aria-controls")
        print(f"Initial aria-expanded: {expanded_initial}")
        print(f"Initial aria-controls: {controls_initial}")

        # Click to open
        hamburger.click()
        page.wait_for_timeout(500) # Wait for animation

        # Expanded state check
        expanded_open = hamburger.get_attribute("aria-expanded")
        print(f"Open aria-expanded: {expanded_open}")

        # Take screenshot of open menu
        page.screenshot(path="verification/mobile_nav_open.png")

        # Click to close
        hamburger.click()
        page.wait_for_timeout(500)

        # Collapsed state check
        expanded_closed = hamburger.get_attribute("aria-expanded")
        print(f"Closed aria-expanded: {expanded_closed}")

        browser.close()

if __name__ == "__main__":
    run()
