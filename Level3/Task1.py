import requests
from bs4 import BeautifulSoup
def scrape_books():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    print("Book Titles and Prices:")
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        print(f"{title} → {price}")
scrape_books()