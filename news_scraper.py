
import requests
from bs4 import BeautifulSoup

# URL of a news site (example used here: BBC)
url = 'https://www.bbc.com/news'

# Send GET request
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# Parse HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all headlines (h3 or h2 tags - based on site structure)
headlines = soup.find_all(['h3', 'h2'])

# Extract text and save to list
headline_list = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

# Write to a .txt file
with open('headlines.txt', 'w', encoding='utf-8') as file:
    for title in headline_list:
        file.write(title + '\n')

print("Headlines saved to 'headlines.txt'")
