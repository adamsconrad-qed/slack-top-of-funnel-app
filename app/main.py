from app.slack_bot import app
from slack_bolt.adapter.socket_mode import SocketModeHandler
from app.config import SLACK_APP_TOKEN

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()