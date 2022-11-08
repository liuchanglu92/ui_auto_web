import unittest
from pages.login_page import LoginPage
from common.keys import Testkeys
class LoginCase(unittest.TestCase):
    def test_login_success(self):
        LoginPage.login(self)
        url1 = Testkeys.get_url(self)
        self.assertEqual(url1,'https://1.cih-index.com/investmentproject/3.0/index')


if __name__ == '__main__':
    unittest.main()
