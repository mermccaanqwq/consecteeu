from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("http://www.google.com")

# Define a function to click an element by XPath with a wait time
def click_Xpath(driver, wait_time, xpath):
    # Wait until the element is clickable
    element = WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    # Click the element
    element.click()

# Use the function to click the 'update_btn'
click_Xpath(driver, 5, "//button[@id='update_btn']")

# Close the driver after the operations are done
driver.quit()
