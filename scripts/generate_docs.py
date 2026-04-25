import os
import asyncio
import markdown
import sys
import base64
from playwright.async_api import async_playwright

# --- Configuration ---
DOCS_DIR = "docs"
FILES = [
    ("business-plan.md", "business-plan.pdf"),
    ("whitepaper.md", "whitepaper.pdf")
]
# Use the new logo if it exists, otherwise fallback to the black one
NEW_LOGO = os.path.join(DOCS_DIR, "XibalbaSolutionsLogo_v2.png")
if os.path.exists(NEW_LOGO):
    LOGO_PATH = NEW_LOGO
else:
    LOGO_PATH = os.path.join(DOCS_DIR, "logo-black.png")
CSS_PATH = os.path.join(DOCS_DIR, "pdf-styles.css")

def get_base64_image(image_path):
    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        return None
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

async def generate_pdf(src_md, dest_pdf):
    print(f"Converting {src_md} to {dest_pdf}...")
    
    # Check if files exist
    md_path = os.path.join(DOCS_DIR, src_md)
    if not os.path.exists(md_path):
        print(f"Error: {md_path} not found.")
        return

    with open(md_path, 'r') as f:
        md_content = f.read()

    # Read CSS and Logo
    try:
        if not os.path.exists(CSS_PATH):
            print(f"Warning: CSS not found at {CSS_PATH}")
            css_content = ""
        else:
            with open(CSS_PATH, "r") as f:
                css_content = f.read()
        
        logo_base64 = get_base64_image(LOGO_PATH)
        if not logo_base64:
            logo_html = ""
        else:
            logo_html = f'<img src="data:image/png;base64,{logo_base64}" alt="Xibalba Solutions" class="pdf-logo">'
            
    except Exception as e:
        print(f"Error loading assets: {e}")
        return

    # Convert Markdown to HTML
    html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'codehilite'])
    
    # Create full HTML with in-lined assets
    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <style>
            {css_content}
        </style>
    </head>
    <body>
        <div class="pdf-header">
            {logo_html}
        </div>
        <div class="content">
            {html_body}
        </div>
        <div class="pdf-footer">
            <p>© 2026 Xibalba Solutions. All rights reserved.</p>
            <p>"We don't build the agents. We verify their worth."</p>
        </div>
    </body>
    </html>
    """

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        
        # We set the content
        await page.set_content(full_html)
        
        # Crucial: Wait for Raleway to load from Google Fonts
        print("Waiting for fonts to load...")
        try:
            # Wait for the network to be idle to ensure external fonts are fetched
            await page.wait_for_load_state("networkidle")
            # Specifically check if fonts are ready
            await page.evaluate("document.fonts.ready")
        except Exception as e:
            print(f"Font loading timed out or failed, proceeding anyway: {e}")

        # Small additional delay for rendering
        await asyncio.sleep(2)

        # Output to PDF
        pdf_path = os.path.join(DOCS_DIR, dest_pdf)
        await page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "0cm", "bottom": "0cm", "left": "0cm", "right": "0cm"},
            display_header_footer=False
        )
        
        await browser.close()
        print(f"Successfully generated {pdf_path}")

async def main():
    for src, dest in FILES:
        await generate_pdf(src, dest)

if __name__ == "__main__":
    asyncio.run(main())
