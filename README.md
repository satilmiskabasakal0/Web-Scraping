# Car Data Scraper

This project is a web scraping application designed to extract car listing data from the **Sahibinden** website. It uses `ChromiumPage` from the `DrissionPage` library and stores the extracted data in CSV files for further analysis.

## Features

1. **Extract Custom Data**: Extracts specific fields from car listing pages, such as price, brand, model, and other details.
2. **Pagination Support**: Scrapes multiple pages of car listings automatically.
3. **Save to CSV**: Saves the extracted data in multiple formats:
   - Full dataset.
   - Selected fields.
4. **Link Extraction**: Extracts URLs of individual car listings for detailed scraping.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver for Selenium

### Required Libraries
Install the dependencies using `pip`:

```bash
pip install -r requirements.txt
