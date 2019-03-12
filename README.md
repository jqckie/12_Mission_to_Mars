# Webscrape Mission to Mars Flask App

## Instructions
* Run [app.py](/Mission to Mars/app.py) to launch the Flask app and display scraped data onto an HTML page.

## Background
Using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter to build a web application that scrapes various websites for data and displays the information in a single HTML page. 

## Details

* Creating a Jupyter Notebook to complete the following scraping and analysis tasks:

    * Scraping the [NASA Mars News Site](https://mars.nasa.gov/news/) and collecting the latest News Title and Paragraph Text.
    
    * Visiting the url for .

    * Using splinter to navigate JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) and find  the image url for the current Featured Mars Image.

    * Scraping the latest Mars weather tweet from [Mars Weather twitter account](https://twitter.com/marswxreport?lang=en). 

    * Using Pandas to scrape the [Mars Facts webpage](http://space-facts.com/mars/) table containing facts about the planet including Diameter, Mass, etc.

   * Using Pandas to convert the data to a HTML table string.

   * Obtaining high resolution images for each of Mar's hemispheres from the [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars).

 * Using MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Creating a route called `/scrape` that imports `scrape_mars.py` script and call a `scrape` function.

 * Storing the return value in Mongo as a Python dictionary.

* Creatings a root route `/` that queries a Mongo database and passes the mars data into an HTML template to display the data.

* Creating a template HTML file that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 
