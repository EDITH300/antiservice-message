#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) king legend

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from sample_config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    app = pyrogram.Client(
        "deleter",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
    )
    app.run()
    
pyrogram.Client.on_message(pyrogram.Filters.service)
async def service(b:bot, u:update):
    await b.delete_messages(chat_id=u.chat.id, message_ids=u.message_id)