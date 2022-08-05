# EDIT THIS FILE AND RENAME TO config.py TO MAKE THIS BOT WORKING

# FILL THESE VALUES ACCORDINGLY.

from hellbot.config.hell_config import Config

class Development(Config):

  # get these values from my.telegram.org. 

  APP_ID = "19927928"    # 6 is a placeholder. Fill your 6 digit api id

  API_HASH = "81c8c2650b2589cb8323671b3935eed1"   # replace this with your api hash

  # create any PostgreSQL database.

  # I recommend to use elephantsql and paste that link here

  DB_URI = "postgres://cbnqcofe:jGPjEHmdLLKhvqwWirB7b5dDGRduT695@kashin.db.elephantsql.com/cbnqcofe"

  # After cloning the repo and installing requirements...

  # Do `python string.py` and fill the on screen prompts.

  # String session will be saved in your saved message of telegram.

  # Put that string here.

  HELLBOT_SESSION = "1AZWarzsBu66PO7w29kMkoXJ0svJjQxfPcPKxwmgXsyboD2tSSxN-lkE7rrEtf6w2EF9Z8nQHN7amSjtqXeJ_D7z6MfT7J6TlMaVT7xTnmSPjxIAglp5ieC7nArq05i4-CXB8orlL9xR06CWOpE-TUvFu_IWAf1vHu9szCTbhZeSwtf2OiqQqKde2gva658psOQNtPm-SQoaf_zpn7kSMBb-1KOqHycg8CgltuOl54AJc2ZA60kvI-hCo80Y92ficgImBSkkpcu3OPg7jlxsdIov-2JtEM4NBQzZex9kD5eXpMB8zlDsYYWdcZeXE5tRJxOaRTS7n6xlbmjK5Y4kAQBTCte_jtjQ="

  # Create a bot in @BotFather

  # And fill the following values with bot token and username.

  BOT_TOKEN = "5487544198:AAEGQ2fGAXa6IgwMJZfRPVENmEup_V6erJ0" #token

  # Custom Command Handler. 

  HANDLER = "."

  # Custom Command Handler for sudo users.

  SUDO_HANDLER = "!"

# end of required config

# hellbot
