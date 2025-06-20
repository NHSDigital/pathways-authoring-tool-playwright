"""
This file contains tests that save clinical content and then checks the history log.
"""

import pytest
import os
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.edit_question_page import EditQuestionPage
from pages.search_question_page import SearchQuestionPage

VERSION_NUMBER = "42.2.0"


@pytest.fixture(autouse=True)
def login(page: Page) -> None:
    page.goto("https://pat-qa.pathways.nhs.uk/Account/Login?")
    page.get_by_role("button", name="Allow all cookies").click()
    page.get_by_placeholder("Email address").fill(
        "nhspathways.test+pwteammember@nhs.net"
    )
    page.get_by_placeholder("Password").fill(os.getenv("USER_PASS"))
    page.get_by_role("button", name="Sign in").click()


def test_save_question(page: Page) -> None:
    """
    This test saves a question against a previous release and checks history log to confirm correct release
    """
    HomePage(page).navigate_to_search_questions()
    SearchQuestionPage(page).search_by_question_id()
    EditQuestionPage(page).save_clinical_content(VERSION_NUMBER)
    EditQuestionPage(page).click_change_history_log()
    expect(page.locator("#tableExpandCollapse")).to_contain_text(
        "Target 61.0.0_Chai(0)"
        # f"Target {VERSION_NUMBER}(0)"
    )


def test_save_care_advice(page: Page) -> None:
    """
    This test saves care advice against a previous release and checks history log to confirm correct release
    """
    page.get_by_role("button", name="Care Advice").click()
    page.get_by_role("link", name="Search").click()
    page.get_by_label("Care Advice Id").fill("Cx221784")
    page.get_by_role("button", name=" Search").click()
    page.get_by_role("cell", name="Cx221784").click()
    page.locator("#btnPreSave").click()
    page.get_by_label("Target Release *").select_option(VERSION_NUMBER)
    page.get_by_role("textbox", name="Author note").fill("Regression testing")
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("cell", name="Automated PW Team Member").first.click()
    expect(page.locator("#tableExpandCollapse")).to_contain_text(
        "Target 61.0.0_Chai(0)"
        # f"Target {VERSION_NUMBER}(0)"
    )


def test_save_disposition(page: Page) -> None:
    """
    This test saves a disposition against a previous release and checks history log to confirm correct release
    """
    page.get_by_role("button", name="Dispositions").click()
    page.get_by_role("link", name="Search").click()
    page.get_by_label("Dispo Id").fill("Dx220235")
    page.get_by_role("button", name=" Search").click()
    page.get_by_role("link", name="Dx220235").click()
    page.locator("#btnPreSave").click()
    page.get_by_label("Target Release *").select_option("42.2.0")
    page.get_by_role("textbox", name="Author note").fill("Regression testing")
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("cell", name="Automated PW Team Member").first.click()
    expect(page.locator("#tableExpandCollapse")).to_contain_text(
        "Target 61.0.0_Chai(0)"
    )


def test_save_pathway(page: Page) -> None:
    """
    This test saves a pathway against a previous release and checks history log to confirm correct release
    """
    page.get_by_role("button", name="Pathways").click()
    page.get_by_role("link", name="Search").click()
    page.get_by_label("Pathway Id").fill("PW1899")
    page.get_by_role("button", name=" Search").click()
    page.get_by_role("link", name="PW1899").click()
    page.locator("#btnPreSave").click()
    page.get_by_label("Target Release *").select_option("42.2.0")
    page.get_by_role("textbox", name="Author note").fill("Regression testing")
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("cell", name="Automated PW Team Member").first.click()
    expect(page.locator("#tableExpandCollapse")).to_contain_text(
        "Target 61.0.0_Chai(0)"
    )


def test_save_template(page: Page) -> None:
    """
    This test saves a template against a previous release and checks history log to confirm correct release
    """
    page.get_by_role("button", name="PaCCS").click()
    page.get_by_title("Search all PaCCS Templates").click()
    page.get_by_label("Template Id").fill("Cs000138")
    page.get_by_role("button", name=" Search").click()
    page.get_by_role("link", name="Cs000138").click()
    page.locator("#btnPreSave").click()
    page.get_by_label("Target Release *").select_option("42.2.0")
    page.get_by_role("textbox", name="Author note").fill("Regression testing")
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("cell", name="Automated PW Team Member").first.click()
    expect(page.locator("#tableExpandCollapse")).to_contain_text(
        "Target 61.0.0_Chai(0)"
    )


def test_save_condition(page: Page) -> None:
    """
    This test saves a condition against a previous release and checks history log to confirm correct release
    """
    page.get_by_role("button", name="PaCCS").click()
    page.get_by_title("Search all PaCCS Conditions").click()
    page.get_by_label("Condition Id").fill("Cn010727")
    page.get_by_role("button", name=" Search").click()
    page.get_by_role("link", name="Cn010727").click()
    page.locator("#btnPreSave").click()
    page.get_by_label("Target Release *").select_option("42.2.0")
    page.get_by_role("textbox", name="Author note").fill("Regression testing")
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("cell", name="Automated PW Team Member").first.click()
    expect(page.locator("#tableExpandCollapse")).to_contain_text(
        "Target 61.0.0_Chai(0)"
    )


def test_save_symptom_group(page: Page) -> None:
    """
    This test saves a symptom group against a previous release and checks history log to confirm correct release
    """
    page.get_by_role("button", name="Misc").click()
    page.get_by_title("Search Symptom Groups").click()
    page.get_by_role("textbox", name="Filter by SG name").fill("SG1272")
    page.get_by_role("button", name="").click()
    page.get_by_role("link", name="SG1272").click()
    page.locator("#btnPreSave").click()
    page.get_by_label("Target Release *").select_option("42.2.0")
    page.get_by_role("textbox", name="Author note").fill("Regression testing")
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("cell", name="Automated PW Team Member").first.click()
    expect(page.locator("#tableExpandCollapse")).to_contain_text(
        "Target 61.0.0_Chai(0)"
    )


def test_save_symptom_discriminator(page: Page) -> None:
    """
    This test saves a symptom discriminator against a previous release and checks history log to confirm correct release
    """
    page.get_by_role("button", name="Misc").click()
    page.get_by_title("Search Symptom Discriminators").click()
    page.get_by_role("textbox", name="Filter by SD name").fill("SD4785")
    page.get_by_role("button", name="").click()
    page.get_by_role("link", name="SD4785").click()
    page.locator("#btnPreSave").click()
    page.get_by_label("Target Release *").select_option("42.2.0")
    page.get_by_role("textbox", name="Author note").fill("Regression testing")
    page.get_by_role("button", name="Save Changes").click()
    page.get_by_role("cell", name="Automated PW Team Member").first.click()
    expect(page.locator("#tableExpandCollapse")).to_contain_text(
        "Target 61.0.0_Chai(0)"
    )
