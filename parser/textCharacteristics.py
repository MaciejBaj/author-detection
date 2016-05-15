from __future__ import division
import numpy as np

special_characters = ('?', '!', '.', ',', ':', ';', '-', '#', '*', '(', ')', '"')
sentence_terminators = ('?', '!', '.')


def count_numerical_statistics(words):

  current_sentence_length = 0
  sentence_lengths = []
  special_characters_count = 0
  words_lengths = []
  words_count = len(words)

  for word in words:
    words_lengths.append(len(word))
    current_sentence_length += 1
    if word in special_characters:
      special_characters_count += 1
      if word in sentence_terminators:
        sentence_lengths.append(current_sentence_length)
        current_sentence_length = 0
  return {
    "words_count": words_count,
    "average_word_length": np.mean(words_lengths),
    "average_sentence_length": np.mean(sentence_lengths),
    "average_sentence_complexity": special_characters_count / words_count,
    "type_token_ratio": type_token_ratio(words)
  }


# words variety
def type_token_ratio(words):
  return len(set(words)) / float(len(words))
