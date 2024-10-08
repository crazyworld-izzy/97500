import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "20185438"))
API_HASH = getenv("API_HASH", "c8f3cb6db40e4eb6e7e43866660e54ac")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "7734293231:AAFZIGbxVoeBWt6UyuwhApdw3aZvUGydkL8")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://monivps5:monivps5@cluster0.kmbq8we.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002354592685"))

OWNER_ID = int(getenv("OWNER_ID", "7712969541"))

OWNER = int(getenv("OWNER", "7712969541"))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HK543fklqxgt66hvxf")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AbhiModszYT/AnieXEricaMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SuperBanSBots")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/AM_YTSUPPORT")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION", "BQE0AV4AkOHlEGUXTgnIHKVyXCxOGFcqn-m08At2L9-B0CEc_Q0egqoWYbJwtSOC9OCb68BrLjaB3Sip0W2KOBXvUcuL5Z-z3X1ul7U77kQx_AN7mdKVZBbigJ5NevVKTyOl3_9FwU2dCykolAlcLoKEQiXVTQ-xlVPO4OnhviNDSLDklbvTRAT54LxBLHp383Aqotr1UwAGg9rWt-HdKcJQc5NBw2SMigHrqIXqJA60sQiioG1wntXywli1_LvzFA7eGvGGQ3W5KEBp-RXE55DqK-JLz8rCCqpmqX5DiL4jbnpm8Gg0u5Blg2zCxCAKC7dDhobGvQFCnoxDpxu2y5yRdolDXwAAAAHLupNFAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/4e68b6d15e042249fb284.png")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/4e68b6d15e042249fb284.png")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://telegra.ph/file/4e68b6d15e042249fb284.png")
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
