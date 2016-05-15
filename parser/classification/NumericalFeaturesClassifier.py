from __future__ import division
from sklearn import naive_bayes
import numpy as np
numerical_characteristics = ["average_sentence_length",
                             "average_sentence_complexity",
                             "average_word_length",
                             "type_token_ratio",
                             "hapax_legomenon_ratio"]


def select_numerical_characteristics(input, precision=7):
  return map(lambda characteristic: round(input[characteristic], precision), numerical_characteristics)


class NumericalFeaturesClassifier:

  def __init__(self):
    pass

  @staticmethod
  def classify(to_detect_position, class_name, numerical_features, training_set):
    gaussian_naive_bayes = naive_bayes.GaussianNB()

    to_detect_text_numerical_characteristics = select_numerical_characteristics(to_detect_position)
    class_names = map(lambda x: x["classes"][class_name], training_set)

    numerical_characteristics_training_set = map(lambda x: select_numerical_characteristics(x), training_set)
    gaussian_naive_bayes.fit(numerical_characteristics_training_set, np.array(class_names))
    return gaussian_naive_bayes.predict([to_detect_text_numerical_characteristics])
