# Creates 10 random partitions for cross-fold validation
import sys
import random

file = 'train.arff'
# number of partitions

with open(file) as arff_file:
	lines = [line.rstrip() for line in arff_file]
	# Data starts at index 26
	lines = lines[26:len(lines)]

	# Generate list of partition indices
	negative = random.sample(xrange(10000), 10000)
	positive = random.sample(xrange(10000, 20000), 10000)

	i = 0
	num_partitions = 10

	while i <= num_partitions - 1:
		indices = [negative[idx] for idx in range(1000*i,1000*(i+1))] + [positive[idx] for idx in range(1000*i,1000*(i+1))]

		filename = 'partition-' + str(i+1) + '.arff'
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

			for idx in indices:
				f.write(lines[idx] + '\n')

		i += 1