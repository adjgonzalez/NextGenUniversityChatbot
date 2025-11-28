import pytest
from playwright.sync_api import sync_playwright


# Fixture to launch browser once per test session
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # set True for CI
        yield browser
        browser.close()


# Fixture to create a new page for each test
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


def test_example_com(page):
    page.goto("https://example.com")
    assert "Example Domain" in page.title()


def test_python_org(page):
    page.goto("https://www.python.org")
    assert page.locator("text=Python").is_visible()
