from playwright.sync_api import Page
from pages.base_page import BasePage


class EditBasePage(BasePage):
    def __init__(self, page: Page) -> None:
        BasePage.__init__(self, page)

    def save_clinical_content(
        self, target_release: str, author_note: str = "Regression testing"
    ) -> None:
        """
        This method clicks Save on a clinical item, populates data on the Change History Modal then saves the changes.
        """
        self.page.locator("#btnPreSave").click()
        self.page.get_by_label("Target Release *").select_option(target_release)
        self.page.get_by_role("textbox", name="Author note").fill(author_note)
        self.page.get_by_role("button", name="Save Changes").click()

    def click_change_history_log(self) -> None:
        """
        This method clicks on the latest log from author "Automated PW Team Member" in the change history table.
        """
        self.page.get_by_role("cell", name="Automated PW Team Member").first.click()
