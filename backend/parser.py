import nltk
nltk.download('punkt')

def parse_request(sentence):
	try:
		tokens = nltk.word_tokenize(sentence)
		print "NLTK Parsing sentence..."
	except:
		print "There was an error when NLTK parsing!"
	return tokens