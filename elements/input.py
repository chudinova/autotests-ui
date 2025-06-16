from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement


class Input(BaseElement):
    def get_locator(self, **kwargs) -> Locator:
        return super().get_locator(**kwargs).locator('input')

    def fill(self, value: str, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.fill(value)

    def set_input_files(self, file: str, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.set_input_files(file)

    def check_have_value(self, value: str, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)
