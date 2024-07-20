from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import pandas as pd

class NewsCrawler:
    def __init__(self, url):
        chrome_options = Options()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.url = url
        self.data = []

    def start(self):
        self.driver.get(self.url)
        self.scrape_articles()
        self.driver.quit()
        self.save_to_excel()

    def scrape_articles(self):
        try:
            go_inside_elements = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//td[@class='sort-td']/a"))
            )

            main_window = self.driver.current_window_handle

            for element in go_inside_elements:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//td[@class='sort-td']/a")))

                for attempt in range(3):
                    try:
                        element.click()
                        break
                    except ElementClickInterceptedException:
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

                self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
                self.extract_data()

                self.driver.back()
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//td[@class='sort-td']/a")))
                go_inside_elements = self.driver.find_elements(By.XPATH, "//td[@class='sort-td']/a")

        except Exception as e:
            print(f"An error occurred: {e}")

    def extract_data(self):
        try:
            article_title_element = self.driver.find_element(By.XPATH, "//td[text()='Article Title']/following-sibling::td/a")
            article_title = article_title_element.text
            article_link = article_title_element.get_attribute('href')
        except NoSuchElementException:
            article_title = 'N/A'
            article_link = 'N/A'

        try:
            authors = self.driver.find_elements(By.XPATH, "//td[text()='Author']/following-sibling::td/a")
            author_names = [author.text for author in authors]
        except NoSuchElementException:
            author_names = []

        try:
            publication_date = self.driver.find_element(By.XPATH, "//td[text()='Publication Date']/following-sibling::td").text
        except NoSuchElementException:
            publication_date = 'N/A'

        try:
            tags_elements = self.driver.find_elements(By.XPATH, "//td[text()='Tags']/following-sibling::td/a")
            tags_text = [tag.text for tag in tags_elements]
        except NoSuchElementException:
            tags_text = []

        self.data.append({
            'URL': self.driver.current_url,
            'Article Title': article_title,
            'Article Link': article_link,
            'Authors': ', '.join(author_names),
            'Publication Date': publication_date,
            'Tags': ', '.join(tags_text)
        })

    def save_to_excel(self):
        df = pd.DataFrame(self.data)
        df.to_excel('extracted_data.xlsx', index=False)
main.py
