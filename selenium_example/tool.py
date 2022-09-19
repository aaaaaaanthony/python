from selenium import webdriver


def get_browser():
    """获取浏览器对象"""
    browser = webdriver.Chrome(executable_path="/Users/anthony/Downloads/chromedriver")
    return browser
