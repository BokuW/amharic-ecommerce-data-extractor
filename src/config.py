# src/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Project Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# Ensure directories exist
os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

# --- Telegram API Credentials ---
# Get these from my.telegram.org after logging in with your phone number.
# NEVER commit them to GitHub!
# They should be set in your .env file like:
# TELEGRAM_API_ID=1234567
# TELEGRAM_API_HASH=your_api_hash_string_here
TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')

# --- Telegram Channels to Scrape ---
# You need to identify at least 5 Telegram e-commerce channel usernames or IDs.
# Example: 'shageronlinestore' (username) or -100123456789 (channel ID)
# You can find usernames in the channel's info, or convert public links.
# For private channels, you'll need their numerical ID.
TELEGRAM_CHANNELS = [
    '@nevacomputer',
    '@marakibrand',
    '@Fashiontera',
    '@Shewabrand',
    '@ethio_brand_collection',
]

# --- Output File Names ---
RAW_MESSAGES_JSON = os.path.join(RAW_DATA_DIR, 'raw_telegram_messages.json')
CLEAN_MESSAGES_CSV = os.path.join(PROCESSED_DATA_DIR, 'clean_telegram_messages.csv')
IMAGE_DOWNLOAD_DIR = os.path.join(RAW_DATA_DIR, 'images') # Directory to save downloaded images

os.makedirs(IMAGE_DOWNLOAD_DIR, exist_ok=True) # Ensure image directory exists

print(f"Project configuration loaded. Data directories created/verified.")
print(f"Telegram Channels configured: {TELEGRAM_CHANNELS}")
