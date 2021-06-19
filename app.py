import re
from flask import Flask, request, render_template
from flask_cors import cross_origin
#from pandas._libs.tslibs import Day
import sklearn
import pickle
import pandas as pd
#from werkzeug.datastructures import T

app = Flask(__name__)
model = pickle.load(open("rf_flight.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Date = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)

        # Departure
        Departure_Hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Departure_Minute = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_Hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_Minute = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)

        # Duration
        dur_hour = abs(Arrival_Hour - Departure_Hour)
        dur_min = abs(Arrival_Minute - Departure_Minute)

        # Total Stops
        Total = int(request.form["stops"])

        Airline = request.form['Airline']
        Airline_val = 0
        if(Airline == 'Jet Airways'):
            Airline_val = 4
        elif(Airline == 'IndiGo'):
            Airline_val = 3
        elif(Airline == 'Air India'):
            Airline_val = 1
        elif(Airline == 'Multiple carriers'):
            Airline_val = 6
        elif(Airline == 'SpiceJet'):
            Airline_val = 8
        elif(Airline == 'Vistara'):
            Airline_val = 10
        elif(Airline == 'GoAir'):
            Airline_val = 2
        elif(Airline == 'Multiple carriers Premium economy'):
            Airline_val = 7
        elif(Airline == 'Jet Airways Business'):
            Airline_val = 5
        elif(Airline == 'Vistara Premium economy'):
            Airline_val = 11
        elif(Airline=='Trujet'):
            Airline_val = 9
        else:
            Airline_val = 0

        Source = request.form["Source"]
        source_val = 0
        if(Source == 'Delhi'):
            source_val = 2
        elif(Source == 'Kolkata'):
            source_val = 3
        elif(Source == 'Mumbai'):
            source_val = 4
        elif(Source == 'Chennai'):
            source_val = 1
        else:
            source_val = 0 

        Source = request.form["Destination"]
        destination_val = 0
        if(Source == 'Cochin'):
            destination_val = 1
        elif(Source == 'Delhi'):
            destination_val = 2
        elif(Source == 'New_Delhi'):
            destination_val = 5
        elif(Source == 'Hyderabad'):
            destination_val = 3
        elif(Source == 'Kolkata'):
            destination_val = 4
        else:
            destination_val = 0

        info = request.form["Info"]
        info_value = 8
        if(info == 'No info'):
            info_value = 8
        elif(info == 'In-flight meal not included'):
            info_value = 5
        elif(info == 'No check-in baggage included'):
            info_value = 7
        elif(info == '1 Short layover'):
            info_value = 1
        elif(info == 'No Info'):
            info_value = 6
        elif(info == '1 Long layover'):
            info_value = 0
        elif(info == 'Change airports'):
            info_value = 4
        elif(info == 'Business class'):
            info_value = 3
        elif(info == 'Red-eye flight'):
            info_value = 9
        elif(info == '2 Long layover'):
            info_value = 2
        
        place1_val = 5
        place2_val = 31
        place3_val = 21
        place4_val = 10
        place5_val = 4
        place6_val = 1
        place1 = request.form["Source"]
        if(place1 == 'BLR'):
            place1_val = 0
        elif(place1 == 'CCU'):
            place1_val = 2
        elif(place1 == 'DEL'):
            place1_val = 3
        elif(place1 == 'MAA'):
            place1_val = 4
        elif(place1 == 'BOM'):
            place1_val = 1
        else:
            place1_val = 5
        
        place2 = request.form["Stop1"]
        place3 = request.form["Stop2"]
        place4 = request.form["Stop3"]
        place5 = request.form["Stop4"]
        for i in range(1,Total+1):
            if(i == 1):
                if(place2 == 'DEL'):
                    place2_val = 10
                elif(place2 == 'IXR'):
                    place2_val = 20
                elif(place2 == 'LKO'):
                    place2_val = 27
                elif(place2 == 'NAG'):
                    place2_val = 29
                elif(place2 == 'BLR'):
                    place2_val = 5
                elif(place2 == 'BOM'):
                    place2_val = 6
                elif(place2 == 'CCU'):
                    place2_val = 7
                elif(place2 == 'AMD'):
                    place2_val = 0
                elif(place2 == 'PNQ'):
                    place2_val = 33
                elif(place2 == 'COK'):
                    place2_val = 8
                elif(place2 == 'IDR'):
                    place2_val = 16
                elif(place2 == 'GAU'):
                    place2_val = 11
                elif(place2 == 'MAA'):
                    place2_val = 28
                elif(place2 == 'HYD'):
                    place2_val = 15
                elif(place2 == 'BHO'):
                    place2_val = 4
                elif(place2 == 'JAI'):
                    place2_val = 23
                elif(place2 == 'ATQ'):
                    place2_val = 1
                elif(place2 == 'JDH'):
                    place2_val = 24
                elif(place2 == 'BBI'):
                    place2_val = 2
                elif(place2 == 'GOI'):
                    place2_val = 12
                elif(place2 == 'BDQ'):
                    place2_val = 3
                elif(place2 == 'TRV'):
                    place2_val = 36
                elif(place2 == 'IXU'):
                    place2_val = 21
                elif(place2 == 'IXB'):
                    place2_val = 18
                elif(place2 == 'UDR'):
                    place2_val = 37
                elif(place2 == 'RPR'):
                    place2_val = 34
                elif(place2 == 'DED'):
                    place2_val = 9
                elif(place2 == 'VGA'):
                    place2_val = 38
                elif(place2 == 'VNS'):
                    place2_val = 39
                elif(place2 == 'IXC'):
                    place2_val = 19
                elif(place2 == 'PAT'):
                    place2_val = 32
                elif(place2 == 'JLR'):
                    place2_val = 25
                elif(place2 == 'KNU'):
                    place2_val = 26
                elif(place2 == 'GWL'):
                    place2_val = 13
                elif(place2 == 'VTZ'):
                    place2_val = 40
                elif(place2 == 'NDC'):
                    place2_val = 30
                elif(place2 == 'IXZ'):
                    place2_val = 22
                elif(place2 == 'HBX'):
                    place2_val = 14
                elif(place2 == 'IXA'):
                    place2_val = 27
                elif(place2 == 'STV'):
                    place2_val = 35
                else:
                    place2_val = 31
            if(i == 2):
                if(place3 == 'BBI'):
                    place3_val = 1
                elif(place3 == 'BOM'):
                    place3_val = 4
                elif(place3 == 'BLR'):
                    place3_val = 3
                elif(place3 == 'DEL'):
                    place3_val = 7
                elif(place3 == 'COK'):
                    place3_val = 6
                elif(place3 == 'AMD'):
                    place3_val = 0
                elif(place3 == 'HYD'):
                    place3_val = 11
                elif(place3 == 'JDH'):
                    place3_val = 18
                elif(place3 == 'MAA'):
                    place3_val = 19
                elif(place3 == 'GOI'):
                    place3_val = 9
                elif(place3 == 'NAG'):
                    place3_val = 20
                elif(place3 == 'GAU'):
                    place3_val = 8
                elif(place3 == 'BHO'):
                    place3_val = 2
                elif(place3 == 'IXR'):
                    place3_val = 16
                elif(place3 == 'IDR'):
                    place3_val = 12
                elif(place3 == 'ISK'):
                    place3_val = 14
                elif(place3 == 'VGA'):
                    place3_val = 26
                elif(place3 == 'PNQ'):
                    place3_val = 22
                elif(place3 == 'JAI'):
                    place3_val = 17
                elif(place3 == 'TRV'):
                    place3_val = 24
                elif(place3 == 'HBX'):
                    place3_val = 10
                elif(place3 == 'IMF'):
                    place3_val = 13
                elif(place3 == 'CCU'):
                    place3_val = 5
                elif(place3 == 'UDR'):
                    place3_val = 25
                elif(place3 == 'VTZ'):
                    place3_val = 27
                elif(place3 == 'IXC'):
                    place3_val = 15
                elif(place3 == 'TIR'):
                    place3_val = 23
                else:
                    place3_val = 21
            if(i == 3):
                if(place4 == 'BLR'):
                    place4_val = 3
                elif(place4 == 'COK'):
                    place4_val = 5
                elif(place4 == 'DEL'):
                    place4_val = 6
                elif(place4 == 'BOM'):
                    place4_val = 4
                elif(place4 == 'HYD'):
                    place4_val = 8
                elif(place4 == 'GWL'):
                    place4_val = 7
                elif(place4 == 'TRV'):
                    place4_val = 11
                elif(place4 == 'BBI'):
                    place4_val = 1
                elif(place4 == 'BHO'):
                    place4_val = 2
                elif(place4 == 'AMD'):
                    place4_val = 0
                elif(place4 == 'NAG'):
                    place4_val = 9
                else:
                    place4_val = 10
            if(i == 4):
                if(place5 == 'BLR'):
                    place5_val = 3
                elif(place5 == 'COK'):
                    place5_val = 5
                elif(place5 == 'DEL'):
                    place5_val = 6
                elif(place5 == 'BOM'):
                    place5_val = 4
                elif(place5 == 'HYD'):
                    place5_val = 8
                elif(place5 == 'GWL'):
                    place5_val = 7
                elif(place5 == 'TRV'):
                    place5_val = 11
                elif(place5 == 'BBI'):
                    place5_val = 1
                elif(place5 == 'BHO'):
                    place5_val = 2
                elif(place5 == 'AMD'):
                    place5_val = 0
                elif(place5 == 'NAG'):
                    place5_val = 9
                else:
                    place5_val = 10
        
        place6 = request.form["FinalStop"]
        if(place6 == 'None'):
            place6_val = 1
        elif(place6 == 'DEL'):
            place6_val = 0
        
        # print(Airline_val,
        #     source_val,
        #     destination_val,
        #     info_value,
        #     Date,
        #     Month,
        #     dur_hour,
        #     dur_min,
        #     Total,
        #     Arrival_Hour,
        #     Arrival_Minute,
        #     Departure_Hour,
        #     Departure_Minute,
        #     place1,
        #     place2,
        #     place3,
        #     place4,
        #     place5)

        prediction = model.predict([[
            Airline_val,
            source_val,
            destination_val,
            info_value,
            Date,
            Month,
            dur_hour,
            dur_min,
            Total,
            Arrival_Hour,
            Arrival_Minute,
            Departure_Hour,
            Departure_Minute,
            place1_val,
            place2_val,
            place3_val,
            place4_val,
            place5_val
        ]])

        output=round(prediction[0],2)
        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)