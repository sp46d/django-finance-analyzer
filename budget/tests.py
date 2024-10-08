from pathlib import Path
import os
from django.test import TestCase
from budget.models import Transaction

# This file is for unit test. From my understanding, two processes need to get tested:
# 1. if the veiw function uses the correct template
# 2. if the view function works as intended


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "budget/home.html")
        
    # def test_displays_all_transactions(self):
    #     Transaction.objects.create(date="2024-10-02",
    #                                transaction_type="EX",
    #                                description="cookies",
    #                                amount="10.00")
    #     Transaction.objects.create(transaction_type="EX",
    #                                description="milk",
    #                                amount="5.00")
    #     response = self.client.get("/")
    #     self.assertContains(response, "cookies")
    #     self.assertContains(response, "milk")
        

class TypingTransactionTest(TestCase):
    def test_uses_typing_template(self):
        response = self.client.get("/new/")
        self.assertTemplateUsed(response, "budget/typing.html")
        
    def test_can_save_a_post_request(self):
        self.client.post("/new/", data={"date": "2024-09-08",
                                       "transaction_type": "expense",
                                       "description": "cookies",
                                       "amount": "5.36"})
        response = self.client.get("/")
        self.assertContains(response, "Sept. 8, 2024")
        self.assertContains(response, "5.36")
        
    def test_can_redirect_home_after_post(self):
        response = self.client.post("/new/", data={"date": "2024-10-02",
                                                   "transaction_type": "expense",
                                                   "description": "cookies",
                                                   "amount": "10.00"})
        self.assertRedirects(response, "/")
        

class UploadStatementTest(TestCase):
    BASE_DIR = Path('.').resolve()
    FILE_PATH = os.path.join(BASE_DIR, "artificial_data", "test.csv")
        
    def test_uses_upload_template(self):
        response = self.client.get("/upload/")
        self.assertTemplateUsed(response, "budget/upload.html")
        
    def test_redirects_after_file_upload(self):
        with open(self.FILE_PATH) as fp:
            response = self.client.post("/upload/", data={"file": fp})
        self.assertRedirects(response, "/")