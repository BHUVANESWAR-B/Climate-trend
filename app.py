from flask import Flask, render_template, jsonify, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv("dataset/GlobalLandTemperaturesByCountry.csv")

df['dt'] = pd.to_datetime(df['dt'])
df['Year'] = df['dt'].dt.year

# Remove missing values
df = df.dropna(subset=['AverageTemperature'])

# ==============================
# GLOBAL ANALYSIS
# ==============================
yearly_temp = df.groupby('Year')['AverageTemperature'].mean().reset_index()

country_temp = df.groupby('Country')['AverageTemperature'].mean() \
                 .sort_values(ascending=False).head(10)

# ==============================
# GLOBAL ML MODEL
# ==============================
X = yearly_temp[['Year']]
y = yearly_temp['AverageTemperature']

global_model = LinearRegression()
global_model.fit(X, y)

# ==============================
# ROUTES
# ==============================

@app.route("/")
def home():
    return render_template("index.html")


# Global temperature trend
@app.route("/data")
def data():
    return jsonify({
        "year": yearly_temp["Year"].tolist(),
        "temp": yearly_temp["AverageTemperature"].round(2).tolist()
    })


# Top 10 hottest countries
@app.route("/countries")
def countries():
    return jsonify({
        "country": country_temp.index.tolist(),
        "temp": country_temp.round(2).tolist()
    })


# Search country trend
@app.route("/search")
def search():

    country = request.args.get("country")

    if not country:
        return jsonify({"year": [], "temp": []})

    country_data = df[df["Country"].str.lower() == country.lower()]

    result = country_data.groupby("Year")["AverageTemperature"].mean().reset_index()

    result = result.dropna()

    return jsonify({
        "year": result["Year"].tolist(),
        "temp": result["AverageTemperature"].round(2).tolist()
    })


# Statistics
@app.route("/stats")
def stats():

    avg_temp = df["AverageTemperature"].mean()
    max_temp = df["AverageTemperature"].max()
    min_temp = df["AverageTemperature"].min()

    return jsonify({
        "avg": round(avg_temp,2),
        "max": round(max_temp,2),
        "min": round(min_temp,2)
    })


# ==============================
# GLOBAL PREDICTION
# ==============================
@app.route("/predict")
def predict():

    year = request.args.get("year")

    if not year:
        return jsonify({"prediction": None})

    year = int(year)

    prediction = global_model.predict([[year]])

    return jsonify({
        "year": year,
        "prediction": round(float(prediction[0]), 2)
    })


# ==============================
# COUNTRY-WISE PREDICTION
# ==============================
@app.route("/predict_country")
def predict_country():

    country = request.args.get("country")
    year = request.args.get("year")

    if not country or not year:
        return jsonify({"prediction": None})

    year = int(year)

    # Filter data
    country_data = df[df["Country"].str.lower() == country.lower()]

    country_yearly = country_data.groupby("Year")["AverageTemperature"].mean().reset_index()

    country_yearly = country_yearly.dropna()

    # Check data availability
    if len(country_yearly) < 5:
        return jsonify({"prediction": "Not enough data"})

    # Train model for that country
    X = country_yearly[['Year']]
    y = country_yearly['AverageTemperature']

    model = LinearRegression()
    model.fit(X, y)

    prediction = model.predict([[year]])

    return jsonify({
        "country": country,
        "year": year,
        "prediction": round(float(prediction[0]),2)
    })


# ==============================
# RUN APP
# ==============================
if __name__ == "__main__":
    app.run(debug=True)