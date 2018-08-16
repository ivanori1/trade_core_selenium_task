# tradecore_selenium_task

This project is written in Pycharm 2018.2 and to make easier to write .feature files install plugin: Gherkin

Suggested tools:
* Python version: Both 2.7.14 and 3.x.x are acceptable. (3.6 used)
* Framework: Behave (BDD) used  
* Webdriver: ChromeWebDriver used 

Requirements: 

install package:
behave  in cmd/terminal type: 
```
pip install behave
```
and selenium
```
pip install selenium
```
Webdriver:

The ChromeDriver controls the browser using Chrome's automation proxy framework.
The server expects you to have Chrome installed in the default location for each system:

Download ChromeDriver on this [link](https://chromedriver.storage.googleapis.com/index.html) (version I am currently using is 2.41)

Set path of ChromeWebDirver:
```
OS          Expected Location of Chrome
-------------------------------------
Linux          /usr/bin/google-chrome
Mac            /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome
Windows XP     %HOMEPATH%\Local Settings\Application Data\Google\Chrome\Application\chrome.exe
Windows Vista  C:\Users\%USERNAME%\AppData\Local\Google\Chrome\Application\chrome.exe
```
more detail on [ChromeDriver wiki](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver)
