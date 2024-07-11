import os
from dotenv import load_dotenv

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
SLACK_CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")
PITCHBOOK_API_TOKEN = os.getenv("PITCHBOOK_API_TOKEN")
PITCHBOOK_API_BASE_URL = "https://api.pitchbook.com"
PITCHBOOK_API_V2_BASE_URL = "https://api-v2.pitchbook.com"