import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN",6578591645:AAGsnCcYF_SByeqRY5mtnpON1J6aRjVS_kc)
    STRING_SESSION = os.environ.get("STRING_SESSION",1BVtsOHMBu6R3iewVS-xL4HUDFffz10Y9pD3XMTIfkMT7O2yUjzK_MNNaF4de6GCQQl9ReUpN5rv9gk-LALCvYZslRLzUB8qt_41pVQ64zFGjTaIdbqCwhLaYoVQPkbhPBZIGRn7ubQOgBI-EpRv4Fj3L2-FBOjnlgT6cE_NzaDNDcw8BJbx91eA8ez7ObYEx-KaXd8Mwx3Ej3lJqnCjyp7iD4nVTC4f131jNzMlmwief3t91CoVVj6vUrqbifaTHoT3mhCtSsOmHuQBmtZOrWNjN2NcTmhfnIcfQ1yaRIYYYolVaTpEmHdYaNLyNawuezrriWmDYzPa3rFRsgm4RAd5dY_G9tlM= )
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
