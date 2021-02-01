from selenium import webdriver
import csv


def scrape(url):
    # webdriver must match current version of chrome on correct OS from https://chromedriver.chromium.org/downloads
    driver = webdriver.Chrome(r"C:\Users\J\Documents\GitHub\selenium_base\chromedriver.exe")
    # load page
    driver.get(url)


    info = []
    elements = driver.find_elements_by_xpath("//figure")
    print(len(elements))
    element = 1
    while element <= (len(elements)+1):
        xpath_title = f"//figure[{int(element)}]/div/img"
        xpath_link = f"//figure[{int(element)}]/div/a[2]"
        # finds all teaser image figures on the page
        try:
            title = driver.find_element_by_xpath(xpath_title).get_attribute('alt')
            link = driver.find_element_by_xpath(xpath_link).get_attribute('href')
            print(title)
            print(link)
            info.append([title, link])
            element += 1
        except Exception as e:
            print(e)
            element += 1
    # for each teaser image figure get title and url
    #for element in title_elements:
    #    titles.append(element.get_attribute('alt'))
    #for link in link_elements:
    #    url_list.append(link.get_attribute('href'))

    # zips titles and urls
    #info = zip(titles, url_list)

    driver.close()
    # append to info.csv
    with open("info.csv", mode="a") as fd:
        fieldnames = ["title", "url"]
        writer = csv.DictWriter(fd, fieldnames=fieldnames)
        writer.writeheader()
        for item in info:
            writer.writerow({"title": item[0], "url": item[1]})


with open(r'C:\Users\J\Documents\GitHub\selenium_base\urls.csv', mode='r') as csv_file:
    # reads csv file for urls in first column
    csv_reader = csv.DictReader(csv_file)
    row_count = 0
    urls = []
    for row in csv_reader:
        # writes url to new line of info.csv
        with open('info.csv', mode='a') as new_file:
            fieldnames = ["url"]
            writer = csv.DictWriter(new_file,fieldnames=fieldnames)
            writer.writerow({"url": row['url']})
        scrape(row['url'])
