import pytest
from playwright.sync_api import Playwright, expect, Page


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill('user.name@gmail.com')

    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill('username')

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text('Dashboard')

    context.storage_state(path="browser-state.json")


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    yield context.new_page()
    browser.close()
