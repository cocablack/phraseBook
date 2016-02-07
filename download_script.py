import urllib.request  			# the lib that handles the url stuff
from random import randint
import logging					# logging  
import time

root = "books/"

def download():
	# download 100 random unique books
	l = [45316]
	# populate 100 book list to download
	while len(l) != 10:
		random = randint(10,51137)
		if not random in l:
			l.append(random)

	# fetch book from url
	for number in l:
		logging.info("Downloading " + str(number))

		filename = "pg{0}.txt".format(number)
		target_url = "http://www.gutenberg.org/cache/epub/{0}/{1}".format(number, filename)
		
		logging.info("URL: " + target_url)
		try:
			data = urllib.request.urlopen(target_url)
		except urllib.error.HTTPError:
			logging.info("{0} could not be found".format(number))
			continue;
		
		with open(root + filename, "w+") as f:
			for line in data: 
				print(line, file=f)
		time.sleep(5)

if __name__ == "__main__":
	logging.basicConfig(format='%(levelname)s:\t%(message)s', level=logging.DEBUG)
	download()