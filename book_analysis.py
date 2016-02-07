import os, glob
from textblob import TextBlob

def sentiment_analysis():
	os.chdir("./books/")
	currDir = os.getcwd()

	count = 0
	for file in glob.glob("*.txt"):
		count = count + 1

		filename = currDir + "/" + file

		text = open(filename, 'r')
		text = text.read()

		blob = TextBlob(text)

		value = 0
		line = 0
		for sentence in blob.sentences:
			value += sentence.sentiment.polarity
			line = line + 1
		
		print(value/line)

	print(count)

if __name__ == "__main__":
	sentiment_analysis()
