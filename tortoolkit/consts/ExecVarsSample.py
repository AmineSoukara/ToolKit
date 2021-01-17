try:
    from .ExecVars import ExecVars
except:
    class ExecVars:
        # TODO optimize for vps use fully - currently only heroku is focused
        # Set true if its VPS [currently not fully working]
        IS_VPS = False
        API_HASH = "11d05c637abdb46e35f51bc73241c75c"
        API_ID = 1250763
        BOT_TOKEN = "1523666805:AAFtDwzSBdHe88aOBsntwsUBxRyrv5GxVug"
        BASE_URL_OF_BOT = "https://toolkit1717.herokuapp.com"
        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [853393439,1453680819,-1001375553926]
        
        # Time to wait before edit message
        EDIT_SLEEP_SECS = 10

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 1900000000

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = False

        # Chracter to use as a completed progress 
        COMPLETED_STR = "■"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "□"

        # DB URI for access
        DB_URI = "postgres://hmyekuffsptavt:de7eec1c2ca584018f0b1c999b942844325da773b2aa10c5649f16c938ffcc5d@ec2-54-157-12-250.compute-1.amazonaws.com:5432/dd8eq05771296g"

        # The base direcory to which the files will be upload if using RCLONE
        RCLONE_BASE_DIR = "/"

        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = False

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = False
        
        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = ""

        # Max size of a playlist that is allowed (Number of videos)
        MAX_YTPLAYLIST_SIZE = 200
        
        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 100

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50,10,2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = False
        





