from bs4 import BeautifulSoup
import requests
import pandas as pd

hotels_data = []
for i in range(0, 901, 25):
    url = f'https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaIgBiAEBmAEZuAEXyAEP2AEB6AEBiAIBqAIDuAKQqd2tBsACAdICJDFiM2JmMTk4LTI0ZDQtNDQ1YS1iM2JkLTExMGMxZDFjNDBkOdgCBeACAQ&sid=3ac9bb671d8a29bbb469e531db5d2ffd&aid=304142&ss=Londonas&ssne=Londonas&ssne_untouched=Londonas&lang=en-gb&src=index&dest_id=-2601889&dest_type=city&checkin=2024-05-03&checkout=2024-05-05&group_adults=2&no_rooms=1&group_children=0&nflt=ht_id%3D204&offset={i}&soz=1&lang_changed=1'
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    hotels = soup.findAll('div', {'data-testid': 'property-card'})

    for hotel in hotels:
        name = hotel.find('h3', class_="aab71f8e4e").text.strip().replace('Opens in new window', '')
        location = hotel.find('span', {'data-testid': 'address'}).text.strip().replace(', London', '')
        price = hotel.find('span', {'data-testid': 'price-and-discounted-price'}).text.strip().replace('€\xa0', '').replace(',', '')
        rating_elem = hotel.find('div', {'class': 'a3b8729ab1 d86cee9b25'})
        rating_meaning_elem = hotel.find('div', {'class': 'a3b8729ab1 e6208ee469 cb2cbb3ccb'})
        distance = hotel.find('span', {'data-testid': 'distance'}).text.strip().replace('km from centre', '').replace('350 m from centre', '0.3')
        breakfast = hotel.find('span', {'class': 'a19404c4d7'})
        free_cancelation = hotel.find('div', {'class': 'abf093bdfe d068504c75'})


        if breakfast is not None:
            breakfast = breakfast.text.strip()
        else:
            breakfast = "-"

        if free_cancelation is not None:
            free_cancelation = free_cancelation.text.strip()
        else:
            free_cancelation = "-"

        rating = rating_elem.text.strip() if rating_elem else ''
        rating_meaning = rating_meaning_elem.text.strip() if rating_meaning_elem else ''



        hotels_data.append({
            'Name': name,
            'Location': location,
            'Price': price,
            'Rating': rating,
            'Rating meaning': rating_meaning,
            'Distance from the centre (km)': distance,
            'Breakfast': breakfast,
            'Free cancelation': free_cancelation
        })

        if not any(hotel['Name'] == name for hotel in hotels_data):
            hotels_data.append(hotels_data)




df = pd.DataFrame(hotels_data)
df.to_csv('booking.csv', header=True, index=False)
print(df)