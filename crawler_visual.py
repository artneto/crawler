# Libraries
from bs4 import BeautifulSoup
import requests
from csv import writer


base_url = "https://www.myhome.ie/rentals/ireland/property-to-rent?"


property_list = []


for i in range(1, 25):    
    url=base_url+f"page={i}"
    print(url)
    response  = requests.get(url)


    soup = BeautifulSoup(response.content, 'html.parser')
    lists = soup.find_all('div', class_='PropertyListingCard__Content')


    # Loop over the property listings
    for list in lists:
        try:
            title = list.find('a', class_='PropertyListingCard__Address').text
        except AttributeError:
            title = "none"
        try: 
            price = list.find('div', class_='PropertyListingCard__Price').text
        except AttributeError:
            price = "none"
        try:
            room = list.find('span', class_='PropertyInfoStrip__Detail').text
        except AttributeError:
            room = "none"


        # Write the data to the file
        info = [title, price, room]
        property_list.append(info)


    print(f'page {i} Done _______________')
    print(len(lists))
    
#Creating csv file and adding data to it
f = open('housefile.csv', 'w', encoding='utf8', newline='')
thewriter = writer(f)
header = ['Title', 'Price', 'Room']
thewriter.writerow(header)





for property in property_list:
    thewriter.writerow(property)
f.close()
print("Completed")
