from app.slack_bot import app
from slack_bolt.adapter.socket_mode import SocketModeHandler # type: ignore
from app.config import SLACK_APP_TOKEN
from app.logger import logger

if __name__ == "__main__":
    logger.info("Starting Slack bot application")
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()