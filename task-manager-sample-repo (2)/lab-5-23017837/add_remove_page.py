
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddRemovePage:

    URL = "http://localhost:5000/add_remove_elements/"

    ADD_BUTTON = (By.CSS_SELECTOR, "button[onclick='addElement()']")
    DELETE_BUTTONS = (By.CSS_SELECTOR, "#elements button.added-manually")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self):
        self.driver.get(self.URL)
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_BUTTON)
        )

    def add_element(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_BUTTON)
        )
        button.click()

    def count_elements(self):
        return len(
            self.driver.find_elements(*self.DELETE_BUTTONS)
        )

    def delete_element(self):
        buttons = self.driver.find_elements(
            *self.DELETE_BUTTONS
        )

        if not buttons:
            raise AssertionError("No Delete button found")

        buttons[0].click()
