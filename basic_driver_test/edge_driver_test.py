import unittest
from selenium import webdriver
from config import edge_web_driver_path, test_title, test_url


class MyTestCase(unittest.TestCase):

    def test_edge_driver_works(self):

        driver = webdriver.Edge(executable_path=edge_web_driver_path)
        driver.get(test_url)
        title = driver.title
        driver.close()
        self.assertEqual(test_title, title)

