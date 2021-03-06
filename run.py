from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv


def set_chrome_options():
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

def scrape(url, fd, writer):
    driver = webdriver.Chrome(options=set_chrome_options())
    # load page
    driver.get(url)


    info = []
    # find all figure elements
    elements = driver.find_elements_by_xpath("//figure")
    print(len(elements))
    element = 1
    
    while element <= (len(elements)+1):
        # return title and link for each 
        xpath_title = f"//figure[{int(element)}]/div/img"
        xpath_link = f"//figure[{int(element)}]/div/a[2]"
        
        try:
            # ignore if they dont contain img and link
            title = driver.find_element_by_xpath(xpath_title).get_attribute('alt')
            link = driver.find_element_by_xpath(xpath_link).get_attribute('href')
            print(title)
            print(link)
            info.append([title, link])
            element += 1
        except Exception as e:

            element += 1

    driver.close()
    # append to info.csv
    for item in info:
        writer.writerow({"title": item[0], "url": item[1]})


with open('./data/urls.txt', mode='r') as csv_file:
    urls = csv_file.readlines()
    
    with open("./data/info.csv", mode="w") as fd:
        fieldnames = ["title", "url"]
        writer = csv.DictWriter(fd, fieldnames=fieldnames)
        writer.writeheader()
        for url in urls:
            scrape(url, fd, writer)
