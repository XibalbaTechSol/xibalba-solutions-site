from playwright.sync_api import sync_playwright
import os

def test_aria_expanded():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Adjust viewport to mobile
        page.set_viewport_size({"width": 375, "height": 667})

        # Load local index.html
        file_path = os.path.abspath("index.html")
        page.goto(f"file://{file_path}")

        hamburger = page.locator(".hamburger")

        # Check initial state
        initial_expanded = hamburger.get_attribute("aria-expanded")
        print(f"Initial aria-expanded: {initial_expanded}")
        assert initial_expanded == "false"

        # Click to open
        hamburger.click()

        # Check expanded state
        expanded_after_click = hamburger.get_attribute("aria-expanded")
        print(f"Expanded after click: {expanded_after_click}")
        assert expanded_after_click == "true"

        # Click to close
        hamburger.click()

        # Check closed state
        closed_after_click = hamburger.get_attribute("aria-expanded")
        print(f"Closed after click: {closed_after_click}")
        assert closed_after_click == "false"

        browser.close()

if __name__ == "__main__":
    try:
        test_aria_expanded()
        print("✅ ARIA expanded test passed!")
    except AssertionError as e:
        print(f"❌ ARIA expanded test failed: {e}")
        exit(1)
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        exit(1)
