from base.BasePageHelper import BasePageHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPageLocators:
    BUTTON_RUN_SQL = (By.CLASS_NAME, "ws-btn")
    BUTTON_RESTORE_DATABASE = (By.ID, "restoreDBBtn")
    CODE_MIRROR = (By.CSS_SELECTOR, ".CodeMirror")
    TABLE_WITH_RESULT = (By.XPATH, '//*[@id="divResultSQL"]/div/table/tbody')
    NUMBER_OF_ROWS_IN_SMALL_TABLE = (By.XPATH, "//*[@id='yourDB']/table/tbody/tr[2]/td[2]")


class MainPageHelper(BasePageHelper):

    def send_query_in_sql_field(self, query):
        codeMirror = self.find_element(MainPageLocators.CODE_MIRROR)
        self.driver.execute_script("arguments[0].CodeMirror.setValue(\"" + query + "\");", codeMirror)

    def click_button_run_sql(self):
        self.find_element(MainPageLocators.BUTTON_RUN_SQL).click()

    def click_button_restore_database(self):
        self.find_element(MainPageLocators.BUTTON_RESTORE_DATABASE).click()

    def wait_for_result_table(self):
        self.wait_until_presence_of_element_located(MainPageLocators.TABLE_WITH_RESULT)

    def find_element_by_text(self, text):
        self.find_element(By.XPATH, "//div[.='" + text + "']")


