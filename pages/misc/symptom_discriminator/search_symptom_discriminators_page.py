from playwright.sync_api import Page


class SearchSymptomDiscriminatorsPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def search_by_symptom_discriminator_id(self, sd_id: str) -> None:
        """
        This method searches for a symptom discriminators using an ID.
        """
        self.page.get_by_role("textbox", name="Filter by SD name").fill(sd_id)
        self.page.get_by_role("button", name="").click()
        self.page.get_by_role("link", name=sd_id).click()
