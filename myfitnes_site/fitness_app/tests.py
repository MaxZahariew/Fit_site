from django.test import TestCase, Client


# Create your tests here.
class TestHomeView(TestCase):

    def setUp(self) -> None:
        self.c = Client()

    def test_title_home(self):
        response = self.c.get('home/')

        self.assertEqual(response.status_code, 200)