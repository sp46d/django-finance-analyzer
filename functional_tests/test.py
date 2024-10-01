from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):
    DRIVER_PATH = "/Users/sanghyuk/.local/bin/chromedriver"
    BRAVE_PATH = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

    def setUp(self):
        option = webdriver.ChromeOptions()
        option.binary_location = self.BRAVE_PATH
        service = Service(executable_path=self.DRIVER_PATH)

        self.browser = webdriver.Chrome(options=option, service=service)

    def tearDown(self):
        self.browser.quit()
        
    # Below are descriptions from the perspective of a user as to how the app should work
    def test_can_create_financial_transactions(self):
        # Ethan visits the webpage
        self.browser.get(self.live_server_url)
        
        # He notices the page title and header mention finance analyzer
        self.assertIn("Finance Analyzer", self.browser.title)
        
        

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
