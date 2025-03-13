import requests
from bs4 import BeautifulSoup
import csv
import os

# URL to scrape
url = "https://v-tel.co.za/product-category/micro-sd-card/"




# Send a GET request to the webpage
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/90.0.4430.93"}  # Mimic a browser
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to retrieve page: {response.status_code}")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find product containers (adjust based on actual HTML structure)
products = soup.find_all("div", class_="product")  # Example class, update this

# Loop through products and extract details
for product in products:
    # Extract product name (update selector based on inspection)
    name = product.find("h3", class_="auxshp-title-heading")  # Example
    name = name.text.strip() if name else "N/A"

    # Extract price (update selector based on inspection)
    price = product.find("span", class_="price")  # Example
    price = price.text.strip() if price else "N/A"

    # Print or store the data
    print(f"Product: {name}")
print(f"Number of records retrieved: {len(products)}")
          
# Optional: Save to a file (e.g., CSV)

# Define the folder name
output_folder = "output_results"

# Create the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Construct the full file path
file_path = os.path.join(output_folder, "micro_sd_card.csv")

with open(file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price"])  # Header
    for product in products:
        name = product.find("h3", class_="auxshp-title-heading")
        name = name.text.strip() if name else "N/A"
        price = product.find("span", class_="price")
        price = price.text.strip() if price else "N/A"
        writer.writerow([name, price]) # Correctly write both name and price. If you only want name, then use writer.writerow([name])