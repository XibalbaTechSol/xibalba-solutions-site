import os
from bs4 import BeautifulSoup

# HTML Fragments
NAV_LINKS_HTML = """
<a href="about.html">About</a>
<a href="solutions.html">Solutions</a>
<a href="products.html">Products</a>
<a href="hardware.html">Hardware</a>
<a href="pricing.html">Pricing</a>
<a href="blog.html">Blog</a>
<a href="community.html">Community</a>
<a href="investors.html" class="nav-item-investor">Investors</a>
<a href="services.html" class="nav-item-services">Services</a>
<a href="schedule.html" class="btn-outline" style="margin-right: 0.5rem;">Schedule</a>
<a href="contact.html" class="btn-outline">Contact</a>
"""

SOCIAL_ICONS_HTML = """
<div class="footer-social" style="justify-content: center; margin-bottom: 2rem;">
    <!-- GitHub -->
    <a href="https://github.com/xibalba-solutions" target="_blank" aria-label="GitHub">
        <svg viewBox="0 0 16 16"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
    </a>
    <!-- LinkedIn -->
    <a href="#" target="_blank" aria-label="LinkedIn">
        <svg viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
    </a>
    <!-- X (Twitter) -->
    <a href="#" target="_blank" aria-label="X">
        <svg viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
    </a>
</div>
"""

COMMUNITY_COL_HTML = """
<div class="sitemap-col">
    <h4>Community</h4>
    <ul>
        <li><a href="blog.html">Blog</a></li>
        <li><a href="community.html">Open Source</a></li>
        <li><a href="schedule.html">Schedule Meeting</a></li>
        <li><a href="dashboard.html" style="opacity: 0.5; font-size: 0.8rem;">Admin Login</a></li>
    </ul>
</div>
"""

META_DESCRIPTION = "Xibalba Solutions provides high-dimensional surgical robotics data, secure HIPAA-compliant local AI, and specialized software engineering for the future of autonomous surgery."

def update_file(filepath):
    print(f"Updating {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # 1. Update Navigation
    nav_links = soup.find(class_='nav-links')
    if nav_links:
        # Clear existing
        nav_links.clear()
        # Parse new HTML and append
        new_nav_soup = BeautifulSoup(NAV_LINKS_HTML, 'html.parser')
        # We need to append the tags, not the root soup object if possible to keep it clean
        # But appending soup object usually works in BS4, it appends children.
        # However, new_nav_soup is a document.
        for element in list(new_nav_soup.contents):
            if element.name:
                nav_links.append(element)

    # 2. Update Footer Sitemap
    footer_sitemap = soup.find(class_='footer-sitemap')
    if footer_sitemap:
        # Check if Community col already exists
        if "Community" not in str(footer_sitemap):
            new_col_soup = BeautifulSoup(COMMUNITY_COL_HTML, 'html.parser')
            # Use the first child (div)
            col_div = new_col_soup.div
            if col_div:
                 footer_sitemap.append(col_div)

    # 3. Add Social Icons
    footer_container = soup.find('footer').find(class_='container') if soup.find('footer') else None
    if footer_container:
        footer_bottom = footer_container.find(class_='footer-bottom')
        # Check if social icons already exist
        if not footer_container.find(class_='footer-social'):
            social_soup = BeautifulSoup(SOCIAL_ICONS_HTML, 'html.parser')
            social_div = social_soup.div
            # Insert before footer-bottom
            if footer_bottom and social_div:
                footer_bottom.insert_before(social_div)
            elif social_div:
                footer_container.append(social_div)

    # 4. Add Meta Tags
    head = soup.head
    if head:
        # Description
        if not head.find('meta', attrs={'name': 'description'}):
            desc_tag = soup.new_tag('meta', attrs={'name': 'description', 'content': META_DESCRIPTION})
            head.append(desc_tag)

        # OG Title
        if not head.find('meta', attrs={'property': 'og:title'}):
            title = soup.title.string if soup.title else "Xibalba Solutions"
            og_title = soup.new_tag('meta', attrs={'property': 'og:title', 'content': title})
            head.append(og_title)

        # OG Description
        if not head.find('meta', attrs={'property': 'og:description'}):
            og_desc = soup.new_tag('meta', attrs={'property': 'og:description', 'content': META_DESCRIPTION})
            head.append(og_desc)

    with open(filepath, 'w', encoding='utf-8') as f:
        # prettify can sometimes mess up formatting, so str() is safer if original formatting was okay,
        # but BS4 modifies the tree so it might be messy anyway.
        # str(soup) is usually best for minimal diffs.
        f.write(str(soup))

if __name__ == "__main__":
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    for f in files:
        update_file(f)
