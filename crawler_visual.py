# Libraries
from bs4 import BeautifulSoup
import requests
from csv import writer

# Make a request to the URL
url = "https://www.myhome.ie/rentals/ireland/property-to-rent"
response  = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.content, 'html.parser')
lists = soup.find_all('div', class_='PropertyListingCard__Content')

# Open the file for writing
f = open('housefile.csv', 'w', encoding='utf8', newline='')
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
    thewriter.writerow(info)
    print(info)
f.close()
print("done")