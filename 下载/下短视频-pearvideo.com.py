import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from selenium_example.tool import get_browser
from 下载 import mp4下载工具

count = 1

browser = get_browser()


def craw():
    """爬排行榜"""
    url = "https://www.pearvideo.com/popular"
    response = requests.get(url)
    file = open("../电影.html", "wb")
    file.write(response.content)
    file.flush()
    file.close()


def parse():
    """分析排行榜"""
    soup = BeautifulSoup(open("../电影.html"), features="lxml")

    for one in soup.find_all("a", class_="actplay"):
        url = one.get("href")
        get_video_url(url)


def get_video_url(url):
    """找到动态的视频地址"""
    url = "https://www.pearvideo.com/" + url

    # 点击播放
    browser.get(url)
    element = browser.find_element(by=By.XPATH, value='//*[@id="poster"]/i')
    element.click()

    # 获取新添加的video代码
    soup = BeautifulSoup(browser.page_source, 'lxml')
    sp1 = soup.find_all('video')
    url = sp1[0].get("src")
    print(url)

    global count
    mp4下载工具.down_from_url(url, str(count))
    count = count + 1


parse()
