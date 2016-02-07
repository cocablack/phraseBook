import urllib2  # the lib that handles the url stuff
from random import randint

def download():
	#download 100 random unique books
	l = []
	#populate 100 book list to download
	while len(l) != 100:
		random = randint(10,51137)
		if not random in l:
			l.append(random)

	# for number in l:
	# 	print number
	
	#fetch book from url
	for number in l:
		target_url = "http://www.gutenberg.org/cache/epub/" + str(number) + \
		"/pg" + str(number) + ".txt"
		data = urllib2.urlopen(target_url) 
		for line in data: 
			print line

if __name__ == "__main__":
    download()
		

