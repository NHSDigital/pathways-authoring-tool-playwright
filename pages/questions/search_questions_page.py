from playwright.sync_api import Page


class SearchQuestionsPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def search_by_question_id(self, question_id: str) -> None:
        """
        This method searches for a question using an ID.
        """
        self.page.get_by_label("Question Id").fill(question_id)
        self.page.get_by_role("button", name=" Search").click()
        self.page.get_by_role("cell", name=question_id).click()
