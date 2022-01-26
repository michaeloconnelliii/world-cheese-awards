import flask
import json
import mysql.connector
import dbConnector
from mysql.connector import Error
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) 

validYears = [2016, 2017, 2018, 2019, 2021]

@app.route("/")
def index(): 
    return flask.render_template('index.html')

@app.route("/allCheeseData", methods=['GET'])
def allCheeseData():
    # Get requested year and validate it
    try:
        requestYear = int(request.args.get('year'))
    except:
        return flask.jsonify(result=None)
    
    if requestYear == None or requestYear not in validYears:
        return flask.jsonify(result=None)
    
    requestYear = str(requestYear)

    # Get data for Google Maps
    mySQLQuery = "SELECT * FROM WorldCheeseWinners" + requestYear
    queryResult = dbConnector.connectAndExecute(mySQLQuery)
                
    mapsResult = {}
    
    for row in queryResult:
        mapsResult[row[0]] = { 'company': row[1], 'website': row[2], 'address': row[3], 
                                'country': row[4], 'lat': float(row[5]), 'long': float(row[6]) }
            
    mapsResult = json.dumps(mapsResult, indent = 4, ensure_ascii=False)

    # Get data for AnyChart
    mySQLQuery = "SELECT country, COUNT(country) AS totalAwards FROM WorldCheeseWinners" + requestYear + " GROUP BY country ORDER BY totalAwards DESC"
    queryResult = dbConnector.connectAndExecute(mySQLQuery)
    
    chartResult = []
    for row in queryResult:
        chartResult.append( {'x':row[0], 'value': row[1]} )

    return flask.jsonify(mapsResult=mapsResult, chartResult=chartResult)


if __name__ == '__main__': 
   app.run(threaded=True, port=5000, debug=True) # application will start listening for web request on port 5000