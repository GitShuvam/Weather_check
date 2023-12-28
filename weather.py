import requests
import json
import win32com.client as wincom


city = input("Enter the name of the city : ")

url = f"https://api.weatherapi.com/v1/current.json?key=bcf42de26c474c73a0c23411231605&q={city}"
r = requests.get(url)
# print(r.text)
# print(type(r.text)) 
# Change the class to Dictionary
wdic = json.loads(r.text)
# print(wdic["current"] ["temp_c"])
# <--------Voice Mode----->>>
d = wdic["current"] ["temp_c"]
t = wdic["location"] ["localtime"]
speak = wincom.Dispatch("SAPI.SpVoice")
text = (f"The current weather in {city} is {d} degree celcius , date and localtime is {t}")
speak.Speak(text)