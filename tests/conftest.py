import pytest
from playwright.sync_api import Page

@pytest.fixture(autouse=True)
def check_console_errors(page: Page):
    error_logs = []
    page.on("console", lambda msg: error_logs.append(msg.text) if msg.type == "error" else None)
    yield
    assert len(error_logs) == 0, f"Console errors found: {error_logs}"
