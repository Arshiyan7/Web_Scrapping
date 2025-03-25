import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the website's HTML
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# Step 2: Extract book details
books = soup.find_all("article", class_="product_pod")  # Finding all books

book_data = []  # List to store book details

for book in books:
    title = book.h3.a["title"]  # Extracting book title
    price = book.find("p", class_="price_color").text  # Extracting price
    availability = book.find("p", class_="instock availability").text.strip()  # Extracting availability

    book_data.append([title, price, availability])  # Store in list

# Step 3: Save data to Excel
df = pd.DataFrame(book_data, columns=["Title", "Price", "Availability"])  # Convert to DataFrame
filename = "books_data.xlsx"
df.to_excel(filename, index=False, engine="openpyxl")  # Save as Excel

print(f"✅ Data scraped and saved to {filename} successfully!")
