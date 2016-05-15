from pymongo import MongoClient
from textCharacteristics import count_numerical_statistics
from XmlParser import XmlParser
from time import time

client = MongoClient('mongodb://localhost:27017/')
db = client.stylometric_analyses
collection = db.long_analysed_texts


def recalculate_simple_characteristics_keeping_impact(author_data, old_positions_impact,
                                                      position_characteristics, new_position_impact,
                                                      characteristics_to_recalculate):
  for characteristic in characteristics_to_recalculate:
    author_data[characteristic] = author_data[characteristic] * old_positions_impact + position_characteristics[
                                                                                         characteristic] * new_position_impact


def recalculate_morphological_characteristics_keeping_impact(author_data, old_positions_impact,
                                                             position_characteristics, new_position_impact,
                                                             speech_path):
  for name in author_data[speech_path]:
    if position_characteristics[speech_path][name]:
      author_data[speech_path][name] = author_data[speech_path][name] * old_positions_impact + \
                                       position_characteristics[speech_path][name] * new_position_impact

  # all new part of speech frequencies merged
  for name in position_characteristics[speech_path]:
    if not author_data[speech_path][name]:
      author_data[speech_path][name] = position_characteristics[speech_path][name]


def clear_characteristics_collection():
  collection.remove()


def clear_author_characteristics(name):
  collection.remove({'name': name})


def save_in_db(record):
  print "inserting into db ... "
  collection.insert_one(record)


def create_new_record(xml_string, text_classes, raw_text):
  t0 = time()
  xml_tree = XmlParser(xml_string)
  print "XML tree generated in  %fs" % (time() - t0)

  text = xml_tree.get_base_words()
  t0 = time()
  numerical_characteristics = count_numerical_statistics(text)
  print "Numerical characteristics counted in  %fs" % (time() - t0)

  xml_tree.set_number_of_words(numerical_characteristics["words_count"])
  t0 = time()
  author_position_characteristics = {
    "raw_text": raw_text,
    "parts_of_speech_frequencies": xml_tree.get_parts_of_speech_frequency(),
    "classes": text_classes
  }
  print "Parts of speech characteristics counted in  %fs" % (time() - t0)
  author_position_characteristics.update(numerical_characteristics)
  t0 = time()
  author_position_characteristics.update(xml_tree.get_top_and_rarest_used_words())
  print "Top and rarest words counted in  %fs" % (time() - t0)
  return author_position_characteristics
