import os, glob
import string
import collections
from textblob import TextBlob

#Input: Type of media to do analysis on in a string format
def analysis(media_type):
	path = "./media/" + media_type + "/"
	os.chdir(path)
	currDir = os.getcwd()

	for file in glob.glob("*.txt"):
		############ ID #############
		fileID = file.split(".")[0]
		filename = currDir + "/" + file

		count = 0
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
					print(author)
				else:
					break

			sentiment_analysis(f)
			frequency_analysis(f)


def sentiment_analysis(f):
	text = f.read()
	blob = TextBlob(text)

	value = 0
	num_sentences = 0
	for sentence in blob.sentences:
		value += sentence.sentiment.polarity
		num_sentences = num_sentences + 1
	
	############ SENTIMENT VALUE #############		
	sentiment_val = (value/num_sentences)*100
	print(sentiment_val)

def frequency_analysis(f):
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
			if word in word_dict:
				word_dict[word] = word_dict[word] + 1
			else:
				word_dict[word] = 1





	# with open('outList.txt', 'w') as out:
	# 	for line in lines:
	# 		words = line.split(" ")
	# 		for character in words:
	# 			out.writelines(character + "\n")

if __name__ == "__main__":
	analysis("music")

