import pandas as pd
import json
import csv
from DrissionPage import ChromiumPage
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuration
BASE_URL = "https://www.sahibinden.com/otomobil"
PAGING_SIZE = 50
PAGE_LIMIT = 200
SLEEP_BETWEEN_PAGES = 2
SLEEP_BETWEEN_ADS = 2

def scrape_ad_links(page, offset):
    """Scrape links from a single page."""
    try:
        url = f"{BASE_URL}?pagingOffset={offset}&pagingSize={PAGING_SIZE}"
        page.get(url)
        time.sleep(SLEEP_BETWEEN_PAGES)  # Rate limiting
        
        hrefs = page.eles("@class:classifiedTitle")
        if not hrefs:
            logging.warning(f"No links found on page with offset {offset}")
            return []
            
        return [href.attr("href") for href in hrefs]
    except Exception as e:
        logging.error(f"Error scraping page {offset}: {e}")
        return []


def scrap_car_feature(link):
    p.get(link)
    # Check if the element exists and retrieve its attribute
    json_element = p.ele('#gaPageViewTrackingJson')
    if json_element is None:
        raise ValueError("The element with ID '#gaPageViewTrackingJson' was not found.")

    json_data = json_element.attr('data-json')

    if not json_data:
        raise ValueError("The 'data-json' attribute is missing or empty.")

    parsed_data = json.loads(json_data)
    return parsed_data


def extract_custom_vars(parsed_data):
    data_dict = {}
    for var in parsed_data['customVars']:
        data_dict[var['name']] = var['value']
    return data_dict


def save_selected_fields_to_csv(parsed_data, filename):
    selected_fields = [
        'İlan No', 'İlan Tarihi', 'loc2', 'loc3', 'loc4', 'Marka', 'Seri', 'Model', 
        'Yıl', 'Yakıt', 'Vites', 'KM', 'Kasa Tipi', 'Motor Gücü', 'Motor Hacmi', 
        'Renk', 'ilan_fiyat'
    ]

    try:
        data_dict = extract_custom_vars(parsed_data)
        selected_data = {field: data_dict.get(field, '') for field in selected_fields}

        with open(filename, 'a', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=selected_fields)
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(selected_data)
    except Exception as e:
        logging.error(f"Error saving data: {e}")


if __name__ == '__main__':
    output_file = 'car_data_direct.csv'
    page = ChromiumPage()
    all_links = []
    
    try:
        # First phase: Collect all links
        for offset in range(0, PAGE_LIMIT * PAGING_SIZE, PAGING_SIZE):
            logging.info(f"Scraping page with offset {offset}")
            page_links = scrape_ad_links(page, offset)
            all_links.extend(page_links)
            
        # Second phase: Scrape individual ads
        for link in all_links:
            try:
                logging.info(f"Scraping ad: {link}")
                all_features = scrap_car_feature(link)
                save_selected_fields_to_csv(all_features, output_file)
                time.sleep(SLEEP_BETWEEN_ADS)
            except Exception as e:
                logging.error(f"Error scraping link {link}: {e}")
                
    except KeyboardInterrupt:
        logging.info("Scraping interrupted by user")
    except Exception as e:
        logging.error(f"Fatal error: {e}")
    finally:
        page.quit()
