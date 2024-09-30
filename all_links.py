from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Google")
    search_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    links = driver.find_elements(By.XPATH, "//a[@href]")

    for i, link in enumerate(links, start=1):
        xpath = f"(//a[@href])[{i}]"
        url = link.get_attribute("href")
        print(f"XPath: {xpath} | URL: {url}")

finally:
    driver.quit()
