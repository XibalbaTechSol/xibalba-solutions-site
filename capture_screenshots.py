import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    async with async_playwright() as p:
        browser = await p.chromium.launch()

        # Desktop Context
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        
        # Mobile Context
        mobile_context = await browser.new_context(
            viewport={"width": 375, "height": 667},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
        )

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
            # Desktop
            page = await context.new_page()
            await page.goto(base_path + file)
            await page.evaluate("document.fonts.ready")
            # Inject style to stop animations for screenshot stability
            await page.add_style_tag(content="""
                *, *::before, *::after {
                    animation-duration: 0s !important;
                    transition-duration: 0s !important;
                }
            """)
            await page.screenshot(path=f"screenshots/{file.replace('.html', '.png')}", full_page=True)
            print(f"Captured Desktop {file}")
            await page.close()

            # Mobile
            page_mobile = await mobile_context.new_page()
            await page_mobile.goto(base_path + file)
            await page_mobile.evaluate("document.fonts.ready")
            await page_mobile.add_style_tag(content="""
                *, *::before, *::after {
                    animation-duration: 0s !important;
                    transition-duration: 0s !important;
                }
            """)
            await page_mobile.screenshot(path=f"screenshots/mobile_{file.replace('.html', '.png')}", full_page=True)
            print(f"Captured Mobile {file}")
            await page_mobile.close()

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
