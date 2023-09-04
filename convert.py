import pandas as pd
import json

file_path = 'british_airways_reviews.json'
with open(file_path, 'rb') as f:
    british_air_json = json.load(f)
    
print(british_air_json[1003])

british_air = pd.json_normalize(british_air_json)

british_air.to_csv('british_airways_reviews.csv')