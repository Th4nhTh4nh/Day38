import requests
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = 55
HEIGHT_CM = 171
AGE = 21

APP_ID = "828de3fd"
API_KEY = "38650d8822890163943ca8310fb98118"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
