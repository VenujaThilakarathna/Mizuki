# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/Mizuki/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 7395896  # integer value, dont use ""
    API_HASH = "cd3998ddf318dad74d7c506731bc0abc"
    TOKEN = "2109331733:AAG4FwTMj2nzej5hMVFy247IlJT3p-p89u4"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1826486119  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Venuja_Sadew"
    SUPPORT_CHAT = "VndBotSupport"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001473463944
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001190806654
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://frecopip:LlIsZsD-i6OaaWXcW5tihi31H6B725NN@fanny.db.elephantsql.com/frecopip"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "VB~tIGZv0p8urCZFM4psuaJX03KN9hQFZw7twou7Fd64B~bDzX~VngaxCK_jOxcS"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = "CAACAgUAAxkBAAIwfWGg7UllDrKruwqh00JcYyCEKrVBAAKVAwACk9MAAVUCg1HqJDy70CIE"  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "XPGUJ8BSXNBRRQVF"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "00850f78b2f05aafbf7f1477058abd2f7ff385d0d8ad73a0b86c3d71010b5f08291d540fdce195d7408121bbea91dd068492e617f5e182c0b20256ef47a2bbda"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
