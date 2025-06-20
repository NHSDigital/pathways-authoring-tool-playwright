from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate_to_search_questions(self) -> None:
        """
        This method navigates to the Search Questions page from the main menu.
        """
        self.page.get_by_role("button", name="Questions").click()
        self.page.get_by_role("link", name="Search").click()
