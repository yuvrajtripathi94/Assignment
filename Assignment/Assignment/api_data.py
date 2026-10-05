"""Part A - API Data Collection (JSONPlaceholder users)."""
import json
import requests

API_URL = "https://jsonplaceholder.typicode.com/users"
USERS_FILE = "users.json"


def fetch_users():
    """A1: Fetch all user records from the API."""
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()


def display_users(users):
    """A1: Display Name, Username, Email, Company Name."""
    print(f"{'Name':<25}{'Username':<18}{'Email':<30}Company")
    print("-" * 90)
    for u in users:
        print(f"{u['name']:<25}{u['username']:<18}{u['email']:<30}{u['company']['name']}")


def count_users(users):
    """A2: Total number of users."""
    return len(users)


def get_company_names(users):
    """A3: Extract all company names."""
    return [u["company"]["name"] for u in users]


def process_users(users):
    """A4: Dictionary {name, email, company} for every user."""
    return [
        {"name": u["name"], "email": u["email"], "company": u["company"]["name"]}
        for u in users
    ]


def save_json(data, filename):
    """A5: Save data to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def main():
    users = fetch_users()
    display_users(users)
    print("\nTotal users:", count_users(users))
    print("Company names:", get_company_names(users))
    processed = process_users(users)
    save_json(processed, USERS_FILE)
    print(f"\nSaved {len(processed)} users to {USERS_FILE}")


if __name__ == "__main__":
    main()
