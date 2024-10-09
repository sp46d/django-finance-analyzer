from pathlib import Path
import os
from datetime import date
from django.contrib.auth import get_user_model
from django.test import TestCase
from budget.models import Transaction
from accounts.models import CustomUser


# This file is for unit test. From my understanding, two processes need to get tested:
# 1. if the veiw function uses the correct template
# 2. if the view function works as intended


class HomePageTests(TestCase):
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


class TypingTransactionTests(TestCase):
    def test_uses_typing_template(self):
        response = self.client.get("/new/")
        self.assertTemplateUsed(response, "budget/typing.html")

    def test_can_save_a_post_request(self):
        self.client.post(
            "/new/",
            data={
                "date": "2024-09-08",
                "transaction_type": "expense",
                "description": "cookies",
                "amount": "5.36",
            },
        )
        response = self.client.get("/")
        self.assertContains(response, "Sept. 8, 2024")
        self.assertContains(response, "5.36")

    def test_can_redirect_home_after_post(self):
        response = self.client.post(
            "/new/",
            data={
                "date": "2024-10-02",
                "transaction_type": "expense",
                "description": "cookies",
                "amount": "10.00",
            },
        )
        self.assertRedirects(response, "/")


class UploadStatementTests(TestCase):
    BASE_DIR = Path(".").resolve()
    CSV_PATH = os.path.join(BASE_DIR, "artificial_data", "test.csv")
    PDF_PATH = os.path.join(BASE_DIR, "artificial_data", "eStmt_2024-05-23.pdf")

    def test_uses_upload_template(self):
        response = self.client.get("/upload/")
        self.assertTemplateUsed(response, "budget/upload.html")

    def test_redirects_after_csv_upload(self):
        with open(self.CSV_PATH) as fp:
            response = self.client.post("/upload/", data={"file": fp})
        self.assertRedirects(response, "/")
        
    def test_redirects_after_pdf_upload(self):
        with open(self.PDF_PATH) as fp:
            response = self.client.post("/upload/", data={"file": fp})
        self.assertRedirects(response, "/")
        
    def test_can_parse_pdf_and_save_to_transaction(self):
        with open(self.PDF_PATH) as fp:
            self.client.post("/upload/", data={"file": fp})
        first_item = Transaction.objects.first()
        self.assertEqual(first_item.date, date(2024, 4, 24))
        self.assertIn("Online", first_item.description)
        self.assertEqual(first_item.amount, "1000.00")
        
    
    def test_can_parse_csv_and_save_to_transaction(self):
        # tests if it parses
        pass


class CustomUserTests(TestCase):
    def test_can_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="sanghyuk", email="sanghyuk@gmail.com", password="1234"
        )
        self.assertTrue(isinstance(user, CustomUser))
        self.assertEqual(user.username, "sanghyuk")
        self.assertEqual(user.email, "sanghyuk@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_can_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="admin", email="admin@gmail.com", password="admin1234"
        )
        self.assertTrue(isinstance(user, CustomUser))
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.email, "admin@gmail.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)