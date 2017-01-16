# Run this program using python 2.7

import sys
import NLPlib
import csv
import re

def twtt1(s):
	''' Removes all html tags and attributes. '''
	
	return re.sub(r"<[^>]+>", "", s)

def twtt2(s):
	''' Replaces html character codes with ASCII equivalent. '''
	return ""

def twtt3(s):
	''' Removes  all URLs (tokens that begin with http or wwww) '''
	return re.sub(r"http\S*\s|www.\S*\s", "", s)

def twtt4(s):
	return ""

def twtt5(s):
	return ""

def twtt6(s):
	return ""

def twtt7(s):
	return ""

def twtt8(s):
	return ""

def twtt9(s):
	return ""

if __name__ == '__main__':

	training_csv = sys.argv[1]
	student_num = sys.argv[2]
	output = sys.argv[3]