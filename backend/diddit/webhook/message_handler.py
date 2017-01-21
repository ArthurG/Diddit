import re

def want_another_article(message):
    if not message.get('quick_reply') or not message['quick_reply'].get('payload'):
        return False
    return re.match("NEXT_ARTICLE_CURRENT_EQ_", message['quick_reply']['payload'])

def want_full_article(message):
    if not message.get('quick_reply') or not message['quick_reply'].get('payload'):
        return False
    return re.match("FULL_ARTICLE_CURRENT_EQ_", message['quick_reply']['payload'])

def want_article(message):
    return message.get('text') and message['text'] == "new"

def get_curr_article_id(message):
    match = re.search("CURRENT_EQ_\\d+", message['quick_reply']['payload'])
    return int(match.group().replace("CURRENT_EQ_", ""))



