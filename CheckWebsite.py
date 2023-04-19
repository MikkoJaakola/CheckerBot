from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



url="https://toas.fi/nopeasti-saatavilla/"

modific_time = "nill"

def getModifiedTime():
    driver = Chrome(service=Service(ChromeDriverManager().install()))

    # Open toas website
    driver.get(url)

    # click cookie consent button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'))).click()


    # driver.find_element("xpath", '//button[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
    x = driver.find_element("xpath", '//meta[@property="article:modified_time"]').get_attribute("content")

    return x

modific_time = getModifiedTime()


print(modific_time)





