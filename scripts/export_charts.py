import os
import asyncio
import glob
from playwright.async_api import async_playwright

async def export_charts():
    base_dir = "/home/xibalba/Projects/xibalba-solutions-site"
    output_dir = os.path.expanduser("~/charts")
    os.makedirs(output_dir, exist_ok=True)
    
    html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        for filepath in html_files:
            rel_path = os.path.relpath(filepath, base_dir)
            file_url = f"file://{filepath}"
            print(f"Processing {rel_path}...")
            
            try:
                await page.goto(file_url)
                # Wait for mermaid to render (usually svg is created inside div.mermaid)
                await page.wait_for_selector(".mermaid svg", timeout=5000)
                
                # Find all mermaid divs
                mermaid_elements = await page.query_selector_all(".mermaid")
                
                for i, element in enumerate(mermaid_elements):
                    chart_id = rel_path.replace("/", "_").replace(".html", "")
                    filename = f"{chart_id}_chart_{i}.png"
                    output_path = os.path.join(output_dir, filename)
                    
                    # Take screenshot of the component
                    await element.screenshot(path=output_path)
                    print(f"  Saved {filename}")
                    
            except Exception as e:
                print(f"  No rendering found or error in {rel_path}: {e}")
                
        await browser.close()
    
    print(f"\nAll charts exported to {output_dir}")

if __name__ == "__main__":
    asyncio.run(export_charts())
