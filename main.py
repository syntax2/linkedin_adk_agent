import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# --- Options Setup ---
chrome_options = Options()
chrome_options.add_argument(r"user-data-dir=C:\Users\ak255213\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument(r"--profile-directory=Profile 4")
chrome_options.add_argument("--disable-dev-shm-usage")

print("Starting our agent with your specific Chrome profile ('Profile 4')...")
# We declare the driver variable here so it's accessible in the 'finally' block
driver = None 

try:
    # We pass the options when creating the driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    print("Navigating to LinkedIn Jobs...")
    driver.get("https://www.linkedin.com/jobs/search/")

    time.sleep(3)

    print("Finding the job search box...")
    search_box = driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Search job titles')]")

    print("Typing 'SRE or DevOps' into the search box...")
    search_box.clear() # Good practice to clear the field first
    search_box.send_keys("SRE or DevOps")

    print("Pressing Enter to start the search...")
    search_box.send_keys(Keys.RETURN)

    print("Waiting for search results to load...")
    time.sleep(5)

finally:
    # This 'finally' block will run NO MATTER WHAT.
    # It ensures the browser closes properly even if the script fails.
    if driver:
        print("Agent has finished its run. Closing the browser.")
        driver.quit()