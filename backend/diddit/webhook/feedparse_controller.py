#import feedparser
#from newspaper import Article

def getOneArticle(feed="http://feeds.reuters.com/Reuters/worldNews", entryNumber=0):
    d = feedparser.parse(feed)
    if (len(d['entries']) <= entryNumber):
        return False, entryNumber

    url = d['entries'][entryNumber].link
    article = ""
    article.download()
    article.parse()
    article.nlp()
    return article.summary, entryNumber

def getFullArticle(feed="http://feeds.reuters.com/Reuters/worldNews", entryNumber=0):
    d = feedparser.parse(feed)
    if (len(d['entries']) <= entryNumber):
        return False, entryNumber

    url = d['entries'][entryNumber].link
    return url, entryNumber


def getSimilarity(article1, article2):
    #source: http://www.artfact-online.fr/blog/blog-post/6
    #use semantic clustering to check if the articles are about same event, return a higher score if they are
    return

def getWorthyScore(article1):
    #Determine how "worthy" a given article is
    #count how many news websites are talking about a related news item

    ...
    return
