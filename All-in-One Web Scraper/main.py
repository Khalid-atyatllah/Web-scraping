from scraper import ChampionshipScraper

def main():
    login_url = 'https://example.com/login'
    blog_url = 'https://example.com/blog'
    ecommerce_url = 'https://example.com/products'
    reviews_url = 'https://example.com/reviews'
    generic_url = 'https://example.com/section'
    username = 'your_username'
    password = 'your_password'
    
    scraper = ChampionshipScraper(login_url, username, password)
    
    scraper.login()

    # Scrape blog articles
    blog_df = scraper.scrape_blog_articles(blog_url, pages=5)
    scraper.save_to_csv(blog_df, 'blog_articles.csv')
    print(f"Scraped blog articles data saved to blog_articles.csv")

    # Scrape e-commerce products
    ecommerce_df = scraper.scrape_ecommerce_products(ecommerce_url, pages=5)
    scraper.save_to_csv(ecommerce_df, 'ecommerce_products.csv')
    print(f"Scraped e-commerce products data saved to ecommerce_products.csv")

    # Scrape reviews
    reviews_df = scraper.scrape_reviews(reviews_url, pages=5)
    scraper.save_to_csv(reviews_df, 'reviews.csv')
    print(f"Scraped reviews data saved to reviews.csv")

    # Scrape generic section
    generic_df = scraper.scrape_generic_section(generic_url, pages=5)
    scraper.save_to_csv(generic_df, 'generic_section.csv')
    print(f"Scraped generic section data saved to generic_section.csv")

    scraper.close()

if __name__ == "__main__":
    main()
