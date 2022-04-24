from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from info import user, password, hashtags
from selenium.webdriver.chrome.service import Service
from random import randint


class LikeBot():

    def __init__(self):
        self.login(user, password)
        self.like_by_hashtag(hashtags)

    def login(self, username, password):
        # driver setup
        service = Service('[chromedriver_path e.g. C:\Python\chromedriver.exe]')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        # go to instagram and login
        self.driver.get('https://instagram.com/')
        sleep(2)
        username_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        sleep(1)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        sleep(1)
        # click through inital popups
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(3)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()  # clicks 'not now'
        sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()  # clicks 'not now'

    def like_by_hashtag(self, hashtags):
        for hashtag in hashtags:
            self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))   # lookup hashtag
            self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/section/main/article/div[2]/div/div[1]/div[1]').click()  # clicks the first 'most recent' post
            for i in range(hashtags[hashtag]):
                sleep(randint(5, 10))
                try:
                    self.driver.find_element(By.CSS_SELECTOR, "[aria-label='Unlike']")  # checks to see if the post is already liked
                except:
                    self.driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()  # likes post
                sleep(randint(2, 4))
                self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div[2]').click() # next picture


def main():
    while True:
        my_bot = LikeBot()
        sleep(3600) # one hour max runtime


if __name__ == '__main__':
    main()