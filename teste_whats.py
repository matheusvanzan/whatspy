from chrome import Chrome
from datetime import datetime

from time import sleep

chrome = Chrome()

chrome.get('http://web.whatsapp.com')


chrome.get_screenshot_as_file('whats_1.png')

# input_submit = chrome.find_element_by_css_selector('input[type=submit]')
# input_submit.click()

# chrome.get_screenshot_as_file('2.png')

# sleep(5)

# chrome.get_screenshot_as_file('3.png')

chrome.quit()