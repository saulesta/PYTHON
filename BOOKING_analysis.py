import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns

file_path = "C:/Users/User/PycharmProjects/pythonPradmenys(1pamoka)/booking.csv"
booking_df = pd.read_csv(file_path)
print(booking_df)


#hoteliai Golders Green
top_hotels = booking_df[booking_df['Location'] == 'Golders Green']
plt.figure(figsize=(20, 10))
plt.scatter(booking_df['Name'], booking_df['Price'], marker='o', alpha=0.6, label='All Hotels')
plt.scatter(x='Name', y='Price', data=top_hotels, color='red', marker='*', label='Golders Green')
plt.ylabel('Price for two nights')
plt.title('Hotel Prices in Different Locations')
plt.legend()
plt.xticks([])
plt.show()



avg_price_by_location_top10 = booking_df.groupby('Location')['Price'].mean().round(2)
plt.figure(figsize = (16,12))
avg_price_by_location_top10.plot(kind = 'bar')
plt.title('Average price by location')
plt.ylabel('Average price')
plt.xticks(rotation = 90,fontsize=8)
plt.savefig('average_price_chart.png')
plt.show()


booking_df['Distance from the centre (km)'] = booking_df['Distance from the centre (km)'].astype('float')


farfromcentre_price = booking_df.groupby('Distance from the centre (km)')['Price'].mean().round(2)
print(farfromcentre_price)


filtered_products1 = (booking_df[booking_df['Breakfast'] == 'Breakfast included'])
filtered_products2 = (filtered_products1['Free cancelation'] == 'Free cancellation')
print(filtered_products2)


