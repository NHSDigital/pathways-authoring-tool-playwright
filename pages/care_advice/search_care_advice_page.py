from playwright.sync_api import Page


class SearchCareAdvicePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def search_by_care_advice_id(self, care_advice_id: str) -> None:
        """
        This method searches for care advice using an ID.
        """
        self.page.get_by_label("Care Advice Id").fill(care_advice_id)
        self.page.get_by_role("button", name=" Search").click()
        self.page.get_by_role("cell", name=care_advice_id).click()
