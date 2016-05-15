from pymongo import MongoClient


class MongoCollection:
  def __init__(self):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.stylometric_analyses
    self.collection = db.long_analysed_texts

  def get_first_from_db(self):
    return self.collection.find_one({})

  def get_training_set_data(self):
    return self.collection.find({})

  def get_positons_with_given_class(self, class_name):
    return map(lambda x: x, self.collection.find({'classes.' + class_name: {"$exists": True}}))

  def get_all_records(self):
    return map(lambda x: x, self.collection.find({}, {"_id": 0}))

  def get_classes_values_from_db(self, class_name):
    return map(lambda x: x["classes"][class_name], self.collection.find({'classes.' + class_name: {"$exists": True}}))

  def get_positions_numerical_characteristics(self, name):
    print name
    return self.collection.find_one({'name': name},
                               {'_id': 0,
                                'average_sentence_complexity': 1,
                                'average_word_length': 1,
                                'type_token_ratio': 1,
                                'average_sentence_length': 1,
                                'hapax_legomana_ratio': 1})

  def get_positions_parts_of_speech_frequencies(self, class_name):
    return map(lambda x: x["parts_of_speech_frequencies"], self.collection.find({},
                                                                           {'_id': 0,
                                                                            'parts_of_speech_frequencies': 1}))

  def get_authors_top_base_words_frequencies(self, name):
    return self.collection.find_one({'name': name},
                               {'_id': 0,
                                'base_words': 1})
