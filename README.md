# tradecore_selenium_task

This project is written in Pycharm 2018.2 and to make easier to write .feature files install plugin: Gherkin

Suggested tools:
* Python version: Both 2.7.14 and 3.x.x are acceptable. (3.6 used)
* Framework: Behave (BDD) used with combination with Page Object Model (POM)
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

For Linux:

1) Move the file to /usr/bin directory sudo mv chromedriver /usr/bin

2) Goto /usr/bin directory and you would need to run something like "chmod a+x chromedriver" to mark it executable. 

For Windows:

Paste the chromedriver.exe file in "C:\Python\Scripts" Folder.

more detail on [ChromeDriver wiki](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver)

Structure of the prject is:

```
.
└── features
   ├── create_your_account.feature
   ├── questionnaire.feature
   ├── environment.py
   ├── steps
   |   ├── questionnaire_steps.py
   |   └── crate_your_account_steps.py
   ├── pages
   |   ├── questionnaire_page.py
   |   └── crate_your_account_page.py
   └── base
       └── browser.py
```
Here's a brief explanation of the files:
* **environment.py**: Define code to run before and after certain events during testing. (starts WebDriver)
* **.feature**: Written test for create account and login, with scenarios an steps.
* **steps/**: This is where Behave will initially look for the code for tests via decorators.
* **pages/**: Use locators in file and webDriver methods from browser.py for implementing steps 
* **base/browser.py**: Contains all webDriver actions wrapped to unique methods to make code reduced and easy to maintain. 

To run test case open terminal in project root directory and type:
```
behave
```
