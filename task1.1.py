import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
myKey = os.getenv('GENDER_API_KEY')

def get_gender_by_name(first_name, last_name, myKey):
    if last_name == 'null':
        url = f"https://gender-api.com/get?name={first_name}&key={myKey}"
    else:
        url = f"https://gender-api.com/get?split={first_name}%20{last_name}&key={myKey}"
    response = requests.get(url)
    data = response.json()
    return data.get('gender')

user_name = ''
first_name = ''
last_name = ''

with open('json_file.json', 'r') as file:
    data = json.load(file)
    file.close()

male_file = open('male.txt', 'a')
female_file = open('female.txt', 'a')
for user in data:
    user_name = user
    first_name = (data[user]["first_name"])
    last_name = (data[user]["last_name"])
    gender = get_gender_by_name(first_name, last_name, myKey)
    if gender == "male":
        male_file.write(user_name + '\n')
    elif gender == "female":
        female_file.write(user_name + '\n')

male_file.close()
female_file.close()
