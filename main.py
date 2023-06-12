from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# ChromeDriver is what connects Selenium to Chrome
chromeDriverPath = "/Users/mig/Development/chromedriver_mac_arm64/chromedriver"
chrome_options = Options()
# Keeps browser open
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.python.org")

searchbar = driver.find_element(By.NAME, "q")

print(searchbar.siz)



