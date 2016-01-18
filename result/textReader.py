from sklearn import naive_bayes

from parser.textCharacteristics import average_word_length, type_token_ratio, hapax_legomana_ratio, avg_sentence_complexity, \
  average_sentence_length

def print_results_in_file(resultFileContent):
  print "Writing results to file results"
  with open("results", "w") as resultFile:
    for result in resultFileContent:
      resultFile.write("%s\n" % result)

if __name__ == '__main__':
  print "\nReading File...\n"
  text = open('./toDetectFile', 'r').readlines()
  resultFileContent = ['average word length: ', average_word_length(text),
                       'type token ratio: ', type_token_ratio(text),
                       'hapax legomana ratio: ', hapax_legomana_ratio(text),
                       'average sentence length: ', average_sentence_length(text),
                       'average sentence complexity: ', avg_sentence_complexity(text)]

  reymontCharacteristicsText = open('./textsCharacteristics/reymont', 'r').read().split('\n')
  sienkiewiczCharacteristicsText = open('./textsCharacteristics/sienkiewicz', 'r').read().split('\n')
  inputCharacteristicsText = open('./results', 'r').read().split('\n')

  # take odd array elements and convert into float
  reymontCharacteristics = map(float, reymontCharacteristicsText[1::2])
  sienkiewiczCharacteristics = map(float, sienkiewiczCharacteristicsText[1::2])
  inputCharacteristics = map(float, inputCharacteristicsText[1::2])

  trainingSet = [reymontCharacteristics, sienkiewiczCharacteristics]
  gaussian_naive_bayes = naive_bayes.GaussianNB()
  gaussian_naive_bayes.fit(trainingSet, ['reymont', 'sienkiewicz'])

  print gaussian_naive_bayes.predict(inputCharacteristics)

  print_results_in_file(resultFileContent)
