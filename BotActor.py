# coding=utf-8
import logging
from pprint import pprint

import sys
import telegram
from telegram import Bot
from telegram import InlineKeyboardMarkup
from telegram import InlineQueryResult
from telegram import InlineQueryResultArticle
from telegram import InlineQueryResultAudio
from telegram.error import NetworkError, Unauthorized
from time import sleep
import paho.mqtt.client as mqtt
import pykka
import urllib
import logging
import json
import os

from telegram.ext import CallbackQueryHandler
from telegram.ext import Filters
from telegram.ext import InlineQueryHandler
from telegram.ext import MessageHandler
from telegram.ext import Updater

import ManagerActor
from telegram import InlineKeyboardButton, CallbackQuery


class BotActor(pykka.ThreadingActor):
    def __init__(self, manager):
        super(BotActor, self).__init__()
        self.manager = manager
        self.token = os.getenv('token')
        self.bot = None

    def on_start(self):
        updater = Updater(self.token)
        self.bot = updater.bot

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        # on noncommand i.e message - echo the message on Telegram
        # dp.add_handler(MessageHandler(Filters.all, self.post))
        # dp.add_handler(CallbackQueryHandler(self.post))
        dp.add_handler(InlineQueryHandler(self.post))

        # Start the Bot
        updater.start_polling()

    def post(self, bot, update):
        replys = [
            u"Подъем",
            u"Ушел спать",
            u"Начал есть",
            u"Закончил еду",
            u"Начал йогу",
            u"Закончил йогу",
            u"В телефоне",
            u"Из телефона",
            u"На прогулку",
            u"С прогулки",
            u"В деле",
            u"Без дела",
            u"Прокрастинация",
            u"ХХХ",
        ]
        results = []
        i = 0
        for r in replys:
            i += 1
            results.append(InlineQueryResultArticle(i, r, r))
