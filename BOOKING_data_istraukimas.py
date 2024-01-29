from bs4 import BeautifulSoup
import requests
import pandas as pd

for i in range(0, 901):
    url = 'https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaIgBiAEBmAEZuAEXyAEP2AEB6AEBiAIBqAIDuAKQqd2tBsACAdICJDFiM2JmMTk4LTI0ZDQtNDQ1YS1iM2JkLTExMGMxZDFjNDBkOdgCBeACAQ&sid=3ac9bb671d8a29bbb469e531db5d2ffd&aid=304142&ss=Londonas&ssne=Londonas&ssne_untouched=Londonas&lang=en-gb&src=index&dest_id=-2601889&dest_type=city&checkin=2024-05-03&checkout=2024-05-05&group_adults=2&no_rooms=1&group_children=0&nflt=ht_id%3D204&offset={i}&soz=1&lang_changed=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

hotels = soup.findAll('div', {'data-testid': 'property-card'})

hotels_data = []

for hotel in hotels:
    name = hotel.find('div', {'data-testid': 'title'}).text.strip()
    location = hotel.find('span', {'data-testid': 'address'}).text.strip()
    price = hotel.find('span', {'data-testid': 'price-and-discounted-price'}).text.strip().replace('€\xa0', '')
    rating = hotel.find('div', {'class': 'a3b8729ab1 d86cee9b25'}).text.strip()
    rating_meaning = hotel.find('div', {'class': 'a3b8729ab1 e6208ee469 cb2cbb3ccb'}).text.strip().replace('Review score', 'Fair')
    distance = hotel.find('span', {'data-testid': 'distance'}).text.strip()
    #stars = hotel.find('div', {'data-testid': 'rating-stars'})
    breakfast = hotel.find('span', {'class': 'a19404c4d7'})
    free_cancelation = hotel.find('div', {'class': 'abf093bdfe d068504c75'})


    hotels_data.append({
        'Name': name,
        'Location': location,
        'Price': price,
        'Rating': rating,
        'Rating meaning': rating_meaning,
        'Distance': distance,
        'Breakfast': breakfast,
        #'Free cancelation': free_cancelation
        #'stars': stars
    })

#print(hotels_data)

pd.set_option('display.max_rows' , 500)
pd.set_option('display.max_columns' , 500)
pd.set_option('display.width' , 2000)

df = pd.DataFrame(hotels_data)
# df.to_csv('booking.csv', header=True, index=False)
print(df)