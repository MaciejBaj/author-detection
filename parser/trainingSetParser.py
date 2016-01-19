from pymongo import MongoClient

from textCharacteristics import average_word_length, type_token_ratio, hapax_legomana_ratio, avg_sentence_complexity, \
  average_sentence_length
from xmlParser import XmlParser

# client = MongoClient('mongodb://10.24.4.96:27017/')
client = MongoClient('mongodb://localhost:27017/')
db = client.authors_db
collection = db.authors_stats


def recalculate_simple_characteristics_keeping_impact(author_data, old_positions_impact,
                                                      position_characteristics, new_position_impact,
                                                      characteristics_to_recalculate):
  for characteristic in characteristics_to_recalculate:
    author_data[characteristic] = author_data[characteristic] * old_positions_impact + position_characteristics[characteristic] * new_position_impact


def recalculate_morphological_characteristics_keeping_impact(author_data, old_positions_impact,
                                                             position_characteristics, new_position_impact,
                                                             speech_path):
  for name in author_data[speech_path]:
    if position_characteristics[speech_path][name]:
      author_data[speech_path][name] = author_data[speech_path][name] * old_positions_impact + position_characteristics[speech_path][name] * new_position_impact

  #all new part of speech frequencies merged
  for name in position_characteristics[speech_path]:
    if not author_data[speech_path][name]:
      author_data[speech_path][name] = position_characteristics[speech_path][name]


def clear_characteristics_collection():
  collection.remove()


def clear_author_characteristics(name):
  collection.remove({'name': name})


def save_characteristics_in_db(file_path, author_name, xml_file_path):
  text = open(file_path, 'r').readlines()
  # xml_tree = XmlParser(xml_file_path)

  author_position_characteristics = {"name": author_name,
                                     "average_word_length": average_word_length(text),
                                     "type_token_ratio": type_token_ratio(text),
                                     "hapax_legomana_ratio": hapax_legomana_ratio(text),
                                     "average_sentence_length": average_sentence_length(text),
                                     "average_sentence_complexity": avg_sentence_complexity(text),
                                     # "base_words": xml_tree.get_base_form_words(),
                                     # "parts_of_speech_frequencies": xml_tree.get_parts_of_speech_frequency(),
                                     # "words_count": xml_tree.get_number_of_words()
                                     }
  author_data = collection.find_one({"name": author_name})
  if author_data:
    print author_position_characteristics["words_count"]
    old_positions_impact = author_data["words_count"] / float(author_position_characteristics["words_count"] + author_data["words_count"])
    print old_positions_impact
    new_position_impact = 1 - old_positions_impact
    characteristics_to_recalculate = ["average_word_length",
                                      "type_token_ratio",
                                      "hapax_legomana_ratio",
                                      "average_sentence_length",
                                      "average_sentence_complexity"]
    recalculate_simple_characteristics_keeping_impact(author_data, old_positions_impact,
                                                      author_position_characteristics, new_position_impact,
                                                      characteristics_to_recalculate)

    recalculate_morphological_characteristics_keeping_impact(author_data, old_positions_impact,
                                                             author_position_characteristics, new_position_impact,
                                                             "parts_of_speech_frequencies")
    collection.find_one_and_replace({"name": author_name}, author_data)

  else:
      collection.insert_one(author_position_characteristics)
