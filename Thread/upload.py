from create_image import CreateImage
from get_meal import Meal
import datetime

def upload_bot(key, city_code, school_code, font_path, output_path, configtool, instagram_bot):
    while True:
        create_image = CreateImage()
        date = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
        if date.weekday() <= 4:
            if date.hour == 0 and date.minute == 0 and date.second == 0:
                if configtool.get_config("upload"):
                    meal = Meal()
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