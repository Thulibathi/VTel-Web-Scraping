import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://v-tel.co.za/product-category/ssd/"
url_ = "https://v-tel.co.za/product-category/ssd/page/2/"




# Send a GET request to the webpage
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/90.0.4430.93"}  # Mimic a browser
response = requests.get(url, headers=headers)
response_ = requests.get(url_, headers=headers)

# Check if the request was successful
if response.status_code != 200 and response_.status_code!=200:

    print(f"Failed to retrieve page: {response.status_code}")
    print(f"Failed to retrieve page: {response_.status_code}")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")
soup_ = BeautifulSoup(response_.text, "html.parser")

# Find product containers (adjust based on actual HTML structure)
products = soup.find_all("div", class_="product")  # Example class, update this
products_ = soup_.find_all("div", class_="product")  # Example class, update this

# Loop through products and extract details
#First page
for product in products:
    # Extract product name (update selector based on inspection)
    name = product.find("h3", class_="auxshp-title-heading")  # Example
    name = name.text.strip() if name else "N/A"

    # Extract price (update selector based on inspection)
    price = product.find("span", class_="price")  # Example
    price = price.text.strip() if price else "N/A"

    # Print or store the data
    print(f"Product: {name}, Price: {price}")

#Second page
for product_ in products_:
    # Extract product name (update selector based on inspection)
    name = product_.find("h3", class_="auxshp-title-heading")  # Example
    name = name.text.strip() if name else "N/A"

    # Extract price (update selector based on inspection)
    price = product_.find("span", class_="price")  # Example
    price = price.text.strip() if price else "N/A"

    # Print or store the data
    print(f"Product: {name}, Price: {price}")
print(f"Number of records retrieved: {len(products+products_)}")

# Optional: Save to a file (e.g., CSV)
import csv
with open("ssd.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price"])  # Header
    for product in products:
        name = product.find("h3", class_="auxshp-title-heading")
        name = name.text.strip() if name else "N/A"
        price = product.find("span", class_="price")
        price = price.text.strip() if price else "N/A"
        writer.writerow([name, price])
    for products_ in products_:
        name_ = product_.find("h3", class_="auxshp-title-heading")
        name_ = name_.text.strip() if name_ else "N/A"
        price_ = product_.find("span", class_="price")
        price_ = price_.text.strip() if price_ else "N/A"
        writer.writerow([name_, price_])