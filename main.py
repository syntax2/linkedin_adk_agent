import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options # <-- Import Options
from webdriver_manager.chrome import ChromeDriverManager

# ---- NEW PART STARTS HERE ----

# Create a new Options object
# Create a new Options object
chrome_options = Options()

# Add an argument to tell Selenium to use your Chrome profile data
# This path points to the main "apartment building"
chrome_options.add_argument(r"user-data-dir=C:\Users\ak255213\AppData\Local\Google\Chrome\User Data")

# ---- NEW LINE HERE ----
# Add a second argument to specify the exact "apartment number"
chrome_options.add_argument(r"--profile-directory=Profile 4")

print("Starting our agent with your specific Chrome profile ('Profile 4')...")

# Pass the options when creating the driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# ---- NEW PART ENDS HERE ----

print("Navigating to LinkedIn Jobs...")
# Now we go to a more specific URL that shows jobs
driver.get("https://www.linkedin.com/jobs/search/")

time.sleep(3)

print("Finding the job search box...")
# The class name might be different on this new page, let's use a more robust one.
# XPath is like a precise address to an element on the page.
search_box = driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Search job titles')]")

print("Typing 'SRE or DevOps' into the search box...")
search_box.send_keys("SRE or DevOps")

print("Pressing Enter to start the search...")
search_box.send_keys(Keys.RETURN)

print("Waiting for search results to load...")
time.sleep(5)

print("Agent has finished its run.")
driver.quit()