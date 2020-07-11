import requests
import random

def randJk():
    random.seed(a=None)
    jk = requests.get('https://bridge.buddyweb.fr/api/blagues/blagues')

    i = random.randrange(len(jk.json()))

    return jk.json()[i]['blagues']
