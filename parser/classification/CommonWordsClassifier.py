from __future__ import division


def find_common_elements(example_words, record_words_rank):
  record_words = [word.keys()[0] for word in record_words_rank]
  if isinstance(example_words[0], dict):
    example_words = [word.keys()[0] for word in record_words_rank]
  return len(list(set(record_words) & set(example_words)))

#precision, recall, f score, accuracy

class CommonWordsClassifier:

  def __init__(self):
    pass

  @staticmethod
  def classify(to_detect_position, class_name, top_words_property_name, training_set):
    example_words = to_detect_position[top_words_property_name]
    class_names = map(lambda x: x["classes"][class_name], training_set)

    top_words_used = map(lambda x: x[top_words_property_name], training_set)
    common_words_counts = \
        map(lambda record_words_rank: find_common_elements(example_words, record_words_rank), top_words_used)

    return class_names[common_words_counts.index(max(common_words_counts))]
