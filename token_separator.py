import re

punctuations = [r'\.', r'\!', r'\?', r'\!', r'\-', r'\/', r"\'", r'\<', r'\>', r'\,', r'\(', r'\)', r'\[', r'\]', r'\:', r'\;', r'\"']

clitics = [r"\'s", r"\'re", r"\'m", r"\'s", r"\'ve", r"\'d", r"\'l"]
clitics_no_space = ['[^\s]' + c for c in clitics]

# Regular expressions useful in separate_clitics(s)
regex_clit_no_space = '|'.join(clitics_no_space)
regex_clit = '|'.join(clitics)

# Regular expressions useful in separate_punctuations(s)
regex_punc = '[' + ''.join(punctuations) + ']'
regex_punc_repeat_no_space = '[^\s][' + ''.join(punctuations) + ']' + '{1,}'

r_clitics = re.compile(regex_clit_no_space)
r2_clitics = re.compile(regex_clit)

r_punc = re.compile(r'(\"[^\s]|\'[^\s]|' + regex_punc_repeat_no_space + ')')
r2_punc = re.compile(regex_punc)

def get_tokens(s):
	s = separate_clitics(s)
	s = separate_punctuations(s)
	return s
		
def separate_clitics(s):
	match = r_clitics.search(s)

	while match:
		clit = match.group()
		match2 = r2_clitics.search(clit)
		if match2:
			clit2 = match2.group()
			s = s.replace(clit2, ' ' + clit2 + ' ')
		match = r_clitics.search(s)

	return s

def separate_punctuations(s):
	tokens = r_punc.split(s)

	# At this point tokens looks something like this ['', "This tweet is the best twee", "t!!", '']
	# Have to format even further
	# Add space before and after punctuation, except if punctuation is the beggining quote " or '
	tokens = map(lambda token: token[0] + ' ' + token[1:] + ' ' if len(token) > 0 and r_punc.search(token) and not r2_punc.search(token[0]) else \
		token[0] + " " + token[1:] if token.startswith('"') or token.startswith("'") else token, tokens)

	#print re.sub('', re.sub(r' +', ' ', ''.join(tokens)))
	return re.sub(r' +', ' ', ''.join(tokens))

if __name__ == '__main__':
	sentences = ["This           tweet's the best tweet!! Everybody says so..!??.!?!!.. I'm bury you. SAD",
				'.......... .......... .......... ....... aaaaa',
				'Today is a non-trash day.    haya',
				'Are YOU burning more cash $$$ than Chrysler and GM? Stop the financial tsunami. Where "bailout" means taking a handout!']
	for s in sentences:
		print separate_punctuations(sentence_separator.get_sentences(s))
