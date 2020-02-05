import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class AmazonComSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_amazon_com(self):
        driver = self.driver
        driver.get("http://www.amazon.com")
        self.assertIn("Amazon", driver.title)
        elem = driver.find_element_by_class("nav-hamburger-menu").click()
        elem = driver.find_element_by_class("hmenu-item")
        elem = driver.find_element_by_link_text("/Amazon-Video/s/browse?node=2858778011&ref_=nav_em_T1_0_4_5_1__aiv")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    

if __name__ == "__main__":
    unittest.main()