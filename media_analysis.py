import os, glob, sys
import string
import collections
from textblob import TextBlob

#Input: Type of media to do analysis on 
def analysis(media_type):
	path = "./media/" + media_type + "/"
	os.chdir(path)
	currDir = os.getcwd()

	for file in glob.glob("*.txt"):
		############ ID #############
		fileID = file.split(".")[0]
		filename = currDir + "/" + file

		count = 0
		f = open(filename, 'r')
		with open(filename, 'r') as f:
			for line in f:
				count = count + 1
				if count == 1:
					############ TITLE #############
					title = line
					print(title)
				elif count == 2:
					############ AUTHOR #############
					author = line
				elif count == 3:
					############ URL LINK #############
					link = line
				else:
					break
		f.close()

		sentiment_analysis(filename)
		frequency_analysis(filename)


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
		print(sentiment_val)
	f.close()

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
		print(most_freq)

	f.close()

if __name__ == "__main__":
	arg = sys.argv[1]
	analysis(arg)

