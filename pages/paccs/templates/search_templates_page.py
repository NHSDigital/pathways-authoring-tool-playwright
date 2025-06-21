from playwright.sync_api import Page


class SearchTemplatesPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def search_by_template_id(self, template_id: str) -> None:
        """
        This method searches for a template using an ID.
        """
        self.page.get_by_label("Template Id").fill(template_id)
        self.page.get_by_role("button", name=" Search").click()
        self.page.get_by_role("link", name=template_id).click()
