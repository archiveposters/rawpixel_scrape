## Web Scrape with Selenium

The project is aimed at returning the image titles and urls from rawpixel search results for all urls in urls.csv and record results in info.csv

### Setup

This script is to be used locally and will not work if run through GitPod

Version originally used Pycharm on Windows, however if system requirements are different please adjust accoringly.

Clone the repo using:

gh repo clone jamiebird119/web_scrape

Install dependencies using pip. In the case of pycharm CLI command is as follows but depends on it being windows and on pycharm IDE.

py -m pip install -r requirements.txt

Ensure that the correct version of chromedriver is used for the corresponding version of chrome on windows. To check version click 3 dots in top right 
go to Help > About Google Chrome. It will show you the version and then go to https://chromedriver.chromium.org/downloads and get the version for your operating system.
Unzip file and place in project directory ensuring Path in run.py has been updated to your version (Path can easily be found by right clicking file in Pycharm and clicking copy path )

Any urls for searches from rawpixel.com can then be added to urls.csv on a new row for each. 

Run programme using on Pycharm using:

py -m run.py

New browser window should open, be scrapped in the background and then close. Do not close window or programme with stop. 






