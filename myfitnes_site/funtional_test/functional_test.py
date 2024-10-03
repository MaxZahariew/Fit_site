from selenium import webdriver
import unittest


class NewUserRegisterTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_new_user_register_title_url(self):
        self.browser.get('http://localhost:8000/user/register')

        self.assertIn('DJF', self.browser.title)
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')
