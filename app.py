import tkinter as tk
import requests
from tkinter import font





def get_weather(city):
    
    weather_key = 'b4a0d305a9d92632a0bfcacc381f2f8c'
    url = "https://api.openweathermap.org/data/2.5/weather"
    params={'APPID': weather_key, 'q': city, 'units':'metric'}
    response= requests.get(url, params=params)
    weather=response.json()
    label['text']= format_response(weather)

def format_response(weather):

    try:
        name= weather['name']
        description=weather['weather'][0]['description']
        temp=weather['main']['temp']
        wind=weather['wind']['speed']
        final_str='Name: %s \nDescription: %s \nTemperature: %s °C \nWind: %s' %(name,description,temp,wind)
    except:
        final_str='Something went wrong'
    return final_str
    




root=tk.Tk()

height=500
width= 600

canvas= tk.Canvas(root,width=width, height=height)
canvas.pack()

upper_frame=tk.Frame(root,bg='#80c1ff', bd=5)
upper_frame.place(relx=0.5,rely=0.1,relwidth=0.7,relheight=0.1, anchor='n')

entry=tk.Entry(upper_frame,font=40)
entry.place(relwidth=0.7,relheight=1)

button=tk.Button(upper_frame,text="Get weather", command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)


lower_frame=tk.Frame(root,bg="#80c1ff", bd=5)
lower_frame.place(relx=0.5,rely=0.3, relwidth=0.7, relheight=0.6, anchor='n')

label= tk.Label(lower_frame, font=('Courier',18), anchor="nw", justify="left", bd=5)
label.place(relheight=1,relwidth=1)


root.mainloop()