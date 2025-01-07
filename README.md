# Hackathon_01

Project Overview

The system integrates multiple APIs to fetch real-time data, including traffic conditions, weather forecasts, and route information. It then processes this data to suggest the most efficient route while calculating the estimated CO2 emissions for the journey.

Key Features:
Real-time Traffic Data: Fetches live traffic conditions using the TomTom API.

Weather Data: Retrieves current weather conditions at the destination using the AQICN API.

Route Optimization: Uses the OSRM API to generate the most efficient route.

CO2 Emission Calculation: Estimates the carbon footprint based on the distance traveled and vehicle type.

Setup Instructions
To get started with the project, follow these steps:

1. Clone the Repository
First, clone the repository to your local machine using the following command:
   on terminal:-
         git clone https://github.com/your-username/dynamic-route-optimization.git
   
2.Install Dependencies
Navigate to the project directory and install the required dependencies using pip:
  on terminal:-
     cd dynamic-route-optimization
     pip install -r requirements.txt
     
3.Run the Application
Once the dependencies are installed and the environment variables are set, you can run the application using the following command:
  on terminal:-
        python main.py

4.Running Tests
To ensure the application works as expected, you can run the unit tests using the following command:
 on terminal:-
    python -m unittest discover tests
    (before you run teste first install library pip install pytest)

Any other issue you face share with me .

Thank you for using the Dynamic Route Optimization and Emission Reduction System! We hope it helps you make more informed and eco-friendly travel decisions.

  

    
