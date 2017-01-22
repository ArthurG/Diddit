import json
import sys
import requests
from .keys import ACCESS_TOKEN

def log(message):  # simple wrapper for logging to stdout on heroku
    print(str(message))
    sys.stdout.flush()

def text_message(recipient, message):
    data = json.dumps({
        "recipient": {
            "id": recipient
            },
        "message": {

            "text": message,

            }
        })
    send_message(data)

def text_request_location(recipient, message):
    data = json.dumps({
        "recipient": {
            "id": recipient
            },
        "message": {

            "text": message,
            "quick_replies" : [
                {
                    "content_type" :"location"   
                }    
            ]

            }
        })
    send_message(data)


def news_article(recipient, article, article_num):
    for line in article.split("\n"):
        data = json.dumps({
            "recipient": {
                "id": recipient
                },
            "message": {

                "text": line,
                "quick_replies":[
                    {
                        "content_type":"text",
                        "title":"Interesting! :D",
                        "payload":"NEXT_ARTICLE_CURRENT_EQ_{}".format(article_num),
                        "image_url":"https://cdn0.iconfinder.com/data/icons/vector-basic-tab-bar-icons/48/forward_button-512.png"
                        },
                    {
                        "content_type":"text",
                        "title":"Boring :(",
                        "payload":"NEXT_ARTICLE_CURRENT_EQ_{}".format(article_num),
                        "image_url":"https://cdn0.iconfinder.com/data/icons/vector-basic-tab-bar-icons/48/forward_button-512.png"
                        },
                    {
                        "content_type":"text",
                        "title":"Full Article",
                        "payload":"FULL_ARTICLE_CURRENT_EQ_{}".format(article_num),
                        "image_url":"http://www.freeiconspng.com/uploads/book-icon-black-good-galleries--24.jpg"
                        }
                    ]
                }
            })
        send_message(data)

def news_url(recipient, url, article_num):
    for line in url.split("\n"):
        data = json.dumps({
            "recipient": {
                "id": recipient
                },
            "message": {

                "text": line,
                "quick_replies":[
                    {
                        "content_type":"text",
                        "title":"Interesting! :D",
                        "payload":"NEXT_ARTICLE_CURRENT_EQ_{}".format(article_num),
                        "image_url":"https://cdn0.iconfinder.com/data/icons/vector-basic-tab-bar-icons/48/forward_button-512.png"
                        },
                    {
                        "content_type":"text",
                        "title":"Boring :(",
                        "payload":"NEXT_ARTICLE_CURRENT_EQ_{}".format(article_num),
                        "image_url":"https://cdn0.iconfinder.com/data/icons/vector-basic-tab-bar-icons/48/forward_button-512.png"
                        },
                    ]
                }
            })
        send_message(data)


def send_photo(recipient, url):
    data = json.dumps({
        "recipient": {
            "id": recipient
            },
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": url,
                }
            }
        }
    })
    send_message(data)


def send_message(data):
    params = {
            "access_token": ACCESS_TOKEN
             }
    headers = {
            "Content-Type": "application/json"
            }
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


