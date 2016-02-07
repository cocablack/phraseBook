import os, glob
import string
import collections
from textblob import TextBlob

def analysis():
	os.chdir("./books/")
	currDir = os.getcwd()

	count = 0
	for file in glob.glob("*.txt"):
		fileID = file[2:]#id

		count = count + 1
		filename = currDir + "/" + file

		with open(filename, 'r') as f:


		sentiment_analysis(filename)

	print(count)

def sentiment_analysis(f):
	text = f.read()
	blob = TextBlob(text)

	value = 0
	num_sentences = 0
	for sentence in blob.sentences:
		value += sentence.sentiment.polarity
		num_sentences = num_sentences + 1
			
	sentiment_val = value/num_sentences
	print(sentiment_val)
		

# def frequency_analysis(filename):
# 	with open(filename, 'r') as textfile:

def frequency_analysis():
	with open("./books/pg103.txt", 'r') as textfile:
		lines = []
		exclude = set(string.punctuation + "\n")
		for line in textfile:
			line = line.lower()
			line = ''.join(ch for ch in line if ch not in exclude)
			lines.append(line)

	unique_words = []
	for line in lines:
		words = line.split(" ")
		unique_words.append(words)
	
	for word in unique_words:
		print(word)

	# with open('outList.txt', 'w') as out:
	# 	for line in lines:
	# 		words = line.split(" ")
	# 		for character in words:
	# 			out.writelines(character + "\n")

if __name__ == "__main__":
	#analysis()
	frequency_analysis()
