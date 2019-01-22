from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from time import sleep
import sys

if len(sys.argv) < 3:
    print("\nNeed to have at least 2 arguments")
    print("First argument is the path to the chrome driver. If you don't have it, it can be downloaded at http://chromedriver.chromium.org/downloads")
    print("Second argument is the url of the youtube video that you would like to repeat")
    print("Additional arguments are optional. Each additional argument is the path to a zip file of a chrome extension (ex. addBlock)\n")
    sys.exit(0)

driver_path = sys.argv[1]
url = sys.argv[2]

# Extensions are optional
extensions_paths = 0
if len(sys.argv) > 3:
    extensions_paths = sys.argv[3:]

chrome_options = Options()
if extensions_paths:
    for path in extensions_paths:
        chrome_options.add_extension(path)

driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
driver.get(url)

def check_for_end():
    try:
        return driver.find_element_by_class_name("ytp-ce-element-show")
    except NoSuchElementException:
        return 0

# Waits til video completes
def play_entire_video():
    end_screen = check_for_end()
    while end_screen == 0:
        sleep(0.5)
        end_screen = check_for_end()

# Main loop
while True:
    play_entire_video()
    driver.refresh()
    sleep(1)
