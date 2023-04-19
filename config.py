# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "14013342"))
API_HASH = os.environ.get("API_HASH", "c3e1d740fd207c7ae1b373a7546e8a62")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5732008293:AAGd7rrqZg6SUOp6ukoYDxCAn1bxIARkuuU")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1128389435")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://akshatsg:6MsVrQc7U6jMyl3F@cluster0.hqrmv5v.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1128389435")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1128389435)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001926772801")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Linkeasy_in") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://telegra.ph/file/68feb51ce9c55c31d3265.png') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
