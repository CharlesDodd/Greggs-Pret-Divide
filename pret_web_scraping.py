import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# Set up ChromeDriver options
options = Options()
options.add_argument('--window-size=1920,1200')

DRIVER_PATH = r'C:\Users\charl\Downloads\chromedriver-win64\chromedriver.exe'

# List of addresses
address_data = []

# Chrome driver with Service
try:
    service = Service(DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    print("Browser opened successfully!")
    driver.get('https://www.pret.co.uk/en-GB/shop-finder/l')  # Test navigation
    print(f"Navigated to: {driver.current_url}")
    print('waiting...')
    time.sleep(5)
    print('done')
    soup = BeautifulSoup(driver.page_source, 'lxml')
    links = [a['href'] for a in soup.find_all('a', href=lambda x: x and 'shop-finder/l/' in x) if a.get('href')]
    print(f"Extracted links: {links}")

    for location in links:
        driver.get(location)
        print(f"Navigated to: {driver.current_url}")
        print('waiting...')
        time.sleep(4)
        print('done')
        soup = BeautifulSoup(driver.page_source, 'lxml')

        print(f"Navigated to: {driver.current_url}")
        print('waiting...')
        time.sleep(4)
        print('done')
        soup = BeautifulSoup(driver.page_source, 'lxml')
        div_text=soup.find_all("div",{"class":"ubsf_sitemap-location-address"})
        for loc in div_text:
            address_data.append(loc.get_text())
        print(address_data)
        
    driver.quit()
    print("Browser closed.")
except Exception as e:
    print(f"Error: {e}")
    print("Ensure ChromeDriver path is correct and matches your Chrome version.")

df = pd.DataFrame({'address': address_data})
df.to_csv('pret_addresses.csv', index=False)
