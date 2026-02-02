from playwright.sync_api import sync_playwright
import os

def capture_screenshots():
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        
        files = [
            "index.html", 
            "about.html", 
            "services.html", 
            "solutions.html", 
            "pricing.html", 
            "contact.html"
        ]
        
        base_path = f"file://{os.getcwd()}/"
        
        for file in files:
            page.goto(base_path + file)
            # Disable animations for faster and deterministic screenshots
            page.add_style_tag(content="*, *::before, *::after { animation-duration: 0s !important; transition: none !important; }")
            screenshot_path = f"screenshots/{file.replace('.html', '.png')}"
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Captured {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    capture_screenshots()
