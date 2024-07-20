from news_crawler import NewsCrawler

if __name__ == "__main__":
    url = 'YOUR_TARGET_NEWS_URL'
    crawler = NewsCrawler(url)
    crawler.start()
