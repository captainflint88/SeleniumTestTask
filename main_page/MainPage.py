from base.BasePageHelper import BasePageHelper
from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_RUN_SQL = (By.CLASS_NAME, "ws-btn")
    BUTTON_RESTORE_DATABASE = (By.ID, "restoreDBBtn")
    CODE_MIRROR = (By.CSS_SELECTOR, ".CodeMirror")
    TABLE_WITH_RESULT = (By.XPATH, "//*[@id='divResultSQL']/div/table/tbody")
    NUMBER_OF_ROWS_IN_CUSTOMER_TABLE = (By.XPATH, "//*[@id='yourDB']/table/tbody/tr[2]/td[2]")
    RESULT_MESSAGE_WITH_NUMBER_OF_RECORDS = (By.XPATH, "//*[@id=\"divResultSQL\"]/div/div")
    LIST_OF_ROWS_IN_RESULT_TABLE = (By.XPATH, "//*[@id=\"divResultSQL\"]/div/table/tbody/tr")

    CELL_1_OF_FIRST_ROW_IN_RESULT_TABLE = (By.XPATH, "//*[@id=\"divResultSQL\"]/div/table/tbody/tr[2]/td[1]")
    CELL_2_OF_FIRST_ROW_IN_RESULT_TABLE = (By.XPATH, "//*[@id=\"divResultSQL\"]/div/table/tbody/tr[2]/td[2]")
    CELL_3_OF_FIRST_ROW_IN_RESULT_TABLE = (By.XPATH, "//*[@id=\"divResultSQL\"]/div/table/tbody/tr[2]/td[3]")
    CELL_4_OF_FIRST_ROW_IN_RESULT_TABLE = (By.XPATH, "//*[@id=\"divResultSQL\"]/div/table/tbody/tr[2]/td[4]")
    CELL_5_OF_FIRST_ROW_IN_RESULT_TABLE = (By.XPATH, "//*[@id=\"divResultSQL\"]/div/table/tbody/tr[2]/td[5]")
    CELL_6_OF_FIRST_ROW_IN_RESULT_TABLE = (By.XPATH, "//*[@id=\"divResultSQL\"]/div/table/tbody/tr[2]/td[6]")
    CELL_7_OF_FIRST_ROW_IN_RESULT_TABLE = (By.XPATH, "//*[@id=\"divResultSQL\"]/div/table/tbody/tr[2]/td[7]")


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

    def find_element_by_text(self, text, time=10):
        self.wait_until_presence_of_element_located((By.XPATH, "//div[.='" + text + "']"), time)


