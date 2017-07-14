#!/bin/env python
import sys
sys.path.append('.')
import unittest
from selenium import webdriver

from challenge1 import *

class TestStringMethods(unittest.TestCase):
    driver = None

    def tearDown(self):
        self.driver.close

    def setUp(self):
        title = load_page_and_get_title;
        path = 'c:\\dev\\bin\\chromedriver.exe'
        self.driver = webdriver.Chrome(path)

    def test_title(self):
        self.driver.get("http://www.skiutah.com");
        title = self.driver.title;
        self.assertEqual ("Ski Utah | Utah Ski Resorts, Lift Tickets, Ski Passes, Maps & More! - Ski Utah",+ title);
