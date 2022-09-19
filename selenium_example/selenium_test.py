import time

from bs4 import BeautifulSoup
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

url = "https://www.pearvideo.com/video_1771522"


# 点击播放
browser = webdriver.Chrome(executable_path="/Users/anthony/Desktop/chromedriver")
browser.get(url)
element = browser.find_element(by=By.XPATH, value='//*[@id="poster"]/i')
element.click()

# 获取新添加的video代码
soup = BeautifulSoup(browser.page_source, 'lxml')
sp1 = soup.find_all('video')
url = sp1[0].get("src")
print(url)