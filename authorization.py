from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from auth_data import username, password
import time
import random


def login(username, password):
    with webdriver.Chrome('../chromedriver/chromedriver') as browser:
        try:
            browser.get('https://www.instagram.com')

            # Waiting while the field for the username is loaded
            username_input = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            username_input.clear()
            username_input.send_keys(username)

            # Waiting for the password field to load
            password_input = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_input.clear()
            password_input.send_keys(password)

            password_input.send_keys(Keys.ENTER)

            # Waiting for Instagram main page to load
            WebDriverWait(browser, 10).until(
                EC.title_contains("Instagram")
            )

            print("Log in to Instagram successfully!")
        except Exception as ex:
            print(f"An error occurred: {ex}")


login(username, password)