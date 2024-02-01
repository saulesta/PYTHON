BOOKING.COM HOTELS AND KAYAK.CO.UK FLIGHTS ANALYSIS

DETAILS
Created by: Saule Staneviciute and Alsu Saakjan

This is the end project in Vilnius Coding School, Data Analytics and Fundamentals of Python program.

Project theme: scraping web pages for hotels in London and flights (VNO - LDN) during May 3rd to 5th, to see...
Project goal:

# Applied Knowledge
Used libraries: pandas, matplotlib, numpy, seaborn, selenium, scikit-learn

# Project Steps

## Scraping Booking.com & Kayak.co.uk → 
BOOKING_data_scraping.py

Steps:
1. Used the requests library to fetch HTML content from Booking.com search results pages.
2. Utilized BeautifulSoup to parse the HTML content and navigate through the structure of the web page.
3. For each hotel listing, extracted relevant details such as name, location, price, rating, distance, breakfast availability, and free cancellation possibility.
5. Used Pandas to convert the list of dictionaries (hotels_data) into a DataFrame, removed duplicate entries.
6. Saved the cleaned data to a CSV file named 'booking.csv'

FLIGHT_data_scraping.py

Steps:
1. Used Selenium with Chrome WebDriver to automate browser interactions, opening the Kayak website, handling any pop-ups, also clicking the "Show More" button and scrolling to reveal more options.
3. Utilized BeautifulSoup to parse the HTML content and extract flight details such as price, outbound and return times, hours, and stops.
4. Implemented error handling to manage potential exceptions while extracting data.
5. Organized flight data, converted it to a Pandas DataFrame, and saved it as 'sorted_flights.csv'.

## Hotel Analysis → 

## Flight Analysis → 

# Conclusions
