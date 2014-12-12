import nltk
from nltk.corpus import stopwords
from nltk import stem
import re

nltk.download('stopwords')

def parse_request(sentence):
	tokens = nltk.word_tokenize(sentence)
	email_list = []
	for i in range(len(tokens)):
		try:
			if tokens[i] == '@':
				try:
					email_list.append(tokens[i-1] + '@' + tokens[i+1])
					tokens.remove(tokens[i-1])
					tokens.remove('@')
					tokens.remove(tokens[i-1])
				except:
					pass
		except IndexError:
			pass

	snowball = stem.snowball.EnglishStemmer()
	tokens_list = [snowball.stem(x.lower()) for x in tokens if x not in stopwords.words('english') and len(x) > 1]
	# organization_list = getPartner(sentence)
	dimension_list = getDimension(tokens_list)
	for item in dimension_list:
		tokens_list.remove(item)
	result_ls = []
	for item in dimension_list:
		tmp_dict = {}
		tmp_dict["dimension"] = str(item)
		result_ls.append(tmp_dict)
	for item in tokens_list:
		tmp_dict = {}
		tmp_dict["measure"] = str(item)
		result_ls.append(tmp_dict)
	for item in email_list:
		tmp_dict = {}
		tmp_dict["measure"] = str(item)
		result_ls.append(tmp_dict)
	return result_ls



def getDimension(tags):
	dimension_list = []
	single_daytime = "januari|februari|march|april|may|june|juli|august|septemb|octob|novemb|decemb|yesterday|today"
	pair_daytime = "month|week|year|day"
	i = 0
	for i in range(len(tags)):
		match_single = re.search(single_daytime, tags[i])
		if match_single:
			dimension_list.append(tags[i])
		match_pair = re.search(pair_daytime, tags[i])
		if match_pair:
			dimension_list.append(tags[i])
			try:
				dimension_list.append(tags[i-1])
			except KeyError:
				pass
	return dimension_list
