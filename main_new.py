import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

# --- Firefox Options Setup ---
firefox_options = FirefoxOptions()

# --- PASTE YOUR FIREFOX PROFILE PATH HERE ---
# Make sure this path points to your 'xxxxxxxx.linkedin_agent' folder
profile_path = r"C:\Users\<YOUR_USERNAME>\AppData\Roaming\Mozilla\Firefox\Profiles\xxxxxxxx.linkedin_agent"
firefox_options.add_argument("-profile")
firefox_options.add_argument(profile_path)

print("Starting our agent with a dedicated Firefox profile...")
# We declare the driver variable here so it's accessible in the 'finally' block
driver = None

try:
    # This automatically downloads/manages GeckoDriver for Firefox
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

    # First, let's log you in. Go to the LinkedIn login page.
    print("Navigating to LinkedIn to ensure we are logged in...")
    driver.get("https://www.linkedin.com/login")

    # IMPORTANT: Manually log in to LinkedIn in the Firefox window that opens.
    # The script will wait for you for up to 2 minutes (120 seconds).
    input("--> Please log in to LinkedIn in the Firefox browser and then press Enter in this terminal to continue...")

    print("Login confirmed. Navigating to LinkedIn Jobs search...")
    driver.get("https://www.linkedin.com/jobs/search/")

    # Give the page a moment to load
    time.sleep(4)

    print("Finding the job search box...")
    # Using a reliable XPath to find the search input
    search_box = driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Search job titles')]")

    print("Typing 'SRE or DevOps' into the search box...")
    search_box.clear() # Good practice to clear the field first
    search_box.send_keys("SRE or DevOps")

    print("Pressing Enter to start the search...")
    search_box.send_keys(Keys.RETURN)

    print("Waiting for search results to load...")
    time.sleep(5)
    print("Search complete! You can view the results in Firefox.")
    time.sleep(10) # Keep the browser open for 10 seconds to see results

finally:
    # This ensures the browser closes properly
    if driver:
        print("Agent has finished its run. Closing the browser.")
        driver.quit()