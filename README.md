# Xibalba Solutions Website

This is the official website for **Xibalba Solutions**, a consultancy firm specializing in local AI infrastructure, data sovereignty, and secure on-premise intelligence systems.

## Overview

The website is a static HTML/CSS site designed to be lightweight, fast, and privacy-focused, mirroring the company's ethos. It features a modern, clean aesthetic using the "Nord" color palette and responsive design principles.

## Structure

- `index.html`: Home page with value propositions and overview.
- `about.html`: Company mission, leadership, and vision.
- `services.html`: Detailed breakdown of services (Hardware, RAG, Fine-tuning).
- `solutions.html`: Use cases across various industries.
- `pricing.html`: Transparent pricing models.
- `contact.html`: Contact form and information.
- `css/style.css`: Main stylesheet source.
- `tests/`: End-to-end tests using Playwright.

## Visual Reference

| Home | About |
|:---:|:---:|
| <img src="screenshots/index.png" width="400"> | <img src="screenshots/about.png" width="400"> |

| Services | Solutions |
|:---:|:---:|
| <img src="screenshots/services.png" width="400"> | <img src="screenshots/solutions.png" width="400"> |

| Pricing | Contact |
|:---:|:---:|
| <img src="screenshots/pricing.png" width="400"> | <img src="screenshots/contact.png" width="400"> |

## Development

### Prerequisites

- Python 3.12+ (for testing and local server)
- Playwright (for running tests)

### Local Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/xibalba-solutions-site.git
    cd xibalba-solutions-site
    ```

2.  **Run locally:**
    You can serve the site using Python's built-in HTTP server:
    ```bash
    python3 -m http.server 8000
    ```
    Then visit `http://localhost:8000` in your browser.

### Running Tests

To ensure the site functions correctly, you can run the included Playwright tests:

1.  **Install dependencies:**
    ```bash
    pip install pytest playwright pytest-playwright
    playwright install chromium
    ```

2.  **Run tests:**
    ```bash
    pytest
    ```

## Deployment

This site is static and can be deployed to any static hosting provider such as:

- **GitHub Pages**: Push to a `gh-pages` branch or configure via Settings.
- **Netlify**: Drag and drop the folder or connect your repo.
- **Vercel**: Connect your Git repo and deploy.

## License

All rights reserved. © 2025 Xibalba Solutions.
