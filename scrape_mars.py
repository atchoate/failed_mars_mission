from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

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
    title = soup.find("div", class_='content_title').text
    paragraph = soup.find("div", class_='article_teaser_body').text

    #paragraph = paragraph.text

    mars_data["title"] = title
    mars_data["paragraph"] = paragraph

    # print(mars_data)

    img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(img_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    image = soup.find("img", class_="thumb")["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + image

    # print(featured_image_url)

    mars_data["img_src"] = featured_image_url

    mf_url = "https://space-facts.com/mars/"
    browser.visit(mf_url)
    mars_table = pd.read_html(mf_url)
    mars_table = pd.DataFrame(mars_table[0])
    mars_facts = mars_table.to_html(header=False, index=False)

    mars_data["table"] = mars_facts


    hemis_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemis_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    mars_hemis = []

    stuff = soup.find("div", class_ = "result-list")
    hemispheres = stuff.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link
        browser.visit(image_link)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        mars_hemis.append({"img_url": image_url, "title": title})

        mars_data["X1"] = mars_hemis
        

    print(mars_data)


    browser.quit()
    return mars_data

