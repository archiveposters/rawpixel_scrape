## Web Scrape with Selenium

The project is aimed at returning the image titles and urls from rawpixel search results for all urls in urls.csv and record results in info.csv

### Setup

This script runs on Docker. Make sure you have Docker installed in your environment.


#### Build the image

```
docker build -t rawpixel_scrape
```

#### Run the container

```
docker run -v `pwd`/data:/app/data rawpixel_scrape
```


Any urls for searches from rawpixel.com can then be added to urls.csv on a new row for each. 

Run programme using on Pycharm using:

$ py -m run.py

New browser window should open, be scrapped in the background and then close. Do not close window or programme with stop. 






