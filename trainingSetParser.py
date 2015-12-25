from pymongo import MongoClient
from textCharacteristics import average_word_length, type_token_ratio, hapax_legomana_ratio, avg_sentence_complexity, \
  average_sentence_length, get_plain_words

client = MongoClient('mongodb://localhost:27017/')
db = client.authors_db
collection = db.authors_stats

text = open('./texts/sienkiewicz_ogniem-i-mieczem', 'r').readlines()
author_characteristics = { "name": "mickiewicz",
                       "average_word_length": average_word_length(text),
                       "type_token_ratio": type_token_ratio(text),
                       "hapax_legomana_ratio": hapax_legomana_ratio(text),
                       "average_sentence_length": average_sentence_length(text),
                       "average_sentence_complexity": avg_sentence_complexity(text),
                       "words": get_plain_words(text)}
collection.insert_one(author_characteristics)

text = open('./texts/reymont_chlopi-3', 'r').readlines()
author_characteristics = { "name": "reymont",
                       "average_word_length": average_word_length(text),
                       "type_token_ratio": type_token_ratio(text),
                       "hapax_legomana_ratio": hapax_legomana_ratio(text),
                       "average_sentence_length": average_sentence_length(text),
                       "average_sentence_complexity": avg_sentence_complexity(text),
                       "words": get_plain_words(text)}
collection.insert_one(author_characteristics)
