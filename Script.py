# Requirements:
#     - Selenium and the corresponding web-drivers
#     - Python 3.6 or above

__author__ = "Shrey Tiwari"
__maintainer__ = "Shrey Tiwari"
__version__ = "1.0.0"
__status__ = "Development"

""" Importing the required headers """
# Webdriver is for navigation through the webpages. Library with the common keys (used in keyboard shortcuts) such as enter etc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# System libraries that will come in handy
import time


""" The Leetcode class with all the functionality """
class Leetcode:
    # Initialization of the object at the time of creation
    def __init__(self, url = "leetcode.com"):         
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        profile.set_preference("browser.fullscreen.autohide", True)
        
        self.url = url
        self.driver = webdriver.Firefox(firefox_profile = profile)

    # To close the webdriver in case of any issues
    def closeBrowser(self):
        self.driver.close()

    # To open the Leetcode website
    def open(self):
        # Flag to indicate success or failure
        flag = False

        # Set the web driver
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(5)

        try:
            # Get function to make a https request. Go to the URL specified by the user (wait for it to load)
            driver.get(self.url)
            time.sleep(3)

        except:
            pass

        current_url = driver.current_url
        if("leetcode" in current_url):
            flag = True
        
        return flag

    # To parse the input test cases
    def parse(self, path = "testcases.txt"):
        pass

if __name__ == "__main__":

    print("\n--------------------------- Welcome ---------------------------")
    
    # Copy and paste the url of the problem statement
    url = input("Please enter the problem statement's URL: ")

    print("\n-------------------------------------------")
    print("Attempting to open the browser...")

    # Open the Leetcode website
    lc = None
    if url:
        lc = Leetcode(url)
    else:
        lc = Leetcode()
    success = lc.open()
    
    if(success):
        print("Leetcode opened successfully.")
    else:
        print("There was an Error.")
        print("Closing the Browser session... ")
        lc.closeBrowser()
        exit(1)
    print("-------------------------------------------\n")

    # Parsing the input test cases
    print("Please enter the path to your input testcases file: ")
    path = input()
    print("Proceeding to parse the input test cases...")
    testcases = None
    if path:
        testcases = lc.parse(path)
    else:
        testcases = lc.parse()

    if(testcases):
        print("The test cases were parsed and loaded successfully")
    else:
        print("There was an Error while parsing the test cases.")
        print("Closing the Browser session... ")
        lc.closeBrowser()
        exit(1)
    print("-------------------------------------------\n")

    choice = 'y'
    yes = ['y', 'Y', 'yes', 'Yes']

    while choice in yes:
        print("Do you wish to run the test cases now? (y/n): ")
        choice = input()

        
        print("\n--------------------------- Result of the execution ---------------------------")
        res = ["Failed", "Pass"]
        for i in range(len(results)):
            print("Test case ", i, ": ", res[results[i]])

    
    
    print("Exiting.")
    ig.closeBrowser()
    exit(0)