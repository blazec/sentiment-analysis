# Run in python 2.7

import sys
import re
import itertools

# tag name: example
# CC Coordinating conjunction: and
# CD Cardinal number: three
# DT Determiner: the
# EX Existential there: there [is]
# FW Foreign word: d'oeuvre
# IN Preposition or subordinating conjunction: in, of, like
# JJ Adjective: green, good
# JJR Adjective, comparative: greener, better
# JJS Adjective, superlative: greenest, best
# LS List item marker: (1)
# MD Modal: could, will
# NN Noun, singular or mass: table
# NNS Noun, plural: tables
# NNP Proper noun, singular John
# NNPS Proper noun, plural: Vikings
# PDT Predeterminer: both [the boys]
# POS Possessive ending: 's, '
# PRP Personal pronoun: I, he, it
# PRP$ Possessive pronoun: my, his, its
# RB Adverb: however, usually, naturally, here, good
# RBR Adverb, comparative: better
# RBS Adverb, superlative: best
# RP Particle: [give] up
# SYM Symbol (mathematical or scientific): +
# TO to: to [go] to [him]
# UH Interjection: uh-huh
# VB Verb, base form: take
# VBD Verb, past tense: took
# VBG Verb, gerund or present participle: taking
# VBN Verb, past participle: taken
# VBP Verb, non-3rd-person singular present: take
# VBZ Verb, 3rd-person singular present: takes
# WDT wh-determiner: which
# WP wh-pronoun: who, what
# WP$ Possessive: wh-pronoun whose
# WRB: wh-adverb 
non_punctuation_tags = [r'\/CC', r'\/CD', r'\/DT', r'\/EX', r'\/FW', r'\/IN', r'\/JJR', r'\/JJS', r'\/JJ', 
						r'\/LS', r'\/MD', r'\/NNPS', r'\/NNS', r'\/NNP', r'\/NN', r'\/PDT', r'\/POS', r'\/PRP\$', 
						r'\/PRP', r'\/RBR', r'\/RBS', r'\/RB', r'\/RP', r'\/SYM', r'\/TO', r'\/UH', r'\/VBD',
						r'\/VBG', r'\/VBN', r'\/VBP', r'\/VBZ', r'\/VB', r'\/WDT', r'\/WP\$', r'\/WP', r'\/WRB' ]

punctuation_tags = [r'\/#', r'\/$', r'\/\.', r'\/,', r'\/:', r'\/(', r'\/)', r'\/"', r"\/'", ]

with open('First-person') as f:
	first_person_pronouns = filter(None, [p.rstrip() for p in f.readlines()])
	first_regex = '|'.join([p + '/PRP' for p in first_person_pronouns]) + '|' + '|'.join([p + '/PRP$' for p in first_person_pronouns])

with open('Second-person') as f:
	second_person_pronouns = filter(None, [p.rstrip() for p in f.readlines()])
	second_regex = '|'.join([p + '/PRP' for p in second_person_pronouns]) + '|' + '|'.join([p + '/PRP$' for p in second_person_pronouns])

with open('Third-person') as f:
	third_person_pronouns = filter(None, [p.rstrip() for p in f.readlines()])
	third_regex = '|'.join([p + '/PRP' for p in third_person_pronouns]) + '|' + '|'.join([p + '/PRP$' for p in third_person_pronouns])

with open('Slang') as f:
	slangs = filter(None, [s.rstrip() for s in f.readlines()])
	slang_regex = '\s' + '(' + '|'.join(slangs) + ')' + r'/'

# non_punctuation_regex = '|'.join(non_punctuation_tags)
non_punctuation_regex = '|'.join(['[A-Za-z]*' + npt for npt in non_punctuation_tags])
all_tokens_regex = '|'.join(non_punctuation_tags + punctuation_tags)

# future tense regexes
ll_regex = r"'/POS ll/"
will_regex = r'will/MD [a-zA-z0-9]*/VB|will/MD [a-zA-z0-9]*/VBP'
gonna_regex = 'gonna/VBG'
going_to_regex = 'going/VBG to/TO'
future_regex = '|'.join([ll_regex, will_regex, gonna_regex, going_to_regex])


def get_polarity(polarity_tag):
	''' Returns polarity of tagged_tweet. polarity_tag format: <A=4>'''
	return int(re.search('[0-4]', polarity_tag).group())
	

def feat1(tagged_tweet):
	''' Returns count of first-person pronouns in tagged_tweet'''
	return len(re.findall(first_regex, tagged_tweet, re.IGNORECASE))

def feat2(tagged_tweet):
	''' Returns count of second-person pronouns in tagged_tweet'''
	return len(re.findall(second_regex, tagged_tweet, re.IGNORECASE))

def feat3(tagged_tweet):
	''' Returns count of third-person pronouns in tagged_tweet'''
	return len(re.findall(third_regex, tagged_tweet, re.IGNORECASE))

def feat4(tagged_tweet):
	''' Returns count of coordinating conjunctions in tagged_tweet'''
	# tag = 'CC'
	return len(re.findall(r'\/CC', tagged_tweet))

def feat5(tagged_tweet):
	''' Returns count of past tense verbs in tagged_tweet'''
	# tag: 'VBD'
	return len(re.findall(r'\/VBD', tagged_tweet))

def feat6(tagged_tweet):
	''' Returns count of future tense verbs in tagged_tweet'''
	return len(re.findall(future_regex, tagged_tweet, re.IGNORECASE))

def feat7(tagged_tweet):
	''' Returns count of commas in tagged_tweet'''
	return len(re.findall(r'/,', tagged_tweet))

def feat8(tagged_tweet):
	''' Returns count of colons and semicolons in tagged_tweet'''
	return len(re.findall(r':/:|;/:', tagged_tweet))

def feat9(tagged_tweet):
	''' Returns count of dashes in tagged_tweet'''
	return len(re.findall(r'-', tagged_tweet))

def feat10(tagged_tweet):
	''' Returns count of parentheses in tagged_tweet'''
	return len(re.findall(r'\/\(.*\/\)', tagged_tweet))

def feat11(tagged_tweet):
	''' Returns count of ellipses in tagged_tweet'''
	return len(re.findall(r'[\.]{2,}', tagged_tweet))

def feat12(tagged_tweet):
	''' Returns count of common nouns in tagged_tweet'''
	# tags = 'NN', 'NNS'
	return len(re.findall(r'\/NN|\/NNS', tagged_tweet))

def feat13(tagged_tweet):
	''' Returns count of proper nouns in tagged_tweet'''
	# tags = 'NNP', 'NNPS'
	return len(re.findall(r'\/NNP|\/NNPS', tagged_tweet))

def feat14(tagged_tweet):
	''' Returns count of adverbs in tagged_tweet'''
	# tags = 'RB', 'RBR', 'RBS'
	return len(re.findall(r'\/RB|\/RBR|\/RBS', tagged_tweet))

def feat15(tagged_tweet):
	''' Returns count of wh-words in tagged_tweet'''
	# tags = 'WDT', 'WP', 'WP$', 'WRB'
	return len(re.findall(r'\/WRB|\/WP|\/WP\$|\/WDT', tagged_tweet))

def feat16(tagged_tweet):
	''' Returns count of modern slang acronyms in tagged_tweet'''
	return len(re.findall(slang_regex, tagged_tweet, re.IGNORECASE))

def feat17(tagged_tweet):
	''' Returns count of uppercase words at least 2 letters long in tagged_tweet'''
	return len(re.findall(r'\s[A-Z]{2,}[/]|^[A-Z]{2,}[/]', tagged_tweet))

def feat18(tagged_tweet):
	''' Returns average length of sentences in tagged_tweet'''
	tweet_split = filter(None, re.split(r'\n', tagged_tweet))
	if len(tweet_split) > 0:
		return float(sum(map(lambda sentence: len(re.findall(all_tokens_regex, sentence)), tweet_split))) / float(len(tweet_split)) 
	return 0

def feat19(tagged_tweet):
	''' Returns average length of non-punctuation tokens in tagged_tweet'''
	# Commented out old code for reference
	# token_split = filter(lambda token: token and not token.isspace(), re.split(non_punctuation_regex, tagged_tweet))
	# token_split = filter(lambda token: token and not token.isspace(), re.split(non_punctuation_regex, tagged_tweet))
	# return float(sum(map(lambda token: len(''.join(token.split())), token_split))) / float(len(token_split))
	tokens = re.findall(non_punctuation_regex, d)
	lengths = map(lambda token: len(token) - len(re.search('/[A-Z]*', token).group() if re.search('/[A-Z]*', token) else len(token)), tokens)
	if len(tokens) > 0:
		return float(sum(lengths)) / float(len(tokens))
	return 0

def feat20(tagged_tweet):
	''' Returns number of sentences in tagged_tweet'''
	# print re.findall(r'\n', tagged_tweet)
	if not tagged_tweet.isspace():
		return len(filter(None, re.findall(r'\n', tagged_tweet)))
	return 0

def write_data(tagged_tweet, polarity, arff_file):

	try:
		f1 = feat1(tagged_tweet)
	except Exception:
		print 'Error feat1'
		f1 = 0

	try:
		f2 = feat2(tagged_tweet)
	except Exception:
		print 'Error feat2'
		f2 = 0

	try:
		f3 = feat3(tagged_tweet)
	except Exception:
		print 'Error feat3'
		f3 = 0

	try:
		f4 = feat4(tagged_tweet)
	except Exception:
		print 'Error feat4'
		f4 = 0

	try:
		f5 = feat5(tagged_tweet)
	except Exception:
		print 'Error feat5'
		f5 = 0

	try:
		f6 = feat6(tagged_tweet)
	except Exception:
		print 'Error feat6'
		f6 = 0

	try:
		f7 = feat7(tagged_tweet)
	except Exception:
		print 'Error feat7'
		f7 = 0

	try:
		f8 = feat8(tagged_tweet)
	except Exception:
		print 'Error feat8'
		f8 = 0

	try:
		f9 = feat9(tagged_tweet)
	except Exception:
		print 'Error feat9'
		f9 = 0

	try:
		f10 = feat10(tagged_tweet)
	except Exception:
		print 'Error feat10'
		f10 = 0

	try:
		f11 = feat11(tagged_tweet)
	except Exception:
		print 'Error feat11'
		f11 = 0

	try:
		f12 = feat12(tagged_tweet)
	except Exception:
		print 'Error feat12'
		f12 = 0

	try:
		f13 = feat13(tagged_tweet)
	except Exception:
		print 'Error feat13'
		f13 = 0

	try:
		f14 = feat14(tagged_tweet)
	except Exception:
		print 'Error feat14'
		f14 = 0

	try:
		f15 = feat15(tagged_tweet)
	except Exception:
		print 'Error feat15'
		f15 = 0

	try:
		f16 = feat16(tagged_tweet)
	except Exception:
		print 'Error feat16'
		f16 = 0

	try:
		f17 = feat17(tagged_tweet)
	except Exception:
		print 'Error feat17'
		f17 = 0

	try:
		f18 = feat18(tagged_tweet)
	except Exception:
		print 'Error feat18'
		f18 = 0

	try:
		f19 = feat19(tagged_tweet)
	except Exception:
		print 'Error feat19'
		f19 = 0

	try:
		f20 = feat20(tagged_tweet)
	except Exception:
		print 'Error feat20'
		f20 = 0

	arff_file.write('\n' + ','.join(map(lambda feat: str(feat), [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10,
								f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, polarity])))


def write_header(f):
	attributes = ['countfirstpersonpronouns',
					'countsecondpersonpronouns',
					'countthirdpersonpronouns',
					'countcoordinatingconjunctions',
					'countpasttenseverbs',
					'countfuturetenseverbs',
					'countcommas',
					'countcolonssemicolons',
					'countdashes',
					'countparentheses',
					'countellipses',
					'countcommonnouns',
					'countpropernouns',
					'countadverbs',
					'countwhwords',
					'countslangacronyms',
					'countuppercase',
					'averagelengthsentences',
					'averagelengthtokens',
					'numbersentences']
	f.write('% 1. Title: Tweets Sentiment Analysis\n')
	f.write('@RELATION tweetfeatures\n\n')

	for attr in attributes:
		f.write('@ATTRIBUTE ' + attr + ' NUMERIC\n')
	f.write('@ATTRIBUTE class {0,4}\n\n')

def write_data_title(f):
	f.write('@DATA')

# Test function
def write_f(num, tagged_tweet, output):
	f = [feat1, feat2, feat3, feat4, feat5, feat6, feat7, feat8, feat9, feat10,
		feat11, feat12, feat13, feat14, feat15, feat16, feat17, feat18, feat19, feat20,]

	output.write(str(f[num-1](tagged_tweet)) + '\n')

if __name__ == '__main__':

	input_file = sys.argv[1]
	output_file = sys.argv[2]

	r = re.compile(r'(<A=[0-4]>\n)')
	with open(input_file) as inpt:
		# inpt looks like:
		# <A=0>\n
		# stellargirl/NN I/PRP loooooooovvvvvveee/NN\n
		# <A=1>\n

		data = filter(None, r.split(inpt.read()))
		with open(output_file, 'w') as output:
			write_header(output)
			write_data_title(output)
			for d in data:
				if r.search(d):
					polarity = get_polarity(d) # current polarity
				else:						
					# Commented out testing code
					# output.write('Tweet ' + str(i) + '\n')
					# output.write(d)
					# write_f(11, d, output)
					# output.write('\n')
					write_data(d, polarity, output)
