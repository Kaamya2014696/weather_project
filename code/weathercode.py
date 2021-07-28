import requests
#import os
from datetime import datetime

api_key = 'ab76f19092d25a34a23d9ef1d8d8ea05'
location = input("Enter the name of the city you want to know the weather forecast of: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temperature_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
humidity = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temperature_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",humidity, '%')
print ("Current wind speed    :",wind_speed ,'kmph')

print("====================================================")


# making a list so that i can print the info to a txt 
txtlist = [temperature_city,weather_desc,humidity,wind_speed,date_time]
#using open() buit-in function to write to a text file
with open("textfile.txt" , mode= 'w' ,encoding= 'utf-8') as f :     
                                     #encoding = utf-8 for linux and cp1252 for win
    f.write("------------------------------------------------------------- \n ")   
    f.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    f.write("\n ------------------------------------------------------------- \n")
    f.write("Current temperature is: {:.2f} deg C\n".format(txtlist[0]))
    
    f.write("{},{} \n".format("Current weather desc  :" ,txtlist[1]))
    f.write("{},{},{} \n".format("Current Humidity      :",txtlist[2],"%"))
    f.write("{},{},{} \n".format("Current wind speed    :",txtlist[3],"kmph"))
    f.write("====================================================")

