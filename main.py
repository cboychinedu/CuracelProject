#!/usr/bin/evn python3 

# Author: Mbonu Chinedum Endurance 
# University: Nnamdi Azikiwe University 
# Description: 
# Date Created: 
# Date Modified: 

# Importing the necessary modules 
import pickle 
import joblib as jb 
import numpy as np 
from xgboost import XGBRegressor 
from sklearn.preprocessing import StandardScaler 

# Building the model 
"Note that the model used here was a regression model [XGboost model regressor]"

# Loading the saved model into disk 
# Setting the path of the serialized model 
modelPath = "model/CombinedModel.pb"

# Building the model 
model = XGBRegressor()

# Building the scaler for scaling 
scaler = StandardScaler() 

# Loading the model and the scaler model into memory 
model, scaler = jb.load(modelPath) 

# Running And Making Predictions by 
# creating a class for model prediction 
class MakePrediction:
    def __init__(self, UserInput):
        # Taking in the input values from the returned Tuple 
        self.BrandName = UserInput["BrandName"]
        self.Year = int(UserInput["Year"])
        self.KilometersDriven = int(UserInput["KilometersDriven"])
        self.FuelType = UserInput["FuelType"]
        self.Transmission = UserInput["Transmission"]
        self.OwnerType = UserInput["OwnerType"]
        self.Mileage = float(UserInput["Mileage"]) 
        self.Engine = float(UserInput["Engine"]) 
        self.EnginePower = float(UserInput["EnginePower"]) 
        self.SeatNumber = float(UserInput["SeatNumber"]) 
            
    
    # Mapping Function / Method 
    # This Function was created to map the string values to numerical values for 
    # The items in the InputTuple before predictions 
    def ModelBuilding(self):
        ### Working with BrandName ###
        # Creating a dictionary to hold the names of the Unique brand name to an assigned number 
        BrandName = {
            "maruti": 0, "hyundai": 1, "honda": 2, "audi": 3, "nissan": 4, "toyota": 5, 
            "volkswagen": 6, "tata": 7, "land": 8, "mitsubishi": 9, "renault": 10, "mercedes-Benz": 11,
            "bmw": 12, "mahindra": 13, "ford": 14, "porsche": 15, "datsun": 16, "jaguar": 17, "volvo": 18,
            "chevrolet": 19, "skoda": 20, "mini": 21, "fiat": 22, "jeep": 23, "smart": 24, "ambassador": 25,
            "isuzu": 26, "force": 28, "bentley": 29, "lamborghini": 30 }
        
        # Getting the value for the user input key 
        for name, value in BrandName.items(): 
            if self.BrandName == name:
                self.BrandName = value 
        
        
        ### Working with FuelType ###
        # Creating a dictionary to hold the names of the unique brand name to an assigned numerical value 
        FuelType = {
            "cng": 0, "diesel": 1, "petrol": 2, 
            "lpg": 3, "electric": 4 }
        
        # Getting the value for the user input key 
        for name, value in FuelType.items(): 
            if self.FuelType == name:
                self.FuelType = value 
        
        
        ### Working with Transmission [Manual / Automatic] ###
        # Creating a dictionary to hold the names of the unique brand name to an assigned numerical value 
        Transmission = {
            "manual": 0, "automatic": 1 }
        
        # Getting the value for the user input key 
        for name, value in Transmission.items(): 
            if self.Transmission == name:
                self.Transmission = value 
        
        
        ### Working with Owner Type [First / Second] Hand ###
        # Creating a dictionary to hold the names of the unique brand name to an assigned numerical value 
        OwnerType = {
            "first": 0, "second": 1, "third": 2, 
            "fourth & above": 3 }
        
        # Getting the value for the user input key 
        for name, value in OwnerType.items(): 
            if self.OwnerType == name: 
                self.OwnerType = value 
                
                
        # Creating a Tuple to hold the values gotten and returning them 
        CleanedTuple = (self.BrandName, self.FuelType, self.Transmission, 
                        self.OwnerType)
        
        
        # Building the input features before model predictions by getting the mapped values for 
        # Each individual inputs 
        brandName = self.BrandName
        year = self.Year 
        kilometersDriven = self.KilometersDriven 
        fuelType = self.FuelType
        transmission = self.Transmission
        ownerType = self.OwnerType
        mileage = self.Mileage 
        engine = self.Engine 
        power = self.EnginePower
        seats = self.SeatNumber 
        
        ## Making predictions 
        XInput = [brandName, year, kilometersDriven, fuelType, transmission, 
                  ownerType, mileage, engine, power, seats]
        
        # Converting the input feature into a numpy array 
        # Reshaping the array to 2D then scaling using standard scaler 
        XInput = np.array(XInput).reshape(1, -1)

        # Scaling 
        XInput = scaler.transform(XInput)
        
        # Model predictions 
        Pred_Y = model.predict(XInput)
        
        ## Returning the predicted value 
        return Pred_Y 
        

         
         
# predict = MakePrediction().ModelBuilding()        
# # Making predictions 
# input_features = [19, 4, 2011, 47000, 1, 0, 0, 25.44, 936.0, 57.60, 5.0]
# input_features = np.array(input_features).reshape(1, -1)
# input_X = scaler.transform(input_features)
# # Prediction 
# pred_y = model.predict(input_X)
# # Printing  
# print(pred_y)