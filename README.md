# The Locations of the World Cheese Award Super Gold Winners
## Project Demo
* Currently <a href="https://worlds-best-cheese.herokuapp.com/">hosted on Heroku</a>.

## How to use
* Simply choose the year you want displayed and click 'submit'.

## Background
* The World Cheese Awards is an annual event where the world's best cheeses are judged on their rind, body, color, texture and taste. Judges decide which cheeses recieve super gold, gold, silver and bronze awards. Super gold is rarest award and the highest achievement a cheesemaker can recieve at the World Cheese Awards. For more information about the event and judging process <a href="https://gff.co.uk/awards/world-cheese-awards/">visit their webpage</a>.
* The data displayed in this project is the name, company, company website and location of the super gold award winners from 2016 to 2021 via Google Maps as well as a pie chart depicting the percentage of awards won by country via AnyChart.
* This project was primarily a learning exercise for me to utilize a MySQL database in a small fullstack application.

## Project Overview
* The project uses Flask as its web framework with Gunicorn as its Web Server Gateway Interface HTTP server (WSGI), MySQL for its database and Javascript for client-side processing (including asynchronous requests and populating the Google Map and AnyChart instances).

## Where did data come from?
* The database was populated using a web scraper on the World Cheese Award webpage/historical archives which included the company name, product (cheese) name and website. Location data (address, latitude and longitude) was added to the database using a script that utilized <a href="https://developers.google.com/maps/documentation/geocoding/overview">Google's Geocoding API</a> where the company name was the input. 

## What is in this repository
* backend.py
    * Handles requests by uri, pulls requested data from the database, formats the data appropriately for our frontend (Javascript) to use in Google Maps and AnyChart and returns the data for our frontend.

* dbConnector.py
   * Connects to our database using a credentials file or environment variables on a server.

* templates/index.html
    * Main page and embedded frontend Javascript code which is used to make asynchronous requests to our backend (what year we want displayed) and use the requested data to update our Google Maps and AnyChart instances.

* static/css/style.css
    * CSS to make our single page responsive and look nice.

### Note
* I intentionally didn't make the web crawler or Geocoder script public. Email me if you want to know more about this.
