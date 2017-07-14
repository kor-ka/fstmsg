# coding=utf-8

import os

import pykka
from telegram import InlineQueryResultArticle
from telegram import InputTextMessageContent
from telegram.ext import InlineQueryHandler
from telegram.ext import Updater


class BotActor(pykka.ThreadingActor):
    def __init__(self):
        super(BotActor, self).__init__()
        self.token = "431107640:AAGsNVNwtQ4SvndIWlA3UjI9WeTOSZBsDVk"
        self.bot = None

    def on_start(self):
        print 'lol'
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
        print 'here'
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
            results.append(InlineQueryResultArticle(i, r, InputTextMessageContent(r)))

        print results

        return bot.answerInlineQuery(update.id, results)
