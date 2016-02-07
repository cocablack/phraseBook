import os, glob, sys
import string
import collections
from textblob import TextBlob

def text_analysis(text):
	blob = TextBlob(text)
	value = 0
	num_sentences = 0
	for sentence in blob.sentences:
		value += sentence.sentiment.polarity
		num_sentences = num_sentences + 1	
	############ SENTIMENT VALUE #############		
	sentiment_val = int((value/num_sentences)*100)
	return sentiment_val

#Input: Type of media to do analysis on 
# def analysis(media_type):
def analysis():

	result = {}

	# result = []

	#for media_type in media_list:
	path = "mashed_media" 
	os.chdir(path)
	currDir = os.getcwd()

	for file in glob.glob("*.txt"):
		############ ID #############
		# fileID = file.split(".")[0]
		link = "default_link"

		# title = "default_title"
		# author = "default_author"
		# link = "default_link"

		filename = currDir + "/" + file

		count = 0
	
		with open(filename, 'r') as f:
			for line in f:
				count = count + 1
					# if count == 1:
					# 	############ TITLE #############
					# 	title = line
					# elif count == 2:
					# 	############ AUTHOR #############
					# 	author = line
					# elif count == 3:
				if count == 3:
						############ URL LINK #############
					link = line

		r = sentiment_analysis(filename)
		result[r] = link #(k,v) = (sentiment val, link)

		
			# r2 = frequency_analysis(filename)

			# entry = [ media_type, fileID, title, author, line, r1, r2 ]
			# result.append(entry)

			# print(entry)
	return result


def sentiment_analysis(filename):
	with open(filename, 'r') as f:
		text = f.read()
		blob = TextBlob(text)

		value = 0
		num_sentences = 0
		for sentence in blob.sentences:
			value += sentence.sentiment.polarity
			num_sentences = num_sentences + 1
		
		############ SENTIMENT VALUE #############		
		sentiment_val = int((value/num_sentences)*100)
	f.close()
	# print(sentiment_val)
	return sentiment_val

def frequency_analysis(filename):
	with open(filename, 'r') as f:
		lines = []
		exclude = set(string.punctuation + "\n")
		for line in f:
			line = line.lower()
			line = ''.join(ch for ch in line if ch not in exclude)
			lines.append(line)
			
		word_dict = {}

		for line in lines:
			words = line.split(" ")
			for word in words:
				if len(word) > 2 and len(word) < 10:
					if word in word_dict:
						word_dict[word] = word_dict[word] + 1
					else:
						word_dict[word] = 1

		max_count = 0

		stopwords = ["the", "to", "and", "of", "a", "was", "his", "her", "that", \
		"i", "you", "was", "had", "for", "they", "said", "with", "should", \
		"but", " but", "but ", " but ", "not", "their", "him", "this", \
		"which", "not", "have", "all", "its", "your", "she", "them", "there", \
		"from", " from", "from ", " from ", "would", " would", "would ", " would ", \
		"will", "when", "who", "were", "are", "been", "then", "upon", "may", "about" \
		"out", " out", "out ", " out ", "one", "what", "could", "about", "some", \
		"ive", "ooh", "doesnt", "ohh", "ooooh", "where", "sometimes"]

		for word, count in word_dict.items():
			if word_dict[word] > max_count:
				if not word in stopwords:
					max_count = word_dict[word]
					freq_word = word

		############ MOST FREQUENT WORD #############					
		most_freq = freq_word	
		# print(most_freq)

	f.close()
	return most_freq

#Input: string text user typed in, dictionary of sentiment value and url
def get_min_diff(text, result):

	print("GETTING MIN DIFF")

	min_diff = 1000;
	min_media = None
	user_sentiment = text_analysis(text)
	# print("SENTIMENT" + user_sentiment)
	cur_entry = None
	for entry in result:
		cur_sentiment = entry[5]
		val = user_sentiment - cur_sentiment
		if abs(val) < min_diff:
			min_diff = abs(val)
			min_media = cur_sentiment
			cur_entry = entry
	print("GET MIN DIFF")
	print(entry)
	return entry



# if __name__ == "__main__":
	# arg = sys.argv[1]

	# result = analysis()
	# print(result)



	

