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

    def navigate_to_search_care_advice(self) -> None:
        """
        This method navigates to the Search Care Advice page from the main menu.
        """
        self.page.get_by_role("button", name="Care Advice").click()
        self.page.get_by_role("link", name="Search").click()

    def navigate_to_search_dispositions(self) -> None:
        """
        This method navigates to the Search Dispositions page from the main menu.
        """
        self.page.get_by_role("button", name="Dispositions").click()
        self.page.get_by_role("link", name="Search").click()

    def navigate_to_search_pathways(self) -> None:
        """
        This method navigates to the Search Pathways page from the main menu.
        """
        self.page.get_by_role("button", name="Pathways").click()
        self.page.get_by_role("link", name="Search").click()

    def navigate_to_search_templates(self) -> None:
        """
        This method navigates to the Search Templates page from the main menu.
        """
        self.page.get_by_role("button", name="PaCCS").click()
        self.page.get_by_title("Search all PaCCS Templates").click()

    def navigate_to_search_conditions(self) -> None:
        """
        This method navigates to the Search Conditions page from the main menu.
        """
        self.page.get_by_role("button", name="PaCCS").click()
        self.page.get_by_title("Search all PaCCS Conditions").click()

    def navigate_to_search_symptom_groups(self) -> None:
        """
        This method navigates to the Search Symptom Groups page from the main menu.
        """
        self.page.get_by_role("button", name="Misc").click()
        self.page.get_by_title("Search Symptom Groups").click()

    def navigate_to_search_symptom_discriminators(self) -> None:
        """
        This method navigates to the Search Symptom Discriminators page from the main menu.
        """
        self.page.get_by_role("button", name="Misc").click()
        self.page.get_by_title("Search Symptom Discriminators").click()
