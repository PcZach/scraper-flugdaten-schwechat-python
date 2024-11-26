import json
import requests
import datetime
from pprint import pprint
from pydantic import BaseModel, Field

url = "https://www.viennaairport.com/jart/prj3/va/data/flights/inc.json"
response = requests.get(url)
data = json.loads(response.text)


class Flight(BaseModel):
    flight_number: str = Field(max_length=12)
    arrival_datetime_planned: datetime.datetime
    arrival_datetime_actual: datetime.datetime
    canceled: bool = False
    airline_iata: str = Field(max_length=4)
    arrival_airport_iata: str = Field(max_length=12)
    departure_airport_iata: str = Field(max_length=12)
    departure_datetime_planned: datetime.datetime
    departure_datetime_actual: datetime.datetime


number = 1
for flight in data["monitor"]["departure"]:
    pprint(flight)
    if number == 1:
        break
