


import os
from Uploader.config import Config
from pyrogram import Client as Tellyhub

if __name__ == "__main__" :
    
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="Uploader")
    Tellybots = Tellyhub("@TellyUploaderProBot",
    bot_token=5546691928:AAFRtZZ_3sINot1-4Z2xJD-8wWlj2lqQJlk,
    api_id=11253846,
    api_hash=8db4eb50f557faa9a5756e64fb74a51a,
    sleep_threshold=120,
    plugins=plugins)
    Tellybots.run()
