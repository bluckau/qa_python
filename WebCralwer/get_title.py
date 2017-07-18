#!/bin/env python

from selenium import webdriver
from automation import *

"""" Demo get title python application"""

def main():
    auto = Automation()
    auto.go_to_page("https://www.skiutah.com")
    print("Title is: " + auto.get_title())


if __name__ == '__main__':
    main()


