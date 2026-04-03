# Xibalba Solutions | Sovereign AI Intelligence

Official website for **Xibalba Solutions**, a specialized engineering firm dedicated to building custom Hermes-based AI agents and deploying HIPAA-compliant local AI infrastructure.

## Overview

Xibalba Solutions focuses on **Sovereign Intelligence**—AI that lives on your hardware, not in the cloud. We specialize in:
- **Custom Hermes Agents**: Autonomous intelligence layers powered by Hermes 3 with high-fidelity, predictive interfaces.
- **Enterprise Local AI**: Secure, HIPAA-compliant, and audit-ready on-premise AI deployments for healthcare, legal, and sensitive sectors.
- **OpenClaw Integration**: Leveraging the OpenClaw framework for local task execution and omnichannel interaction.

The site is built with a high-fidelity, privacy-first aesthetic, featuring immersive UI elements like 3D orbs and real-time observability simulations.

## Structure

- `index.html`: Main landing page with OpenClaw and Hermes integration highlights.
- `about.html`: Our mission for data sovereignty and sovereign intelligence.
- `ai-agents.html`: Details on Hermes 3 foundation, Specialist model, and Learning Loops.
- `local-ai.html`: Focus on HIPAA/GDPR compliance and Sanctum Guard architecture.
- `pricing.html`: Transparent service-based pricing for builds and ongoing support.
- `contact.html`: Self-hosted contact inquiry system.
- `server.py`: Custom Python server for static file serving and secure form handling.
- `css/style.css`: Advanced UI styling with pulsing glows and immersive animations.

## Development

### Prerequisites

- Python 3.12+
- SMTP server access (for contact form functionality)

### Local Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/xibalba-solutions-site.git
    cd xibalba-solutions-site
    ```

2.  **Configure Environment:**
    Rename `.env.example` to `.env` and fill in your SMTP credentials to enable the contact form.
    ```bash
    cp .env.example .env
    ```

3.  **Run locally:**
    Launch the integrated server to serve the site and handle form submissions:
    ```bash
    python3 server.py
    ```
    Visit `http://localhost:8000` in your browser.

### Running Tests

End-to-end validation is handled via Playwright:

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

While the site can be hosted on static platforms (GitHub Pages, Netlify), the **contact form requires a Python backend**. For full functionality, deploy to a sovereign VPS or a containerized environment (Docker) capable of running `server.py`.

## License

All rights reserved. © 2025 Xibalba Solutions.
