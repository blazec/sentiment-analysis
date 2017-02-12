# cross-validate using files partition-1 ... partition-10
def write_arff_file(filename,data):
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

		for d in data:
			f.write(d + '\n')

def get_data(f):
	with open(f) as arff_file:
		lines = [line.rstrip() for line in arff_file]
		lines = lines[26:len(lines)]
	return lines

if __name__ == '__main__':
	for i in range(10):
		filename_train = 'bucket-all-not-' + str(i+1) + '.arff'
		filename_test = 'bucket-' + str(i+1) + '.arff'
		filename_i = 'partition-' + str(i+1) + '.arff'
		data_train = []

		for j in range(0, i) + range(i+1,10):
			filename_j = 'partition-' + str(j+1) + '.arff'
			data_train = data_train + get_data(filename_j)

		data_test = get_data(filename_i)

		write_arff_file(filename_train, data_train)
		write_arff_file(filename_test, data_test)




			        
