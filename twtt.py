# Run this program using python 2.7

import sys
import NLPlib
import csv
import re
import sentence_separator
import token_separator

tagger = NLPlib.NLPlib()

def twtt1(s):
	''' Returns a new string with all html tags and attributes removed from s. '''
	try:
		return re.sub(r'<[^>]+>', '', s)
	except Exception:
		print 'Error: twtt1'
		return s

def twtt2(s):
	''' Returns a new string with html character codes (&#32-&#127) replaced with their
	 ASCII equivalent. '''
	ascii_codes = {'quot': 34, 'amp': 38, 'lt': 60, 'gt': 62}
	try:
		r = re.compile('&#[3][2-9]|&#[4-9][0-9]|&#1[0-1][0-9]|&#1[2][0-7]|&amp|&quot|&lt|&gt')
		match = r.search(s)

		# replace html code with ascii equivalent
		while match:
			html_code = match.group()
			
			# extract ASCII number from html code
			quot_amp_lt_gt = re.search('amp|quot|lt|gt', html_code).group()
			if quot_amp_lt_gt:
				ascii_code = ascii_codes(quot_amp_lt_gt.group())
			else:
				ascii_code = int(re.search('[0-9]{2,3}', html_code).group())

			s = s.replace(html_code, chr(ascii_code))
			match = r.search(s)

		return s
	except Exception:
		print 'Error: twtt2'
		return s

def twtt3(s):
	''' Removes  all URLs (tokens that begin with http or wwww) '''
	try:
		# url regex from http://stackoverflow.com/questions/3809401/what-is-a-good-regular-expression-to-match-a-url
		return re.sub(r'[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)', "", s)
	except Exception:
		print 'Error: twtt3'
		return s

def twtt4(s):
	''' Returns a new string where @ and # (twitter symbols) are removed from s.'''
	try:
		return re.sub(r'@|#', '', s)
	except Exception:
		print 'Error: twtt4'
		return s

def twtt5(s):
	''' Returns a string where each sentence is its own line'''
	try:
		return sentence_separator.get_sentences(s)
	except Exception:
		print 'Error: twtt5'
		return s

def twtt6(s):
	return

def twtt7(s):
	''' Returns a new sting where punctuations and clitics are separated by spaces.
	e.g. don't -> do n't '''
	try:
		return token_separator.get_tokens(s)
	except Exception:
		print 'Error: twtt7'
		return s

def twtt8(s):
	''' Precondition: s is a string where each sentence is separated by a new line. 
	Returns a new string where each token is tagged. The tag will appear beside next to
	a slash next to the token.'''
	try:
		r = re.compile('(\s+)')
		tokens = r.split(s)
		
		# At this point tokens looks like this ["Hi", " ", ".", "\n", "I" " " "am"]
		# The tagger will tag the spaces and new lines. We want to ignore the tags for these
		# space characters later on
		tags = tagger.tag(tokens)

		# Now we want to concatenate the tags to the tokens, but not to the spaces.
		# Tags and tokens should be of equal length because each tag corresponds to one token
		for i in range(len(tokens)):
			if not r.search(tokens[i]):
				tokens[i] = tokens[i] + '/' + tags[i]

		return ''.join(tokens)
	except Exception:
		print 'Error: twtt8'
		return s

def twtt9(s, polarity):
	''' Precondition: s is a string where each token is tagged and separated by a space and
						each sentence is in its own line.
		Adds <A=polarity> as the first line of s
	'''
	pol = '<A=' + str(polarity) + '>'
	return pol + '\n' + s

if __name__ == '__main__':

	# training_csv_file = sys.argv[1]
	# student_num = sys.argv[2]
	# output = sys.argv[3]
	#X = student_num % 80
	QUERY_INDEX = 5
	POLARITY_INDEX = 0
	training_csv_file = "training.1600000.processed.noemoticon.csv"
	student_num = 1000057626
	output = "train.twt"
	X = student_num % 80

	# If the input csv has 1,600,000 lines, then
	# process and concatenate the following lines:
	# X * 10, 000 + [0 . . . 9999]
	# and
	# 800, 000 + X * 10, 000 + [0 . . . 9999]
	# where X is your student ID modulo 80.

	
	with open(training_csv_file) as f:
		for i, l in enumerate(f):
			pass
	
	if i + 1 == 1600000:
		range1 = range(X * 10000, X * 10000 + 10000)
		range2 = range(800000 + X  * 10000, 800000 + X  * 10000 + 10000)
		ranges = range1 + range2
		# range1 = (1,0)
		# range2 = (2,3)
		# ranges = range1 + range2

		with open(training_csv_file) as inpt:

				with open(output, 'w') as output:
					print "Writing training file"
					reader = csv.reader(inpt)
					i = 0
					j = 0
					for row in reader:
						if i in ranges:
							if j % 1000 == 0:
								print str(int((float(j) / float(20000)) * 100)) + '%' + ' complete.'

							tweet = row[QUERY_INDEX]
							polarity = row[POLARITY_INDEX]
							output.write(twtt9(twtt8(twtt7(twtt5(twtt4(twtt3(twtt2(twtt1(tweet))))))), polarity) + '\n')

							j += 1
						i += 1





	# print(twtt2('Hi &#127 how &#128 &#33h &#30h'))
	# tweets = ["@stellargirl I loooooooovvvvvveee my Kindle2. Not that the DX is cool, but the 2 is fantastic in its own right.",
	# "Fuck this economy. I hate aig and their non loan given asses.",
	# "i love lebron. http://bit.ly/PdHur",
	# "@Pmillzz lebron IS THE BOSS",
	# "Ahhh... back in a *real* text editing environment. I &lt;3 LaTeX....",
	# '"Hi," she remarked, "how are you?" "Good." I replied.',
	# 'Hi how are you MR. in the farm. Im good',
	# 'I went to Ala. and I liked it. I went to Ala. Yeah.',
	# 'Fish, dogs, pigs, etc. in the car. But I am Mr. Anderson Jr. the third. My last name is not Jr. Yes.',
	# "This tweet's the best tweet!! Everybody says so. Don't you think?"]

	# for tweet in tweets:
	# 	print twtt5(tweet)
	# 	print '\n'

	# for tweet in tweets:
	# 	print twtt9(twtt8(twtt7(twtt5(tweet))), 4)