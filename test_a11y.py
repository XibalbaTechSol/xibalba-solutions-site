import os
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        abs_path = os.path.abspath("contact.html")
        await page.goto(f"file://{abs_path}")

        # Test keyboard accessibility
        for _ in range(9):
            await page.keyboard.press("Tab")
            focused_html = await page.evaluate("document.activeElement.outerHTML")
            print("Focused:", focused_html[:100], "...")

        await browser.close()

asyncio.run(main())
