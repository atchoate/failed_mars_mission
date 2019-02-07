from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    executable_path = {"executable_path": "/Users/atchoate/Downloads/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data = {}

    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    article = soup.find("div", class_="list_text")
    title = article.find("div", class_='content_title').text
    paragraph = article.find("div", class_='article_teaser_body').text

    mars_data["title"] = title
    mars_data["paragraph"] = paragraph




    browser.quit()
    return mars_data

