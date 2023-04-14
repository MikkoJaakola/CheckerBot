from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time



url="https://toas.fi/nopeasti-saatavilla/"

modific_time = "nill"

def getModifiedTime():
    driver = Chrome(service=Service(ChromeDriverManager().install()))

    # Open toas website
    driver.get(url)

    # click cookie consent button
    driver.find_element("xpath", '//button[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()

    x = driver.find_element("xpath", '//meta[@property="article:modified_time"]').get_attribute("content")

    return x

modific_time = getModifiedTime()


print(modific_time)





