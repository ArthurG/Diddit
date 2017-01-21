from flask import request
from . import webhook
import sys
from . import message_sender


@webhook.route('/webhook', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "WeDiddit":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200



@webhook.route('/webhook', methods=['POST'])
def processWebhook():

    # endpoint for processing incoming messaging events

    data = request.get_json()
    log("incoming msg " + str(data))  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                message_sender.text_message(messaging_event['sender']['id'], messaging_event['message']['text'])
                print(messaging_event['sender']['id'], messaging_event['message']['text'])
                #message_controller.route(messaging_event)
    return "ok", 200

def log(message):  # simple wrapper for logging to stdout on heroku
    print(str(message))
    sys.stdout.flush()
