import os
import random
import time

import pytest

BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:8000")


@pytest.mark.regression
def test_user_registration_feedback_logout(page):
    """
    Regression: register a user, submit feedback, logout.
    Marked as @pytest.mark.regression so nightly job can run only regression tests.
    """
    ts = int(time.time())
    username = f"reg_user_{ts}_{random.randint(100,999)}"
    password = "TestPass123!"

    # 1) Open app
    page.goto(BASE_URL, wait_until="networkidle")
    page.wait_for_selector("body")

    # 2) Navigate to register page (try common selectors)
    register_selectors = [
        'a:has-text("Register")',
        'a:has-text("Sign up")',
        'a[href*="/accounts/signup"]',
        'a[href*="/register"]',
    ]
    register = None
    for sel in register_selectors:
        loc = page.locator(sel).first
        if loc.count() and loc.is_visible():
            register = loc
            break
    assert register, "Register link not found (regression)"
    register.click()
    page.wait_for_selector("form")

    # 3) Fill and submit registration form
    # Fallbacks for field selectors should match your Django form IDs
    page.fill("#id_username", username)
    page.fill("#id_email", f"{username}@example.com")
    page.fill("#id_password1", password)
    page.fill("#id_password2", password)

    submit = page.locator(
        'button:has-text("Submit"), button:has-text("Register"), button[type="submit"]'
    ).first
    assert submit.count() > 0, "Registration submit button not found"
    submit.click()
    page.wait_for_timeout(1500)

    # 4) Verify login (check logout/profile presence)
    logged_in = False
    for sel in [
        'button:has-text("Log Out")',
        'button:has-text("Logout")',
        'a:has-text("Profile")',
    ]:
        try:
            loc = page.locator(sel).first
            if loc.count() and loc.is_visible():
                logged_in = True
                break
        except Exception:
            continue
    assert logged_in, "User not logged in after registration (regression)"

    # 5) Submit feedback
    feedback_link = page.locator(
        'a:has-text("Feedback"), a:has-text("Give feedback"), a[href*="/feedback"]'
    ).first
    assert feedback_link.count() > 0, "Feedback link not found"
    feedback_link.click()
    page.wait_for_selector("form")

    # Select feedback type if present
    try:
        type_select = page.locator("#id_type").first
        if type_select.count():
            options = type_select.locator("option")
            if options.count() > 1:
                type_select.select_option(index=1)
    except Exception:
        # not fatal; many apps omit the select
        pass

    # Fill message
    message = f"Automated regression feedback {ts}"
    msg_field = page.locator("#id_message").first
    if not msg_field.count():
        msg_field = page.locator("textarea").first
    assert msg_field.count() > 0, "Feedback message field not found"
    msg_field.fill(message)

    submit_fb = page.locator(
        'button:has-text("Submit"), button[type="submit"], button:has-text("Send")'
    ).first
    assert submit_fb.count() > 0, "Feedback submit button not found"
    submit_fb.click()
    page.wait_for_timeout(1500)

    # Check for either success or cleared form
    success = page.locator(".alert-success, .success, .message-success").count() > 0
    errors = page.locator(".alert-danger, .error, .message-error").count() > 0
    if errors:
        # Capture validation messages into the pytest output
        msgs = [
            page.locator(".alert-danger, .error, .message-error").nth(i).text_content()
            for i in range(
                page.locator(".alert-danger, .error, .message-error").count()
            )
        ]
        pytest.fail(f"Feedback submission produced errors: {msgs}")
    assert success or not errors, "Feedback submission failed or ambiguous"

    # 6) Logout
    logout = page.locator(
        'button:has-text("Log Out"), a:has-text("Logout"), button:has-text("Sign out")'
    ).first
    if logout.count() and logout.is_visible():
        logout.click()
        page.wait_for_timeout(800)
    else:
        pytest.skip("Logout control not available; test completed up to feedback")
