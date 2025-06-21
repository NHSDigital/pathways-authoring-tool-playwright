from playwright.sync_api import Page


class SearchPathwaysPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def search_by_pathway_id(self, pathway_id: str) -> None:
        """
        This method searches for a pathway using an ID.
        """
        self.page.get_by_label("Pathway Id").fill(pathway_id)
        self.page.get_by_role("button", name=" Search").click()
        self.page.get_by_role("link", name=pathway_id).click()
