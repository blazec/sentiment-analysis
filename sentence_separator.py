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
	# all upper and lower case combos for the abbrv. Done manually and not with re.IGNORECASE because case matters in some cases
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
		# all upper and lower case combos for the abbrv. Done manually and not with re.IGNORECASE because case matters in some cases
		abbrv_ulcomb = map(''.join, itertools.product(*zip(abbrv.upper(), abbrv.lower())))
		for comb in abbrv_ulcomb:
			abbrvs_regex += '[\w\s]*\s' + comb.strip().replace('.','\.') + '\s*[a-z][\w\s]*[\.\!\?]' + '|'

# Regular expressions useful in get_sentences(tweet)
question_exclam_before_small_regex = '[\w\s]*[\.\!\?]\s*[a-z][\w\s]*[\.\!\?]|'
quote_regex = '\w*[\.\!\?]\"|'
period_question_exclaim_regex = '\w*[\.\!\?]'

# After splitting, this regex makes an attempt to follow these rules:
# 	- Place putative sentence boundaries after all occurrences of . ? ! (and maybe ; : -_)
# - Move the boundary after following quotation marks, if any.
# - Disqualify a period boundary in the following circumstances:
#   (1) If it is preceded by a known abbreviation of a sort that does not normally occur word finally, but is commonly followed by a capitalized proper name, such as Prof. or vs.
#   (2) If it is preceded by a known abbreviation and not followed by an uppercase word. This will deal correctly with most usages of abbreviations like etc. or Jr. which   can occur sentence medially or finally.
# - Disqualify a boundary with a ? or ! if It is followed by a lowercase letter (or a known name)
# - Regard other putative sentence boundaries as sentence boundaries
	#
r = re.compile('(' + abbrvs_regex + abbrvs_pn_regex + question_exclam_before_small_regex \
	+ quote_regex + period_question_exclaim_regex + ')')

def get_sentences(tweet):
	''' Sets boundaries for tweet after all occurences of . ? !.
	Returns a list where each element is the extracted sentence'''
	if not tweet:
		return

	# use split with capture group
	tweet_split = r.split(tweet)
	# ex: r.split("Ahhh... back to the real world.")
	# 	  returns ['', 'Ahhh.', '', '.', '', '.' ' back to the real ', 'world.']
	# So we have to format even further

	# Replace space (if it is the first character) with line break '\n'
	tweet_split = filter(None, tweet_split)
	tweet_split = map(lambda elem: '\n' + elem[1:] if len(elem) > 0 and elem[0] == ' ' else elem, tweet_split)
	# tweet_split.insert(0, first)
	tweet_split = map(lambda elem: elem.replace(re.search(r' *\n *', elem).group(), '\n') if re.search(r' *\n *', elem) else elem, tweet_split)
	
	if len(tweet_split) > 0:
		if tweet_split[-1].isspace():
			tweet_split.pop()
	if len(tweet_split) > 0:		
		if tweet_split[0].isspace():
			return ''.join(tweet_split[1:])
		elif tweet_split[0].startswith('\n'):
			tweet_split[0] = tweet_split[0][1:]
	
	return ''.join(tweet_split)


if __name__ == '__main__':
	sentences = ["@stellargirl I loooooooovvvvvveee my Kindle2. Not that the DX is cool, but the 2 is fantastic in its own right.",
	"Fuck this economy. I hate aig and their non loan given asses.",
	"i love lebron. ",
	" - awesome come back lebron. - awesome come back lebron",
	"@Pmillzz lebron IS THE BOSS",
	"Ahhh... back in a *real* text editing environment. I &lt;3 LaTeX....",
	'"Hi," she remarked, "how are you?" "Good." I replied.',
	'Hi how are you MR. in the farm. Im good',
	'I went to Ala. and I liked it. I went to Ala. Yeah.',
	'Fish, dogs, pigs, etc. in the car. But I am Mr. Anderson Jr. the third. My last name is not Jr. Yes.', 
	"This       tweet's the best tweet!! Everybody says so..!??.!?!!.. I'm bury you. SAD",
	'.......... .......... .......... ....... aaaaa',
	'Today is a non-trash day.    haya',
	'Are YOU burning more cash $$$ than Chrysler and GM? Stop the financial tsunami. Where "bailout" means taking a handout!',
	"Reading my kindle2...  Love it... Lee childs is good read.",
	"Trouble in Iran, I see. Hmm. Iran. Iran so far away. #flockofseagullsweregeopoliticallycorrect",
	"So...freaking....tired.... ",
	" no. it is too big. I'm quite happy with the Kindle2."]

	# sentences = ['Fish, dogs, pigs, etc. But I am Mr. Anderson Jr. the third. My last name is not Jr. yes.']

	for sent in sentences:
		if 'happy' in sent:
			print get_sentences(sent)


