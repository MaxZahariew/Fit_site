from django.test import TestCase
from django.urls import resolve

from accounts.views import RegisterView

# Create your tests here.


class UserRegisterAccountTest(TestCase):
    '''Тест регистрации аккоунта'''

    def test_account_register_in_database(self):
        found = resolve('user/register/')
        self.assertSetEqual(found.func, RegisterView)