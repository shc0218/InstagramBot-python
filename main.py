from get_meal import get_meal
from create_image import create_image
import datetime
key = "9361f9c21e834ef58bec4e49db0f2a31"
city_code = "B10"
school_code = "7010092"
font_path = "C:/Users/user/AppData/Local/Microsoft/Windows/Fonts/NanumSquareRoundEB.ttf"
date = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
meal_data = get_meal(key, city_code, school_code, date.strftime("%Y%m%d"))
print(meal_data)
create_image = create_image()
create_image.story_image(meal_data, font_path, date)