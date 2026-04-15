Overview

ClimateTrend is a web-based application that analyzes historical climate data and visualizes global and country-wise temperature trends. It also uses machine learning to predict future temperatures for specific countries.

Features
 Global temperature trend visualization
 Top 10 hottest countries analysis
 World temperature map
 Country-wise climate trend search
 Country-specific temperature prediction using machine learning
Technologies Used:
Python (Flask)
Pandas
Chart.js
Bootstrap
Scikit-learn
Dataset Used:

Due to large file sizes, datasets are not included in this repository.

You can download them from:

👉 https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data

📁 Datasets used in this project:
GlobalLandTemperaturesByCountry.csv
GlobalLandTemperaturesByCity.csv
GlobalLandTemperaturesByMajorCity.csv
GlobalLandTemperaturesByState.csv
GlobalTemperatures.csv

After downloading, place them inside:

dataset/
 How to Run the Project
1️ Clone the repository
git clone https://github.com/YOUR_USERNAME/Climate-trend.git
cd Climate-trend
2️ Install dependencies
pip install flask pandas scikit-learn
3️ Run the application
python app.py
4️ Open in browser
http://127.0.0.1:5000
 How It Works
Loads and preprocesses historical climate data using Pandas
Provides APIs using Flask
Visualizes data using Chart.js
Uses Linear Regression to predict future temperatures
 Objective

To analyze long-term climate changes and provide insights along with future temperature predictions, supporting SDG Goal 13: Climate Action.

 Future Scope
Integration of real-time climate data
More advanced prediction models
Deployment as a live web application
