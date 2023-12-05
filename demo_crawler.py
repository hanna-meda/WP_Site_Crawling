import requests
from bs4 import BeautifulSoup
import csv

# URL of the WordPress site's homepage
url = 'https://shroomareala.ro'

# Send a GET request to fetch the page content
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract hyperlinks from the page
    links = [link.get('href') for link in soup.find_all('a') if link.get('href')]

    # Write the extracted data to a CSV file
    csv_filename = 'wp_site_links.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Links'])  # Write header

        # Write each link to the CSV file
        for link in links:
            writer.writerow([link])

    print(f"Hyperlinks have been extracted and saved to '{csv_filename}'")
else:
    print("Failed to fetch the page")
