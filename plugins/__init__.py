import asyncio
import os
import time
from random import choice

from cython import *
from cython.dB import ULTROID_IMAGES
from cython.functions.helper import *
from cython.functions.info import *
from cython.functions.misc import *
from cython.functions.tools import *
from cython.misc._assistant import asst_cmd, callback, in_pattern
from cython.misc._decorators import ultroid_cmd
from cython.misc._wrappers import eod, eor
from cython.version import __version__, ultroid_version
from telethon import Button, events
from telethon.tl import functions, types

from strings import get_string

Redis = udB.get
client = bot = ultroid_bot

OWNER_NAME = ultroid_bot.me.first_name
OWNER_ID = ultroid_bot.me.id
LOG_CHANNEL = int(udB.get("LOG_CHANNEL"))
INLINE_PIC = udB.get("INLINE_PIC") or choice(ULTROID_IMAGES)
if INLINE_PIC == "False":
    INLINE_PIC = None
Telegraph = telegraph_client()

List = []
Dict = {}
N = 0

STUFF = {}

# Chats, which needs to be ignore for some cases
# Considerably, there can be many
# Feel Free to Add Any other...

NOSPAM_CHAT = [
    -1001327032795,  # UltroidSupport
    -1001387666944,  # PyrogramChat
    -1001109500936,  # TelethonChat
    -1001050982793,  # Python
    -1001256902287,  # DurovsChat
]

KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "Hehe me stel ur stiker...",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pack looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal-Your-Sticker is stealing this sticker... ",
]

ATRA_COL = [
    "DarkCyan",
    "DeepSkyBlue",
    "DarkTurquoise",
    "Cyan",
    "LightSkyBlue",
    "Turquoise",
    "MediumVioletRed",
    "Aquamarine",
    "Lightcyan",
    "Azure",
    "Moccasin",
    "PowderBlue",
]
