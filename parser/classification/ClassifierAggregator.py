from __future__ import division
from parser.MongoCollection import MongoCollection
from time import time
from parser.classification.CommonWordsClassifier import CommonWordsClassifier
from parser.classification.NumericalFeaturesClassifier import NumericalFeaturesClassifier, numerical_characteristics
from parser.classification.PartsOfSpeechClassifier import PartsOfSpeechClassifier


class ClassifierAggregator:
  def __init__(self):
    self.mongoCollection = MongoCollection()

  def full_classification(self, to_detect_position):

    def proceed_classification_for_class_name(class_name):
      print "Classifying for", class_name
      with_class_records = self.mongoCollection.get_positons_with_given_class(class_name)
      # class_names = map(lambda x: x["classes"][class_name], with_class_records)
      t0 = time()
      numerical_classification = NumericalFeaturesClassifier.classify(to_detect_position,
                                                                      class_name,
                                                                      numerical_characteristics,
                                                                      with_class_records)
      print "Numerical classification counted in  %fs" % (time() - t0)
      t0 = time()
      parts_of_speech_classification = PartsOfSpeechClassifier.classify(to_detect_position,
                                                                        class_name,
                                                                        "parts_of_speech_frequencies",
                                                                        with_class_records)
      print "Parts of speech classification counted in  %fs" % (time() - t0)
      t0 = time()
      # most_common_words_class = CommonWordsClassifier.classify(to_detect_position,
      #                                                          "top_words",
      #                                                          class_name,
      #                                                          with_class_records)
      print "Common words classification counted in  %fs" % (time() - t0)

      return {
        class_name: {
          "numerical_classification": numerical_classification[0],
          "parts_of_speech_frequencies_classification": parts_of_speech_classification[0],
          "top_common_words": "no be defined "
        }
      }

    return map(proceed_classification_for_class_name, to_detect_position["classes"])
