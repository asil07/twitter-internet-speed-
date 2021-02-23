from selenium import webdriver
import time
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:/development/chromedriver.exe"
WEBSITE_LINK = "https://www.speedtest.net/"
TWITTER_USERNAME = "Your username"
TWITTER_PASSWORD = "Your password"
class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(WEBSITE_LINK)
        time.sleep(2)
        self.driver.find_element_by_css_selector(".js-start-test").click()
        time.sleep(50)
        self.down = self.driver.find_element_by_css_selector(".download-speed").text
        self.up = self.driver.find_element_by_css_selector(".upload-speed").text
        print(f'down: {self.down}\nup: {self.up}')
        pass


    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]').click()    # login button
        time.sleep(2)
        user_name = self.driver.find_element_by_name("session[username_or_email]")
        user_name.send_keys(TWITTER_USERNAME)
        password = self.driver.find_element_by_name("session[password]")
        password.send_keys(TWITTER_PASSWORD)
        login_profile = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        login_profile.click()

        time.sleep(5)
        entry = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        entry.send_keys(f"My internet speed is \ndown:{self.down}\nup:{self.up} \ncompare to "
                        f"last month \ndown:{PROMISED_DOWN}, up:{PROMISED_UP}")
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet.click()
        self.driver.quit()
        pass