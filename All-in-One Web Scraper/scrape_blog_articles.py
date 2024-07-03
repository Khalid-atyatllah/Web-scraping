from bs4 import BeautifulSoup
import pandas as pd

def scrape_blog_articles(self, blog_url, pages=1):
    session = self.get_cookies()
    articles = []
    
    for page in range(1, pages + 1):
        response = session.get(f"{blog_url}?page={page}")
        soup = BeautifulSoup(response.content, 'html.parser')

        # Modify the following lines based on the structure of the target website
        articles_on_page = soup.find_all('div', {'class': 'blog-article'})
        for article in articles_on_page:
            title = article.find('h2').text.strip() if article.find('h2') else 'No title'
            author = article.find('span', {'class': 'author'}).text.strip() if article.find('span', {'class': 'author'}) else 'No author'
            date = article.find('span', {'class': 'date'}).text.strip() if article.find('span', {'class': 'date'}) else 'No date'
            content = article.find('div', {'class': 'content'}).text.strip() if article.find('div', {'class': 'content'}) else 'No content'
            articles.append({'Title': title, 'Author': author, 'Date': date, 'Content': content})

    df = pd.DataFrame(articles)
    return df
