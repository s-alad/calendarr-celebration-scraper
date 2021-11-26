import requests as req
from bs4 import BeautifulSoup
import csv

page = req.get("https://www.calendarr.com/united-states/observances-2022/")
#print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
holidays = soup.find_all('div', class_='holidays-box-col2')
#print(holidays)

newsoup = BeautifulSoup(str(holidays), 'html.parser')
hols = newsoup.find_all('div', class_='row')
#print(len(hols))

counter = 1
file = open('sheet.csv', 'w', newline='')
for month in hols:
    monthsoup = BeautifulSoup(str(month), 'html.parser')
    split = monthsoup.find_all('ul', class_='list-holidays')
    for sp in split:
        spsoup = BeautifulSoup(str(sp), 'html.parser')
        box = spsoup.find_all('li')
        
        for b in box:
            bsoup = BeautifulSoup(str(b), 'html.parser')
            day = bsoup.find('span', class_='holiday-day').text
            nameday = bsoup.find('span', class_='holiday-weekday').text
            name = bsoup.find('div', class_='list-holiday-title').text
            print(counter, day, name.strip())
            date = "{}/{}/{}".format(counter, day, 2022)
            csv.writer(file).writerow([date, name.strip()])

    counter+=1