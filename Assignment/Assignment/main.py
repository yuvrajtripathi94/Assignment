"""Bonus - Menu-driven program. Run: python main.py"""
import api_data
import web_scraping
import json_processing
import analysis


def generate_json_files():
    """Option 3: (re)build users.json, books.json and report.json."""
    api_data.save_json(api_data.process_users(api_data.fetch_users()), api_data.USERS_FILE)
    web_scraping.save_books(web_scraping.scrape_books())
    json_processing.main()


MENU = """
===== DATA PIPELINE MENU =====
1. Fetch API Data
2. Scrape Book Data
3. Generate JSON Files
4. Analyze Data
5. Exit
"""

ACTIONS = {
    "1": api_data.main,
    "2": web_scraping.main,
    "3": generate_json_files,
    "4": analysis.main,
}


def main():
    while True:
        print(MENU)
        choice = input("Enter choice (1-5): ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = ACTIONS.get(choice)
        if not action:
            print("Invalid choice, try again.")
            continue
        try:
            action()
        except FileNotFoundError:
            print("JSON file missing - run options 1 and 2 first.")
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
