from seleniumbase import BaseCase
from seleniumbase import Driver
import pandas as pd
import json
import selenium
import time
import csv

from DrissionPage import ChromiumPage, ChromiumOptions
from seleniumbase.undetected import ChromeOptions

ad_links = []
ad_headers = []
ad_date = []
ad_numbers = []
locations = []
vehicle_years = []
vehicle_prices = []
vehicle_kilometers = []
vehicle_make = []
vehicle_fuel = []
vehicle_transmission = []
vehicle_status = []
vehicle_body_types = []
vehicle_horse_powers = []
vehicle_engine_volumes = []
vehicle_colors = []
vehicle_guarantees = []
vehicle_damage_registered = []
vehicle_nation = []
vehicle_wheel_drive = []
vehicle_listed_from = []
vehicle_exchangeable = []

json=[]
# class Scraper(BaseCase):
#     def test_get_product_names(self):
#         driver = Driver(uc=True, mobile=True, headless=False)
#         self.open("https://www.sahibinden.com/ilan/vasita-otomobil-ford-hatasiz-ford-mondeo-dizel-1207988058/detay")
#         time.sleep(30)
#         source = self.get_page_source()
#         print(source)
#         self.save_data_as(source,"source.html","/")
#
#
#
#
#
#
#         # ad_names = [ad.text for name in ad_names]
#         # print(names)
#         # links = [link.get_attribute("href") for link in link_elements]
#         # print(links)
#         # print(len(links))
#         #
#         # # Store the links in the DataFrame and save it to a CSV file
#         # for link in links:
#         #     link_df.loc[len(link_df)] = [link]

# Initialize ChromiumPage
p = ChromiumPage()
p.get("https://www.sahibinden.com/ilan/vasita-otomobil-ford-hatasiz-ford-mondeo-dizel-1207988058/detay")
json_data = p.ele('#gaPageViewTrackingJson').attr('data-json')

# JSON string parsing
import json
parsed_data = json.loads(json_data)

def extract_custom_vars(parsed_data):

    data_dict = {}
    for var in parsed_data['customVars']:
        data_dict[var['name']] = var['value']
    return data_dict


car_data = extract_custom_vars(parsed_data)


df = pd.DataFrame([car_data])


df.to_csv('car_data.csv', index=False, encoding='utf-8-sig')  # utf-8-sig Türkçe karakterler için


def save_to_csv_direct(parsed_data, filename):

    data_dict = extract_custom_vars(parsed_data)


    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)


        writer.writerow(data_dict.keys())


        writer.writerow(data_dict.values())


save_to_csv_direct(parsed_data, 'car_data_direct.csv')


def save_selected_fields_to_csv(parsed_data, filename):

    selected_fields = [
        'Marka', 'Seri', 'Model', 'Yıl', 'Yakıt', 'Vites', 'KM',
        'Kasa Tipi', 'Motor Gücü', 'Motor Hacmi', 'Renk', 'ilan_fiyat'
    ]


    data_dict = extract_custom_vars(parsed_data)
    selected_data = {field: data_dict.get(field, '') for field in selected_fields}


    df = pd.DataFrame([selected_data])
    df.to_csv(filename, index=False, encoding='utf-8-sig')


save_selected_fields_to_csv(parsed_data, 'car_data_selected.csv')