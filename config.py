from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "19702484"))
API_HASH = getenv("API_HASH", "
2324cd516acaec234383c5297ca961a2")
BOT_TOKEN = getenv("BOT_TOKEN", "5768486577:AAGEnZhkEytuYEaBQiz_HcVqCE3K4Mdu5bo")
BOT_NAME = getenv("BOT_NAME","HUNTERX MUSIC")
BOT_USERNAME = getenv("BOT_USERNAME", "THE_HUNTERX_MUSIC_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "PAPA_HUNTERX")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "UNK_SUPPORT")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "UNK_BOTS")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/cb2763a4fd9af49b26cb0.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/262e434f76a5f2e414178.jpg")
SESSION_NAME = getenv("SESSION_NAME", "AgCRdLnn7BPEswzsn5Nw3CJZ0LDDVfIB90jMAVU5pxAXvkRDprD3cGhfTwtegWtlCvDyL5NOi-UkPJTMFlwNukwN_8Qm41NzkTBqd7ZA9GZtL_1xdv03QtuXsNQcrXS8T1Ej5Egek8a4Z7_dw37EHnSjUnMVPIaWaAw7wudSevaE5H8Ig-3YV2bII0Dab4ejaTNAUfGvUWpo3MeNhCUiIJo554JG-ISjLTc5Q4f0iYnMx9-gLwaOUSit7_OsMvJB6gaH9DgKFYv-3GzoIcbMr3qTUY88TS3nMHCzgBSMaEGiYrizBuLTOrggveYIOm3QnEcnmasnmE_IBnjo6g6DfdO8AAAAATBv1kUA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")"
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1211015395").split()))
