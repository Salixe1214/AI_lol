import requests
import random

def randJk():
    token = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."+
             "eyJ1c2VyX2lkIjoiMjY3MTEyNDA4NTg0MDI4M"+
             "TYwIiwibGltaXQiOjEwMCwia2V5Ijoid3VjQ2"+
             "JrWXdEQzJkeVdhaTVreHM4TktQTDZWNUNRRk5"+
             "vTjhxbFJqSW44SThWRUZpckQiLCJjcmVhdGVk"+
             "X2F0IjoiMjAyMS0wMy0yOVQwMTowODowMCswM"+
             "DowMCIsImlhdCI6MTYxNjk4MDA4MH0.CxUs1B"+
             "96r8Db-zTEIHHyEaBKT9-4g21lJqBrVSBYMBY")

    response = requests.get('https://www.blagues-api.fr/api/random',
                            headers = {'Authorization': 'Bearer ' + token})
    data = response.json()

    return data["joke"] + "\n\n" + data["answer"]
