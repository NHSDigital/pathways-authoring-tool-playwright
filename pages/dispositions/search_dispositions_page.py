from playwright.sync_api import Page


class SearchDispositionsPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def search_by_disposition_id(self, dispo_id: str) -> None:
        """
        This method searches for a disposition using an ID.
        """
        self.page.get_by_label("Dispo Id").fill(dispo_id)
        self.page.get_by_role("button", name=" Search").click()
        self.page.get_by_role("link", name=dispo_id).click()
