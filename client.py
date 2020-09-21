import socket


import requests 
  
# api-endpoint 
URL = "http://127.0.0.1:8000/cmd"



# location given here 
cmd = "cmd body"
  
# defining a params dict for the parameters to be sent to the API 
params = { "cmd": "ff fff",  'param': "ff ff"} 

# sending get request and saving the response as response object 
r = requests.post(url = URL, json=params) 

t = bytes(100)
r = requests.post(url='http://127.0.0.1:8000/files',data=t )
r = requests.post(url='http://127.0.0.1:8000/files',files = {'file': open('client.py', 'rb')}) 
r = requests.post(url='http://127.0.0.1:8000/uploadfile',files = {'file': open('client.py', 'rb')}) 

r = requests.get(url='http://127.0.0.1:8000/getfile')
r.json()

# extracting data in json format 
data = r.json() 
print(data)
