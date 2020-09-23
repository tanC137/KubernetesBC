import time
import requests

while True:
    time.sleep(30)
    r = requests.get("https://pokeapi.co/api/v2/")
    if r.status_code != 200:
        with open("log.log", "a") as f:
            f.write("API failed \n")

