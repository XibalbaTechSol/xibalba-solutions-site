import asyncio
from playwright.async_api import async_playwright
import os

async def capture(context, file, base_path):
    page = await context.new_page()
    await page.goto(base_path + file)
    # wait a bit for any animations
    await page.wait_for_timeout(500)
    screenshot_path = f"screenshots/{file.replace('.html', '.png')}"
    await page.screenshot(path=screenshot_path, full_page=True)
    print(f"Captured {screenshot_path}")
    await page.close()

async def main():
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Set viewport in context so all pages inherit it
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        
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
            # Wait for fonts to be ready instead of hard sleep
            page.evaluate("document.fonts.ready")
            screenshot_path = f"screenshots/{file.replace('.html', '.png')}"
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Captured {screenshot_path}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
