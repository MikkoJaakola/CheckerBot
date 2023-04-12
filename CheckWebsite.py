from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


url="https://toas.fi/nopeasti-saatavilla/"

driver = Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)





