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


if __name__ == "__main__":

    print("\n--------------------------- Welcome ---------------------------")
    
    # Copy and paste the url of the problem statement
    url = input("Please enter the problem statement's URL: ")

    print("\nAttempting to open the browser...")
    print("-------------------------------------------")

    # Open the Leetcode website
    lc = Leetcode(url)
    success = lc.open()
    
    if(success):
        print("Leetcode opened in successfully. Please")
        print("-------------------------------------------\n")
    else:
        print("There was an Error.")
        print("-------------------------------------------\n")
        print("Closing Browser Session")
        lc.closeBrowser()
        exit(1)


    # Getting the required data
    ig.goToHomePage()
    followers = ig.getFollowers()
    followingAccounts = set(ig.getFollowingAccounts())

    ig.closeBrowser()

    # The important part is the difference (followingAccounts - Followers), i.e who you are following but are not following you
    for follower in followers:
        if(follower in followingAccounts):
            followingAccounts.remove(follower)

    print("\n--------------------------- Result ---------------------------")
    print("Number of accounts not following you back are: ", len(followingAccounts))
    print("The people you need to stop following are:")
    for i in followingAccounts:
        print(i)

    exit(0)