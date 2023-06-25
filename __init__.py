from flask import Flask
from flask_pymongo import PyMongo
import os
from datetime import datetime,timedelta
import numpy as np
from pymongo import *
import Algo

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
#

app.config["MONGO_URI"] =  'mongodb://W:SWPro@141.37.168.25:27017/SW'
#"mongodb+srv://Williami:5VceuObgOJtWMyod@sw.1mvxof8.mongodb.net/Test?retryWrites=true&w=majority"
#setup mongodb

mongo_client = PyMongo(app)
db = mongo_client.db
"""
calc = []
calc2 = []

start_date = {"Day ": 22,"Month ": 6, "Year ": 2023 }
counter = 0
day = start_date["Day "]
month = start_date["Month "]
year = start_date["Year "]
username_g = "Martin"
for i in range(0,7):
      #iterate seven days before start_date
      #because calculation begins with the todays date. And the data in the future isnt available 
     sleepDiary_m_day = db.SleepDiary_m.find_one({"user":username_g,"Date":{"Day ":day-i,"Month ":month,"Year ":year} })
     sleepDiary_e_day = db.SleepDiary_e.find_one({"user":username_g,"Date":{"Day ":day-i,"Month ":month,"Year ":year} })
     calc.append(Algo.clcSleepTime(sleepDiary_m_day["TimeLightOff[HH:MM]"], sleepDiary_m_day["WakeUpTime[HH:MM]"],
                            sleepDiary_m_day["HowLongTotal[HH:MM]"],sleepDiary_m_day["LightOff2Sleep[HH:MM]"]))
     calc2.append(Algo.clcSER(calc[i], sleepDiary_e_day["Time2Bed"] ,sleepDiary_m_day["RiseTime[HH:MM]"])   )
    
    
#after seven day iteration calculate the sum over the list
mean_sleepeff = sum(calc2)/7

sleepTime = Algo.EffControl(calc[i],calc2[i],counter,username_g)

username_g = "Martin"
testlist =[{"Date":{"Day ":15,"Month ":6,"Year ":2023}} ,{"Date":{"Day ":22,"Month ":6,"Year ":2023}}]


day = datetime.now().day

def getLast7days():
    
    try: 
        #test if there is enough data for calculation
        if db.SleepDiary_m.count_documents({"user":username_g}) < 7:
            raise Exception()
    except:
        flash("")
        return redirect("not enough SleeDiarys. Minimal amount 7 Diarys (morning, evening)")


    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    #every morning diarys from the last seven days
    sleepDiary_m_day = db.SleepDiary_m.find({"user":username_g,"Date.Day ":{"$gte":day-7 ,"$lte":day}})  
    sleepDiary_e_day = db.SleepDiary_e.find({"user":username_g,"Date.Day ":{"$gte":day-7 ,"$lte":day}})
    return sleepDiary_m_day,sleepDiary_e_day
        
    

sleepDiary_m_day,sleepDiary_e_day = getLast7days()
sleepDiary_m_day = list(sleepDiary_m_day)
sleepDiary_e_day = list(sleepDiary_e_day)  

for i in range(0,7):
    print("1- ",sleepDiary_m_day[i]["TimeLightOff[HH:MM]"],"\n")
    #print("2- ",sleepDiary_e_day[i])
    print()



#for part in sleepDiary_m_day:
"""   


from routes import *