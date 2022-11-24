from time import sleep

from driver import BaseTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from main_page.MainPage import MainPageHelper, MainPageLocators

page = "https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all"
sql_request_for_test_1 = "SELECT * FROM Customers WHERE ContactName = 'Giovanni Rovelli'"
sql_request_for_test_2 = "SELECT * FROM Customers WHERE City = 'London'"
sql_request_for_test_3 = "INSERT INTO CUSTOMERS VALUES (92, 'John', 'Doe', 'noAdress', 'noCity', 000000, 'noCountry')"


class TestSuite1(BaseTest):

    def setUp(self):
        super().setUp()
        self.main_page = MainPageHelper(self.driver)

    def test_customer_address_is_correct(self):
        driver = self.driver
        driver.get(page)
        self.main_page.send_query_in_sql_field(sql_request_for_test_1)
        self.main_page.click_button_run_sql()
        self.main_page.wait_for_result_table()
        assert self.driver.find_element(By.XPATH, "//*[@id=\"divResultSQL\"]/div/table/tbody/tr[2]/td[4]").text == "Via Ludovico il Moro 22"

    def test_amount_of_rows_in_customer_table_is_correct(self):
        driver = self.driver
        driver.get(page)
        self.main_page.send_query_in_sql_field(sql_request_for_test_2)
        self.main_page.click_button_run_sql()
        self.main_page.wait_for_result_table()
        assert self.driver.find_element(By.XPATH, "//*[@id=\"divResultSQL\"]/div/div").text == "Number of Records: 6"
        assert len(self.driver.find_elements(By.XPATH, "//*[@id=\"divResultSQL\"]/div/table/tbody/tr")) == 7

    def test_add_row_in_table_and_check_amount_of_rows(self):
        driver = self.driver
        driver.get(page)
        amount_of_rows = self.main_page.wait_until_visibility_of_element_located(MainPageLocators.NUMBER_OF_ROWS_IN_SMALL_TABLE)
        self.main_page.send_query_in_sql_field(sql_request_for_test_3)
        self.main_page.click_button_run_sql()
        self.main_page.find_element_by_text('You have made changes to the database. Rows affected: 1')
        # self.main_page.wait_until_presence_of_element_located(By.XPATH, "//*[@id=\"yourDB\"]/table/tbody/tr[2]/td[2]")
        new_amount_of_rows = self.driver.find_element(By.XPATH, "//*[@id=\"yourDB\"]/table/tbody/tr[2]/td[2]").text
        assert amount_of_rows + 1 == new_amount_of_rows




