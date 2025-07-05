import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

print("Starting our agent...")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

print("Navigating to LinkedIn Jobs...")
driver.get("https://www.linkedin.com/jobs/")

# Let's give the page a moment to load all its elements
time.sleep(3) 

# ---- NEW PART STARTS HERE ----

print("Finding the job search box...")
# We find the element by its class name. This is like the 'label' in our robot analogy.
search_box = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")

print("Typing 'SRE or DevOps' into the search box...")
# We use .send_keys() to type into the element we found
search_box.send_keys("SRE or DevOps")

print("Pressing Enter to start the search...")
# We send the 'RETURN' key, which is the same as Enter
search_box.send_keys(Keys.RETURN)

# ---- NEW PART ENDS HERE ----

# Let's wait to see the search results
print("Waiting for search results to load...")
time.sleep(5)

print("Agent has finished its run.")
driver.quit()