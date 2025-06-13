from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form_component = RegistrationFormComponent(self.page)
        self.registration_button = page.get_by_test_id('registration-page-registration-button')

    def check_enable_registration_button(self):
        expect(self.registration_button).to_be_enabled()

    def click_registration_button(self):
        self.registration_button.click()
