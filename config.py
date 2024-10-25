import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 22793098
API_HASH = "fe39d184efaebc3ee0f451f7d28a93f0"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8189799114:AAEUX_4z6slihPPbyLQwIml6McdnAurW_9U"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://sachin25u7:sachin25u7@cluster0.6kesm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002305534434

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7282263969

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/about_Nobita3"
SUPPORT_GROUP = "https://t.me/Og_membars"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQFby4oAhszUHB9ZjPYkiurS7EuWQceFeuGTNthMfB5CqbCH3bRb-KatoqVkt6-3D-QquRFS1ssBEsZJB9nGAyg7QCGStSRKnGq63TdlBkTrVf5s_0hc1Wu5wyxgHqiJxvaWh82z_Fudhc08fF7fJ6gq_StNlRczPOQzoH93JcuLf_nK7AB9uL1co1gZkZEH7G8KscFJNeRLXoMnFRbOqe3-KqyQaSH1_zK1n-N-zXIOL-8YKNkeLeskwyGvNaUaJnuwuG7AUgrAbVYan3RGyjDGXSdnfP9tCl7z5q6Nvbon3pzehIPbHpFok5bQPLKYMRjIVr3smyQuK4eSDxzHVskUuAfa0gAAAABUMA68AA"
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


START_IMG_URL = "https://graph.org/file/096f6d88999670f46aa61-22b1e09efdcc4237d6.jpg"

PING_IMG_URL = "https://graph.org/file/4015ac02f418cc2b2a392-34500566110ab25ef6.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/4015ac02f418cc2b2a392-34500566110ab25ef6.jpg"
STATS_IMG_URL = "https://graph.org/file/4015ac02f418cc2b2a392-34500566110ab25ef6.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/4015ac02f418cc2b2a392-34500566110ab25ef6.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/4015ac02f418cc2b2a392-34500566110ab25ef6.jpg"
STREAM_IMG_URL = "https://graph.org/file/096f6d88999670f46aa61-22b1e09efdcc4237d6.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/096f6d88999670f46aa61-22b1e09efdcc4237d6.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/096f6d88999670f46aa61-22b1e09efdcc4237d6.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/096f6d88999670f46aa61-22b1e09efdcc4237d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/096f6d88999670f46aa61-22b1e09efdcc4237d6.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/096f6d88999670f46aa61-22b1e09efdcc4237d6.jpg"


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
