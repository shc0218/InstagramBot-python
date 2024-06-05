from create_image import CreateImage
from Thread.upload import upload_bot
from Thread.DM import DM_bot
import threading
from bot import InstagramBot
from tool.confing_tool import *


configtool = ConfingTool()
instagram_bot = InstagramBot()

configtool.setup_config()

key = configtool.get_config("neis_api_key")
city_code = configtool.get_config("neis_api_city_code")
school_code = configtool.get_config("neis_api_school_code")
font_path = configtool.get_config("image_font_path")
output_path = os.path.abspath('.') + "/output/"

instagram_bot.bot_start(configtool.get_config("instagram_username"),
                        configtool.get_config("instagram_password"))

threading.Thread(target=upload_bot, args=(key, city_code, school_code, font_path, output_path, configtool, instagram_bot)).start()
threading.Thread(target=DM_bot, args=(key, city_code, school_code, font_path, output_path, instagram_bot)).start()