from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set the URL of the page to download
url = "https://www.classcentral.com/"

# Start a new instance of the Chrome driver
driver = webdriver.Chrome()

# Load the page and wait for it to load completely
driver.get(url)
time.sleep(5)

# Find the Courses button and hover over it
button = driver.find_element("xpath", '//*[@id="page-home"]/div[1]/header/div[1]/nav/div[1]/button[2]')
ActionChains(driver).move_to_element(button).perform()

# Wait for the dynamic content to load
time.sleep(2)

# Get the HTML content of the loaded dynamic content
dynamic_content = driver.find_element("xpath", '//*[@id="page-home"]/div[1]/header/div[1]/nav/div[1]/nav/div').get_attribute('innerHTML')

ActionChains(driver).move_by_offset(200, 10).perform()

# Save the downloaded HTML to a file
with open('classcentral.html', 'w') as f:
    f.write(driver.page_source)
    f.write(dynamic_content)

# Quit the driver
driver.quit()
