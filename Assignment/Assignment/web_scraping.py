"""Part B - Web Scraping (books.toscrape.com)."""
import json
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
BOOKS_FILE = "books.json"
BOOKS_TO_SCRAPE = 40  # at least 20 required; 20 books per page

# B3: rating word -> number
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def parse_books(html):
    """B1/B2: Parse one page into a list of dicts (title, price, rating)."""
    soup = BeautifulSoup(html, "html.parser")
    books = []
    for article in soup.select("article.product_pod"):
        title = article.h3.a["title"]
        price = article.select_one("p.price_color").text.strip()
        rating = article.select_one("p.star-rating")["class"][1]
        books.append({
            "title": title,
            "price": price,                                  # e.g. "£20.99"
            "rating": rating,                                # e.g. "Three"
            "price_value": float(price.replace("£", "")),    # numeric price
            "rating_value": RATING_MAP[rating],              # B3 numeric rating
        })
    return books


def scrape_books(limit=BOOKS_TO_SCRAPE):
    books, page = [], 1
    while len(books) < limit:
        resp = requests.get(BASE_URL.format(page), timeout=10)
        if resp.status_code != 200:
            break
        resp.encoding = "utf-8"  # makes the £ sign render correctly
        books.extend(parse_books(resp.text))
        page += 1
    return books[:limit]


def book_stats(books):
    """B4: most expensive, least expensive, average price."""
    most = max(books, key=lambda b: b["price_value"])
    least = min(books, key=lambda b: b["price_value"])
    avg = sum(b["price_value"] for b in books) / len(books)
    return most, least, avg


def save_books(books, filename=BOOKS_FILE):
    """B5: Save to books.json."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)


def main():
    books = scrape_books()
    print(f"Scraped {len(books)} books")
    most, least, avg = book_stats(books)
    print(f"Most expensive : {most['title']} ({most['price']})")
    print(f"Least expensive: {least['title']} ({least['price']})")
    print(f"Average price  : £{avg:.2f}")
    save_books(books)
    print(f"Saved to {BOOKS_FILE}")


if __name__ == "__main__":
    main()
