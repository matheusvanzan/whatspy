from selenium import webdriver
from chromepy.chrome import Chrome
from datetime import datetime
from time import sleep


class Whatsapp:
    
    def send(message, to):
        
        selectors = {
            'qrcode': 'canvas',
            'search_input':  '#side .copyable-text.selectable-text',
            'search_result': '#side span[title="{}"]'.format(to),
            'message_input': '#main footer div.copyable-text.selectable-text',
            'message_send':  '#main footer button span[data-icon="send"]'
        }
        
        chrome = Chrome()
        chrome.get('http://web.whatsapp.com')
        
        # Not logged in
        if not chrome.element_exists_at(selectors['search_input']):
            qrcode = chrome.wait_for(selectors['qrcode'])
            chrome.screenshot('qrcode.png')
            
            print('Look for whatsapp QRCode inside chromepy folder.')
            input('...')
        else:
            print('Whatsapp already logged in...')
        
        chrome.screenshot('screens/1.png')
        
        chrome.wait_for(selectors['search_input']).send_keys(to)
        chrome.wait_for(selectors['search_result']).click()
        
        chrome.screenshot('screens/2.png')
        
        chrome.wait_for(selectors['message_input']).send_keys(message)
        chrome.wait_for(selectors['message_send']).click()
        
        chrome.screenshot('screens/3.png')
        
        chrome.quit()


if __name__ == '__main__':
    message = 'whatsapp-bot ' + str(datetime.now())
    # to = 'Nathalia Marinho'
    # to = 'Dan Godoy'
    to = 'Saldo Contas'
    
    whats = Whatsapp()
    whats.send(message, to)
    