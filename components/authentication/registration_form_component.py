from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')

    def fill_registration_form(self, email: str, username: str, password: str):
        self.registration_email_input.fill(email)
        self.registration_username_input.fill(username)
        self.registration_password_input.fill(password)

    def check_visible(self, email: str, username: str, password: str):
        expect(self.registration_email_input).to_have_value(email)
        expect(self.registration_username_input).to_have_value(username)
        expect(self.registration_password_input).to_have_value(password)
