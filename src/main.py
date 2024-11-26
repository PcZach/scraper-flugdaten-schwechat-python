import json
import requests

url = "https://www.viennaairport.com/jart/prj3/va/data/flights/inc.json"
response = requests.get(url)
data = json.loads(response.text)
print(data)
