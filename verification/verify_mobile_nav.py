from playwright.sync_api import sync_playwright
import os

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # Mobile viewport
        page = browser.new_page(viewport={"width": 375, "height": 667})

        # Go to index.html
        page.goto(f"file://{os.getcwd()}/index.html")

        # Take screenshot of closed menu (to see hamburger)
        page.screenshot(path="verification/mobile_menu_closed.png")
        print("Captured mobile_menu_closed.png")

        # Click hamburger
        page.click(".hamburger")
        page.wait_for_timeout(1000) # Wait for animation

        # Take screenshot of open menu
        page.screenshot(path="verification/mobile_menu_open.png")
        print("Captured mobile_menu_open.png")

        # Click 'About' link
        # It should now be visible and clickable
        page.click(".nav-links a[href='about.html']")

        # Check if navigated
        page.wait_for_timeout(500)
        if "about.html" in page.url:
            print("Navigation successful")
        else:
            print(f"Navigation failed: {page.url}")

        page.screenshot(path="verification/mobile_nav_after_click.png")
        print("Captured mobile_nav_after_click.png")

        browser.close()

if __name__ == "__main__":
    main()
