#!/bin/env python

from selenium import webdriver


def load_page_and_get_title():
    path = 'c:\\dev\\bin\\chromedriver.exe'

    driver = webdriver.Chrome(path)

    driver.get("http://www.skiutah.com")
    return driver.title
    driver.close()


def main():
    title = load_page_and_get_title()
    print("Title is: " + title)



if __name__ == '__main__':
    main()


