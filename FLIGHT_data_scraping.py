import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from bs4 import BeautifulSoup
import pandas as pd


driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.kayak.co.uk/flights/VNO-LON/2024-05-03/2024-05-05/2adults?sort=bestflight_a"
driver.get(url)
time.sleep(5)


try:
    cookies_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#portal-container > div > div.c-ulo.c-ulo-mod-variant-popup.c-ulo-mod-position-top.c-ulo-mod-direction-none.c-ulo-mod-visible > div > div > div.qMs4 > div > span.qMs4-close > button')))  # Update the CSS selector as per the site's layout
    cookies_button.click()
except (TimeoutException, ElementClickInterceptedException) as e:
    print(f"Error clicking the cookies button: {e}")

for _ in range(34):
    try:
        show_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ULvh-button")))
        driver.execute_script(
            "window.scrollTo(0, arguments[0].getBoundingClientRect().top + window.scrollY - (window.innerHeight / 2));",
            show_more_button)
        time.sleep(2)
        show_more_button.click()
        time.sleep(5)
    except (ElementClickInterceptedException, TimeoutException) as e:
        print(f"Error clicking 'Show More' button: {e}")


soup = BeautifulSoup(driver.page_source, 'html.parser')
flight_elements = soup.find_all('div', class_='nrc6')

flight_data = []

for element in flight_elements:
    try:
        price = element.find('div', class_='f8F1-price-text').text.strip().replace('£', '')
        flight_time_elements = element.find_all('div', class_='vmXl-mod-variant-large')
        if len(flight_time_elements) >= 2:
            outbound_time = flight_time_elements[0].text.strip()
            return_time = flight_time_elements[1].text.strip()
        flight_times = element.find_all('div', class_='xdW8 xdW8-mod-full-airport')
        if len(flight_times) >= 1:
            outbound_hours = flight_times[0].text.strip()
            return_hours = flight_times[1].text.strip()


        stops_elem = element.find('span', class_='JWEO-stops-text')
        stops = stops_elem.text.strip() if stops_elem else 'No stops'

        flight_data.append({
            'Price': price,
            'Outbound Time': outbound_time,
            'Outbound hours': outbound_hours,
            'Return Time': return_time,
            'Return hours': return_hours,
            'Stops': stops})
    except AttributeError:
        print("Error extracting data from an element")

driver.quit()


df = pd.DataFrame(flight_data)
csv_file_name = 'sorted_flights.csv'
df.to_csv(csv_file_name, index=False, encoding='utf-8-sig')


for flight in flight_data:
    print(flight)