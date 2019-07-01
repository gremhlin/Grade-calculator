from selenium import webdriver
import unittest
class NewUserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_enter_averages_and_retrive_grades(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Django', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
