from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time



url="https://toas.fi/nopeasti-saatavilla/"

driver = Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)

time.sleep(5)

# driver.find_element_by_css_selector('CybotCookiebotDialogBodyButton').click()
driver.find_element("xpath", '//button[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()

time.sleep(5)





