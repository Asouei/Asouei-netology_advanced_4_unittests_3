import unittest
from main import login_pass_enter

LOGIN = ''      # Работающий логин
PASS = ''     # Работающий пароль


class TestAuth(unittest.TestCase):

   def test_check_normal(self):
       self.assertEqual(login_pass_enter(LOGIN, PASS), True)

   def test_check_normal_login_bad_pass(self):
       self.assertEqual(login_pass_enter(LOGIN, f'{PASS}1'), False)

   def test_check_normal_pass_bad_login(self):
       self.assertEqual(login_pass_enter(f'{LOGIN}1', PASS), False)

   def test_check_normal_login_no_pass(self):
       self.assertEqual(login_pass_enter(LOGIN, ""), False)

   def test_check_no_login(self):
       self.assertEqual(login_pass_enter("", PASS), False)

   def test_check_not_supported_login(self):
       self.assertEqual(login_pass_enter("#';.:$%_!1N&_", PASS), False)

   def test_check_not_supported_pass(self):
       self.assertEqual(login_pass_enter(LOGIN, "#';.:$%_!1N&_"), False)
