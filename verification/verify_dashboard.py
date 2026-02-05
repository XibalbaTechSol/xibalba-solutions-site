from playwright.sync_api import sync_playwright
import os

BASE_DIR = "/app"

def verify_dashboard():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Go to dashboard
        url = f"file://{os.path.join(BASE_DIR, 'dashboard.html')}"
        page.goto(url)

        # Wait for "Admin Login"
        # We look for the text specifically to ensure it rendered
        page.get_by_text("Admin Login").wait_for()

        # Take screenshot
        output_path = "/app/verification/dashboard_labels.png"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        page.screenshot(path=output_path)
        print(f"Screenshot saved to {output_path}")

        browser.close()

if __name__ == "__main__":
    verify_dashboard()
