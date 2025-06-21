from playwright.sync_api import Page


class SearchSymptomGroupsPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def search_by_symptom_group_id(self, sg_id: str) -> None:
        """
        This method searches for a symptom group using an ID.
        """
        self.page.get_by_role("textbox", name="Filter by SG name").fill(sg_id)
        self.page.get_by_role("button", name="").click()
        self.page.get_by_role("link", name=sg_id).click()
