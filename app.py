import os
import re
import time
from threading import Thread
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from revChatGPT.revChatGPT import Chatbot

ChatGPTConfig = {
    "Authorization": "<Your Bearer Token Here>",  # This is optional
    "session_token": os.environ.get('CHATGPT_SESSION_TOKEN')
}

app = App(token=os.environ.get("SLACK_BOT_TOKEN"),
          signing_secret=os.environ.get("SLACK_SIGNING_SECRET"))
chatbot = Chatbot(ChatGPTConfig, conversation_id=None)

# Listen for an event from the Events API
@app.event("app_mention")
def hoge(event, say):
    print('hoge')
    print(event['text'])
    say("hoge")



# @app.event("app_mention")
# def event_test(event, say):
#     prompt = re.sub('(?:\s)<@[^, ]*|(?:^)<@[^, ]*', '', event['text'])
#     response = chatbot.get_chat_response(prompt)
#     user = event['user']
#     user = f"<@{user}> が発言します:"
#     asked = ['>', prompt]
#     asked = "".join(asked)
#     send = [user, asked, response["message"]]
#     send = "\n".join(send)
#     say(send)


def chatgpt_refresh():
    while True:
        chatbot.refresh_session()
        time.sleep(60)


if __name__ == "__main__":
    thread = Thread(target=chatgpt_refresh)
    thread.start()
    print('hoge')
    app.start(port=int(os.environ.get("PORT", 8080)))
