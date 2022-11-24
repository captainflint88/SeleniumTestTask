from driver import BaseTest
from selenium.webdriver.common.by import By
from main_page.MainPage import MainPageHelper, MainPageLocators

page = "https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all"
sql_request_for_test_1 = "SELECT * FROM Customers WHERE ContactName = 'Giovanni Rovelli'"
sql_request_for_test_2 = "SELECT * FROM Customers WHERE City = 'London'"
sql_request_for_test_3 = "INSERT INTO CUSTOMERS VALUES (92, 'noName', 'noContactName', 'noAdress', 'noCity', 000000, 'noCountry')"
sql_request_for_test_3_check = "SELECT * FROM Customers WHERE ContactName = 'noContactName'"
sql_request_for_test_4 = "UPDATE Customers SET CustomerName='noName', ContactName='noContactName', Address = 'noAdress', City ='noCity', PostalCode = '000000', Country = 'noCountry' WHERE CustomerID=1"
sql_request_for_test_4_check = "SELECT * FROM [Customers]"


class TestMainPage(BaseTest):

    def setUp(self):
        super().setUp()
        self.main_page = MainPageHelper(self.driver)

    def test_customer_address_is_correct(self):
        driver = self.driver
        driver.get(page)
        self.main_page.send_query_in_sql_field(sql_request_for_test_1)
        self.main_page.click_button_run_sql()
        self.main_page.wait_for_result_table()
        assert self.main_page.find_element(MainPageLocators.CELL_4_OF_FIRST_ROW_IN_RESULT_TABLE).text == "Via Ludovico il Moro 22"

    def test_amount_of_rows_in_customer_table_is_correct(self):
        driver = self.driver
        driver.get(page)
        self.main_page.send_query_in_sql_field(sql_request_for_test_2)
        self.main_page.click_button_run_sql()
        self.main_page.wait_for_result_table()
        assert self.main_page.find_element(MainPageLocators.RESULT_MESSAGE_WITH_NUMBER_OF_RECORDS).text == "Number of Records: 6"
        assert len(self.main_page.find_elements(MainPageLocators.LIST_OF_ROWS_IN_RESULT_TABLE)) == 7

    def test_add_row_in_table_and_check_amount_of_rows(self):
        driver = self.driver
        driver.get(page)
        # при открытии в инкогнито таблица с количеством записей в БД не отображается
        # amount_of_rows = self.main_page.wait_until_visibility_of_element_located(MainPageLocators.NUMBER_OF_ROWS_IN_CUSTOMER_TABLE).text
        self.main_page.send_query_in_sql_field(sql_request_for_test_3)
        self.main_page.click_button_run_sql()
        self.main_page.find_element_by_text('You have made changes to the database. Rows affected: 1')
        # new_amount_of_rows = self.main_page.wait_until_visibility_of_element_located(MainPageLocators.NUMBER_OF_ROWS_IN_CUSTOMER_TABLE).text
        # assert amount_of_rows + 1 == new_amount_of_rows
        assert self.main_page.find_element(MainPageLocators.NUMBER_OF_ROWS_IN_CUSTOMER_TABLE, 10).text == "92"
        self.main_page.send_query_in_sql_field(sql_request_for_test_3_check)
        self.main_page.click_button_run_sql()
        self.main_page.wait_for_result_table()
        assert self.main_page.find_element(MainPageLocators.CELL_4_OF_FIRST_ROW_IN_RESULT_TABLE).text == "noAdress"

    def test_update_all_fields_in_one_row_of_customer_table_and_check_update(self):
        driver = self.driver
        driver.get(page)
        self.main_page.send_query_in_sql_field(sql_request_for_test_4)
        self.main_page.click_button_run_sql()
        self.main_page.find_element_by_text('You have made changes to the database. Rows affected: 1')
        self.main_page.send_query_in_sql_field(sql_request_for_test_4_check)
        self.main_page.click_button_run_sql()
        self.main_page.wait_for_result_table()
        assert self.main_page.find_element(MainPageLocators.CELL_1_OF_FIRST_ROW_IN_RESULT_TABLE).text == "1"
        assert self.main_page.find_element(MainPageLocators.CELL_2_OF_FIRST_ROW_IN_RESULT_TABLE).text == "noName"
        assert self.main_page.find_element(MainPageLocators.CELL_3_OF_FIRST_ROW_IN_RESULT_TABLE).text == "noContactName"
        assert self.main_page.find_element(MainPageLocators.CELL_4_OF_FIRST_ROW_IN_RESULT_TABLE).text == "noAdress"
        assert self.main_page.find_element(MainPageLocators.CELL_5_OF_FIRST_ROW_IN_RESULT_TABLE).text == "noCity"
        assert self.main_page.find_element(MainPageLocators.CELL_6_OF_FIRST_ROW_IN_RESULT_TABLE).text == "000000"
        assert self.main_page.find_element(MainPageLocators.CELL_7_OF_FIRST_ROW_IN_RESULT_TABLE).text == "noCountry"

    def test_updates_in_database_are_saved_for_session(self):
        driver = self.driver
        driver.get(page)
        self.main_page.send_query_in_sql_field(sql_request_for_test_3)
        self.main_page.click_button_run_sql()
        self.main_page.find_element_by_text('You have made changes to the database. Rows affected: 1')
        driver.execute_script("window.open('" + page + "', '__blank__');")
        driver.switch_to.window(driver.window_handles[1])
        assert self.main_page.find_element(MainPageLocators.NUMBER_OF_ROWS_IN_CUSTOMER_TABLE, 10).text == "92"