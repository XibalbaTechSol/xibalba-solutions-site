import os
import pytest
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_dashboard_login_labels_static():
    filepath = os.path.join(BASE_DIR, "dashboard.html")
    with open(filepath, "r") as f:
        content = f.read()

    # Extract the renderLogin function body
    render_login_match = re.search(r'function renderLogin\(\) \{([\s\S]*?)\}', content)
    assert render_login_match, "renderLogin function not found"
    render_login_body = render_login_match.group(1)

    # Check for visible labels.
    if '<label' not in render_login_body:
        pytest.fail("No <label> tags found in renderLogin function. UX requirement: Inputs must have visible labels.")

    # If labels exist, check they are correct
    assert 'for="email"' in render_login_body, "Email label missing or not associated correctly"
    assert 'for="password"' in render_login_body, "Password label missing or not associated correctly"
    assert 'id="login-submit-btn"' in render_login_body, "Login button should have id='login-submit-btn'"

def test_dashboard_signup_labels_static():
    filepath = os.path.join(BASE_DIR, "dashboard.html")
    with open(filepath, "r") as f:
        content = f.read()

    # Extract the renderSignup function body
    render_signup_match = re.search(r'function renderSignup\(\) \{([\s\S]*?)\}', content)
    assert render_signup_match, "renderSignup function not found"
    render_signup_body = render_signup_match.group(1)

    if '<label' not in render_signup_body:
        pytest.fail("No <label> tags found in renderSignup function. UX requirement: Inputs must have visible labels.")

    assert 'for="email"' in render_signup_body
    assert 'for="password"' in render_signup_body
    assert 'id="signup-submit-btn"' in render_signup_body, "Signup button should have id='signup-submit-btn'"

def test_dashboard_loading_state_static():
    filepath = os.path.join(BASE_DIR, "dashboard.html")
    with open(filepath, "r") as f:
        content = f.read()

    # Check handleLogin for button disabling and correct ID
    handle_login_match = re.search(r'async function handleLogin\(e\) \{([\s\S]*?)\}', content)
    assert handle_login_match
    handle_login_body = handle_login_match.group(1)

    if 'disabled' not in handle_login_body:
         pytest.fail("handleLogin does not seem to disable the button (no 'disabled' keyword found).")

    assert 'login-submit-btn' in handle_login_body, "handleLogin should use 'login-submit-btn'"

    # Check handleSignup for button disabling and correct ID
    handle_signup_match = re.search(r'async function handleSignup\(e\) \{([\s\S]*?)\}', content)
    assert handle_signup_match
    handle_signup_body = handle_signup_match.group(1)

    if 'disabled' not in handle_signup_body:
         pytest.fail("handleSignup does not seem to disable the button (no 'disabled' keyword found).")

    assert 'signup-submit-btn' in handle_signup_body, "handleSignup should use 'signup-submit-btn'"
