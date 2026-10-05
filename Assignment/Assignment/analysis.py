"""Part D - Data Analysis."""
import json
from collections import Counter

USERS_FILE = "users.json"
BOOKS_FILE = "books.json"


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    users = load_json(USERS_FILE)
    books = load_json(BOOKS_FILE)

    # ---- User Analysis ----
    companies = sorted({u["company"] for u in users})
    print("=" * 50)
    print("USER ANALYSIS")
    print("=" * 50)
    print("Total users       :", len(users))
    print("Unique companies  :", len(companies))
    print("Top 5 (alphabetical):")
    for i, c in enumerate(companies[:5], 1):
        print(f"  {i}. {c}")

    # ---- Book Analysis ----
    avg = sum(b["price_value"] for b in books) / len(books)
    max_rating = max(b["rating_value"] for b in books)
    best = [b["title"] for b in books if b["rating_value"] == max_rating]
    dist = Counter(b["rating"] for b in books)
    order = ["One", "Two", "Three", "Four", "Five"]

    print("\n" + "=" * 50)
    print("BOOK ANALYSIS")
    print("=" * 50)
    print(f"Average price : £{avg:.2f}")
    print(f"Highest rated books ({max_rating} stars): {len(best)}")
    for t in best:
        print(" -", t)
    print("Books per rating category:")
    for r in order:
        print(f"  {r:<6}: {dist.get(r, 0)}")


if __name__ == "__main__":
    main()
