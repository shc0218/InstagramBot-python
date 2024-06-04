from instagrapi import *

class InstagramBot:
    def __init__(self):
        self.__bot = Client()
    def bot_start(self, username: str, password: str):
        self.__bot.login(username, password)
        print("Bot started")
    def bot_stop(self):
        self.__bot.logout()
        print("Bot stopped")
    def upload_feed(self, image: str, caption: str):
        self.__bot.photo_upload(image, caption)
        print("Image uploaded")
    def upload_story(self, image: str):
        story_pk = self.__bot.photo_upload_to_story(image).pk
        self.__bot.story_info(story_pk)