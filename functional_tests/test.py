from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By


DRIVER_PATH = "/Users/sanghyuk/.local/bin/chromedriver"
BRAVE_PATH = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.binary_location = BRAVE_PATH
        service = Service(executable_path=DRIVER_PATH)

        self.browser = webdriver.Chrome(options=option, service=service)

    def tearDown(self):
        self.browser.quit()

    # Below are descriptions from the perspective of a user as to how the app should work
    def test_can_create_financial_transactions(self):
        # Ethan visits the webpage
        self.browser.get(self.live_server_url)

        # He notices the page title and header mention finance analyzer
        self.assertIn("Finance Analyzer", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("Finance Analyzer", header_text)

        # He sees two buttons on the web page, where the two read "Add Transaction" and "Upload Statement"
        button1 = self.browser.find_element(By.ID, "id_type_data")
        button2 = self.browser.find_element(By.ID, "id_upload_data")

        self.assertEqual(button1.text, "Add Transaction")
        self.assertEqual(button2.text, "Upload Statement")

        # insert_transaction_page = button1.click()
        # upload_statement_page = button2.click()

        # self.assertContains(insert_transaction_page, "Submit")

        # He tries to enter a recent transaction record he made.
        # He finds multiple places he can type in and the first one is for date
        # date_input = self.browser.find_element(By.ID, "id_new_date")
        # self.assertEqual(
        #     date_input.get_attribute("placeholder"), "Enter a date (YYYY-MM-DD)"
        # )
        # self.assertTrue(date_input.get_attribute("required"))

        # The second box is for type of the transaction, a dropdown menu that includes
        # two options: 1. expense and 2. income
        # s = self.browser.find_element(By.ID, "id_select_type")
        # dropdown = Select(s)
        # drop_options_text = [option.text for option in dropdown.options]
        # self.assertEqual(len(drop_options_text), 3)
        # self.assertIn("Expense", drop_options_text)
        # self.assertIn("Income", drop_options_text)
        # self.assertIn("Transfer", drop_options_text)

        # The third box is for description of the transaction
        # He finds this box is not rquired to fill in.
        # desc_input = self.browser.find_element(By.ID, "id_new_description")
        # self.assertEqual(desc_input.get_attribute("placeholder"), "Description")

        # The last one is for the amount of the transaction
        # amount_input = self.browser.find_element(By.ID, "id_new_amount")
        # self.assertEqual(amount_input.get_attribute("placeholder"), "Enter the amount")
        # self.assertEqual(amount_input.get_attribute("type"), "number")

        # So, he goes on and type in the first transaction he made yesterday.
        # it was October, 1, 2024, and he bought his favorite cookies at $5.00
        # date_input.send_keys("2024-10-01")
        # dropdown.select_by_visible_text("Expense")
        # desc_input.send_keys("Buy cookies")
        # amount_input.send_keys("5.00")

        # After typing in all the information about the transaction,
        # he finds the submit button located right below
        # submit_button = self.browser.find_element(By.ID, "id_submit")
        # self.assertEqual(submit_button.get_attribute("value"), "Submit")

        # Once he reviews what he wrote, he clicks on the submit button
        # submit_button.click()

        # Then, he sees the transaction record he just submitted show below.
        # table = self.browser.find_element(By.ID, "id_transaction_table")
        # rows = table.find_elements(By.TAG_NAME, "tr")
        # columns = self.browser.find_elements(
        #     By.XPATH, "//*[@id='id_transaction_table']/tbody/tr[2]/td"
        # )
        # self.assertEqual(len(rows), 2)  # table header included
        # self.assertEqual(len(columns), 4)

    # TODO: can upload bank statement to the webpage in either pdf or csv format
    # TODO: write code for parsing bank statement
    # TODO: figure out how to compute account balance
    # WORKING: create two buttons for importing transactions on homepage, where one is for manually typing ing and the other one is for uploading a file

    # def test_can_upload_csv_or_pdf_statements(self):
    #     self.browser.get(self.live_server_url)

    # def test_can_start_a_todo_list(self):
    #     # Edith has heard about a cool new online to-do app.
    #     # She goes to check out its homepage
    #     self.browser.get("http://localhost:8000")

    #     # She notices the page title and header mention to-do lists
    #     self.assertIn("To-Do", self.browser.title)
    #     header_text = self.browser.find_element(By.TAG_NAME, "h1").text
    #     self.assertIn("To-Do", header_text)

    #     # She is invited to enter a to-do item straight away
    #     inputbox = self.browser.find_element(By.ID, "id_new_item")
    #     self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

    #     # She types "Buy peacock feathers" into a text box
    #     # (Edith's hobby is tying fly-fishing lures)
    #     inputbox.send_keys("Buy peacock feathers")

    #     # When she hits enter, the page updates, and now the page lists
    #     # "1: Buy peacock feathers" as an item in a to-do list
    #     inputbox.send_keys(Keys.ENTER)
    #     time.sleep(1)
    #     self.check_for_row_in_list_table("1: Buy peacock feathers")

    #     # There is still a text box inviting her to add another item.
    #     # She enters "Use peacock feathers to make a fly"
    #     # (Edith is very methodical)
    #     inputbox = self.browser.find_element(By.ID, "id_new_item")
    #     inputbox.send_keys("Use peacock feathers to make a fly")
    #     inputbox.send_keys(Keys.ENTER)
    #     time.sleep(1)

    #     # The page updates again, and now shows both items on her list
    #     self.check_for_row_in_list_table("1: Buy peacock feathers")
    #     self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")

    #     # Satisfied, she goes back to sleep
