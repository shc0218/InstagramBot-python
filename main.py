from get_meal import Meal
from create_image import create_image
import datetime

from instagram_bot import InstagramBot
from tool.confing_tool import *

meal = Meal()
configtool = ConfingTool()
create_image = create_image()
configtool.setup_config()
instagram_bot = InstagramBot()

key = configtool.get_config("neis_api_key")
city_code = configtool.get_config("neis_api_city_code")
school_code = configtool.get_config("neis_api_school_code")
font_path = configtool.get_config("image_font_path")
output_path = os.path.abspath('.') + "/output/"

instagram_bot.bot_start(configtool.get_config("instagram_username"), configtool.get_config("instagram_password"))

while True:
    date = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    if date.weekday() <= 4:
        if date.hour == 0 and date.minute == 0 and date.second == 0:
            if configtool.get_config("upload"):
                meal_data = meal.get_meal(key, city_code, school_code, date.strftime("%Y%m%d"))
                if not meal_data["meal_menu"] == [] and not meal_data["meal_allergy"] == []:
                    create_image.feed_image(meal_data, font_path, date)
                    create_image.story_image(meal_data, font_path, date)
                    instagram_bot.upload_feed(output_path, date)
                    instagram_bot.upload_story(output_path, date)
                    configtool.set_config("upload", False)
                else:
                    print("오늘의 급식이 존재하지 않습니다!")
        if date.hour == 0 and date.minute == 0 and date.second == 1:
            configtool.set_config("upload", True)