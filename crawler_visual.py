# Libraries
from bs4 import BeautifulSoup
import requests
from csv import writer


page = 1
while page != 25:
      url = f"https://www.myhome.ie/rentals/ireland/property-to-rent?page={page}"
      print(url)
      page = page + 1
    
response  = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_='PropertyListingCard__Content')
print(lists)

'''
# Open the file for writing
    with open('housefile.csv', 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['Title', 'Price', 'Room']
        thewriter.writerow(header)



    # Loop over the property listings
    for list in lists:
        title = list.find('a', class_='PropertyListingCard__Address').text
        price = list.find('div', class_='PropertyListingCard__Price').text
        room = list.find('span', class_='PropertyInfoStrip__Detail').text

        # Write the data to the file
        info = [title, price, room]
        thewriter.writerow(info)'''
