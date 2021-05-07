# dependencies
from config import database, connect_string
# relational database class with our data retrieval functions
from project import AsylumSeekers 
from flask import Flask, jsonify, render_template
#################################################
# Database Setup
#################################################   
data = AsylumSeekers()
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    #users = data.get_subject_ids()
    #return render_template("index.html", user_ids=users)

@app.route("/api/asylumseekers")
def asy():
    return jsonify(data.asy_seekers_info())

@app.route("/api/demographics")
def demo():
    return jsonify(data.demographics())

@app.route("/api/timeseries")
def time():
    return jsonify(data.time_series_info())

if __name__ == '__main__':
    app.run(debug=True)