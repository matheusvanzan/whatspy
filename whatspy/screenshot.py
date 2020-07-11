from remote import ChromeRemote
from datetime import datetime

remote = ChromeRemote()
remote.save_screenshot('screens/{}.png'.format(datetime.now()))