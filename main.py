#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep

import BotActor

if __name__ == '__main__':
    BotActor.BotActor.start()
    while True:
        sleep(100)