#!/bin/env python

from selenium import webdriver


def main():
    driver = webdriver.Chrome("c:\\dev\\bin\\chromedriver.exe");
    driver.get("http://www.skiutah.com");
    title = driver.title;
    print ("Title = " + title);

if __name__ == '__main__':
    main()


