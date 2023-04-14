from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time



url="https://toas.fi/nopeasti-saatavilla/"

driver = Chrome(service=Service(ChromeDriverManager().install()))

# Open toas website
driver.get(url)

time.sleep(5)

# click cookie consent button
driver.find_element("xpath", '//button[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()

modific_time = driver.find_element("xpath", '//meta[@property="article:modified_time"]').get_attribute("content")

time.sleep(5)

print(modific_time)





