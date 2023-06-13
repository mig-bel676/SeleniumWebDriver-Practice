from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ChromeDriver is what connects Selenium to Chrome
chromeDriverPath = "/Users/mig/Development/chromedriver_mac_arm64/chromedriver"
chrome_options = Options()
# Keeps browser open
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.appbrewery.co/p/newsletter")

# Extracting Web Data
# articleAmount = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# articleAmount.click()

# tools = driver.find_element(By.LINK_TEXT, "View history")
# tools.click()

# Inserting keys into text fields for Form Input
# search = driver.find_element(By.NAME, 'search')
# search.send_keys("Python" + Keys.ENTER)


signUpLink = driver.find_element(By.XPATH, '//*[@id="blocks"]/section[2]/div/a')
signUpLink.click()

nameInput = driver.find_element(By.XPATH, '//*[@id="name"]')
nameInput.send_keys("Miguel Beltran")

emailInput = driver.find_element(By.NAME, "email")
emailInput.send_keys("mlarios676@gmail.com")







