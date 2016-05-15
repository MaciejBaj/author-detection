from __future__ import division
import xml.etree.ElementTree as ET
from collections import Counter, OrderedDict
import os
# https://github.com/CenturyLinkLabs/panamax-ui/wiki/How-To%3A-Port-Forwarding-on-VirtualBox
from utils import stop_list, update_and_return_json


class XmlParser:
  tree = 0
  number_of_words = None
  hapax_legomenons = 0

  def __init__(self, xml_string):
    self.root = ET.fromstring(xml_string)

  def get_base_words(self):
    return [base_word.text.lower().encode('utf-8') for base_word in self.root.iter('base')]

  def get_top_and_rarest_used_words(self):
    #todo: dot cannot be json key
    base_lowercase_words_counted = Counter(filter(lambda word: word not in stop_list, self.get_base_words()))
    ordered_dict_words = OrderedDict(base_lowercase_words_counted)

    def count_rarest(result, word):
      word_occurrences = ordered_dict_words[word]
      update_and_return_json(result, word, word_occurrences)
      if word_occurrences == 1:
        self.hapax_legomenons += 1
      return result

    return {
      # "top_words": map((lambda (word_frequency, val):
      #                   {word_frequency: val}), base_lowercase_words_counted.most_common(1000)),
      # "rarest_words": map(lambda word: {word: ordered_dict_words[word]}, list(ordered_dict_words)[-1000:])
      "top_words": reduce((lambda result, (word_frequency, val):
                          update_and_return_json(result, word_frequency, val)), base_lowercase_words_counted.most_common(1000), {}),
      "rarest_words": reduce(count_rarest, list(ordered_dict_words)[-1000:], {}),
      "hapax_legomenon_ratio": self.hapax_legomenons / float(self.get_number_of_words())
    }

  def get_parts_of_speech_frequency(self):
    part_of_speech_counter = {}
    for tag in self.root.iter('ctag'):
      part_of_speech = tag.text.split(':')[0]
      if part_of_speech in part_of_speech_counter:
        part_of_speech_counter[part_of_speech] += 1
      else:
        part_of_speech_counter[part_of_speech] = 1

    all_words_length = self.get_number_of_words()
    for name in part_of_speech_counter:
      part_of_speech_counter[name] /= float(all_words_length)

    return part_of_speech_counter

  @staticmethod
  def produce_xml_with_morphological_data(text_file_path, output_file_path):
    os.system("wcrft-app -d ~/projects/pwr/master-thesis/tagery/wcrft2/libwcrft/model/model_nkjp10_wcrft_e2 ~/projects/pwr/master-thesis/tagery/wcrft2/libwcrft/config/nkjp.ini -i txt " +
              text_file_path + " -O " + output_file_path)

  def set_number_of_words(self, n):
    self.number_of_words = n

  def get_number_of_words(self):
    if self.number_of_words:
      return self.number_of_words
    return len(self.get_base_words())
