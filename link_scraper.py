# Tek sayfa işliyor şuanlık demo
from seleniumbase import BaseCase
from seleniumbase import Driver
import pandas as pd

# Initialize DataFrame with a list, not a tuple, to define columns
link_df = pd.DataFrame(columns=["Links"])

class Scraper(BaseCase):
    def test_get_product_names(self):
        driver = Driver(uc=True, mobile=True, headless=False)
        self.open("https://www.sahibinden.com/otomobil?pagingOffset=20")
        link_elements = self.find_elements("a.classifiedTitle")
        links = [link.get_attribute("href") for link in link_elements]
        print(links)
        print(len(links))

        # Store the links in the DataFrame and save it to a CSV file
        for link in links:
            link_df.loc[len(link_df)] = [link]

        link_df.to_csv("links.csv", index=False)

