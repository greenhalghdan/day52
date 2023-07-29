import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By

import os

INSTAGRAM_USERNAME = os.environ.get("username")
INSTAGRAM_PASSWORD = os.environ.get("password")
SIMILAR_ACCOUNT = "charles_leclerc"


class InstaFollower():
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--headless=True")
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_web_driver = Service(r"C:\Users\green\Downloads\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.chrome_web_driver, options=self.chrome_options)
        self.driver.maximize_window()

    def login(self):
        self.driver.get(F"https://www.instagram.com/{SIMILAR_ACCOUNT}/")


    def find_followers():
        pass
    def follow(self):
        pass

follow = InstaFollower()
follow.login()
follow.find_followers()
follow.follow()