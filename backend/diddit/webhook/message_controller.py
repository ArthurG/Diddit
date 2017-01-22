from . import message_handler
from . import message_sender
from . import feedparse_controller
from .dist import dist
from ..models import Survey, Surveyquestionanswer, Usersurveystates
from database import db
import random
import datetime

#Routes the messaging event to the correct handler to handle the message
def route(messaging_event):
    
    if not messaging_event:  # someone sent us a message
        return

    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    #message_text = messaging_event["message"]["text"]  # the message's text

    if get_location(messaging_event['message']) and is_not_in_survey(sender_id) and should_get_new_survey(messaging_event['message'], sender_id):
        start_survey(messaging_event['message'], sender_id)
    elif get_location(messaging_event['message']) and is_not_in_survey(sender_id):
        already_completed_survey(sender_id)
    elif did_answer_question(messaging_event['message'], sender_id):
        process_answer(messaging_event['message'], sender_id)
        send_next_question(sender_id)
    else:
        send_introduction(sender_id)

    if messaging_event.get("delivery"):  # delivery confirmation
        pass

    if messaging_event.get("optin"):  # optin confirmation
        pass

    if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
        pass


def is_not_in_survey(sender_id):
    return Usersurveystates.query.filter_by(respondantFbId=sender_id).filter_by(questionState=0).first() == None


def send_introduction(sender_id):
    msg = "Hello! I am Diddit. I send you surveys that you can fill out for an easy discount at your current store! Send me your current location to start :)"
    message_sender.text_request_location(sender_id, msg)


#Check if msg recieved contains location data about user
def get_location(msg):
    if msg.get('attachments', False) and msg['attachments'][0]['type'] == "location":
        return msg['attachments'][0]['payload']['coordinates']
        #returns {'lat': xxx, 'long': xxx}
    return False

def already_completed_survey(sender_id):
    message = "Sorry, you already completed this survey"
    message_sender.text_message(sender_id, message)
    print("already completed")

def start_survey(msg, sender):
    loc = get_location(msg)
    allSurveys = Survey.query.all()
    allSurveys = [i for i in allSurveys if dist(loc['long'], loc['lat'], i.user.lng, i.user.lat) <= 0.5]
    if len(allSurveys) == 0:
        message_sender.text_message(sender, "I do not have a survey for you at the moment. Please make sure you're within distance of a participating location")
    else:
        storename = allSurveys[0].user.store_name
        message = "You are now filling out the survey for '{}'".format(storename)
        message_sender.text_message(sender, message)
        start_questioning(sender, allSurveys[0])
    print("starting survey")

def should_get_new_survey(msg, sender):
    loc = get_location(msg)
    allSurveys = Survey.query.all()
    allSurveys = [i for i in allSurveys if dist(loc['long'], loc['lat'], i.user.lng, i.user.lat) <= 0.5]
    if len(allSurveys) == 0:
        return False
    survey = allSurveys[0]
    question0=survey.questions[0]
    surveyState = Usersurveystates.query.filter_by(respondantFbId=sender).filter_by(questionState=2).filter_by(questionId=question0.id).first()
    return surveyState == None

def start_questioning(sender, survey):
    db.create_all()
    for question in survey.questions:
        tmpState = Usersurveystates(question.id, survey.id, sender)
        db.session.add(tmpState)
    db.session.commit()
    send_next_question(sender)
    print("Starting questioning")


def process_answer(msg, sender):
    q1 = Usersurveystates.query.filter_by(respondantFbId=sender).filter_by(questionState=1).first()
    q1.questionState=2
    question_answered = q1.surveyquestion
    resp = Surveyquestionanswer(msg['text'], question_answered.id)
    db.session.add(resp)
    db.session.commit()
    print("Processing answer")


def send_next_question(sender):
    q1 = Usersurveystates.query.filter_by(respondantFbId=sender).filter_by(questionState=0).first()
    if q1 == None:
        #it might be because the person finished filling out all the surveys
        q1 = Usersurveystates.query.filter_by(respondantFbId=sender).filter_by(questionState=2).first()
        if q1 != None:
            message_sender.text_message(sender, "Thanks for filling out our survey")
            message_sender.text_message(sender, "Here is your QR code for your discount!")
            now = datetime.datetime.now()
            random.seed(now.microsecond)
            QR = random.randint(0,10000)
            message_sender.send_photo(sender, "https://chart.googleapis.com/chart?cht=qr&chl=" + str(QR) + "&chs=250x250&choe=UTF-8&chld=L|2")
            print("sending closing remarks")
        else:
            print("sending no remarks")
    else:
        q1.questionState = 1
        db.session.commit()
        message_sender.text_message(sender, q1.surveyquestion.questionName)
        print("sending next question")


def did_answer_question(msg, sender):
    q1 = Usersurveystates.query.filter_by(respondantFbId=sender).filter_by(questionState=1).first()
    txt = msg.get('text', False)
    print("did answer question", q1, txt)
    return q1 and txt

    #q1.questionState = 1
    #db.session.commit()
    #message_sender.text_message(sender, q1.surveyquestion.questionName)
    print("Answering question")

        

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

