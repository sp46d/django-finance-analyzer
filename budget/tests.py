from django.test import TestCase
from budget.models import Transaction

# This file is for unit test. From my understanding, two processes need to get tested:
# 1. if the veiw function uses the correct template
# 2. if the view function works as intended


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "budget/home.html")
        
    def test_displays_all_transactions(self):
        Transaction.objects.create(date="2024-10-02",
                                   transaction_type="EX",
                                   description="cookies",
                                   amount="10.00")
        Transaction.objects.create(transaction_type="EX",
                                   description="milk",
                                   amount="5.00")
        response = self.client.get("/")
        self.assertContains(response, "cookies")
        self.assertContains(response, "milk")
        
        

