import pandas as pd
import requests
from bs4 import BeautifulSoup
#main link of page, an usko  req karenge aane ko
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XnDEzKgzZaA")
#compulsory hey likhne ko:
soup = BeautifulSoup(page.content, 'html.parser')
#approx ye bhi compulsory hey: bss ismey apn ko jo cheez crawl krni hhey  usko id,class wagera likhni padhti hey
amazon = soup.find(id = "seven-day-forecast-body")
#issmey apn ko chheze chahiye usko filter krte hey upper wali id se
items = amazon.find_all(class_="tombstone-container")
print(items[0])
items2 = items[0].find(class_='period-name').get_text()
items3 = items[0].find(class_='short-desc').get_text()
items4 = items[0].find(class_='temp').get_text()

#print(items2,"\n",items3,"\n",items4)
#foor loop chalaya hey jiss se saari cheezey aajaye::
period_names = [item.find(class_="period-name").get_text() for item in items]
#print(period_names)
description = [item.find(class_="short-desc").get_text() for item in items]
#print(description)
temperature =  [item.find(class_="temp").get_text() for item in items]
#print(temperature)

wheather_stuff = pd.DataFrame({
    'period' : period_names,
    'Description': description,
    'Temperature' : temperature
})
print(wheather_stuff)
wheather_stuff.to_csv("wheather_csv") 