#!/bin/bash

# Xibalba Solutions: Master UI/UX Validation Script
# Performs Playwright testing and Screenshot verification.

PROJECT_ROOT=$(pwd)
TEST_DIR="$PROJECT_ROOT/tests/playwright"
SCREENSHOT_DIR="$PROJECT_ROOT/reports/screenshots"
VENV_PYTHON="/home/xibalba/Projects/integrity-protocol/venv/bin/python3"
PYTEST="/home/xibalba/Projects/integrity-protocol/venv/bin/pytest"

mkdir -p "$SCREENSHOT_DIR"

echo "[*] Starting Xibalba Solutions Master Validation..."
echo "[*] Environment: Headless Playwright / Chromium"

# 1. Run Automated Tests
echo -e "\n[*] Phase 1: Executing UI/UX Assertion Suite..."
$PYTEST "$TEST_DIR" -v

# 2. Perform Visual Artifact Capture (Screenshots)
echo -e "\n[*] Phase 2: Generating Visual Evidence (Screenshots)..."

pages=("index.html" "ai-agents.html" "integrity-protocol.html" "whitepaper.html" "business-plan.html" "blog.html")

for page in "${pages[@]}"; do
    echo "  -> Capturing $page..."
    $VENV_PYTHON -c "
from playwright.sync_api import sync_playwright
import os
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1440, 'height': 900})
    abs_path = os.path.abspath('$page')
    page.goto(f'file://{abs_path}')
    # Wait for Mermaid and KaTeX to render
    page.wait_for_timeout(2000) 
    page.screenshot(path='$SCREENSHOT_DIR/${page%.html}.png', full_page=True)
    browser.close()
"
done

echo -e "\n[SUCCESS] Validation Complete."
echo "[*] Reports saved to: $SCREENSHOT_DIR"
