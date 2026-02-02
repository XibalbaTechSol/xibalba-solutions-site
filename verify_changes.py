from playwright.sync_api import sync_playwright
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR == "/home/jules/verification":
    BASE_DIR = "/app" # Assuming /app is the repo root in the sandbox if the script is in verification/

def get_file_url(filename):
    return f"file://{os.path.join(os.getcwd(), filename)}"

def verify_changes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Verify Index
        page.goto(get_file_url("index.html"))
        page.screenshot(path="/home/jules/verification/index.png", full_page=True)
        print("Captured index.png")

        # Verify Investors
        page.goto(get_file_url("investors.html"))
        page.screenshot(path="/home/jules/verification/investors.png", full_page=True)
        print("Captured investors.png")

        # Verify Services
        page.goto(get_file_url("services.html"))
        page.screenshot(path="/home/jules/verification/services.png", full_page=True)
        print("Captured services.png")

        browser.close()

if __name__ == "__main__":
    verify_changes()
