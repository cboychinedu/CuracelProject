#!/usr/bin/env python3 

# Author: Mbonu Chinedum Endurance 
# University: Nnamdi Azikiwe University 
# Description: 
# Date Created: 
# Date Modified: 

# Importing the necessary modules 
from flask import Flask, render_template, request 
from main import MakePrediction 


# Creating the flask application 
app = Flask(__name__)

# Testing 
@app.route("/test", methods=["GET"])
def Testing(): 
    return render_template("predictedValue.html")


# Creating the first Route for taking in the users car specifications 
# and saving it 
@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

#### 
@app.route("/", methods=["POST"])
def InputText():
    # Getting the name values for the car 
    BrandName = request.form['brand_name'].lower() 
    Year = request.form['year']
    KilometersDriven = request.form['kilometers_driven']
    FuelType = request.form['fuel_type'].lower() 
    Transmission = request.form['transmission'].lower() 
    OwnerType = request.form['owner_type'].lower() 
    Mileage = request.form['mileage']
    Engine = request.form['engine']
    EnginePower = request.form['engine_power']
    SeatNumber = request.form['seat_number']
    
    # Creating a tuple variable and saving the following parameters for the car 
    # predictors into it 
    UserInput = { "BrandName": BrandName, "Year": Year, "KilometersDriven": KilometersDriven, 
                  "FuelType": FuelType, "Transmission": Transmission, "OwnerType": OwnerType, 
                  "Mileage": Mileage, "Engine": Engine, "EnginePower": EnginePower, "SeatNumber": SeatNumber }
    
    # If The user did not fill some values then the main page should be 
    # Returned. 
    for name, value in UserInput.items():
        if value is "":
            # The page rendered here would be an error page explaining that the following values
            # Are missing from the input form. 
            # Thus we show the error page, and click back to go back to the main window. 
            return "<h5> The {} Value is Missing.".format(name)
    
    # perfroming the main function if all the conditions are satified. 
    else:
        # Then we pass the created dictionary into the MakePrediction Class for which 
        # we would get the actual prediction for the value of the car with the specific 
        # parameters in the tuple 
        # Creating an instance of the class 
        Prediction = MakePrediction(UserInput)
        # 
        PredictedPrice = Prediction.ModelBuilding() 
        # 
        CarName = BrandName.upper() 
        
    # Returning the page to show the predicted value
    return render_template("predictedValue.html", CarName=CarName, PredictedPrice=PredictedPrice)


 
# Running the flask application 
if __name__ == '__main__':
    app.run(debug=True)