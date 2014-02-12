import sys

if len(sys.argv) != 2:
	print "You need to specify one, and only one, input argument!"
	exit()
try:
	f = open(sys.argv[1])
	rawList = f.readlines()
except IOError:
	print "Cannot open given file " , sys.argv[1]
except:
	print "Unexpected error:", sys.exc_info()[0]
	
sortedList = []

for newLine in rawList:
	tempWords = newLine.rsplit()
	for word in tempWords:
		lowered = word.lower()
		sortedList.append(word)
		sortedList.sort()

duplicateCounter = 0
for word in sortedList:
	if duplicateCounter != 0:
		if prevWord != word:
			print prevWord, duplicateCounter
			duplicateCounter = 0
	prevWord = word
	duplicateCounter += 1
print prevWord, duplicateCounter
print "There are ", len(rawList), " words in this file."