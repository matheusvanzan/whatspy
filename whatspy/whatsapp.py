from selenium import webdriver
from datetime import datetime
from time import sleep

from chrome import Chrome


class Whatsapp:
    
    def __init__(self):
        self.selectors = {
            'qrcode': 'canvas',
            'search_input':  '#side .copyable-text.selectable-text',
            'search_result': '#side span[title="{}"]',
            'message_input': '#main footer div.copyable-text.selectable-text',
            'message_send':  '#main footer button span[data-icon="send"]'
        }
        
        url = 'http://web.whatsapp.com'
        
        self.chrome = Chrome.instance
        
        if self.chrome.current_url != url:
            self.chrome.get(url)
        
        
    def _ensure_page_load(self):
        pass
        
    def _check_valid_qrcode(self):
        # Not logged in
        small_timeout = 5
        while not self.chrome.element_exists_at(self.selectors['search_input'], timeout=small_timeout):
            qrcode = self.chrome.wait_for(self.selectors['qrcode'], timeout=small_timeout)
            self.chrome.screenshot('screens/qrcode.png')
            
            print('Look for whatsapp QRCode inside your running directory.')
            sleep(small_timeout)
        
        print('Whatsapp successfully logged in...')
        self.chrome.screenshot('screens/1.png')

    def _search_for_chat(self, to):
        self.chrome.wait_for(self.selectors['search_input']).send_keys(to)
        self.chrome.wait_for(self.selectors['search_result'].format(to)).click()
        self.chrome.screenshot('screens/2.png')
    
    def _type_message(self, message):
        self.chrome.wait_for(self.selectors['message_input']).send_keys(message + '\n')
        # self.chrome.wait_for(selectors['message_send']).click()  # replaced by '\n' on previous line
        self.chrome.screenshot('screens/3.png')
    
    def send(self, message, to):
        
        try:
            self._check_valid_qrcode()
            self._search_for_chat(to)
            self._type_message(message)
            
        except Exception as e:
            print('An unexpected error occured. Quiting chrome now')
            self.chrome.screenshot('screens/error.png')
            self.chrome.quit()
            
            raise e
            
            
    def load_chats(self):
        '''
            return a triple (name, timestamp) for every chat open
        '''
        return_chats = []
        sel = '#pane-side'
        
        timeout = 15
        chatbox = self.chrome.wait_for('#pane-side', timeout=timeout)
        chats = chatbox.find_elements_by_css_selector('div[tabindex]')
        
        self.chrome.screenshot('screens/4.png')
        
        # print('chats', chats)
        for chat in chats:
            # print('---')
            items = chat.text.split('\n')
            print(items[1], items[0])
            return_chats.append( (items[1], items[0]) )
        

if __name__ == '__main__':
    message = 'whatsapp-bot ' + str(datetime.now())
    to = 'Saldo Contas'
    
    whats = Whatsapp()
    # whats.send(message, to)
    whats.load_chats()
    