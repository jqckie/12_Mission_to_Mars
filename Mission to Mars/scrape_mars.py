# Dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd
from splinter import Browser
import cssutils
import pymongo
   
def init_browser():
        executable_path = {"executable_path": 'chromedriver.exe'}
        return Browser("chrome", **executable_path, headless=False)

def scrape():
        mars_scrape = {}
        output = latest_mars_news()
        mars_scrape["news"] = output[0]
        mars_scrape["paragraph"] = output[1]
        mars_scrape["image"] = featured_mars_image()
        mars_scrape["weather"] = current_weather_on_mars()
        mars_scrape["facts"] = mars_facts()
        mars_scrape["hemispheres"] = mars_hemispheres()
        return mars_scrape
       
# Latest Mars News
def latest_mars_news():
        browser = init_browser()
        url = "https://mars.nasa.gov/news/"
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("div", class_='list_text')
        news_title = article.find("div", class_="content_title").text
        news_p = article.find("div", class_ ="article_teaser_body").text
        output = [news_title, news_p]
        return output

# Featured Mars Image
def featured_mars_image():
        url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')   
        div_style = soup.find('article', class_="carousel_item")['style']
        style = cssutils.parseStyle(div_style)
        partial_image_url = style['background-image']
        partial_image_url = partial_image_url.replace('url(', '').replace(')', '') 
        featured_image_url = 'https://www.jpl.nasa.gov' + partial_image_url
        return featured_image_url

# Current Weather on Mars
def current_weather_on_mars():
        url = 'https://twitter.com/marswxreport?lang=en'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('p', class_='tweet-text')
        mars_weather = results[0].text    
        return mars_weather

# Mars Facts
def mars_facts():
        url = 'http://space-facts.com/mars/'
        tables = pd.read_html(url)
        df = tables[0]
        df.columns = ['description','value']
        df.set_index('description', inplace=True)
        mars_facts_table = df.to_html()
        mars_facts_table = mars_facts_table.replace('\n', '')
        return mars_facts_table

# Mars Hemispheres
def mars_hemispheres():
        browser = init_browser()
        url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)"
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        hemisphere_image_urls = []
        results = soup.find("div", class_ = "result-list" )
        hemispheres = results.find_all("div", class_="item")
        for hemisphere in hemispheres:
                title = hemisphere.find("h3").text
                title = title.replace(" Enhanced", "")
                partial_imagepage_url = hemisphere.find("a")["href"]
                imagepage_url = "https://astrogeology.usgs.gov/" + partial_imagepage_url   
                browser.visit(imagepage_url)
                html = browser.html
                soup=BeautifulSoup(html, "html.parser")
                download_links = soup.find("div", class_="downloads")
                image_url = download_links.find("a")["href"]
                hemisphere_image_urls.append({"title": title, "img_url": image_url})
        return hemisphere_image_urls
 
 