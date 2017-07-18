#!/bin/env python
import configparser
from selenium import webdriver
from utils import *
import os
import sys

"""Automation utilities class"""


class Automation:
    """Gets the web driver. Uses the chrome driver specified in automation.ini"""

    def __init__(self):
        self._driver = None

    """Gets the current instance of the driver; creates one if none exists."""
    def get_driver(self):
        if self._driver is None:
            print(os.getcwd())
            config = configparser.ConfigParser()
            config.read("automation.ini")
            webdriver_data = config['webdriver']
            path = webdriver_data['path']
            print(path)
            self._driver = webdriver.Chrome(path)
        return self._driver

    """Gets the web driver. Uses the chrome driver specified in automation.ini"""
    def go_to_page(self, page):
        driver = self.get_driver()
        driver.get(page)

    """Gets tht title of the current page"""
    def get_title(self):
        eprint("Automation get title")
        return self._driver.title


    """Cleans up and closes the web browser."""
    def quit(self):
        if self._driver is not None:
            self._driver.quit()
            self._driver=None