from playwright.sync_api import sync_playwright, expect

from config import settings
from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context()
    page = context.new_page()

    page.goto(AppRoute.REGISTRATION)

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill(settings.test_user.email)

    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill(settings.test_user.username)

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill(settings.test_user.password)

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text('Dashboard')

    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto(AppRoute.COURSES)

    courses_button = page.get_by_test_id('courses-drawer-list-item-button')
    courses_button.click()

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()

    courses_list_empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_list_empty_icon).to_be_visible()

    courses_list_empty_title = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_list_empty_title).to_be_visible()
    expect(courses_list_empty_title).to_have_text('There is no results')

    courses_list_empty_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_list_empty_description).to_be_visible()
    expect(courses_list_empty_description).to_have_text('Results from the load test pipeline will be displayed here')
