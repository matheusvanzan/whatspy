import os
from os.path import expanduser

from selenium.webdriver.chrome.options import Options


DEFAULT_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
DEFAULT_DRIVER = '/usr/bin/chromedriver'

PATH = os.path.dirname(os.path.realpath(__file__))
DATA = 'user-data-dir={}/profile'.format(PATH)
SESSION = '{}/session'.format(PATH)


# chrome options
OPTIONS = Options()
OPTIONS.add_argument('--headless')
OPTIONS.add_argument('--window-size=1920x1080')
OPTIONS.add_argument('--disable-infobars')
OPTIONS.add_argument('--disable-dev-shm-usage')
OPTIONS.add_argument('--no-sandbox')
OPTIONS.add_argument('--remote-debugging-port=9222')
OPTIONS.add_argument('--user-agent=' + DEFAULT_USER_AGENT)
OPTIONS.add_argument(DATA)