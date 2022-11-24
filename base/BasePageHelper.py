from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from _pytest.outcomes import fail
from selenium.common.exceptions import TimeoutException


class BasePageHelper:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n"+"Элемент не найден"+str(locator))
            fail()

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Элемент не найден {locator}")

    def wait_until_presence_of_element_located(self, locator, time=10) -> object:
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
