from selenium.webdriver import Chrome as SeleniumChrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException

import os

from random_user_agent.user_agent import UserAgent

from random_user_agent.params import OperatingSystem
from random_user_agent.params import HardwareType
from random_user_agent.params import SoftwareName

DEFAULT_USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
DEFAULT_DRIVER = '/usr/bin/chromedriver'

DEFAULT_OPERATING_SYSTEMS = [
    OperatingSystem.WINDOWS.value, 
    OperatingSystem.LINUX.value,
    OperatingSystem.MAC.value
]

DEFAULT_HARDWARE_TYPES = [
    HardwareType.COMPUTER.value
]

DEFAULT_SOFTWARE_NAMES = [
    SoftwareName.CHROME.value
]


class Chrome(SeleniumChrome):
    
    def __init__(self, rotate_user_agent=False):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1920x1080')
        # chrome_options.add_argument('--remote-debugging-port=8082')
        chrome_driver = DEFAULT_DRIVER
        
        chrome_options.add_argument('user-data-dir=/home/vanzan/whatspy/chromepy/profile')
        
        # User agent
        if rotate_user_agent:
            user_agent_rotator = UserAgent(
                operating_systems=DEFAULT_OPERATING_SYSTEMS,
                hardware_types=DEFAULT_HARDWARE_TYPES,
                software_names=DEFAULT_SOFTWARE_NAMES,
                limit=100
            )
            user_agent = user_agent_rotator.get_random_user_agent()
            chrome_options.add_argument('--user-agent=' + user_agent)
        else:
            chrome_options.add_argument('--user-agent=' + DEFAULT_USER_AGENT)

        return super(Chrome, self).__init__(chrome_options=chrome_options, executable_path=chrome_driver)
        
    def screenshot(self, path):
        return self.get_screenshot_as_file(path)
        
    def element_exists_at(self, selector, timeout=None):
        return self.wait_for(selector, timeout) is not None
        
    def wait_for(self, selector, timeout=None):
        if not timeout: 
            timeout = 60 # seconds
        
        try:
            wait = WebDriverWait(self, timeout)
            loc = (By.CSS_SELECTOR, selector)
            
            wait.until(EC.presence_of_element_located(loc))
            wait.until(EC.visibility_of_element_located(loc))
            # wait.until(EC.elementToBeClickable(loc))
            
            print('Found', selector)
            return self.find_element_by_css_selector(selector)
        except TimeoutException:
            print('Loading took too much time!')
            self.screenshot('chromepy/error.png')
            return None