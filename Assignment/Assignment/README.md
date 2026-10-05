# Data Collection and Processing Using JSON, APIs and Web Scraping

Course: Python for Data Engineering — a small ETL pipeline.

## Structure
| File | Purpose |
|------|---------|
| api_data.py | Part A – fetch users from JSONPlaceholder, save `users.json` |
| web_scraping.py | Part B – scrape books.toscrape.com, save `books.json` |
| json_processing.py | Part C – load JSON, filters, save `report.json` |
| analysis.py | Part D – user & book analysis summary |
| main.py | Bonus – menu-driven runner |

## Setup & Run
```bash
pip install -r requirements.txt
python api_data.py
python web_scraping.py
python json_processing.py
python analysis.py
# or everything via menu:
python main.py
```

## Notes
- Ratings are stored both as words (`rating`) and numbers (`rating_value`).
- Prices are stored as text (`price`, e.g. £20.99) and float (`price_value`).
- Number of books scraped is configurable via `BOOKS_TO_SCRAPE` (default 40, min 20).

## Screenshots
Add output screenshots of each script here (`screenshots/` folder).
