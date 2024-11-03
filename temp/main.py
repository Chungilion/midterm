from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

# Set up the Selenium WebDriver with your specified path
service = Service('D:/Python Code/chromedriver/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Base URL with placeholder for the page number
base_url = "https://www.topuniversities.com/universities/taiwan?country=[TW]&page={}"

# Prepare a list to hold the university data
data = []

# Page counter
page = 1

while True:
    # Load the page based on the page number
    url = base_url.format(page)
    driver.get(url)
    time.sleep(3)  # Wait for the page to load

    # Find university cards on the page
    university_cards = driver.find_elements(By.CSS_SELECTOR, ".card")
    if not university_cards:
        print("No more universities found, ending pagination.")
        break

    # Extract data from the current page
    for card in university_cards:
        try:
            # Find the name and location using the selectors based on the HTML structure
            name = card.find_element(By.CSS_SELECTOR, ".uni-det a .bold-text").text
            location = card.find_element(By.CSS_SELECTOR, ".location").text

            # Extract the QS ranking based on the new structure
            qs_ranking_element = card.find_element(By.CSS_SELECTOR, ".uni_ranking .cont")
            qs_ranking = qs_ranking_element.text.strip() if qs_ranking_element else "N/A"

            # Extract all 'li' items from the university card's 'uni-info' section
            info_items = card.find_elements(By.CSS_SELECTOR, ".uni-info li")
            status = research_output = student_faculty_ratio = international_students = total_faculty = "N/A"

            # Iterate over 'li' items to extract relevant data based on the title attribute
            for item in info_items:
                title = item.get_attribute("title")
                value = item.text.strip()

                if title == "Status":
                    status = value
                elif title == "Research Output":
                    research_output = value
                elif title == "Student/Faculty Ratio":
                    student_faculty_ratio = value
                elif title == "International Students":
                    international_students = value
                elif title == "Total Faculty":
                    total_faculty = value

        except Exception as e:
            # In case any element is missing, handle the exception gracefully and continue
            print(f"An error occurred while extracting data: {e}")
            continue
        
        # Append the data for each university
        data.append([name, location, qs_ranking, status, research_output, student_faculty_ratio, international_students, total_faculty])

    # Increment the page number
    page += 1

# Convert the collected data to a DataFrame
df = pd.DataFrame(data, columns=['Name', 'Location', 'QS Ranking', 'Status', 'Research Output', 'Student/Faculty Ratio', 'International Students', 'Total Faculty'])

# Export the DataFrame to a CSV file
df.to_csv('taiwan_universities_detailed.csv', index=False, encoding='utf-8-sig')

# Close the driver
driver.quit()
