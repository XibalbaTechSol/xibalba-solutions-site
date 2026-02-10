import os
import re
import pytest

def test_dashboard_has_labels():
    """
    Statically analyzes dashboard.html to ensure login, signup, and editor forms
    have proper labels associated with inputs.
    """
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'dashboard.html')
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for login/signup labels
    # We expect <label for="email">Email</label> and <label for="password">Password</label>
    # Note: These might appear twice (once for login, once for signup)

    assert re.search(r'<label\s+for="email"[^>]*>Email</label>', content), "Login/Signup form missing Email label"
    assert re.search(r'<label\s+for="password"[^>]*>Password</label>', content), "Login/Signup form missing Password label"

    # Check for editor labels
    # We expect <label for="post-title">, <label for="post-slug">, <label for="post-content">
    assert re.search(r'<label\s+for="post-title"[^>]*>Title</label>', content), "Editor form missing Title label association"
    assert re.search(r'<label\s+for="post-slug"[^>]*>Slug \(URL\)</label>', content), "Editor form missing Slug label association"
    assert re.search(r'<label\s+for="post-content"[^>]*>Content \(Markdown\)</label>', content), "Editor form missing Content label association"

    # Check for loading state text in JS
    assert "Signing in..." in content, "Missing 'Signing in...' loading text"
    assert "Signing up..." in content, "Missing 'Signing up...' loading text"
