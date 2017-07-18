#!/bin/env python
import sys
sys.path.append('.')
import unittest
from selenium import webdriver


"""See http://scrolltest.com/2015/05/11/selenium-test-case-using-data-driven-testing-in-python/"""
from get_title import *


class TestTitle(unittest.TestCase):

    automation = None

    def tearDown(self):
        #TODO: make this static inside of Automation?
        TestTitle.automation.quit()

    def setUp(self):
        TestTitle.automation = Automation()

    def test_title(self):
        TestTitle.automation.go_to_page("http://www.skiutah.com")
        title = TestTitle.automation.get_title();
        self.assertEqual ("Ski Utah | Utah Ski Resorts, Lift Tickets, Ski Passes, Maps & More! - Ski Utah", title);
