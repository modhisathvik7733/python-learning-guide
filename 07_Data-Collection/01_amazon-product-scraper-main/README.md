# Amazon Product Web Scraper

A Python web scraper that extracts product details from Amazon search results including title, price, rating, reviews, and availability status.

## Disclaimer

This project is for educational purposes only. Web scraping Amazon may violate their Terms of Service. Use responsibly.

## Prerequisites

- Python 3.7+
- Anaconda

## Setup Instructions

### 1. Install Anaconda

1. Download Anaconda from https://www.anaconda.com/download
2. Install the appropriate version for your operating system
3. Verify installation: `conda --version`

### 2. Create Environment

Open Anaconda Prompt/Terminal and run:

```bash
conda create -n amazon_scraper python=3.9
conda activate amazon_scraper
```

### 3. Install Required Packages

```bash
conda install pandas numpy requests beautifulsoup4 jupyter
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Create a new Python 3 notebook.

## Code

Copy this code into your Jupyter notebook:

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# Function to extract Product Title
def get_title(soup):
    try:
        title = soup.find("span", attrs={"id":'productTitle'})
        title_value = title.text
        title_string = title_value.strip()
    except AttributeError:
        title_string = ""
    return title_string

# Function to extract Product Price
def get_price(soup):
    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
    except AttributeError:
        try:
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()
        except:
            price = ""
    return price

# Function to extract Product Rating
def get_rating(soup):
    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""
    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
    except AttributeError:
        review_count = ""
    return review_count

# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()
    except AttributeError:
        available = "Not Available"
    return available

# Main scraper
if __name__ == '__main__':
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }
    
    URL = "https://www.amazon.com/s?k=playstation+4&ref=nb_sb_noss_2"
    
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})
    links_list = []
    
    for link in links:
        links_list.append(link.get('href'))
    
    d = {"title":[], "price":[], "rating":[], "reviews":[], "availability":[]}
    
    for link in links_list:
        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")
        
        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['rating'].append(get_rating(new_soup))
        d['reviews'].append(get_review_count(new_soup))
        d['availability'].append(get_availability(new_soup))
    
    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df['title'] = amazon_df['title'].replace('', np.nan)
    amazon_df = amazon_df.dropna(subset=['title'])
    amazon_df.to_csv("amazon_data.csv", header=True, index=False)
    
    print(f"Scraped {len(amazon_df)} products. Data saved to amazon_data.csv")
```

## Usage

1. Run the code in Jupyter notebook
2. The script will scrape Amazon search results
3. Data will be saved to `amazon_data.csv`
4. Change the search term in the URL to scrape different products

## Output

CSV file with columns:
- title
- price
- rating
- reviews
- availability

## Notes

- Amazon's HTML structure may change requiring code updates
- Be respectful with request frequency
- Some products may have missing data