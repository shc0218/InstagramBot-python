from get_meal import get_meal
from create_image import create_image
import datetime

from instagram_bot import InstagramBot
from confing_tool import *

setup_config()

key = get_config("neis_api_key")
city_code = get_config("neis_api_city_code")
school_code = get_config("neis_api_school_code")
font_path = get_config("image_font_path")
date = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
meal_data = get_meal(key, city_code, school_code, date.strftime("%Y%m%d"))
print(meal_data)
create_image = create_image()
create_image.story_image(meal_data, font_path, date)

instagram_bot = InstagramBot()
instagram_bot.bot_start(get_config("instagram_username"), get_config("instagram_password"))
instagram_bot.upload_story("C:/Python/pythonProject/feed_image.jpg")

