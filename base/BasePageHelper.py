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

    def wait_until_visibility_of_element_located(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def every_downloads_chrome(self):
        if not self.driver.current_url.startswith("chrome://downloads"):
            self.driver.get("chrome://downloads/")
        return self.driver.execute_script("""
            var items = document.querySelector('downloads-manager')
                .shadowRoot.getElementById('downloadsList').items;
            if (items.every(e => e.state === "COMPLETE"))
                return items.map(e => e.fileUrl || e.file_url);
            """)
