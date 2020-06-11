from time import sleep
from chrome import Chrome


chrome = Chrome.instance
chrome.get('https://web.whatsapp.com')

for i in range(5):
    input('Press any key to quit chrome...')
    print(chrome.current_url)
    print('    ', chrome.command_executor._url, chrome.session_id)

chrome.quit()