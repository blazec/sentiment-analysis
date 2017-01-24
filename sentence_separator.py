# Run this program using python 2.7
import re
import itertools

ABBRVS_PN_FILE = 'pn_abbrev.english' # abbrevs non-finally
ABBRVS_FILE = 'abbrev.english'

# abbreviations that do not occur finally
with open(ABBRVS_PN_FILE) as f:
    abbrvs_pn = f.readlines()
abbrvs_pn_regex = ''
for abbrv in abbrvs_pn:
	# all upper and lower case combos for the abbrv
	abbrv_ulcomb = map(''.join, itertools.product(*zip(abbrv.upper(), abbrv.lower())))
	for comb in abbrv_ulcomb:
		abbrvs_pn_regex += '[\w\s]*\s' + comb.strip().replace('.', '\.') + '\s[\w\s]+\.' + '|'

# abbreviations that may or may not occur finally. Will not catch for example: "Mr. Anderson Jr. is in the house."
# Combined with all the regexes, it will split it as ['Mr. Anderson Jr.', 'is in the house']
with open(ABBRVS_FILE) as f:
    abbrvs = f.readlines()
abbrvs_regex = ''
for abbrv in abbrvs:
	if abbrv not in abbrvs_pn:
		abbrv_ulcomb = map(''.join, itertools.product(*zip(abbrv.upper(), abbrv.lower())))
		for comb in abbrv_ulcomb:
			abbrvs_regex += '[\w\s]*\s' + comb.strip().replace('.','\.') + '\s*[a-z][\w\s]*[\.\!\?]' + '|'


def get_putative_boundaries(tweet):
	''' Sets boundaries for tweet after all occurences of . ? !.
	Returns a list where each element is the extracted sentence'''
	if not tweet:
		return

	# After splitting, this regex makes an attempt to follow these rules:
	# 	- Place putative sentence boundaries after all occurrences of . ? ! (and maybe ; : -_)
	# - Move the boundary after following quotation marks, if any.
	# - Disqualify a period boundary in the following circumstances:
	#   (1) If it is preceded by a known abbreviation of a sort that does not normally occur word finally, but is commonly followed by a capitalized proper name, such as Prof. or vs.
	#   (2) If it is preceded by a known abbreviation and not followed by an uppercase word. This will deal correctly with most usages of abbreviations like etc. or Jr. which   can occur sentence medially or finally.
	# - Disqualify a boundary with a ? or ! if It is followed by a lowercase letter (or a known name)
	# - Regard other putative sentence boundaries as sentence boundaries
 	#
	r = re.compile('(' + abbrvs_regex + abbrvs_pn_regex + '[\w\s]*[\.\!\?]\s*[a-z][\w\s]*[\.\!\?]|\w*[\.\!\?]\"|\w*[\.\!\?])')
	

	# use split with capture group
	# ex: r.split("Ahhh... back to the real world.")
	# 	  returns ['', 'Ahhh.', '', '.', '', '.' ' back to the real ', 'world.']
	# so want to join every first and second element
	tweet_split = r.split(tweet)
	updated_tweet_split = []
	i = 1
	print "split", tweet_split
	while i < len(tweet_split) - 1:
		joined_str = tweet_split[i-1] + tweet_split[i]
		# handle repeated . ? !
		if joined_str in ('.', '?', '!') and len(updated_tweet_split) > 0:
			updated_tweet_split[-1] = updated_tweet_split[-1] + joined_str
		else:
			updated_tweet_split.append(joined_str)

		i += 2

	return updated_tweet_split


# def adjust_boundaries_for_quotation_marks(tweet_spilit):
# 	''' Adjusts the boundaries in tweet_split so that quotation marks that
# 	follow . ? ! are joined to the previous sentence.
# 	ex. tweet_split = ['"Hi.', '" he said.', 'Excuse me?']
# 	'''
# 	if len(tweet_split) < 2:
# 		return tweet_split

# 	i = 1
# 	# Compare previous and following sentence
# 	while i < len(tweet_split) - 1:
# 		if tweet_split[i-1][-1] in ('.', '?', '!') \
# 		and  tweet_split[i][0] == '"':
# 			tweet_split[i-1] = tweet_split[i-1] + '"'
# 			tweet_split[i] = tweet_split[i][1:]

# 	return tweet_split

# def disqualify_period_boundaries_for_abbrvs(tweet_split):
# 	''' Disqualifies period boundary if:
# 		- it is preceded by a known abbreviation that does not normally 
# 		occur finally
# 		- it is preceded by a known abbreviation and not followed by an
# 		uppercase word
# 	'''
# 	if len(tweet_split) < 2:
# 		return tweet_split

# 	i = 1
# 	while i < len(tweet_split) - 1:
# 		pass


# 	updated_tweet_split = []


if __name__ == '__main__':
	sentences = ["@stellargirl I loooooooovvvvvveee my Kindle2. Not that the DX is cool, but the 2 is fantastic in its own right.",
	"Fuck this economy. I hate aig and their non loan given asses.",
	"i love lebron. http://bit.ly/PdHur",
	"@Pmillzz lebron IS THE BOSS",
	"Ahhh... back in a *real* text editing environment. I &lt;3 LaTeX....",
	'"Hi," she remarked, "how are you?" "Good." I replied.',
	'Hi how are you MR. in the farm. Im good',
	'I went to Ala. and I liked it. I went to Ala. Yeah.',
	'Fish, dogs, pigs, etc. But I am Mr. Anderson Jr. the third. My last name is not Jr. Yes.']

	# sentences = ['Fish, dogs, pigs, etc. But I am Mr. Anderson Jr. the third. My last name is not Jr. yes.']

	for sent in sentences:
		print get_putative_boundaries(sent)


