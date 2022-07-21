################ Email Alerts settings ################
EMAIL_ALERTS_ENABLED = True
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_SEC_PROTOCOL = 'tls' # valid values: tls, ssl, none

SMTP_REQUIRE_AUTH = True
SMTP_USERNAME = "kevin.tarus@strathmore.edu"
SMTP_PASSWORD = "#m!f4m!l!4#"


FROM = "kevin.tarus@strathmore.edu"
FROM_NAME = "File Monitor System"
TO = "kevin.tarus@strathmore.edu"

################ General settings ################
WATCH_LIST_FILE_PATH = 'watch_list.txt'  # files and directories path list to be watched
DEBUG_LOG_ENABLED = True
DEBUG_LOG_FILE_PATH = 'debug.log'
FILE_RENAME_LOG_FILE_PATH = 'file_rename.log'
FILE_CREATION_LOG_FILE_PATH = 'file_creation.log'
FILE_CHANGE_LOG_FILE_PATH = 'file_change.log'
FILE_DELETION_LOG_FILE_PATH = 'file_delete.log'
