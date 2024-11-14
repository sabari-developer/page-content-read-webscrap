import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to fetch
url = 'https://example.com'

# Sending a GET request to fetch the raw HTML content
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Full HTML content
    html_content = response.text
    print("Full HTML content fetched successfully.")
    
    # If you want to parse and prettify the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup.prettify())
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
