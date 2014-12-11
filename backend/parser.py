#import nltk

def parse_request(sentence):
    try:
        parsed = sentence.split(" ")
        print "Parsing sentence..."
        print parsed
    except:
        print "There was an error when parsing!"
    return parsed
