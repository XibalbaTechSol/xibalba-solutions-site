#!/usr/bin/env python3
"""
Build script: Renders all .mmd Mermaid charts in /charts/ as PNG images
using Playwright + Mermaid.js with the Sovereign Obsidian theme.
"""
import os
import glob
from playwright.sync_api import sync_playwright

CHARTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "charts")

# Mermaid config matching the site's Sovereign Obsidian theme
MERMAID_CONFIG = {
    "theme": "base",
    "themeVariables": {
        "primaryColor": "#00F2FF",
        "primaryTextColor": "#00F2FF",
        "primaryBorderColor": "#00F2FF",
        "lineColor": "#FFD600",
        "secondaryColor": "#FFD600",
        "tertiaryColor": "#1e293b",
        "fontFamily": "Inter, Raleway, sans-serif",
        "fontSize": "14px",
        "nodeBorder": "#00F2FF",
        "mainBkg": "#0f1724",
        "clusterBkg": "#1a2332",
        "clusterBorder": "#333",
        "titleColor": "#00F2FF",
        "edgeLabelBackground": "#0f1724",
        "nodeTextColor": "#e0e0e0",
    }
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  body {{
    background: #0a0e17;
    margin: 0;
    padding: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
  }}
  #chart {{
    background: rgba(15, 23, 36, 0.95);
    padding: 3rem;
    border-radius: 24px;
    border: 1px solid #333;
    display: inline-block;
  }}
  /* Override Mermaid text colors for dark theme */
  .node rect, .node polygon, .node circle {{
    stroke: #00F2FF !important;
    stroke-width: 2px !important;
  }}
  .edgeLabel {{
    background-color: #0f1724 !important;
    color: #e0e0e0 !important;
  }}
</style>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.min.js"></script>
</head>
<body>
<div id="chart" class="mermaid">
{chart_content}
</div>
<script>
  mermaid.initialize({{
    startOnLoad: true,
    theme: 'base',
    themeVariables: {{
      primaryColor: '#00F2FF',
      primaryTextColor: '#00F2FF',
      primaryBorderColor: '#00F2FF',
      lineColor: '#FFD600',
      secondaryColor: '#FFD600',
      tertiaryColor: '#1e293b',
      fontFamily: 'Inter, Raleway, sans-serif',
      fontSize: '14px',
      nodeBorder: '#00F2FF',
      mainBkg: '#0f1724',
      clusterBkg: '#1a2332',
      clusterBorder: '#333',
      titleColor: '#00F2FF',
      edgeLabelBackground: '#0f1724',
      nodeTextColor: '#e0e0e0'
    }}
  }});
</script>
</body>
</html>"""


def build_charts():
    mmd_files = sorted(glob.glob(os.path.join(CHARTS_DIR, "*.mmd")))
    if not mmd_files:
        print("No .mmd files found in charts/")
        return

    print(f"Found {len(mmd_files)} charts to render...")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1400, "height": 900})

        for mmd_path in mmd_files:
            basename = os.path.splitext(os.path.basename(mmd_path))[0]
            png_path = os.path.join(CHARTS_DIR, f"{basename}.png")
            svg_path = os.path.join(CHARTS_DIR, f"{basename}.svg")

            with open(mmd_path, "r", encoding="utf-8") as f:
                chart_content = f.read().strip()

            # Build the HTML page with the chart
            html = HTML_TEMPLATE.format(chart_content=chart_content)
            tmp_html = os.path.join(CHARTS_DIR, "_tmp_render.html")
            with open(tmp_html, "w", encoding="utf-8") as f:
                f.write(html)

            try:
                page.goto(f"file://{tmp_html}")
                page.wait_for_selector(".mermaid svg", timeout=10000)
                # Small extra wait for fonts/animations
                page.wait_for_timeout(500)

                chart_el = page.query_selector("#chart")
                if chart_el:
                    # Save PNG
                    chart_el.screenshot(path=png_path)

                    # Save SVG source
                    svg_content = page.evaluate("""
                        () => {
                            const svg = document.querySelector('#chart svg');
                            return svg ? svg.outerHTML : null;
                        }
                    """)
                    if svg_content:
                        with open(svg_path, "w", encoding="utf-8") as f:
                            f.write(svg_content)

                    print(f"  ✓ {basename}.png + .svg")
                else:
                    print(f"  ✗ {basename} — chart element not found")

            except Exception as e:
                print(f"  ✗ {basename} — {e}")

        # Cleanup
        tmp_html = os.path.join(CHARTS_DIR, "_tmp_render.html")
        if os.path.exists(tmp_html):
            os.remove(tmp_html)

        browser.close()

    print(f"\nDone! Images saved to {CHARTS_DIR}")


if __name__ == "__main__":
    build_charts()
