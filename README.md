# BOOKING.COM HOTELS AND KAYAK.CO.UK FLIGHTS ANALYSIS

### DETAILS

Created by: Saule Staneviciute and Alsu Saakjan

This is the end project in Vilnius Coding School, Data Analytics and Fundamentals of Python program.

Project theme: Scraping web pages for hotels in London and flights (VNO - LDN) from May 3rd to 5th.

Project goal: Identify the most cost-effective accommodation options and secure the best flight deals for an upcoming trip.

# Applied Knowledge
Used libraries: pandas, matplotlib, numpy, seaborn, selenium, scikit-learn

# Project Steps

## Scraping Booking.com & Kayak.co.uk → 
### BOOKING_data_scraping.py

Steps:
1. Used the requests library to fetch HTML content from Booking.com search results pages.
2. Utilized BeautifulSoup to parse the HTML content and navigate through the structure of the web page.
3. For each hotel listing, extracted relevant details such as name, location, price, rating, distance, breakfast availability, and free cancellation possibility.
5. Used Pandas to convert the list of dictionaries (hotels_data) into a DataFrame, and removed duplicate entries.
6. Saved the cleaned data to a CSV file named 'booking.csv'


### FLIGHT_data_scraping.py

Steps:
1. Used Selenium with Chrome WebDriver to automate browser interactions, opening the Kayak website, handling any pop-ups, also clicking the "Show More" button and scrolling to reveal more options.
3. Utilized BeautifulSoup to parse the HTML content and extract flight details such as price, outbound and return times, hours, and stops.
4. Implemented error handling to manage potential exceptions while extracting data.
5. Organized flight data, converted it to a Pandas DataFrame, and saved it as 'sorted_flights.csv'.


## Hotel Analysis → 
A file where calculations and visuals were made for booking.com hotel extracted data.

What was done:
* Bar chart for the 10 most cheap hotels;
* Bar chart for hotels and their average price by locations


## Flight Analysis → 
Having cleaned and transformed the data for analysis,

* Bar chart to represent the average prices for direct flights, flights with one stop, and flights with two stops;

Distribution of flight prices was:

IKELTI <distribution-flights.png>

Correlation of the chosen features looked like this:

IKELTI <correlation-flights.png>

After testing several regression models, the best fit was GradientBoostingRegressor:

| Measure | Score |
|:---:|:---:|
| R2 | 0.743 |
| R2 to train data | 0.858 |
| MAE | 20.419 |
| MSE | 712.077 |
| RMSE | 26.685 |

**The final model can predict flight ticket prices with an error of  ≈ 20.42 £**

IKELTI <final-model-flights.png>

# Conclusions
