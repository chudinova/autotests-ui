from typing import Literal

from playwright.async_api import Page, expect

from components.base_component import BaseComponent

Identifier = Literal["students", "activities", "courses", "scores"]
ChartType = Literal["bar", "line", "pie", "scatter"]


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: Identifier, chart_type: ChartType):
        super().__init__(page)
        self.identifier = identifier
        self.chart_type = chart_type

        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    def check_visible(self, title: str):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)
        expect(self.chart).to_be_visible()
