from playwright.sync_api import Page


class SearchQuestionPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def search_by_question_id(self) -> None:
        """
        This method searches for a question using an ID.
        """
        self.page.get_by_label("Question Id").fill("Tx226532")
        self.page.get_by_role("button", name=" Search").click()
        self.page.get_by_role("cell", name="Tx226532").click()
