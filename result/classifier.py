from sklearn import naive_bayes
from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client.authors_db
collection = db.authors_stats

def get_training_set_data():
  return collection.find({})


def get_author_names_from_db():
  return map(lambda x: x['name'], collection.find({}, {'_id': 0, 'name': 1}))


def get_authors_numerical_characteristics(name):
  print name
  return collection.find_one({'name': name},
                             {'_id': 0,
                              'average_sentence_complexity': 1,
                              'average_word_length': 1,
                              'type_token_ratio': 1,
                              'average_sentence_length': 1,
                              'hapax_legomana_ratio': 1})


def get_authors_parts_of_speech_frequencies(name):
  return map(lambda x: x["parts_of_speech_frequencies"], collection.find({'name': name},
                             {'_id': 0,
                              'parts_of_speech_frequencies': 1}))


def get_authors_top_base_words_frequencies(name):
  return collection.find_one({'name': name},
                             {'_id': 0,
                              'base_words': 1})


def classify_with_db_training_set_with_file():

  characteristics_from_file = open('./results', 'r').read().split('\n')
  to_detect_text_numerical_characteristics = map(float, characteristics_from_file[1::2])

  with open('partsOfSpeechResults') as data_file:
    example_frequencies = json.load(data_file)

  author_names = get_author_names_from_db()
  gaussian_naive_bayes = naive_bayes.GaussianNB()

  # NUMERICAL
  authors_numerical_characteristics = map(get_authors_numerical_characteristics, author_names)
  numerical_characteristics_training_set = convert_characteristics_into_2d_array(authors_numerical_characteristics)
  gaussian_naive_bayes.fit(numerical_characteristics_training_set, author_names)
  numerical_characteristics_classification_result = gaussian_naive_bayes.predict(to_detect_text_numerical_characteristics)

  # PARTS OF SPEECH

  authors_parts_of_speech_frequencies = map(get_authors_parts_of_speech_frequencies, author_names)
  parts_of_speech_frequencies_training_set = pick_parts_of_speech(authors_parts_of_speech_frequencies, example_frequencies)
  gaussian_naive_bayes.fit(parts_of_speech_frequencies_training_set, author_names)
  example_frequencies_as_array = get_values_from_json(example_frequencies)
  parts_of_speech_frequencies_classifications_result = gaussian_naive_bayes.predict(example_frequencies_as_array)

  return "numerical classification: " + numerical_characteristics_classification_result[0] + \
                     " parts of speech freq classification: " + parts_of_speech_frequencies_classifications_result[0]


def pick_parts_of_speech(authors_parts_of_speech_frequencies, example_frequencies):
  parts_of_speech_frequencies_training_set = []
  for author_frequencies in authors_parts_of_speech_frequencies:
    some_author_frequencies = []
    # print author_frequencies[0]
    for frequency_name in example_frequencies:
      some_author_frequencies.append(float(author_frequencies[0].get(frequency_name, 0)))
    parts_of_speech_frequencies_training_set.append(some_author_frequencies)
  return parts_of_speech_frequencies_training_set


def get_values_from_json(json):
  values_array = []
  for keys in json:
    values_array.append(float(json.get(keys)))
  return values_array


def convert_characteristics_into_2d_array(characteristics_map):
  numerical_characteristics_training_set = []
  for characteristics in characteristics_map:
    characteristics_values = []
    for key, value in characteristics.items():
      characteristics_values.append(float(value))
    numerical_characteristics_training_set.append(characteristics_values)

  return numerical_characteristics_training_set
