import pytest

from fixtures.pages import dashboard_page
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage,
        login: str = 'Иван',
        username: str = 'ivan',
        password: str = 'pass',
):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form_component.fill_registration_form(login, username, password)
    registration_page.registration_form_component.check_visible(login, username, password)
    registration_page.click_registration_button()
    dashboard_page.dashboard_toolbar_view_component.check_visible()
