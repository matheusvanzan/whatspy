# WhatsPy

Python Whatsapp API based on Selenium and ChromeDriver

> Working as of Mar 09 2020

## Usage

![ChromePy](/whatspy/img/chromepy.png)

`Chrome` and `ChromeRemote` work together to control the browser instance. Once
`Chrome` has been started with `start_chrome.py`, you can just start the remote 
with `start_remote.py` and it will use the same browser instance.

See my ![ChromePy](https://github.com/matheusvanzan/chromepy) repo for more info on the remote aproach.

## Limitations

- All web.whatsapp.com limitations
- Scan QRCode on first run
- You must have a persons number saved to your phone
- You must set the contact exact and complete saved name
- Names must be unique in your contacts list

## QRCode scan

A `screens/qrcode.png` file is saved for scaning with your smartphone. 
WhatsPy will try to save a profile so you don't need to scan the qrcode everytime.
Keep in mind that whatsapp logs you out if you try to login in multiple browsers.

## Chrome Install

WhatsPy uses a Chrome class that is just a wraper Singleton for the Selenum 
default implementation adding a few easy to use enhancements.

To use chrome with selenium you will need ChromeDriver.

A `profile` directory will be added to your project directory to save chrome profile.

## Roadmap

- [x] Save QRCode image for scan
- [ ] Read latest chats
- [ ] Read latest messages from chat
- [x] Send message to contact by name (unique)
- [ ] Send message to contact by number
- [ ] Read latest archived chats
- [ ] Read latest archived messages from chat
- [ ] Archive chat
- [ ] Unarchive chat