import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "6151017").strip()
API_HASH = os.getenv("API_HASH", "5d125071b09e07b14a7837a2de4c6dad").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "7445547849:AAHfX4_8TQ57cg71Q_l9ABoa6RfgfPWHgsE").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://admin:admin123@cluster0.025ahvi.mongodb.net/").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "movies0x2")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if "postgres" in DATABASE_URL and "postgresql" not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
