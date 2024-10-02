from django.test import TestCase

# This file is for unit test. From my understanding, two processes need to get tested:
# 1. if the veiw function uses the correct template
# 2. if the view function works as intended


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "budget/home.html")
