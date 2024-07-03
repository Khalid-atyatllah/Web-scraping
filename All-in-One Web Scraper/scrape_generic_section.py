from bs4 import BeautifulSoup
import pandas as pd

def scrape_generic_section(self, generic_url, pages=1):
    session = self.get_cookies()
    data = []
    
    for page in range(1, pages + 1):
        response = session.get(f"{generic_url}?page={page}")
        soup = BeautifulSoup(response.content, 'html.parser')

        # Modify the following lines based on the structure of the target website
        items = soup.find_all('div', {'class': 'generic-item'})
        for item in items:
            title = item.find('h2').text.strip() if item.find('h2') else 'No title'
            description = item.find('p', {'class': 'description'}).text.strip() if item.find('p', {'class': 'description'}) else 'No description'
            date = item.find('span', {'class': 'date'}).text.strip() if item.find('span', {'class': 'date'}) else 'No date'
            data.append({
                'Title': title,
                'Description': description,
                'Date': date
            })

    df = pd.DataFrame(data)
    return df
