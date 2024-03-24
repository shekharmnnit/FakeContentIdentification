# services/scraper.py
import requests
from bs4 import BeautifulSoup

class Scraper:
    @staticmethod
    def scrape_article_content(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        return text