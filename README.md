# 📊 Stock Data Scraper

A Python script for crawling stock market data from a website and saving it as a CSV file.

## 🚀 Features

- Uses `requests` to send HTTP requests
- Parses HTML using `BeautifulSoup`
- Automatically writes data to `stock_data.csv` with fields such as:
  - Stock symbol
  - Last updated time
  - Opening, closing, ceiling, floor, high, and low prices
  - Volume, unit, foreign trading volume/value, and remaining room

## 🛠️ Technologies Used

- Python 3.x
- requests
- BeautifulSoup4
- csv (built-in Python module)

## 📁 Project Structure

```text
stock_scraper/
├── stock_scraper.py      # Main script (or stock_scraper.ipynb if using Jupyter)
├── stock_data.csv        # Output file after scraping
└── README.md             # Project documentation
```


## ▶️ How to Run

1. Install required libraries (if not installed yet):

```bash
pip install requests beautifulsoup4
```

2. Run the Jupyter Notebook:
```bash
python stock_scraper.ipynb
```

3. The result will be saved in vcb_data.csv.
