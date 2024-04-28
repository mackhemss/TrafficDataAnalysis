from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# Load the traffic data
traffic_data = pd.read_csv('traffic_data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    # Get filter parameters from the form
    time_of_day = request.form.get('time_of_day')
    date = request.form.get('date')
    print(time_of_day)
    # Filter the data based on selected parameters
    filtered_data = traffic_data[(traffic_data['Time_of_the_day'] == time_of_day) & (traffic_data['Date'] == date)]

    # Create a Plotly bar chart
    fig = px.bar(filtered_data, x='Sr No', y='Traffic PCU/unit time', title='Traffic Data Analysis')

    # Convert the Plotly figure to HTML
    plot_html = fig.to_html(full_html=False)

    return render_template('dashboard.html', plot=plot_html)

if __name__ == '__main__':
    app.run(debug=True)
