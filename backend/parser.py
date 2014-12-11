import nltk
from nltk.corpus import stopwords
from nltk import stem
from nltk.tag import pos_tag


# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('maxent_treebank_pos_tagger')
# nltk.download('all-corpora')


def parse_request(sentence):
	tags = {}
	tokens = nltk.word_tokenize(sentence)
	snowball = stem.snowball.EnglishStemmer()
	tokens_list = [snowball.stem(x.lower()) for x in tokens if x not in stopwords.words('english') and len(x) > 1]
	# organization_list = getPartner(sentence)

	dimension_list = getDimension(sentence)
	tags['dimension'] = dimension_list
	for item in dimension_list:
		tokens_list.remove(item)
	tags['metric']=tokens_list
	print tags
	return tags


def getPartner(text):
	organization_list = []
	for sent in nltk.sent_tokenize(text):
		for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
			if hasattr(chunk, 'node'):
				if chunk.node == "ORGANIZATION":
					organization = ' '.join(c[0] for c in chunk.leaves())
					organization_list.append(organization)
	print organization_list


def getDimension(text):
	date_list = []
	for sent in nltk.sent_tokenize(text):
		for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
			print chunk
			if hasattr(chunk, 'node'):
				if chunk.node == "DATE":
					date = ' '.join(c[0] for c in chunk.leaves())
					date_list.append(date)
	return date_list

text = "what is the Minerva minutes of yesterday"
parse_request(text)


