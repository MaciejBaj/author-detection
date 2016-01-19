from parseAuthorsPlainTexts import parse_all_texts, parse_file
from xmlParser import XmlParser
from textCharacteristics import average_word_length, type_token_ratio, hapax_legomana_ratio, average_sentence_length, \
  avg_sentence_complexity


def print_results_in_file(path, content):
  print "Writing results to file results"
  with open(path, "w") as result_file:
    for result in content:
      result_file.write("%s\n" % result)


def save_text_as_file(name, text):
  file = open(name, "w")
  file.write(text)
  file.write("\n")
  file.close()

if __name__ == '__main__':
  text = open('./texts/toDetectFile', 'r').readlines()
  resultFileContent = ['average word length: ', average_word_length(text),
                     'type token ratio: ', type_token_ratio(text),
                     'hapax legomana ratio: ', hapax_legomana_ratio(text),
                     'average sentence length: ', average_sentence_length(text),
                     'average sentence complexity: ', avg_sentence_complexity(text)]

  print_results_in_file('./numericalResults', resultFileContent)
  XmlParser.produce_xml_with_morphological_data('./numericalResults', './xmlResults/toDetect.xml')
