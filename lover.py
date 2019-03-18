# -*- coding: utf-8 -*-
import random
import time
import logging

import schedule
import pyrogram
from pyrogram import Client, MessageHandler, Filters

from config import app


logging.basicConfig(filename = 'app.log', format="%(asctime)s - %(levelname)s - %(message)s", level=logging.WARNING)
logger = logging.getLogger(__name__)

loves = ['🌹', '❤️', '😘', '💋', '♥️', '🙈', '💌', '💜', '😍']
lover = 74174159

# job that sends love
def send_love():
	logger.info('called')
	try:
		love_text=random.choice(loves)*random.randint(1,5)*random.randint(0,2)
		app.send_message(chat_id=lover, text=love_text)
		logger.warning('sent')
	except pyrogram.api.errors.exceptions.bad_request_400.MessageEmpty:
		logger.warning('empty selected')
	except Exception as e:
		logger.exception(e)

def main():
	schedule.every().hour.at(':30').do(send_love)
	app.start()
	app.send_message(chat_id=74174159, text='I just started to love...')
	while True:
		schedule.run_pending()
		time.sleep(1)

if __name__ == '__main__':
	main()
