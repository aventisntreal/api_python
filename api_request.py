import requests
import json

cntr = input("Enter country name: ")
cntr.lower()

url = 'https://restcountries.com/v3.1/name/' + cntr 
x = requests.get(url)
r = x.text
y = json.loads(r)
if y[0]["status"] == 404:
    raise Exception("Country not found")
else:
    #print(x.json())
    num = int(input("What you want to know: \n 1.Population \n 2.Capital city \n 3.Languages \n 4.Code \n 5.Independence \n"))
    if num == 1:
        print("Population: ", y[0]["population"])
    if num == 2:
        print("Capital city: ", y[0]["capital"])
    if num == 3:
        print("Languages: ", y[0]["languages"])
    if num == 4:
        print("Country code: ", y[0]["ccn3"])
    if num == 5:
        print("Independece: ", y[0]["independent"])






