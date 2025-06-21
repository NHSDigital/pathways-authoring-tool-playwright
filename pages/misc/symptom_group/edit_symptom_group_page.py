from playwright.sync_api import Page
from pages.edit_base_page import EditBasePage


class EditSymptomGroupPage(EditBasePage):
    def __init__(self, page: Page) -> None:
        EditBasePage.__init__(self, page)
