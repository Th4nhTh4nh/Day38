import requests
import datetime

MY_GENDER = "Male"
MY_WEIGHT_KG = 55.0
MY_HEIGHT_CM = 171.0
MY_AGE = 21

APP_ID = "828de3fd"
APP_KEY = "38650d8822890163943ca8310fb98118"

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
excercise_text = input("Tell me what excercises you did: ")
sheety_endpoint = (
    "https://api.sheety.co/b3ee87d266692ec6590e617dcc1188d0/exampleWorkouts/workouts"
)

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

params = {
    "query": excercise_text,
    "gender": MY_GENDER,
    "weight_kg": MY_WEIGHT_KG,
    "height_cm": MY_HEIGHT_CM,
    "age": MY_AGE,
}

basic = ("Thanh", "Thanh12012002")

nutritionix_response = requests.post(
    excercise_endpoint,
    json=params,
    headers=headers,
)
result = nutritionix_response.json()
print(result)

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for excercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": excercise["name"].title(),
            "duration": excercise["duration_min"],
            "calories": excercise["nf_calories"],
        }
    }
    sheet_response = requests.post(url=sheety_endpoint, json=sheet_input, auth=basic)
    print(sheet_response.text)
