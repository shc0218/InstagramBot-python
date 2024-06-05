import datetime

from instagrapi import Client

from tool.confing_tool import ConfingTool
from tool.dateTools import chage_korean_dayofweek


class InstagramBot:
    def __init__(self):
        self.__bot = Client()
        self.__config = ConfingTool()

    def bot_start(self, username: str, password: str) -> Client:
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
    def get_last_message_and_channel(self):
        return int(self.__bot.direct_threads()[0].pk), self.__bot.direct_threads()[0].messages[0].text
    def send_text_message(self, message: str, channel: int):
        self.__bot.direct_send(message, thread_ids=[channel])
    def send_image_message(self, path: str, channel: int):
        self.__bot.direct_send_photo(path, thread_ids=[channel])


