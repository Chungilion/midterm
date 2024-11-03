from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Set up the Selenium WebDriver with your specified path
service = Service('D:/Python Code/chromedriver/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Open the website
base_url = 'https://edurank.org/cs/ai/ar//'
driver.get(base_url)
time.sleep(3)  # Wait for the page to load

# Prepare a list to hold the university data
data = []

# Find university cards on the page
university_cards = driver.find_elements(By.CSS_SELECTOR, 'div.block-cont.pt-4.mb-4')
if not university_cards:
    print("No university cards found on the page. Please verify the CSS selector.")
else:
    # Extract data from the current page
    for card in university_cards:
        try:
            # Extract the university name
            name = card.find_element(By.CSS_SELECTOR, 'h2.h4 a').text.strip()
        except:
            name = "N/A"

        # Extract location (city and country)
        try:
            location = card.find_element(By.CSS_SELECTOR, 'div.uni-card__geo').text.strip()
        except:
            location = "N/A"

        # Extract Latin America rank
        try:
            rank_latam = card.find_element(By.XPATH, ".//div[contains(@class, 'uni-card__rank') and contains(., 'Latin America')]/span[@class='text-fat']").text.strip()
        except:
            rank_latam = "N/A"

        # Extract world rank
        try:
            rank_world = card.find_element(By.XPATH, ".//div[contains(@class, 'uni-card__rank') and contains(., 'the World')]/span[@class='text-fat']").text.strip()
        except:
            rank_world = "N/A"

        # Extract founded year
        try:
            founded_year = card.find_element(By.XPATH, ".//dt[text()='Founded']/following-sibling::dd").text.strip()
        except:
            founded_year = "N/A"

        # Append the data for each university
        data.append([name, location, rank_latam, rank_world, founded_year])

# Convert the collected data to a DataFrame
df = pd.DataFrame(data, columns=['University', 'Location', 'AI Rank Latin America', 'AI Rank World', 'Founded Year'])

# Export the DataFrame to a CSV file
df.to_csv('ai_universities_full_data.csv', index=False, encoding='utf-8-sig')
print("Data saved to ai_universities_full_data.csv")

# Display the DataFrame
print(df)

# Close the driver
driver.quit()
