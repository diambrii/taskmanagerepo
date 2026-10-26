
import json
from pathlib import Path

import pytest
from selenium import webdriver

from add_remove_page import AddRemovePage


def load_test_cases():
    """Load test cases from the external JSON file."""
    data_file = Path(__file__).with_name("test_data.json")
    with data_file.open("r", encoding="utf-8") as handle:
        return json.load(handle)


TEST_CASES = load_test_cases()


@pytest.fixture
def page():
    driver = webdriver.Edge()
    driver.maximize_window()

    task_page = AddRemovePage(driver)

    try:
        task_page.open_page()
        yield task_page
    finally:
        driver.quit()


@pytest.mark.parametrize(
    "test_case",
    [pytest.param(case, id=case["id"]) for case in TEST_CASES],
)
def test_add_remove_elements(page, test_case):
    add_count = test_case["add_count"]
    delete_count = test_case["delete_count"]
    expected_remaining = test_case["expected_remaining"]

    assert page.count_elements() == 0

    for _ in range(add_count):
        page.add_element()

    assert page.count_elements() == add_count

    for _ in range(delete_count):
        page.delete_element()

    assert page.count_elements() == expected_remaining
