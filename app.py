# dependencies
from config import database, connect_string
# relational database class with our data retrieval functions
from project import Asylum_Seekers
from flask import Flask, jsonify, render_template
#################################################
# Database Setup
#################################################   
data = Asylum_Seekers()
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"<h4>Available Routes:</h4>"       
        f'<a href="/api/demographics">Demographics</a><br/>' 
        f'<a href="/api/timeseries">Time Series</a><br/>'  
        f'<a href="/"><h4>Back</h4></a><br/>' 
    )       

# @app.route("/api/asylumseekers")
# def asy():
#     return jsonify(data.asy_seekers_info())

@app.route("/api/demographics")
def demo():
    return jsonify(data.demographics())

@app.route("/api/timeseries")
def time():
    return jsonify(data.time_series_info())

if __name__ == '__main__':
    app.run(debug=True)