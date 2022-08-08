import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By

EMAIL = "sarunasj82@gmail.com"
PASSWORD = "*********"

web_driver_path = "C:\Development/chromedriver.exe"
driver = webdriver.Chrome(web_driver_path)
driver.get("https://tinder.com/")
driver.fullscreen_window()
log_in = driver.find_element(By.XPATH,
                             '//*[@id="q554704800"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()
driver.fullscreen_window()
time.sleep(3)
log_with_facebook = driver.find_element(By.XPATH,
                                        '//*[@id="q-1173676276"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
log_with_facebook.click()
driver.fullscreen_window()
time.sleep(3)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

enter_email = driver.find_element(By.XPATH, '//*[@id="email"]')
enter_email.send_keys(EMAIL)
enter_password = driver.find_element(By.XPATH, '//*[@id="pass"]')
enter_password.send_keys(PASSWORD)
time.sleep(3)
login = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
login.click()

driver.switch_to.window(base_window)

allow_button = driver.find_element(By.XPATH, '//*[@id="q-1173676276"]/div/div/div/div/div[3]/button[1]')
allow_button.click()
time.sleep(2)
not_interest_button = driver.find_element(By.XPATH, '//*[@id="q-1173676276"]/div/div/div/div/div[3]/button[2]')
not_interest_button.click()
time.sleep(2)
i_accept_button = driver.find_element(By.XPATH, '//*[@id="q554704800"]/div/div[2]/div/div/div[1]/div[1]')
i_accept_button.click()

for _ in range(100):
    time.sleep(3)
    try:
        like_button = driver.find_element(By.XPATH,
                                          '//*[@id="q554704800"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            popup.click()
        except NoSuchElementException:
            time.sleep(3)

driver.quit()
