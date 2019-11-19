
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

# engine = create_engine('postgresql://postgres:,rc!7YVI@localhost/ISS')
# connection = engine.connect()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:,rc!7YVI@localhost/ISS'
# db = SQLAlchemy(app)

# Base = automap_base()
# Base.prepare(engine, reflect=True)
# Base.classes.keys()

# # Save references to each table
# ISS_Locations = Base.classes.locations

@app.route("/homepage")
def homepage():
    """Return the homepage."""
    return render_template("homepage.html")

@app.route("/ISSlive")
def ISSlive():
    """Return the homepage."""
    return render_template("ISSlive.html")

@app.route("/predictionmap")
def predictionmap():
    """Return the homepage."""
    return render_template("predictionmap.html")

@app.route("/gallery")
def gallery():
    """Return the homepage."""
    return render_template("gallery.html")

@app.route("/citiesdata")
def citiesdata():
    """Return the homepage."""
    return render_template("citiesdata.html")

# @app.route("/CityNames")
# def names():
#     """Return a list of City Names."""

    # Use Pandas to perform the sql query
    # stmt = db.session.query(ISS_Locations).statement
    # df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    # return jsonify(df.to_dict(orient='records'))


if __name__ == "__main__":
    app.run(debug=True)

