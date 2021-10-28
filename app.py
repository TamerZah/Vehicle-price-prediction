# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 07:01:36 2021

@author: lenovo
"""

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask((__name__))
model = pickle.load(open("random_forest_regression_model.pkl", "rb"))

@app.route("/", methods=["GET"])

def Home():
    return render_template("index.html")


standard_to = StandardScaler()
@app.route("/predict", methods=["POST"])


def predict():
    if request.method == "POST":
        Year = int(request.form["Year"])
        Present_Price = float(request.form("Present_Price"))
        Kms_Driven = int(request.form["Kms_Driven"])
        Owner = int(request.form["Owner"])
        Fuel_Type = request.form["Fuel_Type_Diesel"]
        if Fuel_Type == "Petrol":
            Fuel_Type_Diesel = 0
            Fuel_Type_Petrol = 1
        elif Fuel_Type == "Diesel":
            Fuel_Type_Diesel = 1
            Fuel_Type_Petrol = 0
        elif Fuel_Type  == "CNG":
            Fuel_Type_Diesel = 0
            Fuel_Type_Petrol = 0
            
        Seller_Type = request.form["Seller_Type"]
        if Seller_Type == "Dealer":
            Seller_Type_Individual = 0
        elif Seller_Type  == "Individual":
            Seller_Type_Individual = 1

        Transmission_Type = request.form["Transmission_Type"]
        if Transmission_Type == "Manual Car":
            Transmission_Manual = 1
        elif Transmission_Type  == "Automatic Car":
            Transmission_Manual = 0

        prediction = model.predict([Year, Present_Price, Kms_Driven, Owner, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual])
        output = round(prediction[0], 2)
        
        if output < 0:
            return render_template("index.html", prediction_texts = "Sorry you can't sell this vehicle")
        else:
            return render_template("index.html", prediction_texts = "Vehicle price: {}".format(output))
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)






















