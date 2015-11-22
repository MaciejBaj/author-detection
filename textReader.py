import os.path, math


def read_in_chunks(fileObj, chunkSize=2048):
  while True:
    data = fileObj.read(chunkSize)
    if not data:
      break
    yield data


def print_results_in_file(resultFileContent):
  print "Writing results to file results"
  with open("results", "w") as resultFile:
    for result in resultFileContent:
      resultFile.write("%s\n" % result)


def clean_up(s):
  punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
  result = s.lower().strip(punctuation)
  return result


def average_word_length(text):
  words = [clean_up(each_word) for each_sentence in text
           for each_word in each_sentence.split()]

  # Replace each word with its length
  words = [len(each_word) for each_word in words]
  average = sum(words) / float(len(words))

  return average


def type_token_ratio(text):
  words = [clean_up(each_word) for each_sentence in text
           for each_word in each_sentence.split()]
  ttr = len(set(words)) / float(len(words))
  return ttr


def hapax_legomana_ratio(text):
  words = [clean_up(each_word) for each_sentence in text
           for each_word in each_sentence.split()]
  seen_once = []
  seen_twice = []

  for index, word in enumerate(words):
    # print "in HLR for block", index, len(words)
    seen_once.append(word)
    words[index] = None
    if word in words:
      seen_twice.append(word)
      # print "in HLR if  block", index, len(words)

  exactly_once = [word for word in seen_once if word not in seen_twice]
  HLR = len(exactly_once) / float(len(words))
  return HLR


def split_on_separators(original, separators):

  # To do: Complete this function's body to meet its specification.
  original__ = str(original)
  split_marker = 'MY_SPLIT_MARKER'
  for each in original__:
    if each in separators:
      original__ = original__.replace(each, split_marker)
  result = original__.split(split_marker)

  return result


def average_sentence_length(text):
  terminators = '?!.'

  # Get alllines from text as a huge string.
  #  Need to find better Impl
  all_lines = ''.join(each_line.replace('\n', ' ') for each_line in text)
  sentences = split_on_separators(all_lines, terminators)  # Get sentences

  while ' ' in sentences: sentences.remove(' ')  # Remove empty sentences

  sentences = [each_sentence.split() for each_sentence in sentences]

  total_words = len([clean_up(each_word) for each_sent in sentences
                     for each_word in each_sent
                     if clean_up(each_word) != ''])
  total_sentences = len(sentences)
  return float(total_words) / float(total_sentences)


def avg_sentence_complexity(text):

  sentence_terminators = '?!.'
  phrase_terminators = ',:;'
  # Get alllines from text as a huge string. # Need to find better Impl
  all_lines = ''.join(each_line.replace('\n', ' ') for each_line in text)
  sentences = split_on_separators(all_lines,
                                  sentence_terminators)  # Get sentences
  while ' ' in sentences: sentences.remove(' ')  # Remove empty sentences

  phrases = [split_on_separators(each_sentence, phrase_terminators)
             for each_sentence in sentences]
  phrase_lengths = [len(each) for each in phrases]

  return sum(phrase_lengths) / float(len(phrase_lengths))


if __name__ == '__main__':
  print "\nReading File...\n"
  text = open('./toDetectFile', 'r').readlines()
  resultFileContent = ['average word length: ', average_word_length(text),
                       'type token ratio: ', type_token_ratio(text),
                       'hapax legomana ratio: ', hapax_legomana_ratio(text),
                       'average sentence length: ', average_sentence_length(text),
                       'average sentence complexity: ', avg_sentence_complexity(text)]

  print_results_in_file(resultFileContent)
