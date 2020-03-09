from selenium import webdriver
from datetime import datetime
from time import sleep

from whatspy.chrome import Chrome


class Whatsapp:
    
    @staticmethod
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
        
        try:
        
            # Not logged in
            small_timeout = 5
            while not chrome.element_exists_at(selectors['search_input'], timeout=small_timeout):
                qrcode = chrome.wait_for(selectors['qrcode'], timeout=small_timeout)
                chrome.screenshot('qrcode.png')
                
                print('Look for whatsapp QRCode inside your running directory.')
                sleep(small_timeout)
            
            print('Whatsapp successfully logged in...')
            
            chrome.screenshot('screens/1.png')
            
            chrome.wait_for(selectors['search_input']).send_keys(to)
            chrome.wait_for(selectors['search_result']).click()
            
            chrome.screenshot('screens/2.png')
            
            chrome.wait_for(selectors['message_input']).send_keys(message + '\n')
            # chrome.wait_for(selectors['message_send']).click()  # replaced by '\n' on previous line
            
            chrome.screenshot('screens/3.png')
        except Exception as e:
            print('An unexpected error occured. Quiting chrome now')
            chrome.screenshot('screens/error.png')
            chrome.quit()
            
            raise e

if __name__ == '__main__':
    message = 'whatsapp-bot ' + str(datetime.now())
    to = 'Saldo Contas'
    
    Whatsapp.send(message, to)
    