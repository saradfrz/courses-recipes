import json


credentials_file = "config/json/credentials.json"
f = open(credentials_file, 'r', encoding='utf-8')
credentials = json.load(f)

SECRET_KEY = credentials["Django"]["SECRET_KEY"]