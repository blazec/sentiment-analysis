import sys
import random

file = sys.argv[1]

with open(file) as arff_file:
	lines = [line.rstrip() for line in arff_file]
	# Data starts at index 26
	lines = lines[26:len(lines)]
	# n = count of training data
	n = 20000 

	i = 500
	while i <= 10000:
		filename = 'train-' + str(i) + '.arff'
		with open(filename, 'w') as f:
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
			f.write('@DATA\n')

			# pick random data from first half and random data from second half
			first = random.sample(xrange(n/2), i)
			second = random.sample(xrange(n/2, n), i)

			for idx in first:
				f.write(lines[idx] + '\n')
			for idx in second:
				f.write(lines[idx] + '\n')


		i += 500
