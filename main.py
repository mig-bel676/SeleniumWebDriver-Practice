from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriver is what connects Selenium to Chrome
chromeDriverPath = "/Users/mig/Development/chromedriver_mac_arm64/chromedriver"
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver = webdriver.Chrome(executable_path=chromeDriverPath)

driver.get("https://www.python.org/")
input_text = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[2]/a')
print(input_text.text)


driver.quit()