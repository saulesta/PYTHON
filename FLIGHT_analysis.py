import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

file_path = "C:/Users/User/PycharmProjects/pythonPradmenys(1pamoka)/sorted_flights.csv"
sorted_flights_df = pd.read_csv(file_path)
#print(sorted_flights_df)

stops_counts = sorted_flights_df['Stops'].value_counts()
print("Number of direct flights:", stops_counts.get('direct', 0))
print("Number of flights with one stop:", stops_counts.get('1 stop', 0))
print(stops_counts)

average_prices = sorted_flights_df.groupby('Stops')['Price'].mean().round(2)
print("Average price for direct flights:", average_prices.get('direct', 0))
print("Average price for flights with one stop:", average_prices.get('1 stop', 0))
print(average_prices)


average_prices = sorted_flights_df.groupby('Stops')['Price'].mean().round(2)

fig = px.bar(
    x=average_prices.index,
    y=average_prices.values,
    labels={'x': 'Number of Stops', 'y': 'Average Price'},
    title='Average Prices for Direct Flights and Flights with One Stop'
)
fig.show()

import plotly.express as px
data = {
    'Stops': ['1 stop', 'direct', '2 stops'],
    'Flights': [6, 373, 52],
    'Average Price': [316.00, 229.13, 154.87]
}
df = pd.DataFrame(data)
fig = px.bar(
    df,
    x='Stops',
    y='Average Price',
    text='Flights',
    labels={'Average Price': 'Average Price (£)', 'Flights': 'Number of Flights'},
    title='Average Prices and Number of Flights by Stops'
)
fig.show()

