from bot import InstagramBot
import datetime
from get_meal import Meal
from create_image import CreateImage
from tool.dateTools import chage_korean_dayofweek

def DM_bot(key: str, city_code: str, school_code: str, font_path: str, output_path: str, instagram_bot: InstagramBot):
    create_image = CreateImage()
    while True:
        date = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
        prefix = "!"
        last_DM_data: tuple = instagram_bot.get_last_message_and_channel()
        if last_DM_data[1].replace(prefix, "") == "오늘급식":
            meal = Meal()
            meal_data = meal.get_meal(key, city_code, school_code, date.strftime("%Y%m%d"))
            if not meal_data["meal_menu"] == [] and not meal_data["meal_allergy"] == []:
                image_name = chage_korean_dayofweek(date.strftime("%m월 %d일 (%a) 급식"))
                image = output_path + image_name + "-feed.jpg"
                create_image.feed_image(meal_data, font_path, date)
                instagram_bot.send_image_message(image, last_DM_data[0])
            else:
                instagram_bot.send_text_message("오늘의 급식이 존재하지 않습니다!", last_DM_data[0])
