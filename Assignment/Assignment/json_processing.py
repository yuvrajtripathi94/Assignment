"""Part C - JSON Processing."""
import json

USERS_FILE = "users.json"
BOOKS_FILE = "books.json"
REPORT_FILE = "report.json"


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    users = load_json(USERS_FILE)
    books = load_json(BOOKS_FILE)

    # C1: total records
    print(f"Total users: {len(users)}")
    print(f"Total books: {len(books)}")

    # C2: books with rating > 4
    print("\nBooks with rating greater than 4:")
    top_books = [b["title"] for b in books if b["rating_value"] > 4]
    for t in top_books:
        print(" -", t)
    if not top_books:
        print(" (none)")

    # C3: users whose company contains 'Group'
    print("\nUsers in companies containing 'Group':")
    group_users = [u for u in users if "Group" in u["company"]]
    for u in group_users:
        print(f" - {u['name']} ({u['company']})")
    if not group_users:
        print(" (none)")

    # C4: combined report
    avg_price = round(sum(b["price_value"] for b in books) / len(books), 2)
    report = {
        "total_users": len(users),
        "total_books": len(books),
        "average_price": avg_price,
    }
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
    print(f"\nReport saved to {REPORT_FILE}: {report}")


if __name__ == "__main__":
    main()
