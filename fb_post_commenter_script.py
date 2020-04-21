from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import time

username = "<put your fb account username here>"
password = "<put your account password here>"
# example
# username = "test@test.com"
# password = "12345"

options = Options()
options.add_argument('--disable-notifications')
options.add_argument('--no-sandbox')
options.add_argument('--disable-extensions')
# options.add_argument('--headless')
prefs = {'profile.default_content_setting_values.notifications': 2}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=options)
driver.get("<put fb post link here>")
# example
# driver.get("https://www.facebook.com/test.user/posts/1726976090778944")

username_box = driver.find_element_by_id("email")
username_box.send_keys(username)

password_box = driver.find_element_by_id("pass")
password_box.send_keys(password)

login_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input")
login_btn.submit()
time.sleep(10)

comment_div_select = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div/div/form/div')
comment_div_select.click()
time.sleep(5)

# in range give the comment limit. default is set as 100
for i in range(0, 100):
    comment_div = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div/div/form/div/div/div[2]/div/div/div/div')
    comment_div.send_keys('Comment ', i + 1)
    # time.sleep(10) # uncomment here and give how many seconds you want to wait for every comment
    comment_div.send_keys(Keys.ENTER)
    time.sleep(2)

# comment_div = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div/div/form/div/div/div[2]/div/div/div/div')
# comment_div.send_keys('Comment 984')
# time.sleep(10)
# comment_div.send_keys(Keys.ENTER)
# time.sleep(20)