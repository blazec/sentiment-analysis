# Run this program using python 2.7

import sys
import NLPlib
import csv
import re

def twtt1(s):
	''' Returns a new string with all html tags and attributes removed from s. '''
	return re.sub(r'<[^>]+>', '', s)

def twtt2(s):
	''' Returns a new string with html character codes (&#32-&#127) replaced with their
	 ASCII equivalent. '''
	r = re.compile('&#[3][2-9]|&#[4-9][0-9]|&#1[0-1][0-9]|&#1[2][0-7]')
	match = r.search(s)

	# replace html code with ascii equivalent
	while match:
		html_code = match.group()
		
		# extract ASCII number from html code
		ascii_code = int(re.search('[0-9]{2,3}', html_code).group())

		s = s.replace(html_code, chr(ascii_code))
		match = r.search(s)

	return s

def twtt3(s):
	''' Removes  all URLs (tokens that begin with http or wwww) '''
	return re.sub(r'http\S*\s|www.\S*\s', "", s)

def twtt4(s):
	''' Returns a new string where @ and # (twitter symbols) are removed from s.'''
	return re.sub(r'@|#', '', s)

def twtt5(s):
	''' Returns a string where each sentence is its own line'''
	return ""

def twtt6(s):
	pass

def twtt7(s):
	return ""

def twtt8(s):
	return ""

def twtt9(s):
	return ""

if __name__ == '__main__':

	# training_csv = sys.argv[1]
	# student_num = sys.argv[2]
	# output = sys.argv[3]

	print(twtt2('Hi &#127 how &#128 &#33h &#30h'))

