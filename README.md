# Flight-fare-prediction
Project to predict the flight fare with deployment
# Flight Fare Prediction: 

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Dataset](#dataset)
  * [Future scope of project](#future-scope)


## Demo
Link: [https://get-flightfare.herokuapp.com/](https://get-flightfare.herokuapp.com/)

https://user-images.githubusercontent.com/51751926/122657809-64aed600-d184-11eb-9777-b4565b165f1b.mp4

## Overview
This is a Flask web app which predicts fare of Flight ticket. You have to choose all the options if you have a non-stop flight
<br/> your start destination will be source and final destination will be stop1. <br/>
Similarly if you have 1 stop your start destination would be source 1st stop as stop1 and destination as stop2
<br/> This applies for any number of stops you choose 

## Installation
The Code is written in Python 3.9.1. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). <br/>
Make sure that pip is upgraded if not:
```bash
pip install --upgrade pip
```
- Cloning the repository :
     - 🦖 go to the folder in your device where you want to clone <br/>
     - 🦖 make sure that git is installed already if not click [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
```bash
git clone https://github.com/amey16/Flight-fare-prediction.git
```
After cloning run this command - 
```bash
pip install -r requirements.txt
```
If you still face any import error just run command pip install library_name for windows | sudo apt install library_name for linux

## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

![image](https://user-images.githubusercontent.com/51751926/122658097-f61f4780-d186-11eb-8b74-2b37d9bbb4b9.png)
Click on the create app option once you reach this page
<br/>
Follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.
  
## Directory Tree 
```
├── app.py
├── Data_Train.xlsx
├── Flight fare(Feature engineering + random forest).ipynb
├── Procfile
├── requirements.txt
├── rf_flight.pkl
├── Test_set.xlsx
├── tree.txt
├── .ipynb_checkpoints
|   ├──Flight fare(Feature engineering + random forest)-checkpoint.ipynb
├── static
|   ├── styles.css     
├── templates
    ├── home.html
```

## Dataset

The dataset was collecected from kaggle .To go to the dataset [click here](https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh/).
<br />
What the columns of dataset look like - <br/>
Feature name | Feature meaning
:---: | :---:
Airline | The name of the airline.
Date_of_Journey | The date of the journey
Source | The source from which the service begins.
Destination | The destination where the service ends.
Route | The route taken by the flight to reach the destination.
Dep_Time | The time when the journey starts from the source.
Arrival_Time | Time of arrival at the destination.
Duration | Total duration of the flight.
Total_Stops | Total stops between the source and destination.
Additional_Info | Additional information about the flight
Price | The price of the ticket

## Future Scope

* Use multiple Algorithms other than random forest like XGBoost ,maybe Decision Trees
* Optimize Flask app.py and improve the UI 
* Data analysis to check people preferce of Airlines,etc .
