import requests
from bs4 import BeautifulSoup

# URL of the webpage to extract viewable content from
url = "https://www.example.com"

# Define the custom User-Agent header
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

# Send a GET request to the webpage with the custom User-Agent header
response = requests.get(url, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the viewable content from the HTML
viewable_content = ""
for tag in soup.find_all():
    if tag.name in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a']:
        if tag.string:
            viewable_content += tag.string + "\n"

# Save the viewable content to a text file
with open('viewable_content.txt', 'w', encoding='utf-8') as f:
    f.write(viewable_content)
