import datetime

from instagrapi import *
from tool.confing_tool import *
from tool.dateTools import *

class InstagramBot:
    def __init__(self):
        self.__bot = Client()
        self.__config = ConfingTool()
    def bot_start(self, username: str, password: str):
        self.__bot.login(username, password)
        print("Bot started")
    def bot_stop(self):
        self.__bot.logout()
        print("Bot stopped")
    def upload_feed(self, path: str, date: datetime.datetime):
        image_name = chage_korean_dayofweek(date.strftime("%m월 %d일 (%a) 급식"))
        image = path + image_name + "-feed.jpg"
        self.__bot.photo_upload(image, f"#신림고#{date.month}월{date.day}일#급식")
        print(f"{image_name} Feed uploaded")
    def upload_story(self, path: str, date: datetime.datetime):
        image_name = chage_korean_dayofweek(date.strftime("%m월 %d일 (%a) 급식"))
        image = path + image_name + "-story.jpg"
        story_pk = self.__bot.photo_upload_to_story(image).pk
        if self.__config.get_config("highlights_id") == "":
            print("No highlights_id found")
        else:
            self.__bot.highlight_add_stories(self.__config.get_config("highlights_id"), [story_pk])
        print(f"{image_name} Story uploaded")