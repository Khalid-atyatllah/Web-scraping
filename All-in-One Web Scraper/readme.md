# All-in-One Scraper

The All-in-One Scraper is a versatile web scraping tool designed to extract data from multiple sections of a website. Utilizing Selenium, Requests, BeautifulSoup, and Pandas, this project efficiently scrapes blog articles, e-commerce products, customer reviews, and generic sections, saving the extracted data into CSV files.

## Features

- **Automated Login**: Logs into websites requiring authentication.
- **Cookies Management**: Handles session cookies for authenticated requests.
- **Multi-Section Scraping**: Scrapes blog articles, e-commerce products, customer reviews, and generic sections.
- **Pagination Handling**: Navigates through multiple pages of each section.
- **Data Storage**: Saves scraped data into CSV files for easy analysis.


### __init__.py

Initializes the scraper module.

### championship_scraper.py

Main class containing the logic for logging in, managing cookies, scraping different sections, and saving data.

### login.py

Handles the login functionality.

### get_cookies.py

Manages session cookies for authenticated requests.

### scrape_blog_articles.py

Scrapes blog articles from the specified URL.

### scrape_ecommerce_products.py

Scrapes e-commerce product data from the specified URL.

### scrape_reviews.py

Scrapes customer reviews from the specified URL.

### scrape_generic_section.py

Scrapes data from a generic section of the specified URL.

### close.py

Closes the Selenium WebDriver.

### save_to_csv.py

Saves the scraped data into CSV files.

### main.py

Main script that initializes the scraper, logs in, scrapes data from different sections, and saves the data to CSV files.



1. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
