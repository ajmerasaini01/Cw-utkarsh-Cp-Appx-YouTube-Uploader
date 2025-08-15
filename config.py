#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE

import os

class Config(object):
    # Get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", 26331872))
    API_HASH = os.environ.get("API_HASH", "c93589620441707c37c5683a02eea54e")
    AUTH_USERS = os.environ.get("AUTH_USERS", "8355707251")

