from chromepy.chrome import Chrome

from datetime import datetime
from time import sleep

chrome = Chrome()
chrome.get('http://web.whatsapp.com')
sleep(10)

chrome.get_screenshot_as_file('chromepy/qrcode.png')
print('Waiting for authorization...')
print('Look for whatsapp QRCode inside chromepy folder.')
print('Found it? (y/N)')
input()

chrome.get_screenshot_as_file('chromepy/main.png')

input('press any key')

url = chrome.command_executor._url
session_id = chrome.session_id

print('url', url)
print('session_id', session_id)

print('Press any key to stop ...')
input()

chrome.quit()