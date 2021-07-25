import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def initial():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://translate.google.cn/?hl=zh-CN&tab=TT")
    return driver


def GetTranslationFromGoogle(SendIn):
    driver = initial()

    elem = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
    elem.send_keys(SendIn)
    time.sleep(5)

    text_translation = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[3]')
    string_translation = text_translation.get_attribute("data-text")

    driver.close()
    driver.quit()
    print(string_translation)

    return string_translation



