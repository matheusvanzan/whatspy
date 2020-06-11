from remote import ChromeRemote
from datetime import datetime

remote = ChromeRemote()
remote.save_screenshot('screen_{}.png'.format(datetime.now()))