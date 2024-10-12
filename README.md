# SDT-Project
# Car Listings Dashboard

## Description
This project is a web application that provides an exploratory data analysis tool for car listings. The dashboard visualizes various attributes of car advertisements, helping users make data-driven decisions regarding car purchases. The primary functionalities include displaying histograms of car prices, scatter plots comparing price versus odometer readings, and a data viewer for inspecting the dataset.

## Methods and Libraries
This project utilizes the following Python libraries:
- **Streamlit**: For creating the web application interface.
- **Pandas**: For data manipulation and analysis.
- **Plotly Express**: For creating interactive visualizations.

## Installation and Setup
To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/leo9two/SDT-Project.git
   cd ../SDT-Project

Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:
   pip install streamlit pandas plotly

Run the application:
   streamlit run app.py

Open your web browser and navigate to http://localhost:8501 to view the dashboard.

Make sure the dataset vehicles_us.csv is located in the same directory as app.py for the application to work correctly.
Feel free to explore and modify the code for personalized insights.
