#!/usr/bin/env python3

import requests
import json

url = "https://tides.p.rapidapi.com/tides"

querystring = {"latitude":"48.650879","longitude":"-2.825678","duration":"1440","interval":"60"}

headers = {
    'x-rapidapi-host': "tides.p.rapidapi.com",
    'x-rapidapi-key': "d25af34ea3msh9adecabdc1c8b42p1f50d5jsnc8c2d4975cc3"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

sea_height = response.json()['heights'][0]['height']
sea_state = response.json()['heights'][0]['state']


def getCoefficient():

  b=sea_height+5

  c=b*15

  print(b)

  return 590 -int(c)




def getMovement():

  return str(sea_state)



