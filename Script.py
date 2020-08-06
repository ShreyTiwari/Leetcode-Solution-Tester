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
from pynput.keyboard import Key, Controller

""" The Leetcode class with all the functionality """
class Leetcode:
    # Initialization of the object at the time of creation
    def __init__(self, url = "https://www.leetcode.com"):         
        profile = webdriver.FirefoxProfile()
        #profile.set_preference("browser.privatebrowsing.autostart", True)
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
        fp = open(path, "r")
        file = fp.readlines()
        testcases = ("".join(file)).split(';\n')
        fp.close()
        return testcases[:-1]

    # Run the test cases
    def test(self, testcases):
        time.sleep(3)
        results = []
        
        driver = self.driver
        keyboard = Controller()
        
        # Open the console tab
        button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div/div[3]/div[1]/button")
        button.click()
        time.sleep(5)

        for testcase in testcases:
            # Click on the testcase tab
            button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div")
            button.click()
            time.sleep(1)
            
            # Click on the testcase entry area
            # button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div")
            # button.click()
            # time.sleep(1)

            # button.clear()
            # button.send_keys(testcase)

            # Clear whatever is present
            keyboard.press(Key.tab)
            time.sleep(0.1)

            with keyboard.pressed(Key.ctrl):
                keyboard.press('a')
                keyboard.release('a')
            keyboard.press(Key.backspace)
            print("Testing new test case.")
            time.sleep(1)

            # Type in the test case
            keyboard.type(testcase)
            time.sleep(1)

            # Click on the run test button
            button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div/div[3]/div[2]/button[1]")
            button.click()
            time.sleep(3)

            # Check the results
            res = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]")
            if res.text == "Accepted":
                results.append(1)
            else:
                results.append(0)
            time.sleep(1)

        # Close the console tab
        button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div/div[3]/div[1]/button")
        button.click()
        time.sleep(1)

        return results

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
    path = input("Please enter the path to your input testcases file: ")
    print("Proceeding to parse the input test cases...")
    testcases = None
    if path:
        testcases = lc.parse(path)
    else:
        testcases = lc.parse()

    for i in testcases:
        print("Testcase: ", i, end="")

    if(testcases):
        print("The test cases were parsed and loaded successfully")
    else:
        print("There was an Error while parsing the test cases.")
        print("Closing the Browser session... ")
        lc.closeBrowser()
        exit(1)
    print("-------------------------------------------\n")
    choice = input("Do you wish to run the test cases now? (y/n): ")

    yes = ['y', 'Y', 'yes', 'Yes']
    while choice in yes:
        # Run the test cases
        try:
            results = lc.test(testcases)
        except:
            print("There was an Error while execution.")
            break
        
        print("\n--------------------------- Result of the execution ---------------------------")
        res = ["Failed", "Pass"]
        for i in range(len(results)):
            print("Test case ", i, ": ", res[results[i]])

        print("\n-------------------------------------------")
        choice = input("Re-Run the tests? (y/n): ")    
    
    print("Exiting.")
    lc.closeBrowser()
    exit(0)