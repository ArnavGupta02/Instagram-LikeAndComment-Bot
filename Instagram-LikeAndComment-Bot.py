from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

comments_list = ["wow!", "Amazing", "Well played", "Damn!", "Pure Talent", "Lovely", "Beautiful",
                         "nice", "amazing post", "🔥🔥", "i love this", "this is so good", "dope!", "i like this post",
                         "amaze!", "speechless!", "do check my covers", "you deserve more likes", "❤️❤️❤️"]

hashtags = ["fingerstyle", "guitar", "guitarvideo", "instaguitar"]


class InstaBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Firefox()  # for chrome : self.browser = webdriver.Chrome() 

    def login(self):
        browser = self.browser
        browser.get('https://www.instagram.com/accounts/login/')

        time.sleep(3)
        username_enter = browser.find_element_by_name('username')
        username_enter.send_keys(self.username)

        time.sleep(3)
        password_enter = browser.find_element_by_name('password')
        password_enter.send_keys(self.password)

        password_enter.send_keys(Keys.RETURN)  # press login button (by pressing enter)
        time.sleep(8)

    def initial_posts(self):
        browser = self.browser

        time.sleep(2)
        initial_posts = browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
        initial_posts.click()

        for latest_posts in range(8):   # Navigate to latest Posts
            time.sleep(2)
            browser.find_element_by_link_text('Next').click()

    def next_post(self):
        browser = self.browser

        time.sleep(3)
        next_button = browser.find_element_by_link_text('Next')
        next_button.click()

    def like_post(self):
        browser = self.browser

        time.sleep(random.randint(3, 6))
        like = browser.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button")
        like.click()

    def comment_post(self):
        browser = self.browser

        temp_comments_list = comments_list.copy()

        comment_button = browser.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[2]/button")
        time.sleep(3)
        comment_button.click()

        comment_text_area = browser.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea")
        time.sleep(3)
        comment_text_area.click()
        comment = random.choice(temp_comments_list)

        time.sleep(random.randint(3, 6))
        comment_text_area.send_keys(comment)
        temp_comments_list.remove(comment)

        time.sleep(random.randint(3, 6))
        post_button = browser.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button")
        time.sleep(random.randint(3, 6))
        post_button.click()

    def main(self):
        browser = self.browser

        for hashtag in hashtags:
            browser.get(f"https://www.instagram.com/explore/tags/{hashtag}") 
            print(f"#{hashtag} started...")

            self.initial_posts()
            post_number = 1
            while post_number <= 16:   # Like 15 Posts per hashtag
                self.next_post()
                self.like_post()
                try:
                    self.comment_post()
                except Exception:
                    pass

                print(f"{post_number} post(s) liked and commented...")
                post_number += 1

            print(f"#{hashtag} done...")

        print(""""
        -----------------------------------------------------
        """)


session = InstaBot(username, password)  # Enter username and password in respective positions
session.login()
session.main()
