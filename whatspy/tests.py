import unittest

from chrome import Chrome
from remote import ChromeRemote


class ChromeTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.url1 = 'https://www.google.com/'
        cls.url2 = 'https://www.w3schools.com/'
        cls.chrome = Chrome.instance

    def test_start_chrome(self):
        self.chrome.get(self.url1)
        self.assertEqual(self.url1, self.chrome.current_url)
        
    def test_start_remote_1(self):
        remote1 = ChromeRemote()
        self.assertEqual(self.url1, remote1.current_url)
        remote1.get(self.url2)
        
    def test_start_remote_2(self):
        remote2 = ChromeRemote()
        self.assertEqual(self.url2, remote2.current_url)
        
    @classmethod
    def tearDownClass(cls):
        cls.chrome.quit()

        
        

if __name__ == '__main__':
    unittest.main()
