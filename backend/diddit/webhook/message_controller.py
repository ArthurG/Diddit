import message_handler
import message_sender
import feedparse_controller
from keys import NEWSBOT_WEBSITE

#Routes the messaging event to the correct handler to handle the message
def route(messaging_event):
    if not messaging_event:  # someone sent us a message
        return

    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    #message_text = messaging_event["message"]["text"]  # the message's text

    if message_handler.want_another_article(messaging_event['message']):
        get_next_message(messaging_event['message'], sender_id)
    elif message_handler.want_full_article(messaging_event['message']):
        get_full_article(messaging_event['message'], sender_id)
    elif message_handler.want_article(messaging_event['message']):
        get_article(messaging_event['message'], sender_id)
    else:
        get_introduction(messaging_event['message'], sender_id)

    if messaging_event.get("delivery"):  # delivery confirmation
        pass

    if messaging_event.get("optin"):  # optin confirmation
        pass

    if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
        pass


#Controller to handle default messages
def get_article(message, sender_id):
    articleText, articleIndex = feedparse_controller.getOneArticle()
    if (not articleText):
        return message_sender.text_message(sender_id, "I've run out of articles :(")
    message_sender.news_article(sender_id, articleText, articleIndex)

#Handles request to get the next news article
def get_next_message(message, sender_id):
    articleIndex = message_handler.get_curr_article_id(message) + 1
    articleText, articleIndex = feedparse_controller.getOneArticle(entryNumber=articleIndex)
    if (not articleText):
        return message_sender.text_message(sender_id, "I've run out of articles :(")
    message_sender.news_article(sender_id, articleText, articleIndex)

#HAndles request to get the full news article
def get_full_article(message, sender_id):
    articleIndex = message_handler.get_curr_article_id(message)
    articleText, articleIndex = feedparse_controller.getFullArticle(entryNumber=articleIndex)
    if (not articleText):
        return message_sender.text_message(sender_id, "I've run out of articles :(")
    message_sender.news_url(sender_id, articleText, articleIndex)

def get_introduction(message, sender_id):
    message = "Hello, I am News Bot. I can send you news articles on topics that are relavant to you. Please configure your settings at {}/settings/{}. Or request a new article by typing in 'new'".format(NEWSBOT_WEBSITE,sender_id)
    message_sender.text_message(sender_id, message)

