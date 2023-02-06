# Libraries
from bs4 import BeautifulSoup
import requests

url = 'https://www.myhome.ie/rentals/ireland/property-to-rent'
page = requests.get(url)

# This object will have two paraments to get the html and to parse the html.
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_='PropertyListingCard__Content')

# loop to check the same information in other pages

for list in lists:
    title = list.find('div', class_='PropertyListingCard__Address ng-tns-c193-1')
    price = list.find('div', class_='PropertyListingCard__Price ng-tns-c193-1')
    info = [title,price]
    print(info)