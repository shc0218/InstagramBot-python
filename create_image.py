import datetime

from PIL.JpegImagePlugin import JpegImageFile

from dateTools import chage_korean_dayofweek

from PIL import Image, ImageDraw, ImageFont
import os
from os import path
class create_image:
    def __set_font(self, font_path: str, text: str, font_size: int) -> tuple:
        font = ImageFont.truetype(font=font_path, size=font_size, encoding="utf-8")
        left, top, right, bottom = font.getbbox(text)
        tw = right - left
        th = bottom - top
        return font, tw, th
    def __draw_text(self, origin_image:JpegImageFile, font: ImageFont, text: str, x: int, y: int):
        draw = ImageDraw.Draw(origin_image)
        draw.text((x, y), text, font=font, fill="black")
    def feed_image(self, meal_data: dict, font_path: str, date: datetime.datetime):
        title = date.strftime("%m월 %d일 (%a) 급식")
        title = chage_korean_dayofweek(title)
        origin_image = Image.open(os.path.abspath('.') + "/feed_image.jpg")

        w, h = origin_image.size
        title_font, title_tw, title_th = self.__set_font(font_path, title, 70)
        self.__draw_text(origin_image, title_font, title, w /2 - title_tw / 2, 50)

        for menu in meal_data["meal_menu"]:
            menu_font, menu_tw, menu_th = self.__set_font(font_path, menu, 50)
            self.__draw_text(origin_image=origin_image, font=menu_font, text=menu, x=100, y=(320+(100*meal_data["meal_menu"].index(menu))))

        allergy_text= f"*알러지: {", ".join(meal_data['meal_allergy'])}"
        allergy_font, allergy_tw, allergy_th = self.__set_font(font_path, allergy_text, 30)
        self.__draw_text(origin_image, allergy_font, allergy_text, w/2 - allergy_tw/2, h - 100)
        if not path.exists(os.path.abspath('.') + "/output"):
            os.mkdir(os.path.abspath('.') + f"/output")
        origin_image.save(os.path.abspath('.') + f"/output/{title}-feed.jpg")

    def story_image(self, meal_data: dict, font_path: str, date: datetime.datetime):
        title = date.strftime("%m월 %d일 (%a) 급식")
        title = chage_korean_dayofweek(title)
        origin_image = Image.open(os.path.abspath('.') + "/story_image.jpg")

        w, h = origin_image.size
        title_font, title_tw, title_th = self.__set_font(font_path, title, 80)
        self.__draw_text(origin_image, title_font, title, w /2 - title_tw / 2, 90)

        for menu in meal_data["meal_menu"]:
            menu_font, menu_tw, menu_th = self.__set_font(font_path, menu, 70)
            self.__draw_text(origin_image=origin_image, font=menu_font, text=menu, x=100, y=(500+(150*meal_data["meal_menu"].index(menu))))

        if not path.exists(os.path.abspath('.') + "/output"):
            os.mkdir(os.path.abspath('.') + f"/output")
        origin_image.save(os.path.abspath('.') + f"/output/{title}-story.jpg")