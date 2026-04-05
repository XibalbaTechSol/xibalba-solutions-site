import os
import glob
from bs4 import BeautifulSoup

def main():
    base_dir = "/home/xibalba/Projects/xibalba-solutions-site"
    charts_dir = os.path.join(base_dir, "charts")
    os.makedirs(charts_dir, exist_ok=True)
    
    html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)
    
    count = 0
    for filepath in html_files:
        # Skip files in charts directory if any
        if "/charts/" in filepath:
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
            mermaids = soup.find_all("div", class_="mermaid")
            
            for i, mermaid in enumerate(mermaids):
                rel_path = os.path.relpath(filepath, base_dir)
                chart_text = mermaid.get_text(strip=False).strip()
                
                # Create a safe filename
                safe_name = rel_path.replace(os.sep, "_").replace(".html", "")
                chart_filename = f"{safe_name}_chart_{i}.mmd"
                chart_path = os.path.join(charts_dir, chart_filename)
                
                with open(chart_path, 'w', encoding='utf-8') as out:
                    out.write(chart_text)
                
                print(f"Extracted: {chart_filename} from {rel_path}")
                count += 1
                
    print(f"\nSuccessfully extracted {count} Mermaid charts to {charts_dir}")

if __name__ == "__main__":
    main()
