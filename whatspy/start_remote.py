from time import sleep
from remote import ChromeRemote


remote1 = ChromeRemote()
print('remote1', remote1.current_url)
remote1.get('https://google.com')

# for i in range(5):
#     input('Press any key to quit chrome...')
#     print('remote', remote.current_url)

# remote.quit()

remote2 = ChromeRemote()
print('remote2', remote2.current_url)

# remote1.quit()
# remote2.quit()  CANT QUIT, it quits the driver