import json
from os import path
import os

def setup_config():
    standard_format = {
        "neis_api_key": "",
        "neis_api_city_code": "",
        "neis_api_school_code": "",
        "image_font_path": "",
        "instagram_username": "",
        "instagram_password": ""
    }
    if not path.exists(os.path.abspath('.') + "/config.json"):
        f = open(os.path.abspath('.') + "/config.json","w")
        f.write(json.dumps(standard_format))
        f.close()
def get_config(key: str):
    with open(os.path.abspath('.') + "/config.json", 'r') as f:
        json_data = json.load(f)
    if key in json_data.keys():
        return json_data[key]
    else:
        return None