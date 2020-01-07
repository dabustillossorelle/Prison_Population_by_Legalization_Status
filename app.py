import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify
)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/Legalization_data.sqlite"

db = SQLAlchemy(app)

class Prispopulation(db.Model):
    __tablename__ = 'prispopulation'

    Legalization_Status = db.Column(db.String, primary_key=True)
    Population_in_Private_Prison = db.Column(db.Float)
    Population_in_Public_Prison = db.Column(db.Float)
    Total_Population_in_Prison = db.Column(db.Float)
    
    def __repr__(self):
        return '<Legalization_data %r>' % (self.name)

class Opioid_data(db.Model):
    __tablename__ = 'opioid_data'

    legalization_status = db.Column(db.String, primary_key=True)
    opioid_prescription_100_people = db.Column(db.Float)
    opioid_od_deaths = db.Column(db.Float)

    def __repr__(self):
        return '<Legalization_data %r>' % (self.name)

@app.before_first_request
def setup():
    db.create_all() 

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

@app.route("/population_in_private_prison")
def population_in_private_prison():

    # Query for the emoji data using pandas
    results = db.session.query(Prispopulation.Legalization_Status, Prispopulation.Population_in_Private_Prison).all()

    # Create lists from the query results
    Legalization_Status = [result[0] for result in results]
    Population_in_private_prison = [result[1] for result in results]
   
    # Format the data for Plotly
    trace = {
        "x": Legalization_Status,
        "y": Population_in_private_prison,
        "type": "bar"
    }
    return jsonify(trace)

@app.route("/population_in_public_prison")
def population_in_public_prison():
    """Return population in public prison"""

    # Query for the public prison data
    results = db.session.query(Prispopulation.Legalization_Status, Prispopulation.Population_in_Public_Prison).all()

     # Create lists from the query results
    Legalization_Status = [result[0] for result in results]
    Population_in_public_prison = [result[1] for result in results]
    
    # Generate the plot trace
    trace = {
        "x": Legalization_Status,
        "y": Population_in_public_prison,
        "type": "bar"
    }
    return jsonify(trace)

@app.route("/total_population_in_prison")
def total_population_in_prison():
    """Return population in public prison"""

    # Query for the public prison data
    results = db.session.query(Prispopulation.Legalization_Status, Prispopulation.Total_Population_in_Prison).all()

     # Create lists from the query results
    Legalization_Status = [result[0] for result in results]
    Total_population_in_prison = [result[1] for result in results]
    
    # Generate the plot trace
    trace = {
        "x": Legalization_Status,
        "y": Total_population_in_prison,
        "type": "bar"
    }
    
    return jsonify(trace)

@app.route("/opiod_prescription_100_people")
def opiod_prescription_100_people():
    """Return number of opioid prescription per 100 people"""

    # Query for the public prison data
    results = db.session.query(Opioid_data.legalization_status, Opioid_data.opioid_prescription_100_people).all()

     # Create lists from the query results
    legalization_status = [result[0] for result in results]
    opioid_prescription_100_people = [result[1] for result in results]
    
    # Generate the plot trace
    trace = {
        "x": legalization_status,
        "y": opioid_prescription_100_people,
        "type": "bar"
    }
    
    return jsonify(trace)

@app.route("/opioid_od_deaths")
def opioid_od_deaths():
    """Return number of deaths from opioid od"""

    # Query for the public prison data
    results = db.session.query(Opioid_data.legalization_status, Opioid_data.opioid_od_deaths).all()

     # Create lists from the query results
    legalization_status = [result[0] for result in results]
    opioid_od_deaths = [result[1] for result in results]
    
    # Generate the plot trace
    trace = {
        "x": legalization_status,
        "y": opioid_od_deaths,
        "type": "bar"
    }
    
    return jsonify(trace)

if __name__ == '__main__':
    app.run(debug=True)