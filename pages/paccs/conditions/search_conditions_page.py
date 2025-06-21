from playwright.sync_api import Page


class SearchConditionsPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def search_by_condition_id(self, condition_id: str) -> None:
        """
        This method searches for a condition using an ID.
        """
        self.page.get_by_label("Condition Id").fill(condition_id)
        self.page.get_by_role("button", name=" Search").click()
        self.page.get_by_role("link", name=condition_id).click()
