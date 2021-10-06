#import from selenium driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


#designate each URL to be opened
url_1 = 'https://www.facebook.com/'
url_2 = 'https://www.facebook.com/'
url_3 = 'https://www.facebook.com/'

#designate webdriver as chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

#open 1st URL in first tab
driver.get(url_1)

#wait
driver.implicitly_wait(15)

#open new window (tab 2) and switch over to it
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

#open 2nd URL in current tab
driver.get(url_2)

#wait
driver.implicitly_wait(15)

#open new window (tab 3) and switch over to it
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])

#open 3rd URL in current tab
driver.get(url_3)

#wait
driver.implicitly_wait(15)

#game on
driver.switch_to.window(driver.window_handles[0])

usr = "user_name_here"
pwd = "password_here"

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
# print("Email Id entered")

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
# print("Password entered")

# sleep(1)
# login_box = driver.find_element_by_name('login')
# login_box.click()

#window2

driver.switch_to.window(driver.window_handles[1])

usr2 = "user_name_here"
pwd2 = "password_here"


username_box = driver.find_element_by_id('email')
username_box.send_keys(usr2)
# print("Email Id entered")

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd2)
# print("Password entered")

# sleep(1)
# login_box = driver.find_element_by_name('login')
# login_box.click()

#window3
driver.switch_to.window(driver.window_handles[2])

usr3 = "user_name_here"
pwd3 = "password_here"


username_box = driver.find_element_by_id('email')
username_box.send_keys(usr3)
# print("Email Id entered")

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd3)
# print("Password entered")

# sleep(1)
# login_box = driver.find_element_by_name('login')
# login_box.click()

# driver.switch_to.window(driver.window_handles[0])
for i in range(0, 3):
    driver.switch_to.window(driver.window_handles[i])
    sleep(1)
    login_box = driver.find_element_by_name('login')
    login_box.click()
    i += 1
