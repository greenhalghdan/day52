import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By

import os

INSTAGRAM_USERNAME = os.environ.get("username")
INSTAGRAM_PASSWORD = os.environ.get("password")
SIMILAR_ACCOUNT = "charles_leclerc"
MAX_FOLLOWS = 15


class InstaFollower():
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--headless=True")
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_web_driver = Service(r"C:\Users\green\Downloads\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.chrome_web_driver, options=self.chrome_options)
        self.driver.maximize_window()
    def login(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(5)
        cookies = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        cookies.click()
        time.sleep(5)
        login = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/section/nav/div[2]/div/div/div[3]/div/div/div[2]/div[1]/a')
        login.click()
        time.sleep(2)
        username = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
        username.send_keys(INSTAGRAM_USERNAME)
        password = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
        password.send_keys(INSTAGRAM_PASSWORD)
        login_button = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button')
        login_button.click()
        time.sleep(2)
    def find_followers(self):
        savelogininfo = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        savelogininfo.click()
        time.sleep(2)
        followers = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        all_followers = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div')
        return list_of_followers = all_followers.find_elements(By.TAG_NAME, value="button")
        print(list_of_followers)

    def follow(self, list_of_followers):
        followscompleated = 0
        if followscompleated > MAX_FOLLOWS:
            for follower in list_of_followers:
                follower.click()
                time.sleep(2)
                followscompleated += 1

follow = InstaFollower()
follow.login()
list_of_followers = follow.find_followers()
follow.follow(list_of_followers)
time.sleep(900000)