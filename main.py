import json
from pprint import pprint

from flask import Flask, request
from linebot.v3.webhook import WebhookHandler
import pymysql

from config.line_bot_setting import CHANNEL_SECRET, CHANNEL_ACCESS_TOKEN, BASE_URL
from config.mysql_setting import MYSQL_HOST, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_PORT, DB_NAME
from event_handler import EventHandler

webhook_handler = WebhookHandler(CHANNEL_SECRET)

app = Flask(__name__)
connection = pymysql.connect(
    host=MYSQL_HOST,
    user=MYSQL_USERNAME,
    password=MYSQL_PASSWORD,
    port=MYSQL_PORT,
    db=DB_NAME
)


@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    data = request.get_data(as_text=True)
    webhook_handler.handle(data, signature)

    json_data = json.loads(data)
    pprint(json_data)

    if json_data['events']:
        event = json_data['events'][0]

        event_handler = EventHandler(event, CHANNEL_ACCESS_TOKEN, BASE_URL, connection)
        event_handler.handle()
    else:
        print('webhook 驗證成功')

    return 'OK'


if __name__ == '__main__':
    app.run()

