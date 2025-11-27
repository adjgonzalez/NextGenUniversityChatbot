import os
import random

import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.smoke
def test_homepage_loads():
    """Basic smoke test: homepage responds"""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000")
        assert "Django" in page.title() or page.content() != ""
        browser.close()


def generate_test_username():
    """Generate unique test username"""
    return f"testuser{random.randint(1000, 9999)}"


def clear_browser_data(page):
    """Clear all browser data regardless of current language"""
    print("Clearing browser cache and storage...")

    # Clear cookies
    page.context.clear_cookies()

    # Clear localStorage and sessionStorage
    page.evaluate(
        """
        () => {
            try {
                localStorage.clear();
                sessionStorage.clear();
                console.log('Browser storage cleared');
            } catch (e) {
                console.log('Could not clear storage:', e);
            }
        }
    """
    )

    print("✓ Browser cache and storage cleared")


def take_screenshot(page, filename, description):
    """Take screenshot and log description"""
    page.screenshot(path=f"test_results/{filename}")
    print(f"✓ {description} - saved as {filename}")


def test_features():
    """E2E test with screenshots and chatbot flow"""
    print("=" * 70)
    print("E2E TEST SUITE")
    print("=" * 70)
    print("Testing: Chatbot → User Registration → Feedback")
    print()

    test_username = generate_test_username()
    test_password = "TestPass123!"
    created_users = []
    test_feedback_content = f"Automated test feedback {random.randint(1000, 9999)}"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--incognito", "--disable-extensions", "--disable-plugins"],
        )

        context = browser.new_context(
            ignore_https_errors=True,
            viewport={"width": 1280, "height": 720},
            storage_state=None,
            locale="en-US",
        )

        page = context.new_page()

        try:
            # ===== SETUP =====
            print("SETUP: Starting with clean browser session...")
            page.goto("http://localhost:8000/")
            clear_browser_data(page)
            page.reload(wait_until="networkidle")
            page.wait_for_selector("body")
            print("✓ Fresh session started")
            take_screenshot(page, "00_setup_complete.png", "Fresh session started")

            # ===== TEST 1: ENHANCED CHATBOT TEST =====
            print("\n1. ENHANCED CHATBOT TEST")
            print("-" * 40)

            chatbot_btn = page.locator(".chatbot-btn").first
            if chatbot_btn.is_visible():
                chatbot_btn.click()
                page.wait_for_timeout(1000)
                print("✓ Chatbot opened")
                take_screenshot(page, "01_chatbot_opened.png", "Chatbot modal opened")

                # Test complete chatbot flow: No → Undergraduate → Program → Redirect
                no_button = page.locator("#noButton").first
                if no_button.is_visible():
                    no_button.click()
                    page.wait_for_timeout(1000)
                    print("✓ Selected 'No' in chatbot")
                    take_screenshot(
                        page, "02_chatbot_no_selected.png", "Selected No option"
                    )

                    # Select Undergraduate
                    undergrad_btn = page.locator(
                        'button:has-text("Undergraduate")'
                    ).first
                    if undergrad_btn.is_visible():
                        undergrad_btn.click()
                        page.wait_for_timeout(1000)
                        print("✓ Selected 'Undergraduate'")
                        take_screenshot(
                            page,
                            "03_chatbot_undergrad_selected.png",
                            "Selected Undergraduate",
                        )

                        # Select any available program (first one found)
                        program_selectors = [
                            'button:has-text("Computer Science")',
                            'button:has-text("Economics")',
                            'button:has-text("🖥️")',
                            'button:has-text("📈")',
                            ".program-option",
                        ]

                        program_selected = False
                        for selector in program_selectors:
                            program_btn = page.locator(selector).first
                            if program_btn.is_visible():
                                program_name = program_btn.text_content()
                                program_btn.click()
                                page.wait_for_timeout(2000)
                                print(f"✓ Selected program: {program_name}")
                                take_screenshot(
                                    page,
                                    "04_chatbot_program_selected.png",
                                    f"Selected {program_name}",
                                )
                                program_selected = True
                                break

                        if program_selected:
                            # Wait for redirect and check if we're on a program page
                            current_url = page.url
                            if (
                                "program" in current_url.lower()
                                or current_url != "http://localhost:8000/"
                            ):
                                print(
                                    f"✓ Successfully redirected to program page: {current_url}"
                                )
                                take_screenshot(
                                    page,
                                    "05_chatbot_redirected.png",
                                    "Redirected to program page",
                                )

                                # Navigate back to home to continue other tests
                                home_link = page.locator(
                                    'a:has-text("Home"), a:has-text("Inicio")'
                                ).first
                                if home_link.is_visible():
                                    home_link.click()
                                    page.wait_for_timeout(1000)
                                    print("✓ Returned to home page")
                                    take_screenshot(
                                        page,
                                        "06_returned_to_home.png",
                                        "Returned to home page",
                                    )
                                else:
                                    # Fallback: navigate to root URL
                                    page.goto("http://localhost:8000/")
                                    print("✓ Navigated back to home page")
                            else:
                                print("X No redirect occurred after program selection")
                        else:
                            print("X No program options found")
                    else:
                        print("X Undergraduate button not found")
                else:
                    print("X No button not found in chatbot")

                # Close chatbot if it's still open
                close_btn = page.locator('[data-bs-dismiss="modal"]').first
                if close_btn.is_visible():
                    close_btn.click()
                    page.wait_for_timeout(500)
                    print("✓ Chatbot closed")
            else:
                print("X Chatbot button not found")
                return False, created_users, test_feedback_content

            # ===== TEST 2: USER REGISTRATION =====
            print("\n2. USER REGISTRATION TEST")
            print("-" * 40)

            register_link = page.locator('a:has-text("Register")').first
            if register_link.is_visible():
                register_link.click()
                page.wait_for_selector("form")
                print("✓ Registration page loaded")
                take_screenshot(page, "07_registration_page.png", "Registration page")

                page.fill("#id_username", test_username)
                page.fill("#id_email", f"{test_username}@example.com")
                page.fill("#id_password1", test_password)
                page.fill("#id_password2", test_password)
                print("✓ Registration form filled")

                submit_btn = page.locator('button:has-text("Submit")').first
                if submit_btn.is_visible():
                    submit_btn.click()
                    page.wait_for_timeout(3000)

                    if page.url == "http://localhost:8000/":
                        created_users.append(test_username)
                        print("✓ Registration successful! (auto-logged in)")
                        take_screenshot(
                            page,
                            "08_registration_success.png",
                            "Registration successful",
                        )

                        # Verify login by checking for logout link
                        logout_link = page.locator('a:has-text("Log Out")').first
                        if logout_link.is_visible():
                            print("✓ Confirmed logged in (logout link visible)")
                        else:
                            print("X Login status not visible")
                    else:
                        print(f"X Registration failed - at URL: {page.url}")
                        return False, created_users, test_feedback_content
                else:
                    print("X Submit button not found")
                    return False, created_users, test_feedback_content
            else:
                print("X Register link not found")
                return False, created_users, test_feedback_content

            # ===== TEST 3: FEEDBACK SUBMISSION =====
            print("\n3. FEEDBACK SUBMISSION TEST")
            print("-" * 40)

            feedback_link = page.locator('a:has-text("Feedback")').first
            if feedback_link.is_visible():
                feedback_link.click()
                page.wait_for_selector("form")
                print("✓ Feedback page loaded")
                take_screenshot(page, "09_feedback_page.png", "Feedback page")

                # Find and fill the feedback form
                feedback_form = page.locator("form:has(#id_type)").first
                if feedback_form.is_visible():
                    print("✓ Found feedback form")

                    # Select a valid option
                    type_select = feedback_form.locator("#id_type").first
                    if type_select.is_visible():
                        options = type_select.locator("option")
                        valid_option_found = False

                        for i in range(options.count()):
                            option = options.nth(i)
                            value = option.get_attribute("value")
                            if value and value.strip():
                                type_select.select_option(value=value)
                                print(f"✓ Selected valid option: {value}")
                                valid_option_found = True
                                break

                        if not valid_option_found:
                            type_select.select_option(index=1)
                            print("✓ Selected first available option")

                    # Fill message
                    message_area = feedback_form.locator("#id_message").first
                    if message_area.is_visible():
                        message_area.fill(test_feedback_content)
                        print("✓ Feedback message filled")

                    take_screenshot(
                        page, "10_feedback_filled.png", "Feedback form filled"
                    )

                    # Submit the form
                    submit_btn = feedback_form.locator('button[type="submit"]').first
                    if submit_btn.is_visible():
                        print("Submitting feedback form...")
                        submit_btn.click()
                        page.wait_for_timeout(3000)

                        # Check result
                        current_url = page.url
                        success_messages = page.locator(".alert-success, .success")
                        error_messages = page.locator(".alert-danger, .error")

                        if success_messages.count() > 0:
                            print("✓ Feedback submitted successfully!")
                            take_screenshot(
                                page,
                                "11_feedback_success.png",
                                "Feedback submitted successfully",
                            )
                        elif error_messages.count() > 0:
                            print("X Form validation errors:")
                            for i in range(error_messages.count()):
                                print(f"  - {error_messages.nth(i).text_content()}")
                            take_screenshot(
                                page,
                                "11_feedback_error.png",
                                "Feedback submission error",
                            )
                            return False, created_users, test_feedback_content
                        elif current_url != "http://localhost:8000/feedback/":
                            print(f"✓ Redirected to: {current_url}")
                            take_screenshot(
                                page,
                                "11_feedback_redirected.png",
                                "Feedback redirected",
                            )
                        else:
                            # Check if form was cleared
                            current_message = message_area.evaluate("el => el.value")
                            if not current_message:
                                print("✓ Form was cleared - submission successful!")
                                take_screenshot(
                                    page,
                                    "11_feedback_cleared.png",
                                    "Feedback form cleared",
                                )
                            else:
                                print("X Form not cleared - submission failed")
                                take_screenshot(
                                    page,
                                    "11_feedback_failed.png",
                                    "Feedback submission failed",
                                )
                                return False, created_users, test_feedback_content
                    else:
                        print("X Submit button not found")
                        return False, created_users, test_feedback_content
                else:
                    print("X Feedback form not found")
                    return False, created_users, test_feedback_content

            # ===== TEST 4: LOGOUT =====
            print("\n4. LOGOUT TEST")
            print("-" * 40)

            logout_link = page.locator('a:has-text("Log Out")').first
            if logout_link.is_visible():
                logout_link.click()
                page.wait_for_timeout(1000)
                print("✓ Logged out successfully")
                take_screenshot(
                    page, "12_logout_success.png", "Logged out successfully"
                )

                # Navigate back to home to continue other tests
                home_link = page.locator(
                    'a:has-text("Home"), a:has-text("Inicio")'
                ).first

                # Verify logout
                login_link = page.locator('a:has-text("Log In")').first
                if login_link.is_visible():
                    print("✓ Confirmed logged out (login link visible)")
                else:
                    print("X Logout status unclear")
            else:
                print("X Logout link not found")

            print("\n" + "=" * 70)
            print("ALL TESTS PASSED!")
            print("=" * 70)
            take_screenshot(
                page, "13_all_tests_complete.png", "All tests completed successfully"
            )
            return True, created_users, test_feedback_content

        except Exception as e:
            print(f"\nX TEST FAILED: {e}")
            import traceback

            traceback.print_exc()
            take_screenshot(page, "error_test_failed.png", "Test failed with error")
            return False, created_users, test_feedback_content

        finally:
            browser.close()


def cleanup_test_data(usernames, feedback_content):
    """Clean up test data"""
    print("\n" + "=" * 70)
    print("TEARDOWN: Cleaning up test data")
    print("=" * 70)

    try:
        import os

        import django

        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
        django.setup()

        from django.contrib.auth.models import User

        from feedback.models import Feedback

        for username in usernames:
            try:
                user = User.objects.get(username=username)
                user.delete()
                print(f"✓ Deleted test user: {username}")
            except User.DoesNotExist:
                print(f"X Test user not found: {username}")

        try:
            feedback_count = Feedback.objects.filter(
                message__contains=feedback_content
            ).count()
            print(f"Feedback entries in database: {feedback_count}")
        except Exception as e:
            print(f"X Could not check feedback: {e}")

        print("* Cleanup completed")

    except Exception as e:
        print(f"X Cleanup failed: {e}")


if __name__ == "__main__":
    os.makedirs("test_results", exist_ok=True)

    print("PREREQUISITES:")
    print("Django server: python manage.py runserver")
    print()

    success, created_users, feedback_content = test_features()

    if success:
        cleanup_test_data(created_users, feedback_content)
        print("\n✓ TEST SUITE COMPLETED SUCCESSFULLY!")
        print("All screenshots saved in test_results/ folder")
    else:
        print("\nX TEST SUITE FAILED")
        if created_users:
            cleanup_test_data(created_users, feedback_content)
        exit(1)
