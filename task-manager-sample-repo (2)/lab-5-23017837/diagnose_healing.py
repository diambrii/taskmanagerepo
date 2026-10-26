
from selenium import webdriver
from selenium.webdriver.common.by import By

OLD_LOCATOR = (
    By.CSS_SELECTOR,
    "button[onclick='addElement()']"
)

DELETE_LOCATOR = (
    By.CSS_SELECTOR,
    "#elements button.added-manually"
)

driver = webdriver.Remote(
    command_executor="http://localhost:8085",
    options=webdriver.ChromeOptions()
)

try:
    driver.get(
        "http://host.docker.internal:5000/add_remove_elements/"
    )

    print("HEALENIUM DIAGNOSTIC TEST")
    print("Initial Delete buttons:",
          len(driver.find_elements(*DELETE_LOCATOR)))

    for attempt in range(1, 6):
        button = driver.find_element(*OLD_LOCATOR)

        print(f"\nAttempt {attempt}")
        print("Element selected:",
              button.get_attribute("outerHTML"))

        button.click()

        count = len(driver.find_elements(*DELETE_LOCATOR))
        print("Delete buttons after click:", count)

finally:
    driver.quit()
