from __future__ import division
from sklearn import naive_bayes
import numpy as np


def select_speech_parts_characteristics(input, speech_parts):
  return map(lambda x: input[x], speech_parts)


def pick_parts_of_speech_common_for_all(authors_parts_of_speech_frequencies, example_frequencies):
  parts_common_for_all = map(lambda x: x.keys(), authors_parts_of_speech_frequencies)
  parts_common_for_all.append(example_frequencies.keys())
  return set.intersection(*map(set, parts_common_for_all))


def pick_parts_of_speech(authors_parts_of_speech_frequencies, example_frequencies):
  parts_of_speech_frequencies_training_set = []
  parts_common_for_all = pick_parts_of_speech_common_for_all(authors_parts_of_speech_frequencies, example_frequencies)
  for record_frequencies in authors_parts_of_speech_frequencies:
    parts_of_speech_frequencies_training_set.append(select_speech_parts_characteristics(record_frequencies, parts_common_for_all))

  return parts_of_speech_frequencies_training_set


class PartsOfSpeechClassifier:

  def __init__(self):
    pass

  @staticmethod
  def classify(to_detect_position, class_name, frequencies_property_name, training_set):
    gaussian_naive_bayes = naive_bayes.GaussianNB()
    example_frequencies = to_detect_position[frequencies_property_name]
    class_names = map(lambda x: x["classes"][class_name], training_set)

    positions_parts_of_speech_frequencies = map(lambda x: x[frequencies_property_name], training_set)
    parts_of_speech_frequencies_training_set = \
        pick_parts_of_speech(positions_parts_of_speech_frequencies, example_frequencies)

    gaussian_naive_bayes.fit(parts_of_speech_frequencies_training_set, np.array(class_names))
    possible_example_parts = \
        select_speech_parts_characteristics(example_frequencies,
                                            pick_parts_of_speech_common_for_all(positions_parts_of_speech_frequencies,
                                                                                example_frequencies))
    return gaussian_naive_bayes.predict(np.array(possible_example_parts).reshape(-1, 1))[0]
