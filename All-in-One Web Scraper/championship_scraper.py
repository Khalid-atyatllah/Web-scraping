from selenium import webdriver
import scraper.login
import scraper.get_cookies
import scraper.scrape_blog_articles
import scraper.scrape_ecommerce_products
import scraper.scrape_reviews
import scraper.scrape_generic_section
import scraper.close
import scraper.save_to_csv

class ChampionshipScraper:
    def __init__(self, login_url, username, password):
        self.login_url = login_url
        self.username = username
        self.password = password
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
        self.driver = webdriver.Chrome(options=self.options)  # Change this to your Chrome driver path

    def login(self):
        scraper.login.login(self)

    def get_cookies(self):
        return scraper.get_cookies.get_cookies(self)

    def scrape_blog_articles(self, blog_url, pages=1):
        return scraper.scrape_blog_articles.scrape_blog_articles(self, blog_url, pages)

    def scrape_ecommerce_products(self, ecommerce_url, pages=1):
        return scraper.scrape_ecommerce_products.scrape_ecommerce_products(self, ecommerce_url, pages)

    def scrape_reviews(self, reviews_url, pages=1):
        return scraper.scrape_reviews.scrape_reviews(self, reviews_url, pages)

    def scrape_generic_section(self, generic_url, pages=1):
        return scraper.scrape_generic_section.scrape_generic_section(self, generic_url, pages)

    def close(self):
        scraper.close.close(self)

    def save_to_csv(self, df, filename):
        scraper.save_to_csv.save_to_csv(df, filename)
