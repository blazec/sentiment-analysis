# Run in python 2.7

import sys
import re

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

punctuation_tags = [r'\/#', r'\/$', r'\/\.', r'\/,', r'\/:', r'\/(', r'\/)', r'\/"', r"\/'", ]

with open('First-person') as f:
	first_person_pronouns = [p.rstrip() for p in f.readlines()]

with open('Second-person') as f:
	second_person_pronouns = [p.rstrip() for p in f.readlines()]

with open('Third-person') as f:
	third_person_pronouns = [p.rstrip() for p in f.readlines()]

with open('Slang') as f:
	slangs = [s.rstrip() for s in f.readlines()]
	slang_regex = '|'.join(slangs)


def get_polarity(polarity_tag):
	''' Returns polarity of tagged_tweet. polarity_tag format: <A=4>'''
	return int(re.search('[1-4]').group())

def get_tagged_tweet():
	return

def feat1(tagged_tweet):
	''' Returns count of first-person pronouns in tagged_tweet'''
	
	return 0

def feat2(tagged_tweet):
	''' Returns count of second-person pronouns in tagged_tweet'''
	return 0

def feat3(tagged_tweet):
		''' Returns count of third-person pronouns in tagged_tweet'''
	return 0

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
	return 0

def feat7(tagged_tweet):
	''' Returns count of commas in tagged_tweet'''
	return len(re.findall(r'\,', tagged_tweet))

def feat8(tagged_tweet):
	''' Returns count of colons and semicolons in tagged_tweet'''
	return len(re.findall(r'\:|\;', tagged_tweet))

def feat9(tagged_tweet):
	''' Returns count of dashes in tagged_tweet'''
	return len(re.findall(r'\-', tagged_tweet))

def feat10(tagged_tweet):
	''' Returns count of parentheses in tagged_tweet'''
	return len(re.findall(r'\/(|\/)', tagged_tweet))

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
	# tags = 'WRB', 'RB', 'RBR', 'RBS'
	return len(re.findall(r'\/WRB|\/RB|\/RBR|\/RBS', tagged_tweet))

def feat15(tagged_tweet):
	''' Returns count of wh-words in tagged_tweet'''
	# tags = 'WDT', 'WP', 'WP$', 'WRB'
	return len(re.findall(r'\/WRB|\/WP|\/WP\$|\/WDT', tagged_tweet))

def feat16(tagged_tweet):
	''' Returns count of modern slang acronyms in tagged_tweet'''
	return len(re.findall(slang_regex, tagged_tweet))

def feat17(tagged_tweet):
	''' Returns count of uppercase words in tagged_tweet'''
	return len(re.findall(r'[^\/][A-Z]{2,}', tagged_tweet))

def feat18(tagged_tweet):
	''' Returns average length of sentences in tagged_tweet'''
	return len(filter(None, re.split(r'\n', tagged_tweet)))

def feat19(tagged_tweet):
	''' Returns average length of non-pronunciation tokens in tagged_tweet'''
	return 0

def feat20(tagged_tweet):
	''' Returns number of sentences in tagged_tweet'''
	return 0

if __name__ == '__main__':
	# print first_person_pronouns
	# print second_person_pronouns
	# print third_person_pronouns
	# print data

	r = re.compile('(<A=[0-4]>)')
	with open('test-test.twt') as inpt:
		# inpt looks like:
		# <A=0>\n
		# stellargirl/NN I/PRP loooooooovvvvvveee/NN\n
		# <A=1>\n
		data = filter(None, r.split(inpt.read()))

		for d in data:
			if r.search(d):
				polarity = get_polarity(d) # current polarity
			else:








	# training_csv_file = sys.argv[1]
	# output_file = sys.argv[2]

	# with open(output_file, 'w') as arff:
	# 	# Write the arff header
	# 	arff.write('@relation twit_classification\n\n')