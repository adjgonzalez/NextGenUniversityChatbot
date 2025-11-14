import asyncio
import sys
import os
import django

# Add the project root to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uni-chatbot.mysite.settings')
django.setup()

from playwright.async_api import async_playwright


async def test_home_page_and_navigation():
    """E2E test: Load home page and test basic navigation"""
    async with async_playwright() as p:
        # Use visible browser for debugging, set to False for CI
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        try:
            print("Loading home page...")

            # Test 1: Load home page
            await page.goto('http://localhost:8000/')

            # Test 2: Check page title
            title = await page.title()
            print(f"Page title: {title}")
            assert 'NextGen University' in title or 'Programs' in title

            # Test 3: Check for key elements in hero section
            await page.wait_for_selector('.hero-section, h1', timeout=5000)

            # Test 4: Check for navigation elements
            nav_links = await page.query_selector_all('nav a')
            print(f"🔗 Found {len(nav_links)} navigation links")

            # Test 5: Test navigation to Programs page
            programs_link = await page.query_selector('a[href*="programs"]')
            if programs_link:
                print("Navigating to Programs page...")
                await programs_link.click()
                await page.wait_for_load_state('networkidle')

                # Verify we're on programs page
                current_url = page.url
                print(f"Current URL: {current_url}")
                assert '/programs/' in current_url

                # Check programs page content
                page_content = await page.text_content('body')
                assert 'Programs' in page_content or 'programs' in page_content.lower()
            else:
                print("Programs link not found, testing home page content instead")
                page_content = await page.text_content('body')
                assert 'Enroll' in page_content or 'University' in page_content

            print("✅ All E2E tests passed!")
            return True

        except Exception as e:
            print(f"❌ E2E test failed: {e}")
            return False
        finally:
            await browser.close()


def run_e2e_tests():
    """Run the E2E tests"""
    print("Starting E2E Tests...")
    print("Note: Make sure your Django server is running on http://localhost:8000/")
    print("Run: python manage.py runserver")
    print()

    success = asyncio.run(test_home_page_and_navigation())

    if success:
        print("\nE2E tests completed successfully!")
        return 0
    else:
        print("\nE2E tests failed!")
        return 1


if __name__ == '__main__':
    exit_code = run_e2e_tests()
    exit(exit_code)