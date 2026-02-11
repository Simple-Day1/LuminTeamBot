import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
PROGRESS_IMAGE = os.path.join(ASSETS_DIR, "progress.jpg")
GALLERY_DIR = os.path.join(ASSETS_DIR, "gallery")
BACKSTAGE_DIR = os.path.join(ASSETS_DIR, "backstage")
