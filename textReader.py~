import os.path, math

def readInChunks(fileObj, chunkSize=2048):
    while True:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data

def printResultsInFile(resultFileContent):
	with open("results.txt", "a") as resultFile:
		for result in resultFileContent:
    			resultFile.write("%s\n" % result)

def cleanUp(s):
    punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
    result = s.lower().strip(punctuation)
    return result

def averageWordLength(text):
    words = [cleanUp(each_word) for each_sentence in text
     for each_word in each_sentence.split()]

    # Replace each word with its length
    print words	
    words = [len(each_word) for each_word in words]
    print words
    average = sum(words) / float(len(words))
    print "AVERAGE WORD LENGTH: " 
    print average	
    return average

if __name__ == '__main__':
	print "\nReading File...\n"
	text = open('./toDetectFile', 'r').readlines()
	resultFileContent = ['average word length: ']
	resultFileContent.append(averageWordLength(text))
	printResultsInFile(resultFileContent)





